# THE FADE Handoff Bundle (Latest)

**Prompt #:** 121  
**Phase #:** 2  
**Tranche #:** 31  
**Updated:** 2026-03-30T18:15:00-05:00
**Branch:** `the-fade-phase1-tranche1-foundation` (verify: `git branch --show-current`)

---

## New chat — start rules

1. Read **`THE_FADE_CONTEXT_ANCHOR.md`** (this file’s sibling) first — one-screen truth.
2. Read this bundle second.
3. Verify **on-disk** facts before changing narrative:
   - `future_modules/the_fade/config/mvp_lane_approval.json`
   - `future_modules/the_fade/outputs/lane_b_real_observation/tranche21_fr_slot_runs.jsonl`
4. **Do not** treat THE FADE as live or integrated. **Do not** drift into research swarm, scanner, runtime, dashboard, or broad stock-module work unless the user explicitly scopes it.
5. **Canon:** eight `JARVIS_THE_FADE_*.md` files remain in **`future_modules/stock_module/`** — do not move or delete (`docs/CANON_INDEX.md`).
6. **Process anchor:** `future_modules/stock_module/JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`.

---

## Module reality

| Topic                        | Truth                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Live / integrated            | **No** — early-stage future module under `future_modules/the_fade/`                                                               |
| Phase                        | **2** — MVP lane approval + source reliability pre-audit                                                                          |
| Approval                     | **`mvp_lane_approval.json`:** `approved: false`, `approved_mvp_lanes: []` (verify on disk)                                        |
| Most advanced lane           | `lane_b_official_disclosure` — still not MVP-approved                                                                             |
| Phase 3                      | **Blocked**                                                                                                                       |
| Operator gate review outcome | **Reviewed at this checkpoint** — FR slice strong; whole-gate approval still not justified; no approval change; no Phase 3 unlock |

---

## Roots and paths

| Purpose                        | Path                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Module root                    | `future_modules/the_fade/`                                                                              |
| Bounded lane B outputs         | `future_modules/the_fade/outputs/lane_b_real_observation/`                                              |
| Append-only FR slot run log    | `.../tranche21_fr_slot_runs.jsonl`                                                                      |
| Per-run snapshots              | `.../run_*_tranche21_fr_slot_snapshot.json` (and legacy `*_tranche21_fr_slot_snapshot.json` if present) |
| Full Tranche 21 slot collector | `future_modules/the_fade/scripts/run_tranche21_fr_slot.py`                                              |
| Legacy lane B observe tool     | `future_modules/the_fade/scripts/lane_b_real_observation_slice.py`                                      |
| Approval authority             | `future_modules/the_fade/config/mvp_lane_approval.json`                                                 |
| Evidence registry              | `future_modules/the_fade/config/mvp_lane_evidence_registry.json`                                        |
| Reliability protocol text      | `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md`                                          |
| Evidence log                   | `future_modules/the_fade/docs/MVP_LANE_EVIDENCE_LOG.md`                                                 |

---

## Federal Register collector — what it is

- **Script:** `run_tranche21_fr_slot.py`
- **Scope:** Single Federal Register URL only —  
  `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`
- **One invocation = one slot** — no loop, no retry, no scheduler inside the script.
- **Requires:** `--task-id`, `--scheduled-slot-utc`, `--window-start-utc`, `--window-end-utc`, `--max-slot-drift-seconds`
- **Timing:** Fails **before** HTTP if execution is outside `[window_start_utc, window_end_utc]` or outside drift band.
- **Duplicates:** Rejects if `task_id` or deterministic `slot_identity` already appears in the JSONL log.
- **Success:** JSON object with top-level `results` list; else honest source failure. Source failures still **exit 0** if logged; collector errors **non-zero**.

Example (pattern only — adjust times to a **valid** live window when running):

```text
python future_modules/the_fade/scripts/run_tranche21_fr_slot.py --task-id <UNIQUE> --scheduled-slot-utc <UTC> --window-start-utc <UTC> --window-end-utc <UTC> --max-slot-drift-seconds <INT>
```

---

## Full Tranche 21 window — run summary (verified from JSONL)

**File:** `tranche21_fr_slot_runs.jsonl`

| Metric                                                                                             | On-disk value                   |
| -------------------------------------------------------------------------------------------------- | ------------------------------- |
| Total lines                                                                                        | **23**                          |
| Full-window lines (`window_start_utc=2026-03-27T16:00:00Z`, `window_end_utc=2026-03-29T16:00:00Z`) | **22**                          |
| Full-window successes                                                                              | **22**                          |
| Full-window failures (`source_observation_success` false)                                          | **0**                           |
| Full-window `timing_valid_for_counted_slot_use`                                                    | **true** for all **22**         |
| Excluded from full-window tally (different window)                                                 | **1** — `task_id=t30_valid_002` |

**Latest official full-window slot (last line of JSONL):**

- `task_id`: **`t21_fr_full_20260329T100000Z`**
- `scheduled_slot_utc`: **`2026-03-29T10:00:00Z`**
- `actual_started_at_utc`: **`2026-03-29T10:00:03Z`**
- `source_observation_success`: **true**
- `slot_timing_status`: **`timing_valid`**

**Operator-reported Task Scheduler health (host-side, not in repo):** LastTaskResult **0**, NumberOfMissedRuns **0** — use for ops; re-check on the machine if jobs misbehave.

---

## How to check health and totals

1. **Line count / parse log:**  
   `python -c "import json, pathlib; p=pathlib.Path(r'future_modules/the_fade/outputs/lane_b_real_observation/tranche21_fr_slot_runs.jsonl'); r=[json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()]; ..."`  
   Filter rows where `window_start_utc` / `window_end_utc` match the declared 48h window for gate-relevant **22** slots.

2. **Latest slot:** Read last non-empty line of `tranche21_fr_slot_runs.jsonl` or inspect latest `run_*_tranche21_fr_slot_snapshot.json`.

3. **Scheduler (Windows Task Scheduler):** Open Task Scheduler on the operator PC — **Last Run Result** and **missed runs** are not stored in this git repo.

4. **Approval:** Open `mvp_lane_approval.json` — if `approved` is not `true`, **no** MVP lanes are approved.

---

## Why this evidence matters (without overclaiming)

- Tranche 21 protocol required **≥20** counted attempts before an honest **`reliability = successes / counted_attempts`** comparison vs **0.8**. The **22** full-window records meet the **count floor**; observed ratio on that slice is **22/22 = 1.0**.
- **This does not automatically approve** anything. Binding approval is only **`mvp_lane_approval.json`**, which is still **false** on disk.
- **Freshness (Tranche 31 / Prompt #121):** bounded classification on the **22** full-window FR lines — **12** fresh, **0** stale, **10** cannot classify honestly (see `MVP_LANE_EVIDENCE_LOG.md`). **Not** MVP approval by itself.
- Other MVP dimensions (normalization breadth, stale/outage **system** behavior at scale, conflict permutations, context dominance, production-equivalent runtime) remain **partial** as in registry and prior logs.

---

## Historical context (still true)

- **Tranche 24 interim pilot:** Real, FR-only, **8** counted successes — **did not** satisfy full Tranche 21 protocol; documented as interim.
- Prior micro-samples and mixed-host Tranche 16 session — **do not** merge into one statistic (see Tranche 19 clarification in `MVP_LANE_EVIDENCE_LOG.md`).

---

## Current blockers / gaps

1. ~~**Governed markdown lag**~~ **Closed** (Prompt **#102**): `MVP_LANE_EVIDENCE_LOG.md` + `MVP_SOURCE_RELIABILITY_AUDIT.md` reconciled to `tranche21_fr_slot_runs.jsonl`.
2. **Approval decision** — reviewed at this checkpoint; **whole-gate approval is still not justified** on current live evidence; **`mvp_lane_approval.json`** remains **`approved: false`**.
3. **Phase 3** — remains blocked.

## Operator gate review outcome — 2026-03-30

- **Decision outcome:** Lane B remains **promising-but-unapproved** at this checkpoint.
- **Why:** the FR full-window reliability slice is strong (**22 counted / 22 successes / 0 failures**) but still does **not** close the whole-dimensional MVP gate by itself.
- **Final signoff lock (Prompt #113):** outcome confirmed without changes to approval state; `mvp_lane_approval.json` remains `approved: false`, and `t30_valid_002` remains excluded from the full-window 22-slot tally.
- **Review-quality controls used now:** critic / adversarial review, audit-before-trust, and risk-first scrutiny.
- **Accepted future guardrails only:** auth primitives / permission layers; isolated sub-account / restricted permissions; MCP-first infra filter / anti-affiliate rule; sim-first / dry-run-first bridge; position sizing / drawdown emphasis.
- **Parking lot only:** any concrete critic-agent build, MCP tooling build, exchange/live-execution integration, or other execution-adjacent implementation work.
- **What this does not change:** `mvp_lane_approval.json` remains **false** and **Phase 3 remains blocked**.

---

## Tranche 31 — freshness discipline (executed Prompt #121)

- **Done:** Lane B (Federal Register) **freshness rule** + per-slot classification for **22** full-window JSONL lines (`t30_valid_002` excluded): **12** **fresh**, **0** **stale**, **10** **cannot classify honestly** (advance `publication_date` vs observation). Full rule and limits: `MVP_LANE_EVIDENCE_LOG.md` + `MVP_SOURCE_RELIABILITY_AUDIT.md`.
- **Still not:** approval; Phase 3; scanner/runtime; normalization breadth; stale/outage **system** proof; conflict/context-dominance proof.

## Exact next authorized move

1. **Hold at the Phase 2 gate checkpoint** — current outcome is **promising-but-unapproved**; the FR window slice is strong, but it is **not** approval.
2. **Further gate dimensions:** collect evidence per checklist — **not** fake proof; **`mvp_lane_approval.json`** unchanged until explicit signoff.
3. Update **`mvp_lane_approval.json`** (and downstream registry/escalation) **only** if future evidence and explicit operator signoff later justify approval.
4. Continue all git work on **`the-fade-phase1-tranche1-foundation`** unless governance changes branch policy.

## Key authority files (next edits likely)

- `future_modules/the_fade/docs/MVP_LANE_EVIDENCE_LOG.md`
- `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md`
- `future_modules/the_fade/config/mvp_lane_approval.json` (read first; change only with real gate evidence)
- `future_modules/the_fade/config/mvp_lane_evidence_registry.json`
- `future_modules/the_fade/docs/THE_FADE_CONTEXT_ANCHOR.md`
- `future_modules/the_fade/docs/THE_FADE_PROCESS_CHECKLIST.md`
- This file: `THE_FADE_HANDOFF_BUNDLE_LATEST.md`

---

## Do not drift

- No scanner / universe runner / dashboard contracts unless explicitly prompted.
- No moving THE FADE canon out of `future_modules/stock_module/`.
- No approval narrative unless `mvp_lane_approval.json` says so.
- Do not merge **`t30_valid_002`** into the **22** full-window counted set without explicit operator policy.

---

## Out of scope reminder

- Phase 3 not started.
- `outputs/` stays under bounded lane B observation conventions.
- `JARVIS_CODEBASE_STRUCTURE.md` is not THE FADE state.
