# ATI test 8
@iati-organisation
Feature: Audit report

  Scenario: Audit is present
    Given file is an organisation file
     Then `document-link/category[@code="B06"]` should be present
