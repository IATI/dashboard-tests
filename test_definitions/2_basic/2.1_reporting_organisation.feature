# No ATI equivalent
# TODO decide whether the reporting organisation's name (reporting-org/narrative)
# should be assessed too, as it is for implementing organisations in 2.3.
@iati-activity
Feature: Reporting organisation

  Scenario Outline: Reporting organisation is present
    Given an IATI activity
     And the activity is current
     Then `reporting-org/@ref` should be present

  Scenario Outline: Reporting organisation type is valid
    Given an IATI activity
     And the activity is current
     Then every `reporting-org/@type` should be on the OrganisationType codelist
