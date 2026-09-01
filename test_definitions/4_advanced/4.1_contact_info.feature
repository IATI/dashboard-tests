# ATI test 21
@iati-activity
Feature: Contact info

  Scenario Outline: Contact info is present
    Given an IATI activity
     And the activity is current
     Then `contact-info` should be present
