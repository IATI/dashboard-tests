from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestActivityValueThreshold(TestCase):
    """The value threshold guard used by indicators the proposal restricts to
    projects above a certain size.

    The activity's value is expected to be calculated in advance, in USD, and
    passed in as `activity_value`; the runner does not supply it yet. These tests
    pin down what the step does with and without it, so the behaviour is not
    changed by accident when the runner is updated.
    """

    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', 'test_definitions',
                            '4_advanced', '4.6_conditions.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[0]

    def qualifying_activity(self, conditions=True):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="C01"/>
          {}
        </iati-activity>
        '''.format('<conditions attached="1"/>' if conditions else '')
        return etree.fromstring(xml)

    def test_no_value_supplied_does_not_filter(self):
        # The runner does not pass a value yet, so the test must behave as it did
        # before the threshold was added to its definition.
        result = self.test(self.qualifying_activity())

        assert result is True

    def test_no_value_supplied_still_reports_failure(self):
        result = self.test(self.qualifying_activity(conditions=False))

        assert result is False

    def test_value_above_threshold_is_assessed(self):
        result = self.test(self.qualifying_activity(), activity_value=200000)

        assert result is True

    def test_value_above_threshold_still_reports_failure(self):
        result = self.test(self.qualifying_activity(conditions=False),
                           activity_value=200000)

        assert result is False

    def test_value_below_threshold_is_not_relevant(self):
        result = self.test(self.qualifying_activity(conditions=False),
                           activity_value=50000)

        assert result is None

    def test_value_exactly_at_threshold_is_assessed(self):
        result = self.test(self.qualifying_activity(), activity_value=100000)

        assert result is True
