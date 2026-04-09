# Option A — Explicit Rubric Anchor Matrix

**Last updated:** 2026-04-12

Canonical anchor strings and version id live in the dashboard:

- `dashboard/src/lib/foundry-rubric-anchors.ts` — `RUBRIC_ANCHORS`, `RUBRIC_ANCHOR_VERSION`
- `dashboard/src/lib/foundry-rubric-proposal.ts` — bounded mapping from source text to proposed 0–5 per dimension (cites anchor level in reasons)

Authoritative module docs that summarize scoring (aligned with this flow):

- `../JARVIS_THE_FOUNDRY_CONTEXT_ANCHOR.md` — §11 intake scoring reality
- `../JARVIS_THE_FOUNDRY_MODULE_SPEC.md` — §6.1 intake vs engine
- `../JARVIS_THE_FOUNDRY_MASTER_BUILD_CHECKLIST.md` — Phase 4 intake scoring truth
- `../JARVIS_THE_FOUNDRY_HANDOFF_BUNDLE_LATEST.md` — §9 intake scoring

## Flow

1. **Heuristic prefill** — legacy length/keyword buckets only; stored as `heuristic_prefill_scores`; labeled as not rubric truth.
2. **Rubric proposal** — explicit-anchor evaluation → `proposed_scores`, `score_reasons`, `evidence_support`; method `bounded_explicit_rubric_anchor_proposal_v1`.
3. **Operator lock** — dashboard sends `option_a_locked_rubric_scores`; engine runs on **final** integers only; sidecar method `bounded_explicit_rubric_anchor_operator_locked_v1`.

Historical sidecars keep their original `evaluation_method` and values (no silent rewrite on UI toggle).

## Operator testing

Run `npm run dev` from `dashboard/`, then use Foundry intake pages: Option A requires **Preview rubric proposal** before **Submit Intake**.
