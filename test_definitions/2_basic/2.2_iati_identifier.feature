# ATI test 25
@iati-activity
Feature: IATI Identifier

  @2.2.1_iati_identifier_present
  Scenario Outline: IATI Identifier is present
    Given an IATI activity
     And the activity is current
     Then `iati-identifier` should be present

  @2.2.2_iati_identifier_starts_with_org_ref
  Scenario Outline: IATI Identifier starts with reporting org ref
    Given an IATI activity
     And the activity is current
     Then `iati-identifier/text()` should start with either `reporting-org/@ref` or `other-identifier[@type="B1"]/@ref`
