# Test definitions

One file per indicator, grouped into the four components of the Comprehensiveness
dimension. File names follow the indicator numbering used in the proposal.

## 1. Organisation

| # | Indicator | File | ATI test |
| --- | --- | --- | --- |
| 1.1 | Organisation strategy | `1_organisation/1.1_organisation_strategy.feature` | 3 |
| 1.2 | Annual report | `1_organisation/1.2_annual_report.feature` | 4 |
| 1.3 | Allocation policy | `1_organisation/1.3_allocation_policy.feature` | 5 |
| 1.4 | Procurement policy | `1_organisation/1.4_procurement_policy.feature` | 6 |
| 1.5 | Strategy (country/sector or MoU) | `1_organisation/1.5_country_strategy_or_mou.feature` | 7 |
| 1.6 | Audit | `1_organisation/1.6_audit.feature` | 8 |
| 1.7 | Organisation budget (1/2/3 years forward) | `1_organisation/1.7_organisation_budget.feature` | 9 |
| 1.8 | Country budgets (1/2/3 years forward) | `1_organisation/1.8_country_budgets.feature` | 10 |

## 2. Basic fields

| # | Indicator | File | ATI test |
| --- | --- | --- | --- |
| 2.1 | Reporting Organisation | `2_basic/2.1_reporting_organisation.feature` | — |
| 2.2 | IATI Identifier | `2_basic/2.2_iati_identifier.feature` | 25 |
| 2.3 | Implementing organisation (name and type) | `2_basic/2.3_implementing_organisation.feature` | 30 |
| 2.4 | Title | `2_basic/2.4_title.feature` | 16 |
| 2.5 | Description | `2_basic/2.5_description.feature` | 17 |
| 2.6 | Current status | `2_basic/2.6_current_status.feature` | 20 |
| 2.7 | Dates (start / end; planned / actual) | `2_basic/2.7_dates.feature` | 18, 19 |
| 2.8 | Sector | `2_basic/2.8_sector.feature` | 22, 15 |
| 2.9 | Country or region | `2_basic/2.9_country_or_region.feature` | — |
| 2.10 | Aid Type | `2_basic/2.10_aid_type.feature` | 27 |
| 2.11 | Flow Type | `2_basic/2.11_flow_type.feature` | 26 |
| 2.12 | Finance Type | `2_basic/2.12_finance_type.feature` | 28 |
| 2.13 | Tied Status | `2_basic/2.13_tied_status.feature` | 29 |

## 3. Financials

| # | Indicator | File | ATI test |
| --- | --- | --- | --- |
| 3.1 | Commitments | `3_financials/3.1_commitments.feature` | 13 |
| 3.2 | Disbursements / expenditures | `3_financials/3.2_disbursements_and_expenditures.feature` | 14 |
| 3.3 | Traceability | `3_financials/3.3_traceability.feature` | — |
| 3.4 | Project budgets (1/2/3 years forward) | `3_financials/3.4_project_budgets.feature` | 11 |

## 4. Advanced fields

| # | Indicator | File | ATI test |
| --- | --- | --- | --- |
| 4.1 | Contact info | `4_advanced/4.1_contact_info.feature` | 21 |
| 4.2 | Location (sub-national) | `4_advanced/4.2_location.feature` | 23 |
| 4.3 | Capital spend | `4_advanced/4.3_capital_spend.feature` | 15 |
| 4.4 | Recipient language | `4_advanced/4.4_recipient_language.feature` | — |
| 4.5 | Results | `4_advanced/4.5_results.feature` | 35 |
| 4.6 | Conditions | `4_advanced/4.6_conditions.feature` | 24 |
| 4.7 | Organisation identifiers | `4_advanced/4.7_organisation_identifiers.feature` | 30 |
| 4.8 | Documents | `4_advanced/4.8_documents.feature` | see below |

### 4.8 Documents

The proposal disaggregates documents "into multiple tests, while retaining it as a
single indicator", so all eight are scenarios of one feature file. That matters for
scoring as well as tidiness: IATI Stats groups tests by feature filename and scores a
component as the mean over features, so eight files would give documents 8/15 of the
advanced fields component rather than 1/8.

| # | Test | Scenario | ATI test |
| --- | --- | --- | --- |
| 4.8.1 | Budget | Budget document is present | 12 |
| 4.8.2 | Conditions | Conditions document | 24 |
| 4.8.3 | Tender | Tender is present | 31 |
| 4.8.4 | Contract | Contract is present | 31 |
| 4.8.5 | Objectives | Objectives of activity document | 32 |
| 4.8.6 | Pre- and/or post-project impact appraisal | Pre- and/or post-project impact appraisal documents | 33 |
| 4.8.7 | Project performance and evaluation | Project performance and evaluation document | 34 |
| 4.8.8 | Results | Results document | 35 |

All eight live in `4_advanced/4.8_documents.feature`, in the order above, and each
scenario carries its 4.8.x number as a comment.

## Still to do

Every indicator in the proposal now has a file. Two of them are placeholders that
return "not relevant" rather than a result, so they are excluded from scoring until
they can be written:

- **3.3 Traceability** — the proposal redefines this as *"the % of this
  organisation's spend which is traceable to downstream partners"*: a spend-weighted
  figure for the whole publisher, not a per-activity pass or fail, so it cannot come
  from a test in this repository. The direction depends on the publisher's
  organisation type — downward for government publishers and foundations, upward for
  NGOs, the private sector, academic and other, both for multilaterals. NB the
  proposal's ranges do not map exactly onto the OrganisationType codelist: 12, 13 and
  14 are not codes on it, and 80 and 90 fall outside its stated groups (they are
  treated as upward here).

  IATI Stats already calculates both directions. The downward one is in exactly the
  form the proposal asks for, as a numerator and denominator per publisher:

      /stats/current/aggregated-publisher/<publisher>/
        traceable_sum_commitments_and_disbursements_by_publisher_id.json
        traceable_sum_commitments_and_disbursements_by_publisher_id_denominator.json

  For FCDO these were 17.13bn of 379.43bn USD, i.e. 4.5% of commitments and
  disbursements traceable. The upward one is `transaction_traceability` in IATI
  Stats' `analytics.py`, which looks for `provider-org/@provider-activity-id` on
  incoming funds — note that it currently passes automatically when the activity
  comes from a donor publisher, which is precisely the automatic credit the proposal
  removes.

- **4.7 Organisation identifiers** — the proposal assesses whether organisations are
  using correctly structured organisation identifiers. Annex 4 scores this as "the
  proportion of relevant participating organisations that have valid references",
  averaged across an organisation's activities, so it is a proportion rather than a
  per-activity pass or fail. It needs only activity files, but it needs all of them.

  IATI Stats already calculates it, per publisher and per organisation role:

      /stats/current/aggregated-publisher/<publisher>/
        implementing_org_transaction_stats.json
        receiver_org_transaction_stats.json

  Each returns `total_orgs`, `total_refs`, `total_valid_refs`, `total_full_refs` and
  `total_notself_refs`, so the score is `total_valid_refs / total_orgs`. For GAC that
  was 6,387 of 8,782 implementing organisations, i.e. 72.7% carrying a valid
  reference.

  Before using these figures, note that the IATI Stats calculation is **not
  restricted to current activities**: `_transaction_org_stats` iterates every
  transaction of every activity, with no filter on activity status or date, and
  nothing filters the activities before it is called. Every other indicator here is
  scoped by `And the activity is current`, so as things stand 4.7 would be measured
  over a different population from the rest of the framework — counting
  organisations from activities that closed years ago. The same question applies to
  the traceability figures behind 3.3, which have not been checked.
- **Publisher-type exclusions on 1.3 to 1.8 are not implemented.** The Organisation
  component carries notes [1], [2] and [3]: INGOs and NGOs excluded from 1.3, 1.4,
  1.5 and 1.8; NGOs excluded from 1.6; and NGOs assessed on the previous year rather
  than forward projections for 1.7. None of this is expressed, so every NGO publisher
  is currently marked down on indicators the proposal says should not apply to them.
  They can be written as ordinary guards on `reporting-org/@type`, which both
  `iati-activity` and `iati-organisation` carry, with no change to the runner. 1.7 is
  the awkward one: it needs two scenarios with complementary guards and a
  backward-looking `Then` step that does not exist yet.

## Open questions

- **What the thresholds should be.** Six tests are restricted to larger projects —
  4.6 Conditions, and documents 4.8.2 conditions, 4.8.3 tender, 4.8.4 contract,
  4.8.6 impact appraisal and 4.8.7 performance and evaluation. All six currently use
  a provisional 100,000 USD, which is a placeholder rather than a proposal: the
  proposal says only that the figure "would need to be consulted on". Worth settling
  both the figure and whether one figure suits all six — a project performance and
  evaluation document is a heavier ask of a publisher than a budget document, so they
  may not warrant the same cut-off.
- **Documents and organisation files.** The proposal notes that the document types
  assessed are those used by the ATI for government donors, and that further
  consultation is needed on which documents are relevant for other organisation types.
  These definitions should be treated as provisional.

## Conventions

- Feature-level tags (`@iati-activity`, `@iati-organisation`) record which kind of file
  a test applies to. Note that the pinned `bdd-tester` does not expose feature-level
  tags to scenarios at runtime — `Test.tags` is always empty — so nothing should depend
  on reading them back from the parser.
- Placeholder tests use `Given this test is not yet implemented`, which returns
  "not relevant" for every input. Note that this is indistinguishable, in the result,
  from a genuine publisher-type exclusion.
- Indicators the proposal restricts to larger projects carry the guard
  `And the activity value is at least 100000 USD`. The figure is a provisional
  placeholder: the proposal says the threshold "would need to be consulted on".
  The activity's value is expected to be calculated for the whole activity in
  advance, in USD, and passed to the runner as `activity_value` — working it out
  needs currency conversion and a decision about which transactions count, neither
  of which belongs in an individual test. **The runner does not supply it yet**, and
  until it does the step does not filter anything, so these tests behave exactly as
  they did before the threshold was added. See
  `tests/test_activity_value_threshold.py`, which pins down the behaviour with and
  without a value so it is not changed by accident.
- `` `X` is present `` guards a scenario on an element actually being there, so an
  indicator applies only where what it depends on exists: 4.4 uses it to filter out
  activities with no recipient country rather than failing them, and 2.9 uses it to
  validate country and region codes against their two separate codelists without
  marking down an activity that uses only one of the two. It is registered
  before the more general `` `X` is <const> `` step, because whichever pattern is
  registered first wins and `is present` would otherwise be read as a comparison
  against the literal string "present".
- Reference data that a test needs in line lives in `data/`, with its provenance in
  `data/README.md`. At present that is only the country-to-official-language map used
  by 4.4, vendored from IATI Stats and overridable by passing `country_languages`.
- `current_data.feature` defines the "activity is current" precondition shared by most
  activity-level tests. It is implemented in `step_definitions.py` rather than composed
  from the feature file.
