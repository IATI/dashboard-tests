# ATI test 24
@iati-activity
Feature: Conditions

  Scenario Outline: Conditions data
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is one of A01, A02, C01 or F01
     Then `conditions` should be present
