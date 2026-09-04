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
