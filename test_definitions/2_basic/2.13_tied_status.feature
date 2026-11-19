# ATI test 29
@iati-activity
Feature: Tied status

  @2.13.1_tied_status_present
  Scenario Outline: Tied status is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `default-tied-status | transaction/tied-status` should be present

  @2.13.2_tied_status_valid
  Scenario Outline: Tied status is valid
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then every `default-tied-status/@code | transaction/tied-status/@code` should be on the TiedStatus codelist
