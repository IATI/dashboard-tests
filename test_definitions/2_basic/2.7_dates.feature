# ATI tests 18 (planned) and 19 (actual)
@iati-activity
Feature: Dates

  @2.7.1_planned_start_date
  Scenario Outline: Planned start date is present
    Given an IATI activity
     And the activity is current
     Then `activity-date[@type="1"]` should be present

  @2.7.2_planned_end_date
  Scenario Outline: Planned end date is present
    Given an IATI activity
     And the activity is current
     And `default-finance-type/@code | transaction/finance-type/@code` is not any of 501, 433, 432, 1100 or 210
     Then `activity-date[@type="3"]` should be present

  @2.7.3_actual_start_date
  Scenario Outline: Actual start date is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `activity-date[@type="2"]` should be present

  @2.7.4_actual_end_date
  Scenario Outline: Actual end date is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 3 or 4
     Then `activity-date[@type="4"]` should be present
