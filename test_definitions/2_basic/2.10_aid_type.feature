# ATI test 27
@iati-activity
Feature: Aid type

  @2.10.1_aid_type_present
  Scenario Outline: Aid type is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `default-aid-type | transaction/aid-type` should be present

  @2.10.2_aid_type_valid
  Scenario Outline: Aid type is valid
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then every `default-aid-type[not(@vocabulary) or @vocabulary="1"]/@code | transaction/aid-type[not(@vocabulary) or @vocabulary="1"]/@code` should be on the AidType codelist
