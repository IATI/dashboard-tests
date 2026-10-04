# ATI tests 12, 24, 31, 32, 33, 34 and 35.
#
# Proposal 4.8: "There is currently one indicator which assesses the presence of any
# documents ... the intention here is to disaggregate this into multiple tests, while
# retaining it as a single indicator." All eight tests therefore live in one feature
# file. IATI Stats groups tests by feature filename and scores a component as the
# mean over features, so eight separate files gave documents eight fourteenths of the
# advanced fields component instead of one eighth.
#
# Several scenarios are restricted to larger projects. The 100,000 USD figure is a
# provisional placeholder - see the threshold convention in ../README.md.
@iati-activity
Feature: Documents

  # 4.8.1 - ATI test 12
  Scenario Outline: Budget document is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02 or G01
     And `transaction/aid-type/@code` is not any of A01 or A02
     Then `document-link/category[@code="A05"]` should be present

  # 4.8.2 - ATI test 24
  Scenario Outline: Conditions document
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is one of A01, A02, C01 or F01
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A04"]` should be present

  # 4.8.3 - ATI test 31
  Scenario Outline: Tender is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02, B02 or G01
     And `transaction/aid-type/@code` is not any of A01, A02 or B02
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A10"]` should be present

  # 4.8.4 - ATI test 31
  Scenario Outline: Contract is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02, B02 or G01
     And `transaction/aid-type/@code` is not any of A01, A02 or B02
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A06"] | document-link/category[@code="A11"]` should be present

  # 4.8.5 - ATI test 32
  Scenario Outline: Objectives of activity document
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not G01
     Then `document-link/category[@code="A02"] | description[@type="2"]` should be present

  # 4.8.6 - ATI test 33
  Scenario Outline: Pre- and/or post-project impact appraisal documents
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02, B01, B02, B03, B04, D01, D02, E01, E02, F01, H01, H02, H03, H04, H05 or G01
     And `transaction/aid-type/@code` is not any of A01, A02, B01, B02, B03, B04, D01, D02, E01, E02, F01, H01, H02, H03, H04, H05 or G01
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A01"]` should be present

  # 4.8.7 - ATI test 34. Thresholded because the introduction to proposal 4.8 uses
  # evaluations as its example of something that "may not be realistic or reasonable
  # to expect for smaller projects", even though the table does not mark it [1].
  Scenario Outline: Project performance and evaluation document
    Given an IATI activity
     And the activity is current
     And `default-aid-type/@code` is not G01
     And either `document-link/category[@code="A07"]` is present, or `activity-status/@code` is one of 3 or 4
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A07"]` should be present

  # 4.8.8 - ATI test 35
  Scenario Outline: Results document
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of F01 or G01
     Then `document-link/category[@code="A08"]` should be present
