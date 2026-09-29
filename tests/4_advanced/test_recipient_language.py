from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestRecipientLanguage(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '4_advanced', '4.4_recipient_language.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[0]

    def activity(self, country='KE', language='en', element='title'):
        country_el = ('<recipient-country code="%s"/>' % country) if country else ''
        lang_attr = (' xml:lang="%s"' % language) if language else ''
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          {country}
          <{element}><narrative{lang}>Some text</narrative></{element}>
        </iati-activity>
        '''.format(country=country_el, element=element, lang=lang_attr)
        return etree.fromstring(xml)

    def test_official_language(self):
        assert self.test(self.activity('KE', 'en')) is True

    def test_second_official_language(self):
        assert self.test(self.activity('KE', 'sw')) is True

    def test_not_an_official_language(self):
        assert self.test(self.activity('KE', 'fr')) is False

    def test_no_recipient_country_is_not_relevant(self):
        assert self.test(self.activity(None, 'en')) is None

    def test_no_declared_language(self):
        assert self.test(self.activity('FR', None)) is False

    def test_activity_level_language_is_inherited(self):
        xml = '''
        <iati-activity xml:lang="fr">
          <activity-status code="2"/>
          <recipient-country code="FR"/>
          <title><narrative>Un titre</narrative></title>
        </iati-activity>
        '''
        assert self.test(etree.fromstring(xml)) is True

    def test_supplied_mapping_overrides_the_bundled_file(self):
        result = self.test(self.activity('KE', 'fr'),
                           country_languages={'KE': {'fr'}})

        assert result is True

    def test_description_scenario(self):
        test = self.feature.tests[1]

        assert test(self.activity('FR', 'fr', element='description')) is True
        assert test(self.activity('FR', 'en', element='description')) is False
