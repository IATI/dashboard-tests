# ATI test 16
@iati-activity
Feature: Title

  @2.4.1_title_present
  Scenario Outline: Title is present
    Given an IATI activity
     And the activity is current
     Then `title/narrative/text()` should be present

  @2.4.2_title_min_10_characters
  Scenario Outline: Title has at least 10 characters
    Given an IATI activity
     And the activity is current
     Then `title/narrative/text()` should have at least 10 characters
