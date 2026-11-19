# ATI test 23
@iati-activity
Feature: Location (sub-national)

  @4.2.1_location_present
  Scenario Outline: Location is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `recipient-region/@code` is not 998
     And `default-aid-type/@code` is not any of B01, B02, F01, H01, H02, H03, H04, H05 or G01
     And `transaction/aid-type/@code` is not any of B01, B02, F01, H01, H02, H03, H04, H05 or G01
     Then `location` should be present

  @4.2.2_location_point_or_administrative
  Scenario Outline: Location has a point or a coded area
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `recipient-region/@code` is not 998
     And `default-aid-type/@code` is not any of B01, B02, F01, H01, H02, H03, H04, H05 or G01
     And `transaction/aid-type/@code` is not any of B01, B02, F01, H01, H02, H03, H04, H05 or G01
     Then `location/point` should be present, or at least one `location/administrative/@vocabulary | location/location-id/@vocabulary` should be on the GeographicVocabulary codelist
