# ATI test 31 (tender); split from 29_project_procurement.feature
# Proposal 4.8 note [1]: restricted to projects above a certain threshold.
# The figure below is provisional and needs consulting on.
@iati-activity
Feature: Documents - tender

  Scenario Outline: Tender is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02, B02 or G01
     And `transaction/aid-type/@code` is not any of A01, A02 or B02
     And the activity value is at least 100000 USD
     Then `document-link/category[@code="A10"]` should be present
