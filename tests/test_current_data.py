from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestCurrentData(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', 'test_definitions',
                            'current_data.feature')

        tester = BDDTester(steps_path)

        self.today = '2010-01-01'
        feature = tester.load_feature(feature_path)
        self.test = feature.tests[0]

    def test_activity_is_in_implementation(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_activity_is_not_in_implementation(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_activity_recently_ended(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <activity-date type="4" iso-date="2009-09-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_activity_end_is_in_the_future(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <activity-date type="3" iso-date="2011-01-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_activity_has_recent_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <transaction>
            <transaction-type code="2" />
            <transaction-date iso-date="2009-12-01" />
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True


class TestCurrentViaTransactionDate(TestCase):
    """An activity can qualify as current by any of four routes. Whichever route it
    takes, the rest of the scenario must still be evaluated against the activity.

    Regression test: the transaction-date route used to return the transaction
    element, so every later step in the scenario ran against that instead. An
    activity current only by that route failed checks on activity-level elements it
    actually had - and because it still passed the given, it was counted as in scope
    rather than skipped, so it showed up as a genuine failure.
    """

    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', 'test_definitions', '2_basic',
                            '2.2_iati_identifier.feature')

        tester = BDDTester(steps_path)
        self.test = tester.load_feature(feature_path).tests[0]
        self.today = '2026-10-22'

    def activity(self, status, transaction_date=None, end_date=None):
        transaction = ''
        if transaction_date:
            transaction = '''
            <transaction>
              <transaction-type code="3"/>
              <transaction-date iso-date="{}"/>
              <value>100</value>
            </transaction>'''.format(transaction_date)
        end = ''
        if end_date:
            end = '<activity-date type="4" iso-date="{}"/>'.format(end_date)
        xml = '''
        <iati-activity>
          <iati-identifier>XM-DAC-1-ABC</iati-identifier>
          <reporting-org ref="XM-DAC-1" type="40"/>
          <activity-status code="{}"/>{}{}
        </iati-activity>
        '''.format(status, end, transaction)
        return etree.fromstring(xml)

    def test_current_by_status(self):
        result = self.test(self.activity('2'), today=self.today)

        assert result is True

    def test_current_by_actual_end_date(self):
        result = self.test(self.activity('3', end_date='2026-06-01'),
                           today=self.today)

        assert result is True

    def test_current_by_transaction_date(self):
        result = self.test(self.activity('3', transaction_date='2026-06-01'),
                           today=self.today)

        assert result is True

    def test_not_current_is_skipped_rather_than_failed(self):
        result = self.test(self.activity('3'), today=self.today)

        assert result is None
