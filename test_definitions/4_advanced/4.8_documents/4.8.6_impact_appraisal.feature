# ATI test 33
# Proposal 4.8 note [1]: restricted to projects above a certain threshold.
# The figure below is provisional and needs consulting on.
@iati-activity
Feature: Documents - pre- and/or post-project impact appraisal

  Scenario Outline: Pre- and/or post-project impact appraisal documents
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02, B01, B02, B03, B04, D01, D02, E01, E02, F01, H01, H02, H03, H04, H05 or G01 
     And `transaction/aid-type/@code` is not any of A01, A02, B01, B02, B03, B04, D01, D02, E01, E02, F01, H01, H02, H03, H04, H05 or G01 
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A01"]` should be present
