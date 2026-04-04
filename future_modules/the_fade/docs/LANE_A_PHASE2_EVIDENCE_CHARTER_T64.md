# Lane A — Phase 2 bounded evidence charter (Tranche 64)

**Tranche:** 64  
**T64 implementation rollout (canonical):** Prompt **#294**  
**Governing charter decision (prose only):** Prompt **#293**  
**Updated:** 2026-04-04T23:21:19+00:00

This file **does not** grant MVP approval, **does not** change `approved` in `mvp_lane_approval.json`, and **does not** unblock Phase 3.

---

## 1. Lane identity

- **`lane_id`:** `lane_a_public_signal`
- **Conceptual tie only:** Aligns with the **`curated_public_signal_lane`** block in `future_modules/the_fade/config/mvp_lane_approval.json` (`TBD_CURATED_PUBLIC_SIGNAL_PROVIDER`) as a **placeholder** — **no edit** to that file in T64.
- **Registry:** Lane A remains `evidence_status: not_started` until **T65** produces a first observation record.

---

## 2. Source class (bounded)

- **Exactly one** read-only **HTTPS** public endpoint class (e.g. public JSON or RSS over TLS).
- **Exact URL:** **`TBD`** until the operator names it **before** executing **T65**. **No fabricated URL.**
- **Operator responsibility:** ToS, rate limits, and lawful read-only use are **operator-owned**; this charter does not perform legal review.

---

## 3. T64 objective (this tranche)

- **Charter + doc lock only** — commit bounded scope in writing and reconcile control docs.
- **Lane B default freeze:** New Lane B evidence tranches are **paused by default**; resume **only** under a **new governed charter** that explicitly names Lane B scope and bounds. Existing Lane B artifacts stay on disk; **no** claim that Lane B is closed for approval.
- **No observation execution in T64** — no network collection, no new `outputs/` population for Lane A in this tranche.

---

## 4. T65 first evidence hook (next tranche)

- **One** bounded **observe-or-honest-failure** pass against the charter URL (after `TBD` is resolved).
- **Dimensions touched first:** **`reliability`** (single attempt, explicit success vs failure) and **`normalization_viability`** (explicit `normalized_signal_event` vs explicit `scout_failure` / failure path — no silent drop).
- **Execution code:** **Out of scope for T64**; T65 may add or adapt tooling under a future governed prompt.

---

## 5. Expected T65 artifacts

- **One** committed record in `future_modules/the_fade/docs/MVP_LANE_EVIDENCE_LOG.md` (command, UTC window, outcome class, redacted/summary JSON as appropriate).
- **Optional** local output under `future_modules/the_fade/outputs/lane_a_public_signal/` **when created in T65**, with `*.json` gitignored if mirroring Lane B output discipline.

---

## 6. Lane B posture during Lane A rotation

- **Paused by default** for **new** Lane B tranches.
- **Reopen** only via a **new governed charter** that explicitly re-authorizes Lane B work.

---

## 7. T64 stop line

- This charter file exists on disk.
- Registry + listed control docs reference it and state **T65** as the next step.
- Lane B freeze language appears in those control docs.
- **Not required in T64:** numeric evidence, approval, Phase 3, or Lane C / Lane E work.

---

## 8. Explicit out of scope / non-goals (T64)

- No multi-feed aggregation or fan-in.
- No authentication flows, API keys in repo, or credential handling.
- No Lane C or Lane E tranches or unpause.
- No change to `mvp_lane_approval.json`.
- No Phase 3 scanner, runtime, or dashboard execution.
- **No execution code** added in T64 (no new scripts, no changes to observe/collect tools for Lane A in this tranche).
