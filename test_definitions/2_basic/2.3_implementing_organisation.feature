# ATI test 30
# TODO proposal 2.3 also requires assessing participating-org/@type
@iati-activity
Feature: Implementing organisation

  Scenario Outline: Implementing organisation
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `participating-org[@role="Implementing" or @role="4"]/@ref | participating-org[@role="Implementing" or @role="4"]/narrative/text()` should have at least 1 characters
