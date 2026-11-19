# ATI test 20
@iati-activity
Feature: Current status

  @2.6.1_current_status_present
  Scenario Outline: Current status is present
    Given an IATI activity
     And the activity is current
     Then `activity-status` should be present

  @2.6.2_current_status_valid
  Scenario Outline: Current status is valid
    Given an IATI activity
     And the activity is current
     Then every `activity-status/@code` should be on the ActivityStatus codelist
