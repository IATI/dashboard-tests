# ATI test 26
@iati-activity
Feature: Flow type

  @2.11.1_flow_type_present
  Scenario Outline: Flow type is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `default-flow-type | transaction/flow-type` should be present

  @2.11.2_flow_type_valid
  Scenario Outline: Flow type uses the FlowType codelist
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then every `default-flow-type/@code | transaction/flow-type/@code` should be on the FlowType codelist
