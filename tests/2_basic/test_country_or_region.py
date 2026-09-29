from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestCountryOrRegion(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '2_basic', '2.9_country_or_region.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[0]

    def test_neither_country_nor_region(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is False

    def test_recipient_country(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <recipient-country code="KE"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_recipient_region(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <recipient-region code="298"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_country_on_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <recipient-country code="KE"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_dac_region_with_explicit_vocabulary(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <recipient-region code="298" vocabulary="1"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_un_region_alone_is_not_enough(self):
        # Only DAC regions count: an activity identified solely by a UN region code
        # has not said where the money goes in comparable terms.
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <recipient-region code="489" vocabulary="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is False

    def test_country_plus_un_region(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <recipient-country code="KE"/>
          <recipient-region code="489" vocabulary="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_region_on_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <recipient-region code="298"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True


class TestCountryOrRegionCodelists(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '2_basic', '2.9_country_or_region.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.country_test = self.feature.tests[1]
        self.region_test = self.feature.tests[2]
        self.codelists = {'Country': ['KE', 'FR'], 'Region': ['298']}

    def activity(self, body):
        xml = '<iati-activity><activity-status code="2"/>%s</iati-activity>' % body
        return etree.fromstring(xml)

    def test_country_on_codelist(self):
        activity = self.activity('<recipient-country code="KE"/>')

        assert self.country_test(activity, codelists=self.codelists) is True

    def test_country_not_on_codelist(self):
        activity = self.activity('<recipient-country code="ZZ"/>')

        assert self.country_test(activity, codelists=self.codelists) is False

    def test_region_only_activity_skips_the_country_check(self):
        # The whole point of guarding each codelist scenario: a region-only activity
        # must not be marked down for having no country.
        activity = self.activity('<recipient-region code="298"/>')

        assert self.country_test(activity, codelists=self.codelists) is None

    def test_region_on_codelist(self):
        activity = self.activity('<recipient-region code="298"/>')

        assert self.region_test(activity, codelists=self.codelists) is True

    def test_region_not_on_codelist(self):
        activity = self.activity('<recipient-region code="999"/>')

        assert self.region_test(activity, codelists=self.codelists) is False

    def test_country_only_activity_skips_the_region_check(self):
        activity = self.activity('<recipient-country code="KE"/>')

        assert self.region_test(activity, codelists=self.codelists) is None

    def test_un_region_is_not_validated(self):
        # A UN region code is not on the DAC Region codelist, and the publisher must
        # not be marked down for publishing one alongside a valid DAC region.
        activity = self.activity('<recipient-region code="298"/>'
                                 '<recipient-region code="489" vocabulary="2"/>')

        assert self.region_test(activity, codelists=self.codelists) is True

    def test_un_region_alone_skips_the_region_check(self):
        activity = self.activity('<recipient-region code="489" vocabulary="2"/>')

        assert self.region_test(activity, codelists=self.codelists) is None
