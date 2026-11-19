# No ATI equivalent
# TODO decide whether the reporting organisation's name (reporting-org/narrative)
# should be assessed too, as it is for implementing organisations in 2.3.
@iati-activity
Feature: Reporting organisation

  @2.1.1_reporting_organisation_present
  Scenario Outline: Reporting organisation is present
    Given an IATI activity
     And the activity is current
     Then `reporting-org/@ref` should be present

  @2.1.2_reporting_organisation_type_valid
  Scenario Outline: Reporting organisation type uses the OrganisationType codelist
    Given an IATI activity
     And the activity is current
     Then every `reporting-org/@type` should be on the OrganisationType codelist
