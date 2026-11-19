# ATI test 9
@iati-organisation
Feature: Organisation budget

  @1.7.1_one_year_forward
  Scenario: Organisation budget is available one year forward
    Given file is an organisation file
     Then `total-budget` should be available 1 year forward

  @1.7.2_two_years_forward
  Scenario: Organisation budget is available two years forward
    Given file is an organisation file
     Then `total-budget` should be available 2 years forward

  @1.7.3_three_years_forward
  Scenario: Organisation budget is available three years forward
    Given file is an organisation file
     Then `total-budget` should be available 3 years forward
