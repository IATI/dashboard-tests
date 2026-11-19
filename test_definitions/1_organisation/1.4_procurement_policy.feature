# ATI test 6
@iati-organisation
Feature: Procurement policy

  @1.4.1_procurement_policy
  Scenario: Procurement policy is present
    Given file is an organisation file
     Then `document-link/category[@code="B05"]` should be present
