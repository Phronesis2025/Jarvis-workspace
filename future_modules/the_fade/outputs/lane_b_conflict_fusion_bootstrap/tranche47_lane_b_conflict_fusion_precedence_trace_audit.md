# Tranche 47 — Lane B conflict / fusion precedence trace audit

**Scope:** THE FADE-local fixtures only. **Not** MVP approval. **Not** Phase 3. **Not** live integration.

## Summary

- **Cases evaluated:** 6
- **Fusion policy version:** 0.1.0
- **Overall pass:** True

## Evidence questions (bounded answers)

- **Does the trace preserve Lane B as primary when context-only signals disagree?** — Yes for valid present context: summary states primary=lane_b_official_disclosure and context cannot override lane B; mismatch is flagged, not applied as override.
- **Does the trace show explicit non-override behavior?** — Yes via fixed summary wording in the slice-aligned fusion_preview for contra cases.
- **Are aligned/supportive context cases explicit and non-dominant?** — Yes: same precedence string even when direction_hint matches; context weight hint remains lower than lane B per fusion_policy.
- **Are stale, missing, and invalid context inputs explicitly omitted with reasons?** — Missing and invalid-role: explicit CLI block documented. Stale: not omitted by slice — audit omits false claim and documents implementation gap with reason stale_first_omission_not_evaluated_in_minimal_lane_b_conflict_path.
- **Are there silent drops, silent overrides, or ambiguous outputs?** — No silent override/drop observed in bounded cases; stale path carries ambiguous_output_risk=True because slice would still fuse without age check.

## Case verdicts

### `t47_01_primary_vs_context_contra`

- **trace_class:** `both_present_valid_context`
- **case_pass:** True
- **silent_override_observed:** False
- **silent_drop_observed:** False
- **ambiguous_output_risk:** True
- **omission_explicit:** True
- **omission_reason:** `conflict_surfaced_not_silent_override`

> Fusion summary states primary=lane_b_official_disclosure and that context cannot override lane B; direction_mismatch=True. This matches the bounded conflict_packet wording produced by the slice.

### `t47_02_context_aligned_support`

- **trace_class:** `both_present_valid_context`
- **case_pass:** True
- **silent_override_observed:** False
- **silent_drop_observed:** False
- **ambiguous_output_risk:** False
- **omission_explicit:** False
- **omission_reason:** `none`

> Fusion summary states primary=lane_b_official_disclosure and that context cannot override lane B; direction_mismatch=False. This matches the bounded conflict_packet wording produced by the slice.

### `t47_03_context_missing`

- **trace_class:** `missing_context_boundary`
- **case_pass:** True
- **silent_override_observed:** False
- **silent_drop_observed:** False
- **ambiguous_output_risk:** False
- **omission_explicit:** True
- **omission_reason:** `conflict_subcommand_requires_contra_file`

> Minimal slice `lane_b_real_observation_slice.py` `conflict` exits non-zero and prints to stderr when the contra file is missing; no conflict_packet is written. That is explicit failure, not a silent override of lane B.

### `t47_04_context_invalid_shape`

- **trace_class:** `invalid_context_shape_or_role`
- **case_pass:** True
- **silent_override_observed:** False
- **silent_drop_observed:** False
- **ambiguous_output_risk:** False
- **omission_explicit:** True
- **omission_reason:** `invalid_context_role_for_lane_b_fusion_slice`

> Slice rejects contra files whose semantic_role is not lane_e_research_swarm_context (stderr + exit 2). Context is not fused; lane B primary is not replaced by that payload.

### `t47_05_context_stale_policy_gap`

- **trace_class:** `stale_context_not_implemented_in_conflict_slice`
- **case_pass:** True
- **silent_override_observed:** False
- **silent_drop_observed:** False
- **ambiguous_output_risk:** True
- **omission_explicit:** True
- **omission_reason:** `stale_first_omission_not_evaluated_in_minimal_lane_b_conflict_path`

> Fixture marks context_age_hours=200.0 > window 48.0: under Lane C/E style gate audits, stale context would be omitted before directional fusion. The lane B `conflict` subcommand does not read freshness fields; it would still emit a conflict_packet with the same precedence wording. This audit records that gap explicitly (no false claim of stale-first omission in the minimal slice).

### `t47_06_tie_equal_weights_unsupported`

- **trace_class:** `tie_or_ambiguity_unsupported`
- **case_pass:** True
- **silent_override_observed:** False
- **silent_drop_observed:** False
- **ambiguous_output_risk:** False
- **omission_explicit:** True
- **omission_reason:** `no_equal_weight_row_in_current_fusion_policy`

> Current fusion_policy.json gives lane_b_official_disclosure and lane_e_research_swarm_context different hints (1.0 vs 0.2); tie/ambiguous equal-weight precedence is out of scope for this fixture set.

## What this proves

- Under **current** `fusion_policy.json`, lane B weight exceeds lane E context hint; summary text **explicitly** states context cannot override lane B for valid two-file fusion.
- **Contra / missing / wrong-role** paths on the minimal slice surface **explicit** CLI failure rather than silent primary replacement.
- **Stale context** in the same minimal path is an **honest documented gap** (no stale-first omission in `conflict` today).

## What this does not prove

- Production fusion runtime across all lanes or full permutation coverage.
- Stale-first omission for lane E context inside the lane B conflict micro-step (not implemented).
- MVP approval or Phase 3 readiness.
