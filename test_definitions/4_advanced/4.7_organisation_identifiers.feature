# ATI test 30 (participating org references).
# The proposal assesses whether organisations are using correctly structured
# organisation identifiers, scored as the proportion of references that are valid.
# That is a proportion across a publisher's activities rather than a per-activity
# pass or fail, and IATI Stats already calculates it - see the 4.7 entry in
# ../README.md for the endpoints.
@iati-activity
Feature: Organisation identifiers

  Scenario: Organisation identifiers
    Given this test is calculated across an organisation's activities
     Then skip it
