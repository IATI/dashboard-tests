# Was 38_networked_data_transactions_with_valid_receiver.
# The proposal redefines this as the share of a publisher's spend that is traceable,
# with the direction depending on the publisher's organisation type. It is a
# publisher-level figure that IATI Stats already calculates - see the 3.3 entry in
# ../README.md for the endpoints and the caveats for integrating them.
@iati-activity
Feature: Traceability

  Scenario: Traceability
    Given this test involves activity files from other organisations
     Then skip it
