# No ATI test number given in Annex 4. Proposal 4.4, note [1]: "the title and
# description should be in one of the country's official languages".
#
# The country-to-official-language mapping is read from data/country_lang_map.csv,
# vendored from IATI-Stats - see data/README.md. A caller holding its own copy can
# override it by passing a `country_languages` mapping instead.
#
# The declared language is the narrative's own `xml:lang`, falling back to the
# activity's. Activities with no recipient country - region-only activities - are
# filtered out rather than failed.
@iati-activity
Feature: Recipient language

  Scenario Outline: Title is in an official language of the recipient country
    Given an IATI activity
     And the activity is current
     And `recipient-country/@code | transaction/recipient-country/@code` is present
     Then `title` should be in an official language of the recipient country

  Scenario Outline: Description is in an official language of the recipient country
    Given an IATI activity
     And the activity is current
     And `recipient-country/@code | transaction/recipient-country/@code` is present
     Then `description` should be in an official language of the recipient country
