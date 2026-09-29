# ATI test 24
# Proposal 4.6: "This could be restricted to projects which are: a) above a
# certain threshold; b) implemented through government." The threshold below is a
# provisional placeholder - the proposal says the exact figure needs consulting on.
# The government-implementation half looks for a public-sector organisation type on
# the implementing participating-org or the transaction receiver: 10 (Government),
# 11 (Local Government) or 15 (Other Public Sector), which are all of the 1x codes
# on the OrganisationType codelist.
@iati-activity
Feature: Conditions

  Scenario Outline: Conditions data
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is one of A01, A02, C01 or F01
     And the activity value is at least 100000 USD
     And `participating-org[@role="Implementing" or @role="4"]/@type | transaction/receiver-org/@type` is one of 10, 11 or 15
     Then `conditions` should be present
