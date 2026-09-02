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
| 2.1 | Reporting Organisation | *not yet written* | — |
| 2.2 | IATI Identifier | `2_basic/2.2_iati_identifier.feature` | 25 |
| 2.3 | Implementing organisation (name and type) | `2_basic/2.3_implementing_organisation.feature` | 30 |
| 2.4 | Title | `2_basic/2.4_title.feature` | 16 |
| 2.5 | Description | `2_basic/2.5_description.feature` | 17 |
| 2.6 | Current status | `2_basic/2.6_current_status.feature` | 20 |
| 2.7 | Dates (start / end; planned / actual) | `2_basic/2.7_dates.feature` | 18, 19 |
| 2.8 | Sector | `2_basic/2.8_sector.feature` | 22, 15 |
| 2.9 | Country or region | *not yet written* | — |
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
| 4.4 | Recipient language | *not yet written* | — |
| 4.5 | Results | `4_advanced/4.5_results.feature` | 35 |
| 4.6 | Conditions | `4_advanced/4.6_conditions.feature` | 24 |
| 4.7 | Organisation identifiers | `4_advanced/4.7_organisation_identifiers.feature` | 30 |
| 4.8 | Documents | `4_advanced/4.8_documents/` | see below |

### 4.8 Documents

| # | Test | File | ATI test |
| --- | --- | --- | --- |
| 4.8.1 | Budget | `4.8_documents/4.8.1_budget.feature` | 12 |
| 4.8.2 | Conditions | `4.8_documents/4.8.2_conditions.feature` | 24 |
| 4.8.3 | Tender | `4.8_documents/4.8.3_tender.feature` | 31 |
| 4.8.4 | Contract | `4.8_documents/4.8.4_contract.feature` | 31 |
| 4.8.5 | Objectives | `4.8_documents/4.8.5_objectives.feature` | 32 |
| 4.8.6 | Pre- and/or post-project impact appraisal | `4.8_documents/4.8.6_impact_appraisal.feature` | 33 |
| 4.8.7 | Project performance and evaluation | `4.8_documents/4.8.7_performance_and_evaluation.feature` | 34 |
| 4.8.8 | Results | `4.8_documents/4.8.8_results.feature` | 35 |

## Still to do

Tests that the proposal requires but which have no definition yet — placeholders for
these are the next step:

- **2.1 Reporting Organisation** — no test exists; `reporting-org/@ref` is currently
  only referenced from within the IATI Identifier test.
- **2.9 Country or region** — no test exists.
- **4.4 Recipient language** — no test exists. Title and description should be in one
  of the recipient country's official languages.

Existing definitions that the proposal changes, flagged with `TODO` comments in the
files themselves:

- **2.3 Implementing organisation** — currently checks `@ref` or narrative only; the
  proposal also requires assessing `participating-org/@type`.
- **3.3 Traceability** — currently a placeholder that skips (it needs both organisation
  and activity files). The proposal redefines it as the share of a publisher's spend
  traceable to downstream partners, with the direction of traceability depending on
  publisher type. The Dashboard already runs these tests so we need to find a way to pull them in.
- **4.7 Organisation identifiers** — currently a placeholder that skips. The proposal
  requires assessing whether organisation identifiers are correctly structured. The Dashboard already runs these tests so we need to find a way to pull them in.

## Open questions

- **Publisher type.** Several indicators in the proposal carry publisher-type rules —
  INGOs or NGOs excluded, forward budgets assessed as previous-year for NGOs,
  traceability direction varying by organisation type. These can be expressed
  directly in Gherkin: both `iati-activity` and `iati-organisation` carry
  `reporting-org/@type`, which holds the OrganisationType code the proposal's rules
  key on (10-15 government, 21-24 NGO, 30/40 multilateral, 60 foundation, 70+ private
  sector). The existing `is one of` / `is not any of` steps handle it with no change
  to the runner, and an excluded activity returns "not relevant" rather than a
  failure, which is what the weighting rule requires. Where a rule changes the
  assertion rather than just filtering — note [3] on 1.7, where NGOs are assessed on
  the previous year rather than forward projections — it becomes two scenarios with
  complementary guards.

  Two things still need deciding:

  - `reporting-org/@type` is optional, and `is one of` treats an absent value as
    passing. An activity with no `@type` therefore satisfies *both* sides of a
    complementary pair of guards, and would be counted under each. Either the guard
    steps need a stricter variant, or missing `@type` needs a defined default.
  - `@type` is self-declared per file and can disagree with the organisation type
    registered for that publisher on the IATI Registry. Since the Dashboard groups
    publishers by type, which of the two is authoritative should be settled before
    these guards are written.
- **`4.2_location_activity_scope_exclusion.feature`** duplicates the location test with
  an additional `activity-scope` exclusion. Annex 4 of the proposal specifies the
  location test without it. One of the two should be dropped.
- **Documents and organisation files.** The proposal notes that the document types
  assessed are those used by the ATI for government donors, and that further
  consultation is needed on which documents are relevant for other organisation types.
  These definitions should be treated as provisional.

## Conventions

- Feature-level tags (`@iati-activity`, `@iati-organisation`) record which kind of file
  a test applies to. Note that the pinned `bdd-tester` does not expose feature-level
  tags to scenarios at runtime — `Test.tags` is always empty — so nothing should depend
  on reading them back from the parser.
- `current_data.feature` defines the "activity is current" precondition shared by most
  activity-level tests. It is implemented in `step_definitions.py` rather than composed
  from the feature file.
