# ATI test 30
# Proposal 2.3: "this test should be adjusted to specifically look for implementing
# organisations (rather than any kind of organisation). Both organisation names and
# types should be assessed."
# NB the ATI test accepted either a `@ref` or a narrative. The name scenario asks for
# the name specifically, since the proposal assesses names and types separately and
# identifiers are assessed by 4.7.
@iati-activity
Feature: Implementing organisation

  Scenario Outline: Implementing organisation name is present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `participating-org[@role="Implementing" or @role="4"]/narrative/text()` should have at least 1 characters

  Scenario Outline: Implementing organisation type is valid
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then every `participating-org[@role="Implementing" or @role="4"]/@type` should be on the OrganisationType codelist
