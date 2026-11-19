# ATI test 28
@iati-activity
Feature: Finance type

  @2.12.1_finance_type_present
  Scenario Outline: Finance type is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `default-finance-type | transaction/finance-type` should be present

  @2.12.2_finance_type_valid
  Scenario Outline: Finance type uses the FinanceType codelist
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then every `default-finance-type/@code | transaction/finance-type/@code` should be on the FinanceType codelist
