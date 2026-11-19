# ATI test 8
@iati-organisation
Feature: Audit report

  @1.6.1_audit
  Scenario: Audit report is present
    Given file is an organisation file
     Then `document-link/category[@code="B06"]` should be present
