# MVP Lane Evidence Log (Phase 2)

**Prompt #:** 86  
**Phase #:** 2  
**Tranche #:** 24  

Updated: 2026-03-26T12:16:32.0994279-05:00

## Purpose

This document is an operator-facing place to record lane-level evidence against the **Phase 2 MVP approval gate** standard.

This log does **NOT** grant approval and does **NOT** change `approved` in `mvp_lane_approval.json`.

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

This log is created for evidence collection. As of creation, evidence is expected to be recorded by the operator before any MVP approval change.

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
- evidence_summary: Evidence timestamps were present in the observed outputs and could be classified for freshness vs staleness using a planned freshness window.
- freshness window reference: Defined later by the operator in the log (align to `MVP_SOURCE_RELIABILITY_AUDIT.md` freshness discipline).
- notes: Recorded. Still requires full application of the freshness window definition.

### Normalization viability
- evidence_summary: Normalization produced candidate normalized events without obvious silent drops in the observed sample.
- silent-drop checks observed: Limited sample. Silent-drop guarantees require more coverage.
- notes: Recorded. More normalization runs are needed before treating this as gate-sufficient.

### Stale/outage behavior
- evidence_summary: Tranche 12 captured **simulated harness rehearsal** stdout for Protocol A (see "Lane B simulated harness rehearsal (Tranche 12)" below). Inputs were **operator-authored**; the harness fetched **no external vendor data**. That output does **not** demonstrate real lane stale/outage `system behavior` for the gate; it only shows the harness can emit a constrained record when given those inputs. **Tranche 16 (Prompt #52)** added a **non-simulated** lane B `observe` run plus real `scout_failure` outcomes where HTTPS returned **403** (SEC.gov / issuer IR in this environment), and one **successful** `normalized_signal_event` from a **live** public regulatory disclosure API (Federal Register JSON). See "Lane B first honest non-simulated observation run (Tranche 16)" below.
- observed downgrade/escalation/omit behavior: **Recorded (bounded slice):** the real observation slice emits explicit `scout_failure` with `error_type: SOURCE_UNAVAILABLE` and HTTP 403 summaries for blocked fetches, and emits `normalized_signal_event` when bytes return (HTTP 200). This is **gate-honest real observation** for the adapter path; it is **not** full production scout runtime or a statistical outage study.
- notes: Tranche 16 advances **real** availability/staleness-classification evidence for the slice. Full pre-audit outage dominance vs `required_reliability_threshold` remains outstanding.

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
| Tomorrow | **2:13:55 PM** CDT |

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
### Counted-attempt ceiling (honest)

- **Tranche 22-23 (original UTC grid):** **2** (`t22_fr_000`, `t22_fr_001`).
- **Pilot slots executed:** **5** / **6** (`t24_fr_pilot_01`, `t24_fr_pilot_02`, `t24_fr_pilot_03`, `t24_fr_pilot_04`, `t24_fr_pilot_05`).
- **Cumulative counted (this slice):** **7** (**7** successes, **0** failures).
- **Maximum cumulative if all pilot slots run and count:** **8** -- still **does NOT** meet Tranche 21's **>= 20** minimum for any **0.8** comparison.

### What this pilot can and cannot prove

- **Can:** support a **go / no-go** judgment on whether **continued** Federal Register lane B testing is worth scheduling when a **full** Tranche 21 window becomes feasible.
- **Cannot:** justify comparison to **`required_reliability_threshold` 0.8**; **cannot** satisfy the full pre-audit protocol; **cannot** grant MVP approval.

**Approval:** unchanged -- `mvp_lane_approval.json` remains `approved: false`.

ENDPOINT POINTER:
- Approval gate: `future_modules/the_fade/config/mvp_lane_approval.json`
- Evidence registry: `future_modules/the_fade/config/mvp_lane_evidence_registry.json`


