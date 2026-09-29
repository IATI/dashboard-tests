from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestImplementingOrganisation(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '2_basic', '2.3_implementing_organisation.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.name_test = self.feature.tests[0]
        self.type_test = self.feature.tests[1]
        self.codelists = {'OrganisationType': ['10', '21', '40']}

    def activity(self, participating_org):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          {}
        </iati-activity>
        '''.format(participating_org)
        return etree.fromstring(xml)

    def test_name_is_present(self):
        activity = self.activity(
            '<participating-org role="4"><narrative>An NGO</narrative>'
            '</participating-org>')

        assert self.name_test(activity) is True

    def test_name_is_absent(self):
        activity = self.activity('<participating-org role="4" ref="XM-DAC-1"/>')

        assert self.name_test(activity) is False

    def test_name_on_a_non_implementing_org_does_not_count(self):
        activity = self.activity(
            '<participating-org role="1"><narrative>A funder</narrative>'
            '</participating-org>')

        assert self.name_test(activity) is False

    def test_type_is_valid(self):
        activity = self.activity('<participating-org role="4" type="21"/>')

        assert self.type_test(activity, codelists=self.codelists) is True

    def test_type_is_absent(self):
        activity = self.activity(
            '<participating-org role="4"><narrative>An NGO</narrative>'
            '</participating-org>')

        assert self.type_test(activity, codelists=self.codelists) is False

    def test_type_is_not_on_codelist(self):
        activity = self.activity('<participating-org role="4" type="999"/>')

        assert self.type_test(activity, codelists=self.codelists) is False
