# ATI test 17
@iati-activity
Feature: Description

  @2.5.1_description_present
  Scenario Outline: Description is present
    Given an IATI activity
     And the activity is current
     Then `description/narrative/text()` should be present

  @2.5.2_description_min_80_characters
  Scenario Outline: Description has at least 80 characters
    Given an IATI activity
     And the activity is current
     Then `description/narrative/text()` should have at least 80 characters
