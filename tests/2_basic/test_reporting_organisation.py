from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestReportingOrganisation(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '2_basic', '2.1_reporting_organisation.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[0]
        self.codelists = {'OrganisationType': ['10', '21', '40']}

    def test_reporting_org_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is False

    def test_reporting_org_is_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <reporting-org ref="XM-DAC-1" type="10"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_reporting_org_without_ref(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <reporting-org type="10">
            <narrative>An organisation</narrative>
          </reporting-org>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is False

    def test_type_is_on_codelist(self):
        test = self.feature.tests[1]
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <reporting-org ref="XM-DAC-1" type="40"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = test(activity, codelists=self.codelists)

        assert result is True

    def test_type_is_not_on_codelist(self):
        test = self.feature.tests[1]
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <reporting-org ref="XM-DAC-1" type="999"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = test(activity, codelists=self.codelists)

        assert result is False

    def test_type_is_missing(self):
        test = self.feature.tests[1]
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <reporting-org ref="XM-DAC-1"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = test(activity, codelists=self.codelists)

        assert result is False
