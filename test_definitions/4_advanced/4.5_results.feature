# ATI test 35
@iati-activity
Feature: Results

  @4.5.1_results
  Scenario Outline: Results data
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of F01 or G01
     Then `result` should be present
