# ATI test 3
@iati-organisation
Feature: Organisation strategy

  @1.1.1_organisation_strategy
  Scenario: Organisation strategy is present
    Given file is an organisation file
     Then `document-link/category[@code="B02"]` should be present
