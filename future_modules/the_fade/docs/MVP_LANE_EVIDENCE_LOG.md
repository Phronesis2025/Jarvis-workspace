# MVP Lane Evidence Log (Phase 2)

**Prompt #:** 176  
**Phase #:** 2  
**Tranche #:** 41  

Updated: 2026-03-31T16:48:00+00:00

## Purpose

This document is an operator-facing place to record lane-level evidence against the **Phase 2 MVP approval gate** standard.

This log does **NOT** grant approval and does **NOT** change `approved` in `mvp_lane_approval.json`.

**Execution discipline (Prompt #134):** Remaining Phase **2** work order is **locked** in **`THE_FADE_PHASE2_REMAINING_GATE_PLAN.md`** — **Tranches 35/36/37/38/39/40/41 executed** under governed prompts; post-T39 **PATH B** decision stop remains locked (Lane E bootstrap paused). **Tranche 40 is governance/registry truth-closure only** and **Tranche 41 is bounded Lane C policy tracing only** (no live market-data integration). **Do not** treat this log as a license for ad-hoc tranche chains outside that plan.

## Approval authority (binding)

The only binding approval gate is:

`future_modules/the_fade/config/mvp_lane_approval.json`

Until that file is updated to `approved: true`, **no MVP lanes are approved**.

## Evidence-tracking authority

Use this registry to track evidence completeness across lanes:

`future_modules/the_fade/config/mvp_lane_evidence_registry.json`

## Candidate lanes under deferred review (same four lanes as the Phase 2 gate)

- `lane_a_public_signal`
- `lane_b_official_disclosure`
- `lane_c_market_context`
- `lane_e_research_swarm_context` (context-only evidence; must not override primary lane truth)

## Evidence dimensions (exact list)

For each lane, collect evidence for these dimensions:

- `reliability`
- `freshness`
- `normalization_viability`
- `stale_outage_behavior`
- `conflict_handling`
- `context_dominance_risk`

## Review format (record evidence per lane)

Use this format per lane. Fill the fields with operator observations; if something is unknown, write `unknown` and keep it explicit.

### Lane: `<lane_id>`

- Reliability:
  - evidence_summary:
  - pass/fail criteria reference:
  - notes:
- Freshness:
  - evidence_summary:
  - freshness window reference:
  - notes:
- Normalization viability:
  - evidence_summary:
  - silent-drop checks observed:
  - notes:
- Stale/outage behavior:
  - evidence_summary:
  - observed downgrade/escalation/omit behavior:
  - notes:
- Conflict handling:
  - evidence_summary:
  - how conflicts were resolved safely:
  - notes:
- Context dominance risk:
  - evidence_summary:
  - proof that context-only reads did not override primary truth:
  - notes:

## Status (current)

**Tranche 30 (Prompt #102):** Full-window Federal Register slot evidence is **captured on disk** and summarized in **Lane B full Tranche 21 Federal Register reliability window (Tranche 30 -- Prompt #102)** below. **`mvp_lane_approval.json`** remains **`approved: false`** unless and until that file is updated — this log does **not** grant approval. **Phase 3** remains **blocked**.

**Tranche 31 — freshness discipline executed (Prompt #121):** Bounded classification pass complete for the **22** full-window FR JSONL lines (**`t30_valid_002`** excluded). See **Lane B full Tranche 21 FR window — Tranche 31 freshness (Prompt #121)** below. **`mvp_lane_approval.json`** remains **`approved: false`** — this log does **not** grant approval. **Phase 3** remains **blocked**. Other gate dimensions remain **partial** until separately evidenced.

**Tranche 32 — ambiguity resolution executed (Prompt #129):** Cohort review complete for the **10** Tranche **31** **`cannot classify honestly`** rows — see **Lane B — Tranche 32 ambiguity resolution (Prompt #129)** below. **`mvp_lane_approval.json`** remains **`approved: false`**. **Phase 3** remains **blocked**.

Earlier sections remain **historical** unless this file explicitly points forward to a newer slice.

## Lane B full Tranche 21 FR window — Tranche 31 freshness (Prompt #121)

**Population:** **22** JSONL lines with `window_start_utc=2026-03-27T16:00:00Z` and `window_end_utc=2026-03-29T16:00:00Z`. **`task_id=t30_valid_002`** is **not** in this population.

**Freshness rule (operator-facing, narrow):**

- **Observation instant:** `actual_started_at_utc` from each JSONL line.
- **Publication date (source):** `publication_date` (YYYY-MM-DD) for **`results[0]`** in the Federal Register API JSON, taken from each run’s `*_tranche21_fr_slot_snapshot.json` field `response_preview_utf8` (first `"publication_date"` after the substring `"results":[{`).
- **Publication instant for age:** `T_pub` = that calendar date at **00:00:00 UTC** (API is date-only).
- **Age:** `Δ = T_obs − T_pub` (observation minus publication instant).
- **fresh:** `Δ ≥ 0` and `Δ ≤ 48 hours`.
- **stale:** `Δ > 48 hours`.
- **cannot classify honestly:** `Δ < 0` (observation is **before** the publication calendar day at UTC midnight). This happens when the **newest** document’s **`publication_date`** is **after** the observation instant (e.g. **advance / public-inspection** style listings in the feed). This is **not** labeled “stale” here — strict age math is **undefined** without time-of-day semantics from the API.

**Classification counts (22 rows):**

| Outcome | Count |
|--------|------:|
| fresh | 12 |
| stale | 0 |
| cannot classify honestly | 10 |

**Cannot-classify rows (all `Δ < 0` under the rule above):** `t21_fr_full_20260328T160000Z` through `t21_fr_full_20260329T100000Z` (10 consecutive slots). **Fresh rows:** earlier slots in the same window (12 rows) — see helper output in repo script `future_modules/the_fade/scripts/_tranche31_freshness_classify.py` for per-`task_id` detail.

**What Tranche 31 does not prove:** stale/outage **system** behavior at scale; normalization breadth; conflict handling; context-dominance; production-equivalent runtime; Phase 3 readiness; MVP approval.

## Tranche 32 — planned (Prompt #125)

**Cohort:** The **10** Tranche 31 **`cannot classify honestly`** rows: `t21_fr_full_20260328T160000Z` through `t21_fr_full_20260329T100000Z` (same full-window bounds; **`t30_valid_002`** still excluded from the **22**-line population).

**Purpose:** For each row, either (a) obtain a **defensible** fresh/stale (or explicitly named alternate) label using **supplementary verifiable facts**, or (b) record an **explicit gate limitation** (“unresolvable under available API fields / without new policy”) — **no** fabricated certainty.

**Evidence question:** Can every row in this cohort be assigned a **transparent** outcome **without** pretending the Tranche 31 midnight rule already resolved it?

**Candidate approaches (execution prompt may choose order):**

1. **Existing artifacts:** Re-read the **10** `*_tranche21_fr_slot_snapshot.json` files for any **non-preview** fields; confirm `document_number` / `publication_date` extraction against full JSON if available on disk.
2. **Bounded read-only follow-up:** Optional **public** Federal Register API document fetch by **`document_number`** (distinct values in cohort) — **no** new scheduled collector window; caps and URLs documented in the execution prompt.
3. **Honest limitation:** If (1)-(2) still leave ambiguity, **document** that lane B freshness under **advance listings** + **date-only** `publication_date` is **not** reducible to a binary fresh/stale for those rows without an **operator policy** statement (still **not** approval).

**Success:** Per-row row in this log (or audit) with **cited** basis **or** **explicit** unresolvable — **no** silent “all 22 fresh.”

**Non-success:** Claiming MVP approval; claiming the **freshness** dimension is **fully closed** while ambiguity remains hand-waved.

**Stop when:** All **10** rows have a documented outcome **or** a single honest **blocker** statement for the cohort.

**Still would not prove:** Normalization breadth; stale/outage **system** behavior; conflict; context dominance; Phase 3; MVP approval.

## Lane B — Tranche 32 ambiguity resolution (Prompt #129)

**Cohort (10 `task_id`s):** `t21_fr_full_20260328T160000Z`, `t21_fr_full_20260328T180000Z`, `t21_fr_full_20260328T200000Z`, `t21_fr_full_20260328T220000Z`, `t21_fr_full_20260329T000000Z`, `t21_fr_full_20260329T020000Z`, `t21_fr_full_20260329T040000Z`, `t21_fr_full_20260329T060000Z`, `t21_fr_full_20260329T080000Z`, `t21_fr_full_20260329T100000Z`.

**Evidence used:**

1. **Existing snapshots:** Each row’s `*_tranche21_fr_slot_snapshot.json` — **`results[0].document_number`** = **`2026-06133`** and **`results[0].publication_date`** = **`2026-03-30`** (from `response_preview_utf8`; first match after `"results":[{`) for **all 10** rows.
2. **Bounded read-only fetch (distinct document):** One **GET** to `https://www.federalregister.gov/api/v1/documents/2026-06133.json` at Tranche **32** execution. Response confirms **`publication_date`:** **`2026-03-30`**, **`effective_on`:** **`2026-03-30`**, **`signing_date`:** **`null`** — **no** sub-day **publication** instant in the **fields used for this gate review**.

**Tranche 31 rule unchanged:** `Δ = T_obs − (publication_date @ 00:00 UTC)` → **Δ < 0** for **every** cohort row (observation instants **2026-03-28**/**29** vs **publication** calendar **2026-03-30**).

**Per-row assignment (strict Tranche 31 buckets):** **still cannot classify honestly** — **all 10** rows. **Rationale (same for each):** supplementary document JSON **does not** provide a finer-grained **publication instant** that makes **`Δ ≥ 0`** under the **midnight** **`publication_date`** model; **reclassifying** as **fresh** or **stale** would require an **additional operator policy** for **advance / public-inspection “newest”** semantics (not adopted in this pass).

**Tranche-level totals after Tranche 32 (strict Tranche 31 rule, full-window 22 rows, `t30_valid_002` excluded):**

| Outcome | Count |
|--------|------:|
| fresh | 12 |
| stale | 0 |
| still cannot classify honestly | 10 |

**Remaining limitation (explicit):** For this **document** and **window**, **date-only** **`publication_date`** **plus** **advance** listing behavior **blocks** a **binary** **fresh/stale** label **under** the **Tranche** **31** **midnight** **rule** **without** **policy** **beyond** **this** **audit**.

**What Tranche 32 does not prove:** normalization breadth; stale/outage **system** behavior; conflict; context dominance; Phase **3** readiness; MVP approval.

## Lane B — Tranche 33 freshness policy comparator (Prompt #131)

**Purpose:** Operator-visible **comparison** of **explicit** freshness-policy interpretations on the **same** **22** full-window FR rows (**`t30_valid_002`** excluded) using **stored** JSONL + snapshots **only** (**no** network in the script).

**Artifacts (reproducible):**

- Script: `future_modules/the_fade/scripts/compare_tranche31_freshness_policies.py`
- Outputs: `future_modules/the_fade/outputs/lane_b_real_observation/tranche33_freshness_policy_comparison.json` and `.md`

**Policies implemented:** `strict_midnight_utc` (Tranche **31** rule), `publication_day_fresh`, `advance_listing_bucket`, plus `publication_end_of_day_utc`. Definitions and per-row matrix are in the `.md` / `.json`.

**Truth:** Comparator output alone is **policy exploration** — **not** MVP approval; **not** gate closure; **not** Phase **3** readiness; **`mvp_lane_approval.json`** unchanged.

## Lane B — Tranche 33 freshness policy decision (Prompt #132)

**Hard decision — `ADOPT_ONE_POLICY`:** The **operator-facing** Phase **2** Lane B (Federal Register) **freshness interpretation** for **binary** evidence scoring is **`strict_midnight_utc`** — the same rule as Tranche **31** (`T_pub` = `publication_date` @ **00:00 UTC**; **48h** window; **`cannot_classify_honestly`** when **Δ < 0**).

**Executable artifact (machine-readable):** `future_modules/the_fade/config/lane_b_phase2_freshness_policy_decision.json`

**Why this policy (least-bad honest choice):** Tranche **32** showed supplementary document JSON **does not** fix **Δ** under midnight anchoring for the **10**-row cohort. Comparator policies **`publication_day_fresh`** and **`publication_end_of_day_utc`** map **all 22** rows to **fresh** on this window — **overstating** binary freshness relative to the **documented** advance-listing + date-only field conflict. **`advance_listing_bucket`** is kept as **descriptive context only** (not adopted as the **primary** gate verdict). **Adopted** policy **preserves** **10**/**22** **`cannot_classify_honestly`** — **honest partiality** over **false completeness**.

**Park:** **Freshness-only** Phase **2** **tranche workstream** on this FR slice is **PARKED** — **no** further freshness-only tranches unless **governance** reopens or **evidence** **sources** **change** (e.g. sub-day timestamps). Other gate dimensions (normalization, stale/outage **system** behavior, etc.) remain **separately** governed.

**Still not:** MVP approval; whole-gate closure; Phase **3** unlock. **`mvp_lane_approval.json`** unchanged.

## Lane B — Tranche 34 normalization breadth audit (Prompt #133)

**Executable artifact:** `future_modules/the_fade/scripts/audit_lane_b_normalization_breadth.py`  
**Outputs:** `future_modules/the_fade/outputs/lane_b_real_observation/tranche34_normalization_breadth_audit.json` and `.md`  
**Grounding:** Field set from `run_tranche21_fr_slot.py` JSONL/snapshot contracts + **`results[0]`** fields used in **`response_preview_utf8`** (same path as freshness). **No** network.

**Findings (22 rows, `t30_valid_002` excluded):** JSONL **identity/timing/outcome** keys **complete**; **all** snapshots present; **`response_sha256`** present; **full** `json.loads` of **`response_preview_utf8`** **0**/**22** (truncated previews — **expected**); regex extraction of **`document_number`** in **`results[0]`** region **22**/**22**; **3** distinct **`document_number`** values across the window. **Rich** full-document normalization (complete JSON object, agencies, excerpts) **not** available from preview alone.

**Verdict:** Collector **shell** + **regex** identity fields are **solid** for this slice; **breadth** for full structured normalization is **partial** / **not closed** — **not** MVP approval; **not** gate closure.

## Lane E — Tranche 37 context non-dominance audit (Prompt #152)

**Scope:** THE FADE-local bounded fixture audit only (no network, no live Research Swarm integration).

**Grounding:** `lane_registry.json` contract for `lane_e_research_swarm_context`:
- `direction_model_default: CONTEXT_ONLY`
- `scoring_method: enrich_only`
- `failure_policy: omit_if_missing`

**Artifacts:**
- Script: `future_modules/the_fade/scripts/audit_lane_e_context_non_dominance.py`
- Fixtures: `future_modules/the_fade/examples/lane_e_context_bootstrap/tranche37_cases.json`
- Outputs: `future_modules/the_fade/outputs/lane_e_context_bootstrap/tranche37_lane_e_non_dominance_audit.json` and `.md`

**Explicit cases evaluated:**
1. `case_1_context_missing` — omission explicit when context is absent.
2. `case_2_context_supports_primary` — context agrees with primary lane direction.
3. `case_3_context_conflicts_primary` — context disagrees with primary lane direction.

**Case verdict summary:** all three cases passed bounded checks:
- `lane_e_remained_non_primary: true`
- `no_silent_override_of_primary_truth: true`
- missing-context omission explicitly recorded in case 1

**What this proves now:** bounded non-dominance/omission behavior for Lane E in local controlled cases.

**What this does not prove:** full Lane E gate closure, live Research Swarm integration behavior, production-scale fusion/runtime behavior, approval readiness, or Phase 3 readiness.

## Lane E — Tranche 38 freshness + omission trace audit (Prompt #157)

**Scope:** THE FADE-local bounded fixture audit only (no network, no live Research Swarm integration).

**Grounding:** same Lane E contract from `lane_registry.json`:
- `direction_model_default: CONTEXT_ONLY`
- `scoring_method: enrich_only`
- `failure_policy: omit_if_missing`

**Artifacts:**
- Script: `future_modules/the_fade/scripts/audit_lane_e_freshness_omission_trace.py`
- Fixtures: `future_modules/the_fade/examples/lane_e_context_bootstrap/tranche38_cases.json`
- Outputs: `future_modules/the_fade/outputs/lane_e_context_bootstrap/tranche38_lane_e_freshness_omission_audit.json` and `.md`

**Explicit cases evaluated:**
1. `case_1_fresh_context_present`
2. `case_2_stale_context_present`
3. `case_3_missing_context`
4. `case_4_borderline_window_edge`

**Case verdict summary:** all cases passed bounded checks with explicit fields:
- `freshness_classification` (`fresh` / `stale` / `missing`)
- `omission_explicit` (true for stale/missing)
- `no_primary_override: true` across all cases
- trace explanation per case for operator readability

**What this proves now:** bounded Lane E freshness + omission-trace semantics are explicit under a declared local freshness window.

**What this does not prove:** full Lane E gate closure, live Research Swarm integration behavior, production-scale runtime behavior, approval readiness, or Phase 3 readiness.

## Lane E — Tranche 39 normalization + omission-reason trace audit (Prompt #162)

**Scope:** THE FADE-local bounded fixture audit only (no network, no live Research Swarm integration).

**Grounding:** same Lane E contract from `lane_registry.json`:
- `direction_model_default: CONTEXT_ONLY`
- `scoring_method: enrich_only`
- `failure_policy: omit_if_missing`

**Artifacts:**
- Script: `future_modules/the_fade/scripts/audit_lane_e_normalization_omission_reason_trace.py`
- Fixtures: `future_modules/the_fade/examples/lane_e_context_bootstrap/tranche39_cases.json`
- Outputs: `future_modules/the_fade/outputs/lane_e_context_bootstrap/tranche39_lane_e_normalization_omission_reason_trace_audit.json` and `.md`

**Explicit cases evaluated:**
1. `case_1_fresh_valid_context`
2. `case_2_stale_context`
3. `case_3_missing_context`
4. `case_4_invalid_shape_context`

**Case verdict summary:** all cases passed bounded checks with explicit fields:
- `normalization_status` (`normalized` / `omitted`)
- `omission_reason` (`none` / `stale_context` / `missing_context` / `invalid_context_shape`)
- `omission_explicit` (true for omitted cases)
- `no_primary_override: true` across all cases
- concise trace explanation per case for operator readability

**What this proves now:** bounded Lane E normalization + omission-reason trace semantics are explicit across four controlled local cases.

**What this does not prove:** full Lane E gate closure, live Research Swarm integration behavior, production-scale runtime behavior, approval readiness, or Phase 3 readiness.

## Lane C — Tranche 41 FOLLOW + stale-policy trace audit (Prompt #176)

**Scope:** THE FADE-local bounded fixture audit only (no network, no live market-data integration).

**Grounding:** `lane_registry.json` contract for `lane_c_market_context`:
- `direction_model_default: FOLLOW`
- `failure_policy: invalidate_if_stale_vs_policy`
- `trust_tier: TBD_POST_APPROVAL`
- `freshness_class: TBD_POST_APPROVAL`

**Artifacts:**
- Script: `future_modules/the_fade/scripts/audit_lane_c_follow_stale_policy_trace.py`
- Fixtures: `future_modules/the_fade/examples/lane_c_market_context_bootstrap/tranche41_cases.json`
- Outputs: `future_modules/the_fade/outputs/lane_c_market_context_bootstrap/tranche41_lane_c_follow_stale_policy_trace_audit.json` and `.md`

**Explicit cases evaluated:**
1. `case_1_fresh_valid_market_context`
2. `case_2_stale_market_context`
3. `case_3_missing_market_context`
4. `case_4_invalid_shape_market_context`

**Case verdict summary:** all four cases passed bounded checks with explicit fields:
- `policy_outcome` (`accepted_follow` / `invalidated_omit`)
- `freshness_or_validity_status` (`fresh_valid` / `stale` / `missing` / `invalid_shape`)
- `omission_reason` (`none` / `stale_market_context` / `missing_market_context` / `invalid_market_context_shape`)
- `omission_explicit` (true for omitted cases)
- `no_hidden_override: true` across all cases
- concise trace explanation per case for operator readability

**What this proves now:** bounded Lane C FOLLOW + stale-policy semantics are explicit in local fixtures.

**What this does not prove:** live market-data reliability, full Lane C gate closure across all dimensions, production-scale runtime behavior, approval readiness, or Phase 3 readiness.

## Evidence entry: lane_b_official_disclosure (Tranche 4)

Lane name:
- Official / disclosure (MVP slot)

Evidence captured in this tranche:
- Preliminary operator evidence observations were recorded for `lane_b_official_disclosure` to start filling the Phase 2 gate dimensions.
- Approval remains NOT granted; this is evidence-in-progress only.

### Reliability
- evidence_summary: **Tranche 18 (Prompt #59)** tightened the honesty bar. The only **countable** real `observe` HTTPS attempts currently documented for lane B in this log are the **Tranche 16** session: **`t16_honest_001`-`t16_honest_003`** (`scout_failure`, HTTP **403** to SEC / issuer IR URLs in that environment) and **`t16_honest_005`** (**HTTP 200**, `normalized_signal_event` to Federal Register API). That is **four attempts**, **one success**, **three failures** -- a **single-session micro-sample**, **not** a calendar **pre-audit window** and **not** i.i.d. draws from one MVP provider. A naive success rate **1/4** does **not** meet **0.8**, and **must not** be used as a gate statistic: URL families and failure mechanisms differ (automation/policy 403 vs successful open API).
- pass/fail criteria reference: `required_reliability_threshold` **0.8** in `config/mvp_lane_approval.json` -- compare **only** once a **defined** pre-audit window and **comparable** adapter/source draws exist; **not** justified from current evidence.
- notes: **Partial / conservative.** See **Lane B reliability window evidence (Tranche 18)** below. Approval remains NOT justified.

### Freshness
- evidence_summary: **Tranche 31 (Prompt #121)** + **Tranche 32 (Prompt #129)** on the **22** full-window FR lines (**`t30_valid_002`** excluded): **12** **fresh**, **0** **stale**, **10** **still cannot classify honestly** — **explicit limitation** (see **Lane B — Tranche 32**). **Tranche 33 (Prompt #131)** **policy comparator** + **Prompt #132** **decision:** **adopt** **`strict_midnight_utc`** as **operator-facing** Phase **2** interpretation; **reject** **`publication_day_fresh`** / **`publication_end_of_day_utc`** as **primary** (overstate freshness on this window); **`advance_listing_bucket`** **not** primary — see **`lane_b_phase2_freshness_policy_decision.json`** and **Lane B — Tranche 33 freshness policy decision (Prompt #132)**. **Not** MVP approval; **not** gate closure.
- freshness window reference: **48 hours** max age (`Δ` from `publication_date` @ 00:00 UTC to `actual_started_at_utc`), plus **cannot_classify_honestly** when `Δ < 0` under **adopted** **`strict_midnight_utc`**.
- notes: Freshness remains **partial** (**10**/**22** **cannot_classify_honestly**); **freshness-only** tranche line **parked** per Prompt **#132**; **not** production stale/outage system proof.

### Normalization viability
- evidence_summary: **Tranche 34 (Prompt #133)** **normalization breadth audit** on **22** full-window FR lines (**`t30_valid_002`** excluded): JSONL + snapshot **metadata** consistent; **`document_number`** / **`publication_date`** extractable via **regex** from **`response_preview_utf8`** for **all** rows; **full** JSON parse of preview **0**/**22** (truncated). **3** distinct **`document_number`** values in-window. See **`tranche34_normalization_breadth_audit.json`**. **Not** gate-sufficient breadth for full rich document objects.
- silent-drop checks observed: Audit checks presence/parsability of grounded fields; **does not** prove silent-drop guarantees at scale.
- notes: Normalization **breadth** for Lane B on this slice remains **partial** — **not** approval; **not** Phase **3**.

### Stale/outage behavior
- evidence_summary: Tranche 12 captured **simulated harness rehearsal** stdout for Protocol A (see "Lane B simulated harness rehearsal (Tranche 12)" below). Inputs were **operator-authored**; the harness fetched **no external vendor data**. That output does **not** demonstrate real lane stale/outage `system behavior` for the gate; it only shows the harness can emit a constrained record when given those inputs. **Tranche 16 (Prompt #52)** added a **non-simulated** lane B `observe` run plus real `scout_failure` outcomes where HTTPS returned **403** (SEC.gov / issuer IR in this environment), and one **successful** `normalized_signal_event` from a **live** public regulatory disclosure API (Federal Register JSON). See "Lane B first honest non-simulated observation run (Tranche 16)" below.
- observed downgrade/escalation/omit behavior: **Recorded (bounded slice):** the real observation slice emits explicit `scout_failure` with `error_type: SOURCE_UNAVAILABLE` and HTTP 403 summaries for blocked fetches, and emits `normalized_signal_event` when bytes return (HTTP 200). This is **gate-honest real observation** for the adapter path; it is **not** full production scout runtime or a statistical outage study.
- notes: Tranche 16 advances **real** availability/staleness-classification evidence for the slice. Full pre-audit outage dominance vs `required_reliability_threshold` remains outstanding.

- Tranche 35 (Prompt #135 — executed): `audit_lane_b_stale_outage_escalation_alignment.py` + `tranche35_stale_outage_escalation_audit.{json,md}` audits whether stored Lane B evidence cleanly distinguishes stale/outage-relevant states and aligns with `escalation_policy.json` + collector semantics.
- Tranche 35 findings (grounded): on the **22-row FR full-window slice** (excluding `t30_valid_002`), `source_observation_success`, `collector_execution_success`, and `timing_valid_for_counted_slot_use` are **all True** — so escalation/policy failure handling is **not exercised** in the counted FR population. Stored `*_scout_failure.json` artifacts do represent outage as `error_type=SOURCE_UNAVAILABLE`, but no evidence exists yet for the other escalation-policy failure types or for `escalation_required` toggling.
- Verdict: stale/outage behavior is still **thin/ambiguous** for standard **#4** if restricted to the FR full-window slice; this is **not** gate closure and does **not** justify MVP approval.

### Conflict handling
- evidence_summary: Additional conflict-case situations were recorded within the captured lane B runs. In these cases, fusion/conflict handling preserved primary lane truth (no dominance by context-only enrichment was observed in the recorded outputs).
- how conflicts were resolved safely: context-only enrichment did not override primary lane truth in the recorded conflict cases; precedence remained safe. Still requires adversarial/permutation coverage to fully validate the gate standard.
- notes: Recorded partially / still in review. The current evidence improves coverage, but broader conflict-case permutations are still not established to gate-sufficient confidence.

### Context dominance risk
- evidence_summary: Tranche 12 captured **simulated harness rehearsal** stdout for Protocol B (see "Lane B simulated harness rehearsal (Tranche 12)" below). Inputs were **operator-authored**; the harness fetched **no external vendor data**. That output does **not** demonstrate real lane dominance/conflict `system behavior` for the gate; it only shows the harness can emit a constrained record when given those inputs. **Tranche 16** ran the **real** `conflict` subcommand against a **live** lane B artifact from Tranche 16 observe plus a **THE FADE-local, operator-authored** contra JSON (explicitly **not** live external research). See "Lane B first honest non-simulated observation run (Tranche 16)" below.
- proof that context-only reads did not override primary truth: **Recorded (bounded slice):** emitted `conflict_packet` states fusion precedence primary `lane_b_official_disclosure` and that context cannot override lane B (`fusion_policy.json` weights read-only). The contra input is **operator-authored** for mechanics only; it must **not** be read as external proof.
- notes: Tranche 16 provides real THE FADE-local precedence/conflict output tied to a real observe artifact. Broader adversarial permutations and production fusion remain outstanding.

## Lane B simulated harness rehearsal (Tranche 12)

Scope: `lane_b_official_disclosure` only. This section records **actual constrained harness stdout** from one Protocol A rehearsal and one Protocol B rehearsal, using operator-authored JSON inputs under:

`future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/tranche12_simulated_rehearsal/`

Classification (Prompt #42 correction):
- **Simulated harness rehearsal only** (operator-authored inputs; **no external/vendor data** fetched by the harness).
- **Not** real lane evidence **from this harness alone** for `stale_outage_behavior` or `context_dominance_risk` (the rehearsal does not satisfy those dimensions by itself). **Tranche 16** added separate bounded real slice evidence; see "Lane B first honest non-simulated observation run" below -- registry dimensions for those items are **recorded (bounded)**, not production-complete.
- Useful as **protocol rehearsal**, not as proof of production FADE behavior.

Discipline:
- These runs are **not** smoke-test fixtures (`protocol_a_lane_b_evidence.json` / `protocol_a_scenario.json` under the parent folder).
- These runs are **not** production FADE runtime evidence.
- No approval is implied.

### Protocol A -- `LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1` (simulated rehearsal stdout)

```json
{
  "_meta": {
    "title": "lane_b_controlled_evidence_observation",
    "harness": "lane_b_controlled_evidence_harness",
    "protocol": "LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1"
  },
  "observed_at": "2026-03-25T16:54:11.984222+00:00",
  "lane_id": "lane_b_official_disclosure",
  "result": {
    "scenario_name": "LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1",
    "evidence_item_timestamp": "2026-03-25T18:00:00-05:00",
    "stale_window_definition": "Lane B evidence older than 48h is stale for this controlled run.",
    "unavailable_condition_definition": "Simulated: disclosure feed returned HTTP 503 for 120s during replay window.",
    "observed_behavior": "downgrade",
    "input_fingerprint": "595f4dcf7c1544511336ce97333b8598c05eb6ca566addb5288b8e4707522a26"
  },
  "notes": "Harness output is constrained to protocol-bounded fields; no external data was fetched. This is not an approval statement."
}
```

### Protocol B -- `LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1` (simulated rehearsal stdout)

```json
{
  "_meta": {
    "title": "lane_b_controlled_evidence_observation",
    "harness": "lane_b_controlled_evidence_harness",
    "protocol": "LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1"
  },
  "observed_at": "2026-03-25T16:54:12.319887+00:00",
  "lane_id": "lane_b_official_disclosure",
  "result": {
    "scenario_name": "LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1",
    "primary_truth_source": "lane_b_official_disclosure",
    "context_only_source": "lane_e_research_swarm_context",
    "conflict_description": "Controlled conflict: lane B direction disagrees with context-only enrichment for this run.",
    "precedence_result": "lane_b_remained_primary",
    "primary_evidence_item_timestamp": "2026-03-25T18:05:00-05:00",
    "context_only_evidence_item_timestamp": "2026-03-25T18:05:01-05:00",
    "input_fingerprint": "b7653fa2ea354773f3888d9bc7bbe40afb59e81124aabb037188dc0f19a9a236"
  },
  "notes": "Harness output is constrained to protocol-bounded fields; no external data was fetched. This is not an approval statement."
}
```

## Lane B controlled evidence protocol (operator checklist)

This protocol defines the **minimum controlled evidence** required to clear the current honest blocker for `lane_b_official_disclosure` without claiming runtime readiness or flipping approval.

### Protocol A -- Controlled stale/unavailable incident replay (timestamps required)

- scenario_name: `LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1`
- preconditions:
  - Lane under test is `lane_b_official_disclosure`.
  - Approval gate remains unchanged (`config/mvp_lane_approval.json` has `approved:false`).
  - Evidence is being recorded only (no runner/scanner/dashboard-contract work).
- required_inputs_artifacts:
  - A lane-B evidence sample where the lane is intentionally made stale/unavailable (operator-controlled).
  - The resulting system observation record written into this log entry (not a code output file).
- required_timestamps_fields_to_capture (must be written in the log):
  - `observed_at` (ISO8601)
  - `evidence_item_timestamp` (ISO8601) if any stale evidence item exists
  - `stale_window_definition` (plain text; e.g. "older than X minutes/hours/days is stale")
  - `unavailable_condition_definition` (plain text; what "unavailable" meant in this controlled test)
  - `observed_behavior` (one of: downgrade / escalate / omit) and any follow-on action taken
- expected_allowed_outcomes:
  - The system **does not fabricate** values.
  - The system behavior is **explicit**: it either downgrades confidence, escalates, or omits lane B evidence, consistent with the Phase 2 gate standard.
- disallowed_outcomes:
  - Any fabricated evidence content.
  - Silent substitution where missing/stale lane B evidence is replaced with non-lane-B truth without explicit labeling.
  - Context-only enrichment becoming precedence because lane B is missing/stale.
- gate_sufficient_evidence (minimum bar for this protocol):
  - A recorded, timestamped controlled stale/unavailable replay with explicit `observed_behavior` and a clear stale/unavailable definition (not "no incident observed").
- still_insufficient_evidence:
  - "No stale/outage observed in sampling."
  - Any replay without timestamps or without explicit behavior outcomes.

### Protocol B -- Context-dominance adversarial/conflict-case (explicit outcomes required)

- scenario_name: `LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1`
- preconditions:
  - Lane under test is `lane_b_official_disclosure`.
  - Context-only enrichment source is present (conceptually "lane_e_research_swarm_context") but must remain non-dominating.
  - Approval gate remains unchanged (`approved:false`).
- required_inputs_artifacts:
  - A constructed conflict-case where:
    - lane B primary truth indicates outcome \(X\), and
    - context-only enrichment indicates contradictory outcome \(Y\)
  - The resulting decision/precedence observation recorded in this log entry.
- required_timestamps_fields_to_capture (must be written in the log):
  - `observed_at` (ISO8601)
  - `primary_truth_source` (must name lane B as primary)
  - `context_only_source` (must indicate context-only)
  - `conflict_description` (plain text)
  - `precedence_result` (plain text; must state lane B remained primary)
- expected_allowed_outcomes:
  - Context-only enrichment may be additive/annotative but never becomes precedence over lane B primary truth.
  - Conflict is recorded as conflict/contra rather than silently resolved in favor of context-only.
- disallowed_outcomes:
  - Any output where context-only enrichment becomes the deciding/primary truth over lane B in a conflict-case.
  - Silent override without explicit conflict recording.
- gate_sufficient_evidence (minimum bar for this protocol):
  - A recorded adversarial/conflict-case with explicit precedence outcome showing context-only remains non-dominating under gate conditions.
- still_insufficient_evidence:
  - "No dominance override detected in sampling."
  - Any case without an explicit conflict and explicit precedence statement.

## Protocol execution status (Tranche 10)

Outcome: **SIMULATED REHEARSAL EXECUTED (TRANCHE 12 -- HARNESS ONLY)** (no approval flip; see Tranche 12 section -- **not** real lane evidence for gate dimensions).

Execution path now exists (bounded harness):
- Harness script: `future_modules/the_fade/scripts/lane_b_controlled_evidence_harness.py`
- Example fixtures: `future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/`

Important: Running the harness produces a JSON observation for copy/paste into this log; it does not fetch real vendor data and does not grant approval.

Operator usage (Protocol A):
- Edit/create your lane B evidence + scenario JSONs (or start from the fixtures), then run:
  - `python future_modules/the_fade/scripts/lane_b_controlled_evidence_harness.py --protocol A --lane-b-evidence future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/protocol_a_lane_b_evidence.json --protocol-a-scenario future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/protocol_a_scenario.json`
- Paste the emitted JSON observation into the lane B section of this log.

Operator usage (Protocol B):
- Edit/create your primary/context/scenario JSONs (or start from the fixtures), then run:
  - `python future_modules/the_fade/scripts/lane_b_controlled_evidence_harness.py --protocol B --lane-b-primary future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/protocol_b_lane_b_primary_truth.json --context-only future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/protocol_b_context_only_signal.json --protocol-b-scenario future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/protocol_b_scenario.json`
- Paste the emitted JSON observation into the lane B section of this log.

Hardening note:
- The harness **rejects unknown fields** in the input JSONs (allowlist only) and emits only protocol-bounded fields.
- Protocol B `precedence_result` is constrained to: `lane_b_remained_primary` (any other value fails loudly).

Confidence level / limits:
- confidence: 0.45
- limits: Tranche 12 remains **simulated harness rehearsal only** for stale/dominance. **Tranche 16** adds **bounded real** slice evidence (see Tranche 16 section). **Tranche 18** documents reliability as **partial** (micro-sample only; no 0.8 test). Lane B remains **not gate-ready**: no defined pre-audit reliability window; conflict handling still lacks broader permutations; production-equivalent scout runtime is not established.

Decision signal:
- insufficient_for_gate_decision_pending_remaining_dimension_evidence

What is still missing before approval could be considered:
- reliability: **Tranche 18** documented the Tranche 16 micro-sample explicitly; **no** honest 0.8 comparison yet -- need defined pre-audit window + comparable draws (see "Lane B reliability window evidence (Tranche 18)")
- freshness: finalize and fully apply freshness window classification
- normalization_viability: expand silent-drop coverage
- stale_outage_behavior: Tranche 16 recorded **bounded real** slice behavior (see Tranche 16 section); full pre-audit outage statistics still outstanding
- conflict_handling: broaden conflict-case permutations and record explicit safe precedence checks aligned to the Phase 2 gate standard
- context_dominance_risk: Tranche 16 recorded **bounded real** slice behavior (see Tranche 16 section); broader adversarial coverage still outstanding

## Real evidence path spec (Tranche 14)

Normative path definition:

`future_modules/the_fade/docs/LANE_B_MINIMAL_REAL_EVIDENCE_PATH_SPEC.md`

Prompt #48 correction: the spec is **fully inside THE FADE** (no `research_swarm/` or other module dependency). Context/precedence uses a **THE FADE-local operator-placed contra file**; honesty rules for that file are stated in the spec.

The harness (`lane_b_controlled_evidence_harness.py`) remains **rehearsal-only** and does not satisfy that spec.

## Lane B real observation slice (Tranche 15 -- implementation exists)

Script: `future_modules/the_fade/scripts/lane_b_real_observation_slice.py`

- **observe:** reads one real **HTTPS URL** or **local file path** �?�?�?¢�?¢â�??¬�? �?¢â�??¬â�??¢ writes `future_modules/the_fade/outputs/lane_b_real_observation/{task_id}_scout_failure.json` **or** `{task_id}_normalized_signal_event.json` (stdout prints the same object).
- **conflict:** reads one **lane B artifact** (normalized JSON from observe) + one **THE FADE-local** `context_only_contra` JSON (`semantic_role` = `lane_e_research_swarm_context`) �?�?�?¢�?¢â�??¬�? �?¢â�??¬â�??¢ writes `{task_id}_conflict_packet.json`; uses `config/fusion_policy.json` **read-only** for weight wording.

**Smoke tests** (developer-run, not gate approval): file read + `https://example.com` fetch + conflict against `inputs/lane_b_real_evidence/context_only_contra.example.json` succeeded locally. **This does not substitute for operator gate evidence** using a real disclosure URL/file and honest contra provenance -- it only proves the slice runs.

Operator usage (see also `inputs/lane_b_real_evidence/README_operator.txt`):

```text
python future_modules/the_fade/scripts/lane_b_real_observation_slice.py observe --task-id <TASK> --ticker <SYM> --file <path> --out-dir future_modules/the_fade/outputs/lane_b_real_observation
python future_modules/the_fade/scripts/lane_b_real_observation_slice.py observe --task-id <TASK> --ticker <SYM> --url <https://...> --out-dir future_modules/the_fade/outputs/lane_b_real_observation
python future_modules/the_fade/scripts/lane_b_real_observation_slice.py conflict --task-id <TASK> --ticker <SYM> --lane-b-artifact <normalized.json> --contra <context_only_contra.json> --out-dir future_modules/the_fade/outputs/lane_b_real_observation
```

Ephemeral `*.json` outputs under `outputs/lane_b_real_observation/` are gitignored by default (see `.gitignore` there).

## Lane B first honest non-simulated observation run (Tranche 16 -- Prompt #52)

**Classification:** Phase 2 lane B only; **not** approval; **not** scanner; **not** multi-lane.

### Provenance separation (required)

| Kind | What it is | This run |
|------|------------|----------|
| **Real lane B observation** | External anchor: bytes read via `observe` from a live HTTPS URL (or an honest local file path), with traceable URL/path and outcome class | **Primary:** `task_id=t16_honest_005`, URL `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`, Federal Register public API (official U.S. government disclosure index JSON). HTTP **200**, `normalized_signal_event` written. **Supplementary real availability observations:** `t16_honest_001`-`t16_honest_003` against SEC / issuer IR URLs returned **403** `scout_failure` in this environment (honest `SOURCE_UNAVAILABLE`, not rehearsed JSON). |
| **Operator-authored contra** | THE FADE-local `semantic_role: lane_e_research_swarm_context`; **not** live external proof | `future_modules/the_fade/inputs/lane_b_real_evidence/context_only_contra.tranche16_operator_authored.json` -- labeled in-file as operator-authored for precedence mechanics only. |

**Not used as real lane-B disclosure content for this run:** `inputs/lane_b_real_evidence/sample_disclosure_stub.txt` (stub only). **Not used as Tranche 16 contra:** `context_only_contra.example.json` (shape reference / smoke only). **Not claimed as real evidence:** Tranche 12 harness rehearsal blocks in this log.

Freshness window for observe classification in tool: default `--stale-after-hours 48` (see script); `t16_honest_005` classified `lag_class: fresh` (`freshness_hours: 0.0`).

### Exact recorded output -- `observe` (`t16_honest_005`)

Authoritative JSON file (under `outputs/lane_b_real_observation/`; gitignored): `t16_honest_005_normalized_signal_event.json` -- same object as stdout from the run. Full payload includes `raw_text` (API body, truncated in tool after 8k chars per script). **SHA256** of raw bytes and HTTP metadata appear in `notes` on the artifact.

### Exact recorded output -- `conflict` (`t16_honest_005`)

Authoritative JSON file: `t16_honest_005_conflict_packet.json`

```json
{
  "conflict_packet_id": "cf_t16_honest_005_015e5148ff6d",
  "task_id": "t16_honest_005",
  "ticker": "FR",
  "created_at": "2026-03-25T18:41:33Z",
  "summary": "fusion_policy lane_weight_hints: lane_b_official_disclosure=1.0, lane_e_research_swarm_context=0.2; precedence: primary=lane_b_official_disclosure; context cannot override lane B. direction_hint lane_b='neutral' context_role='bearish' mismatch=True.",
  "conflict_reasons": [
    "lane_b_vs_context_role_under_fusion_policy",
    "direction_hint_mismatch=True"
  ],
  "evidence_paths": [
    "C:\\dev\\jarvis-workspace\\future_modules\\the_fade\\outputs\\lane_b_real_observation\\t16_honest_005_normalized_signal_event.json",
    "C:\\dev\\jarvis-workspace\\future_modules\\the_fade\\inputs\\lane_b_real_evidence\\context_only_contra.tranche16_operator_authored.json"
  ],
  "notes": "THE FADE local slice; no research_swarm/ read."
}
```

**Approval:** unchanged -- `mvp_lane_approval.json` remains `approved: false`. This run does **not** justify flipping approval.

## Lane B reliability window evidence (Tranche 18 -- Prompt #59)

**Scope:** Lane B only; **reliability** dimension; **no** new observe runs in this pass -- analysis of what is already logged.

### What is actually evidenced

| Item | Value |
|------|--------|
| **Calendar pre-audit window** | **Not evidenced.** No start/end dates or scheduled sampling plan is recorded for lane B. |
| **Bounded session window (Tranche 16)** | Single operator session **2026-03-25** (UTC) encompassing the logged `observe` tasks below. |
| **Countable HTTPS `observe` attempts (this log)** | **4** -- `t16_honest_001`, `t16_honest_002`, `t16_honest_003`, `t16_honest_005`. |
| **Successes** | **1** -- `t16_honest_005` (HTTP 200, Federal Register API). |
| **Failures** | **3** -- `t16_honest_001`-`003` (HTTP **403**, `SOURCE_UNAVAILABLE` / `scout_failure`). |
| **Inferred vs evidenced** | **Evidenced:** discrete outcomes per task_id above. **Not evidenced:** population failure rate, steady-state availability, or dominance over a multi-day window. |

### Comparison to `required_reliability_threshold` (0.8)

**Not honestly justified today.** The gate requires reliability **during the pre-audit window** against **0.8** (`mvp_lane_approval.json`). We have **no** defined pre-audit window execution for lane B and **no** statistically meaningful sample from a **single** MVP disclosure adapter. A raw **1/4** success ratio **does not** support a pass and **must not** be read as the lane's reliability.

### Conclusion

Reliability for `lane_b_official_disclosure` stays **conservative / partial** for approval purposes until a **named window** and **comparable** repeated observations (or a clearly scoped pilot against one target source) are recorded.

## Lane B provider / source path (Tranche 19 -- Prompt #61)

**Scope:** Clarify what lane B's **provider story** is today -- **no** new `observe` runs in this pass.

### What is actually defined

| Item | State |
|------|--------|
| **Locked MVP provider in `mvp_lane_approval.json`** | **Not defined.** `official_disclosure_lane.provider_key` is **`TBD_OFFICIAL_DISCLOSURE_PROVIDER`** -- placeholder only. |
| **Single provider path for reliability statistics** | **No.** Until one **source class** is chosen for sampling, mixed URLs must **not** be read as one adapter. |

### What polluted the evidence story (Tranche 16)

The session logged **four** HTTPS tries that mixed **different source classes**:

| Class | Examples in log | Outcome in environment |
|-------|-----------------|-------------------------|
| **U.S. Federal Register public API** | `t16_honest_005` -- `www.federalregister.gov` API JSON | HTTP **200**, normalized event |
| **SEC / EDGAR / sec.gov** | `t16_honest_001`, `t16_honest_003` | HTTP **403** (automation policy) |
| **Issuer investor relations** | `t16_honest_002` (e.g. Apple IR) | HTTP **403** |

Aggregating these into **one** success/failure tally **without** separating provider class **pretends** there is a single lane-B disclosure feed -- there is **not** in this log.

### Smallest honest next target (one provider / source class only)

For the **next** bounded reliability pass (when the operator runs new evidence), use **one class** end-to-end in that pass:

- **Provisional class:** **U.S. Federal Register public API** -- `https://www.federalregister.gov/api/v1/...` (same **host + API family**; query parameters may vary).
- **Rationale (bounded, not a product commitment):** It is the **only** class in Tranche 16 that returned **HTTP 200** with the current `lane_b_real_observation_slice.py` client; it is a **single coherent** official public-disclosure channel (federal regulatory index). It is **not** issuer EDGAR HTML, not issuer IR -- different classes.
- **What this is not:** A claim that MVP lane B **must** be Federal Register forever, or that SEC/issuer paths are rejected -- only that **reliability sampling must not mix** unrelated hosts in one statistic.

**Alternative class** (separate pass, separate log section): **SEC EDGAR / issuer disclosure** -- requires **declared** traffic per SEC guidance and is **not** interchangeable with Federal Register evidence.

**Approval:** unchanged -- `mvp_lane_approval.json` remains `approved: false`.

## Lane B single-source reliability slice (Tranche 20 -- Prompt #63)

**Scope:** Lane B reliability dimension only; **single** source-class discipline.

**Locked source class used for this pass:** U.S. Federal Register public API only (no SEC URLs, no issuer IR URLs, no mixed provider tally).

**Exact endpoint repeated (same host/API family):**
`https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`

### Exact attempts (countable evidence)
- Total attempts: **5** (`t20_fb_001`, `t20_fb_002`, `t20_fb_003`, `t20_fb_004`, `t20_fb_005`)
- Successes: **5** (each produced `event_id` / `normalized_signal_event`, `lag_class: fresh`)
- Failures: **0** (`scout_failure` not emitted in this pass)

### Comparison to `required_reliability_threshold` (0.8)
Not honestly justified today. This pass documents a **bounded session micro-sample** and still does **not** provide a defined **calendar pre-audit window** or comparable adapter/source draws per the gate discipline. Therefore, we do **not** claim any pass/fail result against `0.8`.

### Resulting reliability wording/state
Reliability for `lane_b_official_disclosure` remains **partial / conservative** for gate purposes, pending a defined pre-audit window sampling plan.

**Approval remains not justified:** `mvp_lane_approval.json` is unchanged (`approved: false`).

## Lane B pre-audit reliability window -- live kickoff (Tranche 22 -- Prompt #67)

**Scope:** Lane B only; **Federal Register public API** at the **exact** URL from Tranche 21 protocol -- no SEC URLs, no issuer IR URLs, no other lanes.

**Protocol reference:** `docs/MVP_SOURCE_RELIABILITY_AUDIT.md` �?�?�?¢�?¢â�??¬�? �?¢â�??¬â�??¢ **Lane B pre-audit reliability window protocol (Tranche 21)** (stricter target -- **preserved**; **not** erased).

**Tranche 24 note:** The full **24-attempt UTC grid** below remains the **documented Tranche 21 standard**. Operator **real availability** no longer supports completing it; **remaining** executions are replanned under **Lane B availability-constrained interim pilot (Tranche 24 -- Prompt #73)** -- **not** a claim that the full pre-audit window is still being executed.

### Window bounds (UTC)

| Field | Value |
|-------|--------|
| `window_start_utc` | `2026-03-25T21:13:55Z` (ISO8601 UTC -- start of **attempt 0** `observe`; aligns with tool `ingested_at` / internal `created_at` at run start) |
| `window_end_utc` | `2026-03-27T21:13:55Z` (`window_start_utc` + **48 hours**, strict) |

### Full 24-attempt schedule (UTC) -- `window_start_utc + (i �?�?�?�??�?¢â�??¬â�?� 2h)` for `i = 0..23`

| i | Scheduled UTC |
|---|----------------|
| 0 | `2026-03-25T21:13:55Z` |
| 1 | `2026-03-25T23:13:55Z` |
| 2 | `2026-03-26T01:13:55Z` |
| 3 | `2026-03-26T03:13:55Z` |
| 4 | `2026-03-26T05:13:55Z` |
| 5 | `2026-03-26T07:13:55Z` |
| 6 | `2026-03-26T09:13:55Z` |
| 7 | `2026-03-26T11:13:55Z` |
| 8 | `2026-03-26T13:13:55Z` |
| 9 | `2026-03-26T15:13:55Z` |
| 10 | `2026-03-26T17:13:55Z` |
| 11 | `2026-03-26T19:13:55Z` |
| 12 | `2026-03-26T21:13:55Z` |
| 13 | `2026-03-26T23:13:55Z` |
| 14 | `2026-03-27T01:13:55Z` |
| 15 | `2026-03-27T03:13:55Z` |
| 16 | `2026-03-27T05:13:55Z` |
| 17 | `2026-03-27T07:13:55Z` |
| 18 | `2026-03-27T09:13:55Z` |
| 19 | `2026-03-27T11:13:55Z` |
| 20 | `2026-03-27T13:13:55Z` |
| 21 | `2026-03-27T15:13:55Z` |
| 22 | `2026-03-27T17:13:55Z` |
| 23 | `2026-03-27T19:13:55Z` |

**Discipline:** Future attempts **i = 1..23** are **not** executed or recorded in this pass -- operator runs them per schedule before `window_end_utc`. **Do not** fabricate outcomes.

### Executed in this pass only

| Attempt | `task_id` | Counted? | Outcome class | Notes |
|---------|-----------|----------|---------------|-------|
| **0** | `t22_fr_000` | **Yes** (valid JSON on stdout) | **`normalized_signal_event`** (success) | `event_id`: `evt_t22_fr_000_fc970c32455d`; endpoint `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`; HTTP **200**; `lag_class`: **fresh**; notes field records `http_status=200` and latency. |

**At Tranche 22 kickoff closure (attempt 0 only):** counted **1** (successes: **1**, failures: **0**).

**Honest comparison at kickoff:** **Not allowed** -- protocol requires **>= 20** counted attempts before any reliability ratio vs **0.8**; **23** scheduled attempts were **not** run in this kickoff pass.

**Update (Tranche 23 -- Prompt #71):** Cumulative counts under the **original UTC schedule** for attempts **0-1** are **2** / **2** successes / **0** failures -- see **attempt 1** below.

**Update (Tranche 24 -- Prompt #73):** **Do not** treat the test as an in-progress **full** 48h / 24-attempt pre-audit gate run. See **availability-constrained interim pilot** below for the **CDT** execution plan and honest limits.

**Approval:** unchanged -- `mvp_lane_approval.json` remains `approved: false`.

## Lane B pre-audit window -- attempt 1 (Tranche 23 -- Prompt #71)

**Scope:** Same locked window as Tranche 22 -- **do not** redefine `window_start_utc` / `window_end_utc`. Federal Register API only; endpoint unchanged.

### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `attempt_1_scheduled_utc` | `2026-03-25T23:13:55Z` (Tranche 22 schedule, `i = 1`) |
| `due_verified_at_utc` | `2026-03-25T23:29:06Z` |
| **Due?** | **Yes** -- `due_verified_at_utc` >= `attempt_1_scheduled_utc` |

### Attempt 1 -- observed result

| Field | Value |
|-------|--------|
| `task_id` | `t22_fr_001` |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t22_fr_001_fc970c32455d` |
| `ingested_at` (tool) | `2026-03-25T23:29:14Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes: `http_status=200 latency_ms=206.3`; `lag_class`: **fresh** |

### Cumulative counted results (original UTC schedule -- attempts 0-1 only)

| Metric | Value |
|--------|--------|
| Counted attempts | **2** |
| Successes | **2** (`t22_fr_000`, `t22_fr_001`) |
| Failures | **0** |

**Documented Tranche 21 bounds (audit trail):** `window_start_utc` **`2026-03-25T21:13:55Z`**, `window_end_utc` **`2026-03-27T21:13:55Z`** -- **not** asserted here as an active full-protocol completion commitment after **Tranche 24**.

**Honest comparison to `required_reliability_threshold` (0.8):** **Not allowed** from this slice -- counted **2** \< **20**; **no** pass/fail vs **0.8**. **Tranche 24** further records that the **interim pilot** caps total counted attempts at **8** even if all pilot slots run -- still **not** a valid **0.8** gate test.

**Approval:** unchanged -- `mvp_lane_approval.json` remains `approved: false`.

## Lane B availability-constrained interim pilot (Tranche 24 -- Prompt #73)

**Scope:** Lane B only; **Federal Register public API** at the **exact** Tranche 21 URL -- no SEC URLs, no issuer IR URLs, no other lanes.

**Honest reclassification:** Operator availability (**tonight:** remaining evening slot(s); **tomorrow:** ~**6:00 AM**-**3:00 PM** CDT, every **2 hours**) **cannot** satisfy the **full** Tranche 21 protocol (**48h**, **24** attempts, **>= 20** counted before **0.8**). This pilot is an **interim** plan -- **not** the original pre-audit gate window. The **stricter** Tranche 21 protocol text remains in `docs/MVP_SOURCE_RELIABILITY_AUDIT.md` and the **UTC grid** in this log (**not** erased).

### Revised execution plan (CDT)

| Pilot slot | Local time (CDT) |
|------------|------------------|
| Tonight (evening) | **8:13:55 PM** CDT -- **done** (Prompt **#75**, `t24_fr_pilot_01`) |
| Tomorrow | **6:13:55 AM** CDT -- **done** (Prompt **#78**, `t24_fr_pilot_02`) |
| Tomorrow | **8:13:55 AM** CDT -- **done** (Prompt **#80**, `t24_fr_pilot_03`) |
| Tomorrow | **10:13:55 AM** CDT -- **done** (Prompt **#82**, `t24_fr_pilot_04`) |
| Tomorrow | **12:13:55 PM** CDT -- **done** (Prompt **#86**, `t24_fr_pilot_05`) |
| Tomorrow | **2:13:55 PM** CDT -- **done** (Prompt **#88**, `t24_fr_pilot_06`) |

### Pilot slot 1 -- evening (Tranche 24 -- Prompt #75)

**Interim pilot only** -- **not** the full Tranche 21 gate window. Federal Register API **only**; endpoint unchanged.

#### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `pilot_slot_1_scheduled_cdt` | **2026-03-25 20:13:55** CDT (**8:13:55 PM** CDT) |
| `due_verified_at_utc` | `2026-03-26T01:53:24Z` |
| `due_verified_at_cdt` | **2026-03-25 20:53:24** CDT |
| **Due?** | **Yes** -- `due_verified_at_cdt` >= `pilot_slot_1_scheduled_cdt` |

#### Observed result

| Field | Value |
|-------|--------|
| `task_id` | **`t24_fr_pilot_01`** (**new** -- **not** reused from Tranche **22-23**) |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t24_fr_pilot_01_fc970c32455d` |
| `ingested_at` (tool) | `2026-03-26T01:53:54Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes include `http_status=200 latency_ms=236.3`; `lag_class`: **fresh** |

### Pilot slot 2 -- morning (Tranche 24 -- Prompt #78)

**Interim pilot only** -- **not** the full Tranche 21 gate window. Federal Register API **only**; endpoint unchanged.

#### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `pilot_slot_2_scheduled_cdt` | **2026-03-26 06:13:55** CDT (**6:13:55 AM** CDT) |
| `due_verified_at_utc` | `2026-03-26T11:15:52Z` |
| `due_verified_at_cdt` | **2026-03-26 06:15:52** CDT |
| **Due?** | **Yes** -- `due_verified_at_cdt` >= `pilot_slot_2_scheduled_cdt` |

#### Observed result

| Field | Value |
|-------|--------|
| `task_id` | **`t24_fr_pilot_02`** (**new** -- not reused from prior runs) |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t24_fr_pilot_02_ae4f0ce1ec02` |
| `ingested_at` (tool) | `2026-03-26T11:16:02Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes include `http_status=200 latency_ms=326.0`; `lag_class`: **fresh** |
 
### Pilot slot 3 -- morning (Tranche 24 -- Prompt #80)

**Interim pilot only** -- **not** the full Tranche 21 gate window. Federal Register API **only**; endpoint unchanged.

#### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `pilot_slot_3_scheduled_cdt` | **2026-03-26 08:13:55** CDT (**8:13:55 AM** CDT) |
| `due_verified_at_utc` | `2026-03-26T13:16:33Z` |
| `due_verified_at_cdt` | **2026-03-26 08:16:33** CDT |
| **Due?** | **Yes** -- `due_verified_at_cdt` >= `pilot_slot_3_scheduled_cdt` |

#### Observed result

| Field | Value |
|-------|--------|
| `task_id` | **`t24_fr_pilot_03`** (**new** -- not reused from prior runs) |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t24_fr_pilot_03_5fb099931df8` |
| `ingested_at` (tool) | `2026-03-26T13:16:45Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes include `http_status=200 latency_ms=328.8`; `lag_class`: **fresh** |

### Pilot slot 4 -- morning (Tranche 24 -- Prompt #82)

**Interim pilot only** -- **not** the full Tranche 21 gate window. Federal Register API **only**; endpoint unchanged.

#### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `pilot_slot_4_scheduled_cdt` | **2026-03-26 10:13:55** CDT (**10:13:55 AM** CDT) |
| `due_verified_at_utc` | `2026-03-26T15:29:38Z` |
| `due_verified_at_cdt` | **2026-03-26 10:29:38** CDT |
| **Due?** | **Yes** -- `due_verified_at_cdt` >= `pilot_slot_4_scheduled_cdt` |

#### Observed result

| Field | Value |
|-------|--------|
| `task_id` | **`t24_fr_pilot_04`** (**new** -- not reused from prior runs) |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t24_fr_pilot_04_5fb099931df8` |
| `ingested_at` (tool) | `2026-03-26T15:37:28Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes include `http_status=200 latency_ms=290.2`; `lag_class`: **fresh** |

### Pilot slot 5 -- midday (Tranche 24 -- Prompt #86)

**Interim pilot only** -- **not** the full Tranche 21 gate window. Federal Register API **only**; endpoint unchanged.

#### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `pilot_slot_5_scheduled_cdt` | **2026-03-26 12:13:55** CDT (**12:13:55 PM** CDT) |
| `due_verified_at_utc` | `2026-03-26T17:16:14Z` |
| `due_verified_at_cdt` | **2026-03-26 12:16:14** CDT |
| **Due?** | **Yes** -- `due_verified_at_cdt` >= `pilot_slot_5_scheduled_cdt` |

#### Observed result

| Field | Value |
|-------|--------|
| `task_id` | **`t24_fr_pilot_05`** (**new** -- not reused from prior runs) |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t24_fr_pilot_05_5fb099931df8` |
| `ingested_at` (tool) | `2026-03-26T17:16:23Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes include `http_status=200 latency_ms=239.0`; `lag_class`: **fresh** |

### Pilot slot 6 -- afternoon final slot (Tranche 24 -- Prompt #88)

**Interim pilot only** -- **not** the full Tranche 21 gate window. Federal Register API **only**; endpoint unchanged. This is the **final** scheduled slot of the Tranche 24 interim pilot.

#### Due-time check (before execution)

| Field | Value |
|-------|--------|
| `pilot_slot_6_scheduled_cdt` | **2026-03-26 14:13:55** CDT (**2:13:55 PM** CDT) |
| `due_verified_at_utc` | `2026-03-26T19:16:40Z` |
| `due_verified_at_cdt` | **2026-03-26 14:16:40** CDT |
| **Due?** | **Yes** -- `due_verified_at_cdt` >= `pilot_slot_6_scheduled_cdt` |

#### Observed result

| Field | Value |
|-------|--------|
| `task_id` | **`t24_fr_pilot_06`** (**new** -- not reused from prior runs) |
| Counted? | **Yes** (valid JSON on stdout) |
| Outcome class | **`normalized_signal_event`** (**success**) |
| `event_id` | `evt_t24_fr_pilot_06_5fb099931df8` |
| `ingested_at` (tool) | `2026-03-26T19:16:48Z` |
| Endpoint | `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest` |
| HTTP / notes | **200**; notes include `http_status=200 latency_ms=237.8`; `lag_class`: **fresh** |

## Lane B full Tranche 21 Federal Register reliability window (Tranche 30 -- Prompt #102)

**Governed post-run reconciliation.** Source of truth for machine-readable counts:  
`future_modules/the_fade/outputs/lane_b_real_observation/tranche21_fr_slot_runs.jsonl`  
Collector: `future_modules/the_fade/scripts/run_tranche21_fr_slot.py`.

### Full-window counted evidence (gate-relevant tally)

- **Declared window (UTC):** `window_start_utc` **`2026-03-27T16:00:00Z`**, `window_end_utc` **`2026-03-29T16:00:00Z`** (48h).
- **Counted full-window records:** **22**.
- **Successes (`source_observation_success: true`):** **22**.
- **Failures:** **0**.
- **Timing for counted-slot use:** all **22** have **`timing_valid_for_counted_slot_use: true`** and (where present) slot timing consistent with **`timing_valid`** / **`slot_timing_status: timing_valid`** per JSONL rows.

### Explicitly excluded from the 22-slot full-window tally

- **One** additional JSONL line records **`task_id: t30_valid_002`** under **different** `window_start_utc` / `window_end_utc` (out-of-window **smoke / harness**). **Do not** count it toward the full-window gate unless operator policy explicitly merges it.

### Latest full-window slot (chronological last among the 22)

| Field | Value |
|-------|--------|
| `task_id` | **`t21_fr_full_20260329T100000Z`** |
| `scheduled_slot_utc` | **`2026-03-29T10:00:00Z`** |
| `actual_started_at_utc` | **`2026-03-29T10:00:03Z`** |
| `source_observation_success` | **true** |
| `slot_timing_status` | **`timing_valid`** |

### Honest `required_reliability_threshold` (0.8) language (count floor only)

- Tranche 21 protocol allows documenting **`reliability = successes / counted_attempts`** vs **0.8** only when **`counted_attempts >= 20`**. Here, **full-window counted attempts = 22**, so **that numeric comparison is eligible to be stated** for **this slice only**: **22 / 22** observed on the logged outcomes.
- **This evidence does not equal MVP approval.** Binding approval remains **`mvp_lane_approval.json`** — still **`approved: false`**, **`approved_mvp_lanes: []`** until changed there. Other MVP dimensions (freshness discipline at scale, normalization breadth, stale/outage dominance, conflict permutations, context dominance, production-equivalent runtime) are **not** proven by this window alone.
- **Phase 3** stays **blocked**.

### Operator gate-review triage note (Prompt #103)

- **Current-review-now controls used at this checkpoint:** critic/adversarial review, audit-before-trust, and risk-first scrutiny against over-reading one strong full-window slice.
- **Future guardrails only:** auth/permission layering, isolated sub-account permissions, MCP-first infra filter with anti-affiliate rule, sim-first bridge, and position sizing/drawdown controls.
- **Parking lot only:** any concrete critic-agent build, MCP tooling build, exchange/live execution integration, or execution-adjacent implementation.
- **No state change from this triage:** lane B remains **promising-but-unapproved**; `mvp_lane_approval.json` remains **`approved: false`** with **`approved_mvp_lanes: []`**; **Phase 3 remains blocked**.
- **Final signoff lock (Prompt #113):** outcome re-validated with no approval flip; the strong FR full-window slice remains **22 counted / 22 successes / 0 failures** with **`t30_valid_002` excluded** from that tally.

### Counted-attempt ceiling (honest) -- historical pilot slice only

- **Tranche 22-23 (original UTC grid):** **2** (`t22_fr_000`, `t22_fr_001`).
- **Pilot slots executed:** **6** / **6** (`t24_fr_pilot_01`, `t24_fr_pilot_02`, `t24_fr_pilot_03`, `t24_fr_pilot_04`, `t24_fr_pilot_05`, `t24_fr_pilot_06`).
- **Cumulative counted (pilot slice only, before full window):** **8** (**8** successes, **0** failures). The **full Tranche 21 window** adds the **22** JSONL rows above — **separate** governed tally.

### What this pilot can and cannot prove (historical pilot slice)

- **Can (when this was current):** support a **go / no-go** on whether **continued** Federal Register lane B testing was worth scheduling before the full window existed.
- **Cannot (pilot-only):** the **8**-attempt pilot slice **alone** did **not** justify an honest **0.8** comparison or full pre-audit completion; **cannot** grant MVP approval.
- **Tranche 30 note:** The **full-window** **22** counted / **22** successes / **0** failures slice is documented **above**; use that section for gate-relevant Tranche 21 tallies.

**Approval:** unchanged -- `mvp_lane_approval.json` remains `approved: false` unless updated there.

ENDPOINT POINTER:
- Approval gate: `future_modules/the_fade/config/mvp_lane_approval.json`
- Evidence registry: `future_modules/the_fade/config/mvp_lane_evidence_registry.json`


