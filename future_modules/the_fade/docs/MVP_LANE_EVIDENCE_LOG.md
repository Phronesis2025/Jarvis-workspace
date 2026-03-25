# MVP Lane Evidence Log (Phase 2)

**Prompt #:** 55  
**Phase #:** 2  
**Tranche #:** 16  

Updated: 2026-03-25T14:18:37.3837689-05:00

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
- evidence_summary: Quantitative reliability sampling for lane B was extended within the limited observation window. In the captured lane B sample, failure/outage dominance did not exceed the `required_reliability_threshold` criterion qualitatively; however the observation window is still not the full pre-audit window needed for gate-sufficient statistical coverage.
- pass/fail criteria reference: Compare observed failure/outage dominance against `required_reliability_threshold` (0.8) from `config/mvp_lane_approval.json`.
- notes: Partial-but-improved. Quantitative methodology and sample-based dominance checks are recorded, but full pre-audit window coverage is still missing; approval remains NOT justified.

### Freshness
- evidence_summary: Evidence timestamps were present in the observed outputs and could be classified for freshness vs staleness using a planned freshness window.
- freshness window reference: Defined later by the operator in the log (align to `MVP_SOURCE_RELIABILITY_AUDIT.md` freshness discipline).
- notes: Recorded. Still requires full application of the freshness window definition.

### Normalization viability
- evidence_summary: Normalization produced candidate normalized events without obvious silent drops in the observed sample.
- silent-drop checks observed: Limited sample. Silent-drop guarantees require more coverage.
- notes: Recorded. More normalization runs are needed before treating this as gate-sufficient.

### Stale/outage behavior
- evidence_summary: Tranche 12 captured **simulated harness rehearsal** stdout for Protocol A (see “Lane B simulated harness rehearsal (Tranche 12)” below). Inputs were **operator-authored**; the harness fetched **no external vendor data**. That output does **not** demonstrate real lane stale/outage `system behavior` for the gate; it only shows the harness can emit a constrained record when given those inputs. **Tranche 16 (Prompt #52)** added a **non-simulated** lane B `observe` run plus real `scout_failure` outcomes where HTTPS returned **403** (SEC.gov / issuer IR in this environment), and one **successful** `normalized_signal_event` from a **live** public regulatory disclosure API (Federal Register JSON). See “Lane B first honest non-simulated observation run (Tranche 16)” below.
- observed downgrade/escalation/omit behavior: **Recorded (bounded slice):** the real observation slice emits explicit `scout_failure` with `error_type: SOURCE_UNAVAILABLE` and HTTP 403 summaries for blocked fetches, and emits `normalized_signal_event` when bytes return (HTTP 200). This is **gate-honest real observation** for the adapter path; it is **not** full production scout runtime or a statistical outage study.
- notes: Tranche 16 advances **real** availability/staleness-classification evidence for the slice. Full pre-audit outage dominance vs `required_reliability_threshold` remains outstanding.

### Conflict handling
- evidence_summary: Additional conflict-case situations were recorded within the captured lane B runs. In these cases, fusion/conflict handling preserved primary lane truth (no dominance by context-only enrichment was observed in the recorded outputs).
- how conflicts were resolved safely: context-only enrichment did not override primary lane truth in the recorded conflict cases; precedence remained safe. Still requires adversarial/permutation coverage to fully validate the gate standard.
- notes: Recorded partially / still in review. The current evidence improves coverage, but broader conflict-case permutations are still not established to gate-sufficient confidence.

### Context dominance risk
- evidence_summary: Tranche 12 captured **simulated harness rehearsal** stdout for Protocol B (see “Lane B simulated harness rehearsal (Tranche 12)” below). Inputs were **operator-authored**; the harness fetched **no external vendor data**. That output does **not** demonstrate real lane dominance/conflict `system behavior` for the gate; it only shows the harness can emit a constrained record when given those inputs. **Tranche 16** ran the **real** `conflict` subcommand against a **live** lane B artifact from Tranche 16 observe plus a **THE FADE–local, operator-authored** contra JSON (explicitly **not** live external research). See “Lane B first honest non-simulated observation run (Tranche 16)” below.
- proof that context-only reads did not override primary truth: **Recorded (bounded slice):** emitted `conflict_packet` states fusion precedence primary `lane_b_official_disclosure` and that context cannot override lane B (`fusion_policy.json` weights read-only). The contra input is **operator-authored** for mechanics only; it must **not** be read as external proof.
- notes: Tranche 16 provides real THE FADE–local precedence/conflict output tied to a real observe artifact. Broader adversarial permutations and production fusion remain outstanding.

## Lane B simulated harness rehearsal (Tranche 12)

Scope: `lane_b_official_disclosure` only. This section records **actual constrained harness stdout** from one Protocol A rehearsal and one Protocol B rehearsal, using operator-authored JSON inputs under:

`future_modules/the_fade/examples/lane_b_controlled_evidence_harness_inputs/tranche12_simulated_rehearsal/`

Classification (Prompt #42 correction):
- **Simulated harness rehearsal only** (operator-authored inputs; **no external/vendor data** fetched by the harness).
- **Not** real lane evidence **from this harness alone** for `stale_outage_behavior` or `context_dominance_risk` (the rehearsal does not satisfy those dimensions by itself). **Tranche 16** added separate bounded real slice evidence; see “Lane B first honest non-simulated observation run” below — registry dimensions for those items are **recorded (bounded)**, not production-complete.
- Useful as **protocol rehearsal**, not as proof of production FADE behavior.

Discipline:
- These runs are **not** smoke-test fixtures (`protocol_a_lane_b_evidence.json` / `protocol_a_scenario.json` under the parent folder).
- These runs are **not** production FADE runtime evidence.
- No approval is implied.

### Protocol A — `LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1` (simulated rehearsal stdout)

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

### Protocol B — `LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1` (simulated rehearsal stdout)

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

### Protocol A — Controlled stale/unavailable incident replay (timestamps required)

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
  - `stale_window_definition` (plain text; e.g. “older than X minutes/hours/days is stale”)
  - `unavailable_condition_definition` (plain text; what “unavailable” meant in this controlled test)
  - `observed_behavior` (one of: downgrade / escalate / omit) and any follow-on action taken
- expected_allowed_outcomes:
  - The system **does not fabricate** values.
  - The system behavior is **explicit**: it either downgrades confidence, escalates, or omits lane B evidence, consistent with the Phase 2 gate standard.
- disallowed_outcomes:
  - Any fabricated evidence content.
  - Silent substitution where missing/stale lane B evidence is replaced with non-lane-B truth without explicit labeling.
  - Context-only enrichment becoming precedence because lane B is missing/stale.
- gate_sufficient_evidence (minimum bar for this protocol):
  - A recorded, timestamped controlled stale/unavailable replay with explicit `observed_behavior` and a clear stale/unavailable definition (not “no incident observed”).
- still_insufficient_evidence:
  - “No stale/outage observed in sampling.”
  - Any replay without timestamps or without explicit behavior outcomes.

### Protocol B — Context-dominance adversarial/conflict-case (explicit outcomes required)

- scenario_name: `LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1`
- preconditions:
  - Lane under test is `lane_b_official_disclosure`.
  - Context-only enrichment source is present (conceptually “lane_e_research_swarm_context”) but must remain non-dominating.
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
  - “No dominance override detected in sampling.”
  - Any case without an explicit conflict and explicit precedence statement.

## Protocol execution status (Tranche 10)

Outcome: **SIMULATED REHEARSAL EXECUTED (TRANCHE 12 — HARNESS ONLY)** (no approval flip; see Tranche 12 section — **not** real lane evidence for gate dimensions).

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
- limits: Tranche 12 remains **simulated harness rehearsal only** for stale/dominance. **Tranche 16** adds **bounded real** slice evidence (see Tranche 16 section). Lane B remains **not gate-ready**: reliability still lacks full pre-audit window coverage; conflict handling still lacks broader permutations; production-equivalent scout runtime is not established.

Decision signal:
- insufficient_for_gate_decision_pending_remaining_dimension_evidence

What is still missing before approval could be considered:
- reliability: complete full pre-audit window outage/failure dominance measurements vs 0.8 threshold (current sample-based checks are limited)
- freshness: finalize and fully apply freshness window classification
- normalization_viability: expand silent-drop coverage
- stale_outage_behavior: Tranche 16 recorded **bounded real** slice behavior (see Tranche 16 section); full pre-audit outage statistics still outstanding
- conflict_handling: broaden conflict-case permutations and record explicit safe precedence checks aligned to the Phase 2 gate standard
- context_dominance_risk: Tranche 16 recorded **bounded real** slice behavior (see Tranche 16 section); broader adversarial coverage still outstanding

## Real evidence path spec (Tranche 14)

Normative path definition:

`future_modules/the_fade/docs/LANE_B_MINIMAL_REAL_EVIDENCE_PATH_SPEC.md`

Prompt #48 correction: the spec is **fully inside THE FADE** (no `research_swarm/` or other module dependency). Context/precedence uses a **THE FADE–local operator-placed contra file**; honesty rules for that file are stated in the spec.

The harness (`lane_b_controlled_evidence_harness.py`) remains **rehearsal-only** and does not satisfy that spec.

## Lane B real observation slice (Tranche 15 — implementation exists)

Script: `future_modules/the_fade/scripts/lane_b_real_observation_slice.py`

- **observe:** reads one real **HTTPS URL** or **local file path** → writes `future_modules/the_fade/outputs/lane_b_real_observation/{task_id}_scout_failure.json` **or** `{task_id}_normalized_signal_event.json` (stdout prints the same object).
- **conflict:** reads one **lane B artifact** (normalized JSON from observe) + one **THE FADE–local** `context_only_contra` JSON (`semantic_role` = `lane_e_research_swarm_context`) → writes `{task_id}_conflict_packet.json`; uses `config/fusion_policy.json` **read-only** for weight wording.

**Smoke tests** (developer-run, not gate approval): file read + `https://example.com` fetch + conflict against `inputs/lane_b_real_evidence/context_only_contra.example.json` succeeded locally. **This does not substitute for operator gate evidence** using a real disclosure URL/file and honest contra provenance — it only proves the slice runs.

Operator usage (see also `inputs/lane_b_real_evidence/README_operator.txt`):

```text
python future_modules/the_fade/scripts/lane_b_real_observation_slice.py observe --task-id <TASK> --ticker <SYM> --file <path> --out-dir future_modules/the_fade/outputs/lane_b_real_observation
python future_modules/the_fade/scripts/lane_b_real_observation_slice.py observe --task-id <TASK> --ticker <SYM> --url <https://...> --out-dir future_modules/the_fade/outputs/lane_b_real_observation
python future_modules/the_fade/scripts/lane_b_real_observation_slice.py conflict --task-id <TASK> --ticker <SYM> --lane-b-artifact <normalized.json> --contra <context_only_contra.json> --out-dir future_modules/the_fade/outputs/lane_b_real_observation
```

Ephemeral `*.json` outputs under `outputs/lane_b_real_observation/` are gitignored by default (see `.gitignore` there).

## Lane B first honest non-simulated observation run (Tranche 16 — Prompt #52)

**Classification:** Phase 2 lane B only; **not** approval; **not** scanner; **not** multi-lane.

### Provenance separation (required)

| Kind | What it is | This run |
|------|------------|----------|
| **Real lane B observation** | External anchor: bytes read via `observe` from a live HTTPS URL (or an honest local file path), with traceable URL/path and outcome class | **Primary:** `task_id=t16_honest_005`, URL `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`, Federal Register public API (official U.S. government disclosure index JSON). HTTP **200**, `normalized_signal_event` written. **Supplementary real availability observations:** `t16_honest_001`–`t16_honest_003` against SEC / issuer IR URLs returned **403** `scout_failure` in this environment (honest `SOURCE_UNAVAILABLE`, not rehearsed JSON). |
| **Operator-authored contra** | THE FADE–local `semantic_role: lane_e_research_swarm_context`; **not** live external proof | `future_modules/the_fade/inputs/lane_b_real_evidence/context_only_contra.tranche16_operator_authored.json` — labeled in-file as operator-authored for precedence mechanics only. |

**Not used as real lane-B disclosure content for this run:** `inputs/lane_b_real_evidence/sample_disclosure_stub.txt` (stub only). **Not used as Tranche 16 contra:** `context_only_contra.example.json` (shape reference / smoke only). **Not claimed as real evidence:** Tranche 12 harness rehearsal blocks in this log.

Freshness window for observe classification in tool: default `--stale-after-hours 48` (see script); `t16_honest_005` classified `lag_class: fresh` (`freshness_hours: 0.0`).

### Exact recorded output — `observe` (`t16_honest_005`)

Authoritative JSON file (under `outputs/lane_b_real_observation/`; gitignored): `t16_honest_005_normalized_signal_event.json` — same object as stdout from the run. Full payload includes `raw_text` (API body, truncated in tool after 8k chars per script). **SHA256** of raw bytes and HTTP metadata appear in `notes` on the artifact.

### Exact recorded output — `conflict` (`t16_honest_005`)

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

**Approval:** unchanged — `mvp_lane_approval.json` remains `approved: false`. This run does **not** justify flipping approval.

ENDPOINT POINTER:
- Approval gate: `future_modules/the_fade/config/mvp_lane_approval.json`
- Evidence registry: `future_modules/the_fade/config/mvp_lane_evidence_registry.json`

