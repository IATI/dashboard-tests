# No ATI equivalent: Annex 4 of the proposal does not define this test, so the
# definition below is a first reading of indicator 2.9 and needs confirming.
#
# `recipient-region` carries a `@vocabulary`: 1 (or absent, which defaults to 1) is
# the OECD DAC region list, 2 is the UN list. Only DAC regions count towards this
# indicator, so that an activity is required to identify where the money goes in
# country codes or DAC region codes, but is not marked down for additionally
# publishing UN region codes.
#
# Country and Region are separate codelists, so each is validated in its own
# scenario, guarded so that an activity using only one of them is not marked down
# for the absence of the other.
@iati-activity
Feature: Country or region

  Scenario Outline: Country or region is present
    Given an IATI activity
     And the activity is current
     Then `recipient-country | transaction/recipient-country | recipient-region[not(@vocabulary) or @vocabulary="1"] | transaction/recipient-region[not(@vocabulary) or @vocabulary="1"]` should be present

  Scenario Outline: Recipient country uses the Country codelist
    Given an IATI activity
     And the activity is current
     And `recipient-country/@code | transaction/recipient-country/@code` is present
     Then every `recipient-country/@code | transaction/recipient-country/@code` should be on the Country codelist

  Scenario Outline: Recipient region uses the Region codelist
    Given an IATI activity
     And the activity is current
     And `recipient-region[not(@vocabulary) or @vocabulary="1"]/@code | transaction/recipient-region[not(@vocabulary) or @vocabulary="1"]/@code` is present
     Then every `recipient-region[not(@vocabulary) or @vocabulary="1"]/@code | transaction/recipient-region[not(@vocabulary) or @vocabulary="1"]/@code` should be on the Region codelist
