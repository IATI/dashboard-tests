# Reference data

## `country_lang_map.csv`

Maps ISO 3166-1 country codes to the ISO 639-1 codes of that country's official
languages, one row per country/language pair. Used by indicator 4.4 (recipient
language) to check that an activity's title and description are in an official
language of the recipient country.

Copied verbatim from IATI-Stats, which is the canonical source:
`helpers/transparency_indicator/country_lang_map.csv` on the `develop` branch.
Per its own header, it was compiled from the OpenStreetMap list of official
languages per country code, with manual adjustments so that every ISO 3166-1
country is listed and every language code is on the ISO 639-1 codelist.

It is vendored here so that 4.4 runs without the caller having to supply the data.
A caller that already holds its own copy — IATI-Stats does — can override it by
passing a `country_languages` mapping of `{country code: set of language codes}`,
in which case the bundled file is not read. If this copy drifts from IATI-Stats',
prefer theirs.
