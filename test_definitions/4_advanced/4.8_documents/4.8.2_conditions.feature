# ATI test 24 (document); split from 28_conditions.feature
@iati-activity
Feature: Documents - conditions

  Scenario Outline: Conditions document
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is one of A01, A02, C01 or F01
     Then `document-link/category[@code="A04"]` should be present
