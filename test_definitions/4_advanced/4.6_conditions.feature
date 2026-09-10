# ATI test 24
# Proposal 4.6: "This could be restricted to projects which are: a) above a
# certain threshold; b) implemented through government." The threshold below is a
# provisional placeholder - the proposal says the exact figure needs consulting on.
# The "implemented through government" half is not yet expressed.
@iati-activity
Feature: Conditions

  Scenario Outline: Conditions data
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is one of A01, A02, C01 or F01
     And the activity value is at least 100000 USD
     Then `conditions` should be present
