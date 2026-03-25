# Lane B minimal real evidence path (spec only)

**Prompt #:** 50  
**Phase #:** 2  
**Tranche #:** 15  

Updated: 2026-03-25T13:20:54.8711512-05:00

## Authority

- Approval gate (unchanged): `future_modules/the_fade/config/mvp_lane_approval.json` — remains `approved: false` until explicitly changed by an operator.
- This document is **not** evidence and does **not** grant approval. It defines **what must exist** to collect **real, non-simulated, gate-honest** observations for `lane_b_official_disclosure` on stale/unavailable and context-dominance dimensions.

## Scope boundary (Prompt #48 correction)

This path is **fully inside `future_modules/the_fade/`**. It **does not** read **`future_modules/research_swarm/`** or any other non–THE FADE module.  
**No cross-module filesystem dependencies** are required for the minimal slice.

## Problem statement (from Prompt #46)

The harness at `future_modules/the_fade/scripts/lane_b_controlled_evidence_harness.py` is **rehearsal-only**: it validates JSON on disk and prints a constrained observation. It **does not** fetch vendor data and **cannot** satisfy the gate’s **system behavior** bar for lane B by itself.

## Definition: “real, gate-honest” for this spec

An observation is **real** only if:

1. **External anchor:** At least one **non-authoritative** input is read from **outside** operator-authored harness JSON (e.g. HTTP(S) response from a disclosure URL, or a file on disk whose bytes/mtime are not invented in-repo for the test).
2. **Traceable:** The run records **how** that input was obtained (URL/path, HTTP status or file error, timestamps).
3. **Policy-visible:** The observation ties to an explicit **scout-layer outcome class** (see artifacts below) that can be checked against existing policy **meaning** (read-only): `config/escalation_policy.json` and `config/fusion_policy.json` are **referenced for labeling**; this spec does **not** require editing them in Tranche 14.

## Smallest real evidence path (single slice)

One **lane-B-only observation capture** with two **sequenced** runs (same codebase entrypoint; different conditions). No universe scanner, no dashboard, no multi-lane MVP implementation.

### A) Stale / unavailable behavior (real)

| Element | Specification |
|--------|----------------|
| **Input source** | Exactly **one** operator-designated **official/disclosure** source: either a stable **HTTPS URL** to a public filing/issuer disclosure page or RSS/Atom endpoint, **or** a **local file path** to a downloaded disclosure file that the operator places outside simulated harness JSON (path passed as CLI arg or env). Path must be **under** `future_modules/the_fade/` **or** a general OS path; if under THE FADE, prefer a **fixed** convention e.g. `future_modules/the_fade/inputs/lane_b_real_evidence/disclosure_source.*` (created at implementation time). |
| **Adapter boundary** | A **single** module (future implementation): `lane_b_real_observation` — responsible only for: fetch/read → raw payload metadata → classification of **availability** and **staleness** vs a **documented freshness window** (operator states the window in the evidence log; same window used for all runs). |
| **Policy / decision surface to observe** | Map the outcome to **scout-layer** behavior consistent with `escalation_policy.json` rules (read-only), e.g. `SOURCE_UNAVAILABLE` → `record_scout_failure_downgrade_or_continue_if_non_critical`. The implementation **observes and records** which branch applies; it does **not** silently substitute lane B with another lane’s truth. |
| **Artifacts to emit (minimum)** | Prefer **`scout_failure`** (`schemas/scout_failure.schema.json`) when the source is unavailable or cannot be normalized; **or** one **`normalized_signal_event`** (`schemas/normalized_signal_event.schema.json`) when bytes exist, with **`source_lane`** = `lane_b_official_disclosure`, **`ingested_at`**, **`event_time`** (from content or HTTP `Last-Modified` if present), **`freshness_hours`** / **`lag_class`** / **`notes`** explicitly stating stale vs fresh, and **`evidence_url`** or **`evidence_path`**. |
| **Timestamps / fields required** | `ingested_at` (ISO8601), `event_time` or explicit “unknown” with reason, HTTP status or file errno, round-trip latency ms (if HTTP), content hash (sha256) of raw bytes if body present. |
| **Failure cases (must be exercisable)** | DNS failure, TLS failure, HTTP **4xx/5xx**, timeout, empty body, stale by freshness rule, success path with fresh classification. |

### B) Context-dominance / precedence (THE FADE–local, honest)

This slice tests **precedence** using **only** THE FADE inputs. It does **not** claim a live Research Swarm pipeline or any other module.

| Element | Specification |
|--------|----------------|
| **Input sources** | **Two inputs** in the same **task window**: (1) **Lane B primary:** one real disclosure-derived artifact from the adapter in section A (same `task_id`). (2) **Context-only contra (bounded local):** a **single file** placed by the operator at a **fixed path under THE FADE**, e.g. `future_modules/the_fade/inputs/lane_b_real_evidence/context_only_contra.json` (exact filename fixed at implementation; directory created then). That file **must** be tagged in content (or adjacent sidecar) so the fusion step treats it as **`lane_e_research_swarm_context` role** for weighting **only** (semantic role: context-only; **not** a cross-module read). The **bytes** may be **real** (e.g. operator pasted excerpt from an external research note with **provenance recorded in `MVP_LANE_EVIDENCE_LOG.md`**). If the operator **authors** the contra file for the test, that is **not** “live external” evidence — **do not** label it as such; it is a **bounded local contradiction** for precedence mechanics only, and the log must say so. |
| **Adapter boundary** | Same `lane_b_real_observation` module **plus** a **minimal fusion step** that is **lane-B-scoped**: inputs = lane B artifact + **one** THE FADE-local context-only contra file + `fusion_policy.json` **lane_weight_hints** (read-only). **No other lanes.** No reads outside `future_modules/the_fade/` except the lane B URL/file from section A. |
| **Policy / decision surface to observe** | Precedence must reflect **`lane_e_research_swarm_context` weight ≤ primary lanes** per `fusion_policy.json` (read-only). Outcome must be explicit: lane B remains primary or conflict is surfaced — **no** silent override. |
| **Artifacts to emit (minimum)** | **`conflict_packet`** (`schemas/conflict_packet.schema.json`) with `conflict_reasons` naming lane B vs context-role, and `evidence_paths` pointing to **both** THE FADE-local paths; **or** a documented thinner fallback that still names precedence. |
| **Timestamps / fields required** | `created_at`, `task_id` shared across both inputs, paths to both files under THE FADE, explicit `summary` of contradiction. |
| **Failure cases** | Missing contra file, missing lane B artifact, fusion refuses to elevate context over B (expected pass for gate). |

## In scope (Tranche 14 / next implementation)

- Lane id **`lane_b_official_disclosure`** only.
- All inputs and outputs under **`future_modules/the_fade/`** (except OS temp if implementation requires it — avoid if possible).
- One **CLI or single-script** entrypoint (exact filename left to implementation prompt).
- Emit **JSON artifacts** that validate against **existing** schemas (or strict subset documented in implementation).
- Write outputs under a **single bounded directory** e.g. `future_modules/the_fade/outputs/lane_b_real_observation/` (created in implementation; not required in this spec commit).
- Operator copies relevant JSON **or** summarized fields into `MVP_LANE_EVIDENCE_LOG.md` for the gate record.

## Out of scope

- Phase 3 **universe scanner**, scanner_policy runner, `scanner_candidate_set` production.
- Dashboard contracts / UI.
- Changing **`mvp_lane_approval.json`**, **`lane_registry.json`**, **`escalation_policy.json`** (Tranche 14).
- **Any** dependency on `future_modules/research_swarm/` or other modules for this minimal slice.
- Multi-lane fusion productization beyond the **two-input** contradiction slice above.
- Heartbeat, broker execution, portfolio.

## Smallest implementation after this spec (narrow prompt target)

Implement **only**:

1. `lane_b_real_observation` (name may vary) — fetch/read real disclosure source + emit `scout_failure` or `normalized_signal_event`.
2. Minimal **fusion micro-step** for **one** lane B artifact + **one** THE FADE-local **context-only contra** file → **`conflict_packet`** (or documented fallback).

**Explicitly forbid** in the implementation prompt: extra lanes, generic plugin framework, scanner, dashboard, **reads from `research_swarm/`** or other non–THE FADE modules for this slice.

## Link to rehearsal harness

`lane_b_controlled_evidence_harness.py` remains valid for **protocol rehearsal** only. Real evidence for the two dimensions must come from the path above, recorded separately in `MVP_LANE_EVIDENCE_LOG.md`.

## Implementation note (Tranche 15)

A minimal slice matching this spec is implemented as `future_modules/the_fade/scripts/lane_b_real_observation_slice.py` (subcommands `observe` and `conflict`). See `docs/MVP_LANE_EVIDENCE_LOG.md` for operator usage. **Spec remains normative** if the script behavior drifts—fix the script, not the gate bar.
