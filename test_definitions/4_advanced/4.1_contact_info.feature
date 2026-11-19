# ATI test 21
@iati-activity
Feature: Contact info

  @4.1.1_contact_info
  Scenario Outline: Contact info is present
    Given an IATI activity
     And the activity is current
     Then `contact-info` should be present
