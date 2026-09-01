# ATI test 31 (contract); split from 29_project_procurement.feature
@iati-activity
Feature: Documents - contract

  Scenario Outline: Contract is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of A01, A02, B02 or G01
     And `transaction/aid-type/@code` is not any of A01, A02 or B02
     Then `document-link/category[@code="A06"] | document-link/category[@code="A11"]` should be present
