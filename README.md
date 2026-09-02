# IATI Data Quality Dashboard — test definitions

Data quality test definitions for the new IATI Data Quality Dashboard.

The tests are written in [Gherkin](https://cucumber.io/docs/gherkin/) and are run
against individual IATI activity and organisation XML elements. They originate from
[pwyf/2024-Index-indicator-definitions](https://github.com/pwyf/2024-Index-indicator-definitions),
the rule-set used by Publish What You Fund in their Aid Transparency Index (ATI),
and are being adapted to the framework set out in *Reimagining Data Quality:
A User Centric Approach* (Proposal for Consultation, v1.3).

## Scope

The proposal defines four data quality dimensions: **Availability**, **Timeliness**,
**Coverage** and **Comprehensiveness**. This repository covers **Comprehensiveness
only**.

The other three dimensions are publisher- or file-level calculations — validator
output, publication frequency, share of reference spend covered, quarters with
financial data across a dataset. They cannot be expressed as tests against a single
activity or organisation element, and belong in IATI Stats rather than here.

## Structure

Test definitions live in [test_definitions/](test_definitions/), grouped into the four
components of the Comprehensiveness dimension:

| Component | Directory |
| --- | --- |
| 1. Organisation | [1_organisation/](test_definitions/1_organisation/) |
| 2. Basic fields | [2_basic/](test_definitions/2_basic/) |
| 3. Financials | [3_financials/](test_definitions/3_financials/) |
| 4. Advanced fields | [4_advanced/](test_definitions/4_advanced/) |

One file per indicator, named for its number in the proposal. See
[test_definitions/README.md](test_definitions/README.md) for the full indicator-to-file
mapping, the tests still to be written, and open methodology questions.

Shared step definitions are in
[test_definitions/step_definitions.py](test_definitions/step_definitions.py), and
[test_definitions/current_data.feature](test_definitions/current_data.feature) defines
the "activity is current" precondition used by most tests.

## Running the tests

The tests in [tests/](tests/) are unit tests of the test definitions themselves — they
check that each scenario gives the expected result for known-good and known-bad XML.
They mirror the structure of `test_definitions/`.

```bash
pip install -r requirements_dev.txt
pytest
```

Tested against Python 3.10 to 3.14.

## Licence

MIT — see [LICENSE](LICENSE). The test definitions derive from Publish What You Fund's
Aid Transparency Index rule-set, which is also MIT licensed.
