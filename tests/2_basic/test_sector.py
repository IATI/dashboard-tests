from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestSector(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '2_basic', '2.8_sector.feature')

        self.codelists = {'Sector': ['11110', '11120']}
        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[0]

    def test_sector_is_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <sector code="11110"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

    def test_sector_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is False

    def test_sector_uses_dac_no_vocab(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <sector code="11110"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        test = self.feature.tests[1]
        result = test(activity, codelists=self.codelists)

        assert result is True

    def test_sector_uses_dac_and_vocab(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <sector vocabulary="1" code="11110"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        test = self.feature.tests[1]
        result = test(activity, codelists=self.codelists)

        assert result is True

    def test_sector_we_dont_support_1_0x_vocabularies(self):
        '''
        Like the above, but using "DAC" instead of "1", which was the
        vocabulary name in IATI Standard v1.0x.
        '''

        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <sector vocabulary="DAC" code="11110"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        test = self.feature.tests[1]
        result = test(activity, codelists=self.codelists)

        assert result is False

    def test_sector_does_not_use_dac(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <sector vocabulary="99" code="11110"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        test = self.feature.tests[1]
        result = test(activity, codelists=self.codelists)

        assert result is False

    def test_multiple_sector_vocabs(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <sector vocabulary="99" code="999"/>
          <sector code="11110"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        test = self.feature.tests[1]
        result = test(activity, codelists=self.codelists)

        assert result is True


class TestCRSCode(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            '2_basic', '2.8_sector.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[2]
        self.codelists = {'Sector': ['1000']}

    def test_sector_code(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
          </transaction>
          <sector code="1000"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is True

    def test_sector_code_in_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
            <sector code="1000"/>
          </transaction>
          <transaction>
            <aid-type code="A03"/>
            <sector code="1000"/>
            <sector code="NOTDAC" vocabulary="NOTDAC"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is True

    def test_sector_code_not_in_every_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
            <sector code="1000"/>
          </transaction>
          <transaction>
            <aid-type code="A03"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is False

    def test_sector_code_not_on_list_in_every_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
            <sector code="1000"/>
          </transaction>
          <transaction>
            <aid-type code="A03"/>
            <sector code="NOT_ON_LIST"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is False

    def test_bad_sector_code(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
          </transaction>
          <sector code="43030"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is False

    def test_not_sector_code(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is False

    def test_sector_code_not_on_codelist(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
          </transaction>
          <sector code="NOTACODE"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)
