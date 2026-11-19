# ATI test 4
@iati-organisation
Feature: Annual report

  @1.2.1_annual_report
  Scenario: Annual report is present
    Given file is an organisation file
     Then `document-link/category[@code="B01"]` should be present
