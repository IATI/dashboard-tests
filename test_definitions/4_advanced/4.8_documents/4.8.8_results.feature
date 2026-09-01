# ATI test 35 (document); split from 33_results.feature
@iati-activity
Feature: Documents - results

  Scenario Outline: Results document
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of F01 or G01
     Then `document-link/category[@code="A08"]` should be present
