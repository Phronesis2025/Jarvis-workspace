
# THE FADE — Phase 0 final lock (active authority)

**Prompt #:** 4  
**Phase #:** 0  
**Tranche #:** 0

**This document:** sole execution-control artifact for THE FADE Phase 0 / Tranches 0–3 scope, together with the eight canon Markdown files named below (paths resolved only via `future_modules/the_fade/docs/CANON_INDEX.md` after Tranche 1). **No code. No architecture expansion.**

---

## Canonical inputs (eight files, paths not hardcoded here)

The following **filenames** are canon for THE FADE design. **This lock does not state their directory.** After Tranche 1, `**future_modules/the_fade/docs/CANON_INDEX.md`** must list the workspace-relative path to each file as it exists at commit time. Until `CANON_INDEX.md` exists, operators resolve paths by search; **do not treat any historical folder (including deprecated locations noted in §5) as authoritative except via that index.

1. `JARVIS_THE_FADE_SYSTEM_OVERVIEW.md`
2. `JARVIS_THE_FADE_BUILD_CHECKLIST.md`
3. `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md`
4. `JARVIS_THE_FADE_ARCHITECTURE_AND_STORAGE_SPEC.md`
5. `JARVIS_THE_FADE_TRADING_AND_REVIEW_SPEC.md`
6. `JARVIS_THE_FADE_DASHBOARD_SPEC.md`
7. `JARVIS_THE_FADE_REVISION_NOTES_v2_TO_CANON.md`
8. `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`

**Authority order** (unchanged meaning; filenames only): build order → `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md` over `JARVIS_THE_FADE_BUILD_CHECKLIST.md`; scout mechanics → `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md`; storage/contracts → `JARVIS_THE_FADE_ARCHITECTURE_AND_STORAGE_SPEC.md`; downstream → `JARVIS_THE_FADE_TRADING_AND_REVIEW_SPEC.md`; dashboard → `JARVIS_THE_FADE_DASHBOARD_SPEC.md`; revision context → `JARVIS_THE_FADE_REVISION_NOTES_v2_TO_CANON.md`; narrative → `JARVIS_THE_FADE_SYSTEM_OVERVIEW.md` (does not override Signal Engine).

---

## 1. Defect correction summary (this revision)

| defect                                           | why it matters                                              | exact correction made                                                                                             |
| ------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Canon paths under `future_modules/stock_module/` | Implies wrong permanent home; couples FADE to legacy layout | Canon = eight **filenames**; paths only in `CANON_INDEX.md`. Deprecated: assuming stock_module is normative (§5). |
| Dangling “§8 obsolete framing”                   | Checklist referenced missing section                        | Full **§5 Obsolete framing** list inlined; exit checklist points to **§5**.                                       |
| `schemas/*.schema.json`, `example_*.json`        | Wildcards invite extra files                                | **§3** and **§7** list **exact** schema and example filenames.                                                    |
| Exit lines referencing vague “acceptance”        | Not binary / not self-contained                             | **§6** each line is checkable from text in this file.                                                             |
| Broken `*` around paths (dashboard_contract)     | Ambiguous rendering                                         | Normalized path prose; no broken emphasis.                                                                        |
| MASTER doc link with stock_module path           | Path residue                                                | References by **filename** + “path per `CANON_INDEX.md`”.                                                         |

---

## 2. Remaining ambiguity resolution table

| ambiguity                                  | resolution                                                                        |
| ------------------------------------------ | --------------------------------------------------------------------------------- |
| Heartbeat vs MASTER Phase 1 “placeholders” | **§3.1** — prose only in `module_spec.md`; no heartbeat schema through Tranche 3. |
| MVP approval                               | **§3.2** — `mvp_lane_approval.json` + stop condition.                             |
| Dashboard artifacts                        | **§3.3** — definitions + dual gate for `dashboard_contract/`.                     |
| Empty dirs                                 | **§4** — anti-padding; exact create list.                                         |
| Artifact lifecycle                         | **§8** — producer / consumer / absence (renumbered from prior §4).                |
| Plan authority                             | **§3.4** — single active file + supersession.                                     |

---

## 3. Final rulings

### 3.1 Heartbeat

**Ruling:** Placeholder **note only** in Tranche 1. **No** `scout_heartbeat.schema.json`. **No** heartbeat metrics code through Tranche 3.

**Satisfies** MASTER Phase 1 wording “Define Heartbeat Monitor contract placeholders” by exactly one subsection in `future_modules/the_fade/module_spec.md`, title **Heartbeat monitor (deferred)**, body containing: (1) heartbeat/failover out of scope until MASTER Phase 13; (2) normative requirements in `JARVIS_THE_FADE_SIGNAL_ENGINE_SPEC.md` §20 (path via `CANON_INDEX.md`); (3) no `schemas/scout_heartbeat.schema.json` and no heartbeat metrics code until Phase 13.

**Editing** `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md` is **not** required by this lock. Machine-readable heartbeat before Phase 13 = **scope change** — amend MASTER and this lock first.

**Forbidden Tranches 1–3:** `schemas/scout_heartbeat.schema.json`, any `config` key file whose sole purpose is heartbeat, any `dashboard_contract` file for heartbeat health.

### 3.2 MVP lane approval gate

**Authoritative file:** `future_modules/the_fade/config/mvp_lane_approval.json`

**When `approved` is `true`, these top-level keys must exist and be non-empty where string-valued:** `approved`, `approved_at`, `approved_by`, `plan_lock_id` (exact string `THE_FADE_PHASE0_FINAL_LOCK`), `official_disclosure_lane`, `market_data_lane`, `curated_public_signal_lane`, `research_swarm_context`. Each lane object: `provider_key`, `description`, `integration_boundary`. `research_swarm_context` must include `"mode": "read_only"` and `paths_glob` or `paths_note` restricted to `future_modules/research_swarm/outputs/`.

**Mutation:** Humans only; committed change with message stating MVP approval decision.

**Tranche 2 while `approved !== true` MAY:** create `mvp_lane_approval.json` with `approved: false`; edit `deferred_sources.json` with generic deferred categories only; edit `escalation_policy.json` for failure classes that do not name MVP implementations.

**Tranche 2 while `approved !== true` MAY NOT:** put concrete vendor/API/product names for the three MVP evidence lanes into `MVP_SOURCE_RELIABILITY_AUDIT.md`, `lane_registry.json`, or `mvp_lane_approval.json` as final; claim MASTER Phase 2 proof passed; start adapters, fetch scripts, or credentials.

**Stop:** Phase 2 failed if Tranche 2 ends without `approved: true` and all required fields. **Do not start Phase 3.**

### 3.3 Hard dashboard trigger

**Dashboard implementation (forbidden before gate):** New or modified UI route under repository `dashboard/` for THE FADE; TS/JS under `dashboard/` that reads `future_modules/the_fade/` for display; any path under `future_modules/the_fade/dashboard_contract/`; any JSON Schema whose stated purpose is FADE dashboard read model or UI contract.

**Dashboard impact notes (allowed):** Markdown only in `future_modules/the_fade/module_spec.md` and/or `future_modules/the_fade/docs/DASHBOARD_READ_MODEL_NOTES.md` — no schema, no dashboard imports.

`**future_modules/the_fade/dashboard_contract/`: Forbidden until both: (1) MASTER Phase 8 execution authorized (recorded); (2) at least one JSON validates against `future_modules/the_fade/schemas/signal_packet.schema.json` — from `examples/example_signal_packet.json` after Phase 7 or from `outputs/signal_packets/` proof.

**Early stubs:** Forbidden.

### 3.4 Single active plan source

| Rule                         | Statement                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Implementation authority** | `**future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK.md`** is the only execution-control document. Implementation follows **that file plus the eight canon MDs (via `CANON_INDEX.md`).                                                      |
| **Bootstrap**                | Until the repo file exists, `**c:\Users\phron\.cursor\plans\the_fade_phase0_plan_543f9d04.plan.md`** is the working draft; **first Tranche 1 commit** adds `THE_FADE_PHASE0_FINAL_LOCK.md` as a **byte-consistent copy of the approved lock text. |
| **Superseded**               | All prior Phase 0 plans, Cursor drafts, and “Pasted markdown” versions: **no execution authority.**                                                                                                                                               |
| **History only**             | Prior drafts may be read for history; **no** scope, gate, or path may be taken from them if this lock differs.                                                                                                                                    |
| **Conflict**                 | Repo `THE_FADE_PHASE0_FINAL_LOCK.md` wins over the Cursor plan file; update Cursor plan to match.                                                                                                                                                 |

---

## 4. File and directory creation order (anti-padding)

**Rule (Tranches 1–3):** Create a path only if required by **that tranche’s proof gate**, **a named schema**, **a named example**, **a runner introduced that tranche**, or **a consumer that exists in repo that tranche**. Otherwise **defer**.

| Path                                                                    | Tranche | Justification                                                  |
| ----------------------------------------------------------------------- | ------- | -------------------------------------------------------------- |
| `future_modules/the_fade/README.md`                                     | 1       | Module boundary / manual-first                                 |
| `future_modules/the_fade/module_spec.md`                                | 1       | Spec + §3.1 subsection                                         |
| `future_modules/the_fade/docs/CANON_INDEX.md`                           | 1       | Maps eight canon filenames → paths                             |
| `future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK.md`            | 1       | §3.4 active authority                                          |
| `future_modules/the_fade/docs/DASHBOARD_READ_MODEL_NOTES.md`            | 1       | **Optional** — omit if unused                                  |
| `future_modules/the_fade/schemas/fade_task_packet.schema.json`          | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/scanner_candidate_set.schema.json`     | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/normalized_signal_event.schema.json`   | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/lane_scorecard.schema.json`            | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/contra_signal_result.schema.json`      | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/signal_packet.schema.json`             | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/conflict_packet.schema.json`           | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/schemas/scout_failure.schema.json`             | 1       | Phase 1 contract                                               |
| `future_modules/the_fade/config/lane_registry.json`                     | 1       | Registry; no locked MVP vendor strings until §3.2              |
| `future_modules/the_fade/config/direction_models.json`                  | 1       | v2 registry                                                    |
| `future_modules/the_fade/config/fusion_policy.json`                     | 1       | Threshold/weight policy                                        |
| `future_modules/the_fade/config/scanner_policy.json`                    | 1       | Scanner; consumer Tranche 3                                    |
| `future_modules/the_fade/config/escalation_policy.json`                 | 1       | Escalation                                                     |
| `future_modules/the_fade/config/safety_governor_policy.json`            | 1       | Baseline manual-only                                           |
| `future_modules/the_fade/examples/example_fade_task_packet.json`        | 1       | Validates `fade_task_packet` schema                            |
| `future_modules/the_fade/examples/example_scanner_candidate_set.json`   | 1       | Validates `scanner_candidate_set` schema                       |
| `future_modules/the_fade/examples/example_normalized_signal_event.json` | 1       | Validates `normalized_signal_event` schema                     |
| `future_modules/the_fade/examples/example_lane_scorecard.json`          | 1       | Validates `lane_scorecard` schema                              |
| `future_modules/the_fade/examples/example_contra_signal_result.json`    | 1       | Validates `contra_signal_result` schema                        |
| `future_modules/the_fade/examples/example_signal_packet.json`           | 1       | Validates `signal_packet` schema                               |
| `future_modules/the_fade/examples/example_conflict_packet.json`         | 1       | Validates `conflict_packet` schema                             |
| `future_modules/the_fade/examples/example_scout_failure.json`           | 1       | Validates `scout_failure` schema                               |
| `future_modules/the_fade/config/mvp_lane_approval.json`                 | 2       | §3.2                                                           |
| `future_modules/the_fade/config/deferred_sources.json`                  | 2       | Phase 2 deliverable                                            |
| `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md`          | 2       | Only after `approved: true`                                    |
| `future_modules/the_fade/scripts/run_universe_scan.py`                  | 3       | Scanner runner (this exact basename)                           |
| `future_modules/the_fade/outputs/scanner/`                              | 3       | Directory created when runner lands; holds scanner JSON output |

**Not Tranche 1:** `tasks/`, `outputs/failures/`, `state/`, `outputs/scanner/`, `logs/` — add when a committed consumer or runner requires them.

`**logs/`:** Tranche 3 **only if** `run_universe_scan.py` is specified to write a log file under `future_modules/the_fade/logs/`; if the runner is stdout-only, **do not create `logs/`.

**Never before §3.3 gate:** `future_modules/the_fade/dashboard_contract/` (any file).

**Never before Phase 13 execution:** `schemas/scout_heartbeat.schema.json`, heartbeat metrics code.

**Grouped pattern note:** Only the nine schemas and eight examples above are in scope for Tranche 1 proof. Adding other `*.schema.json` or `example_*.json` in `the_fade` before MASTER Phase 4 requires amending this lock or the active MASTER phase scope.

---

## 5. Obsolete framing and do-not-carry-forward

**None of the following may drive scout-layer execution, naming, or proof gates:**

1. **Stock analyst module as THE FADE product identity** — brief/risk pipeline is **downstream**, not the scout worker.
2. **Brief-first or confirm-symbol → brief as the FADE front door** — scout entry is scanner + signal packets per canon.
3. **Watchlist-first as synonym for signal-first** — deprecated per revision notes.
4. **Filename-suffix pairing as the long-term linkage standard** — ID-based linkage is target; do not encode mtime/suffix hacks into scout contracts.
5. **Research Swarm as a scoring lane for MVP** — RS is **read-only context** only; it must not dominate fusion.
6. **Adding Lane D, shadow lanes, or ghost lane registry in Tranches 1–3** to compensate for missing proof.
7. **Treating dashboard routes or `dashboard_contract` files as Phase 1–2 success criteria** — forbidden per §3.3.
8. **Treating MVP lane recommendations (oral or draft text) as locked canon** — only `mvp_lane_approval.json` with `approved: true` locks vendors.
9. **Legacy assumption:** that the eight canon MD files **must** live under `future_modules/stock_module/` — **deprecated**; path truth is `**CANON_INDEX.md` only after Tranche 1.

---

## 6. Phase 0 exit lock (binary)

**Phase 0 incomplete if any item is false:**

1. [ ] **Canon:** The eight filenames in the **Canonical inputs** block are recognized as the only design canon; path resolution will use `future_modules/the_fade/docs/CANON_INDEX.md` after Tranche 1.
2. [ ] **Heartbeat:** Tranches 1–3 will add no `scout_heartbeat.schema.json` and no heartbeat metrics code; `module_spec.md` will contain subsection **Heartbeat monitor (deferred)** satisfying §3.1.
3. [ ] **MVP gate:** `mvp_lane_approval.json` rules in §3.2 are binding; Phase 2 does not complete and Phase 3 does not start without `approved: true` and all required keys.
4. [ ] **Dashboard:** No `dashboard_contract` files and no dashboard implementation per §3.3 until both conditions in §3.3 are met.
5. [ ] **Anti-padding:** Tranche 1 creates only paths listed in **§4** for Tranche 1 (optional: omit `DASHBOARD_READ_MODEL_NOTES.md`).
6. [ ] **Build order:** `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md` (path via `CANON_INDEX.md`) governs execution order over `JARVIS_THE_FADE_BUILD_CHECKLIST.md`.
7. [ ] **MVP stack:** Three evidence lanes plus Research Swarm read-only context; no Lane D, shadow, ghost, or heartbeat **implementation** in Tranches 1–3.
8. [ ] **Downstream deferred:** Paper trading, daily summary, learning/calibration, autonomy, live readiness, live pilot are out of scope until their MASTER phases.
9. [ ] **Obsolete framing:** Every bullet in **§5** is acknowledged as **rejected** for current execution control.
10. [ ] **Active authority:** `THE_FADE_PHASE0_FINAL_LOCK.md` in repo will be the sole lock artifact after first Tranche 1 commit; prior drafts have **zero** execution authority.
11. [ ] **Jarvis discipline:** No worker expansion without contracts; no dashboard theater; MASTER proof gates enforced in order.

---

## 7. Filename precision table (Tranches 1–3)

| path                                                                    | tranche | required now / later / deferred     | why exact naming matters                                    |
| ----------------------------------------------------------------------- | ------- | ----------------------------------- | ----------------------------------------------------------- |
| `future_modules/the_fade/module_spec.md`                                | 1       | required now                        | Stable spec anchor; heartbeat subsection title is literal.  |
| `future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK.md`            | 1       | required now                        | Single authority filename; agents search this string.       |
| `future_modules/the_fade/docs/CANON_INDEX.md`                           | 1       | required now                        | Prevents scattered wrong paths; eight rows for eight files. |
| `future_modules/the_fade/schemas/fade_task_packet.schema.json`          | 1       | required now                        | Matches artifact name; validator wiring.                    |
| `future_modules/the_fade/schemas/scanner_candidate_set.schema.json`     | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/schemas/normalized_signal_event.schema.json`   | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/schemas/lane_scorecard.schema.json`            | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/schemas/contra_signal_result.schema.json`      | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/schemas/signal_packet.schema.json`             | 1       | required now                        | Same; dashboard gate references this basename.              |
| `future_modules/the_fade/schemas/conflict_packet.schema.json`           | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/schemas/scout_failure.schema.json`             | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/config/lane_registry.json`                     | 1       | required now                        | Single registry filename per Arch intent.                   |
| `future_modules/the_fade/config/direction_models.json`                  | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/config/fusion_policy.json`                     | 1       | required now                        | Threshold/weight registry filename fixed.                   |
| `future_modules/the_fade/config/scanner_policy.json`                    | 1       | required now                        | Scanner runner must read known path.                        |
| `future_modules/the_fade/config/escalation_policy.json`                 | 1       | required now                        | Writers resolve failures consistently.                      |
| `future_modules/the_fade/config/safety_governor_policy.json`            | 1       | required now                        | Arch baseline file name.                                    |
| `future_modules/the_fade/config/mvp_lane_approval.json`                 | 2       | later (Tranche 2)                   | Gate artifact; exact name for grep and CI.                  |
| `future_modules/the_fade/config/deferred_sources.json`                  | 2       | later                               | Phase 2 deliverable.                                        |
| `future_modules/the_fade/docs/MVP_SOURCE_RELIABILITY_AUDIT.md`          | 2       | later                               | Phase 2; no vendor names until approval.                    |
| `future_modules/the_fade/scripts/run_universe_scan.py`                  | 3       | later                               | Single agreed runner entrypoint basename.                   |
| `future_modules/the_fade/outputs/scanner/`                              | 3       | later                               | Scanner output directory name fixed.                        |
| `future_modules/the_fade/logs/`                                         | 3       | deferred unless runner writes files | No dir without consumer.                                    |
| `future_modules/the_fade/examples/example_fade_task_packet.json`        | 1       | required now                        | One example per schema; no wildcard.                        |
| `future_modules/the_fade/examples/example_scanner_candidate_set.json`   | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/examples/example_normalized_signal_event.json` | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/examples/example_lane_scorecard.json`          | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/examples/example_contra_signal_result.json`    | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/examples/example_signal_packet.json`           | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/examples/example_conflict_packet.json`         | 1       | required now                        | Same.                                                       |
| `future_modules/the_fade/examples/example_scout_failure.json`           | 1       | required now                        | Same.                                                       |

---

## 8. Artifact dependency table (Phase 1 contracts + registries)

| artifact                    | producer                    | consumer                            | first tranche    | schema vs runtime | absence effect                           |
| --------------------------- | --------------------------- | ----------------------------------- | ---------------- | ----------------- | ---------------------------------------- |
| fade_task_packet            | Human / future task builder | Normalization+ (Phase 4+)           | Phase 4+ runtime | schema T1         | Hard fail when task assumed              |
| scanner_candidate_set       | `run_universe_scan.py`      | Future task/normalize               | T3 output        | schema T1         | Hard fail Phase 3 if invalid             |
| normalized_signal_event     | Future normalizer           | Scoring                             | Phase 4          | schema T1         | Unused T1–T3                             |
| lane_scorecard              | Future scorer               | Fusion                              | Phase 5          | schema T1         | Unused T1–T3                             |
| contra_signal_result        | Future contra               | Fusion                              | Phase 6          | schema T1         | Unused T1–T3                             |
| signal_packet               | Future fusion               | Dashboard Phase 8, research Phase 9 | Phase 7          | schema T1         | Blocks dashboard_contract per §3.3       |
| conflict_packet             | Future fusion               | Triage / UI later                   | Phase 7          | schema T1         | Unused T1–T3                             |
| scout_failure               | Stage writers               | Escalation / health later           | Phase 4+         | schema T1         | Soft T1–T3; hard if invalid when written |
| lane_registry.json          | Human                       | Audit T2, adapters T4+              | T1 struct        | runtime           | Hard fail Phase 2 if bad                 |
| direction_models.json       | Human                       | Scoring Phase 5                     | T1               | runtime           | Hard fail Phase 5                        |
| fusion_policy.json          | Human                       | Fusion Phase 7                      | T1               | runtime           | Hard fail Phase 7                        |
| scanner_policy.json         | Human                       | Scanner T3                          | T1               | runtime           | Hard fail Phase 3                        |
| escalation_policy.json      | Human                       | All writers                         | T1               | runtime           | Hard fail if missing row when needed     |
| safety_governor_policy.json | Human                       | Paper/autonomy later                | T1               | runtime           | Hard fail when those phases start        |
| mvp_lane_approval.json      | Human operator              | Phase 2 content                     | T2               | gate              | Hard stop Phase 2/3 without approval     |

---

## 9. Explicit next move

Execute **MASTER Phase 1** using **only** §4 Tranche 1 rows. Commit `future_modules/the_fade/docs/THE_FADE_PHASE0_FINAL_LOCK.md` as the approved text of this lock.

---

## 10. Explicit do-not-do-next

- Do not create `future_modules/the_fade/dashboard_contract/` before §3.3.
- Do not add `schemas/scout_heartbeat.schema.json` before Phase 13.
- Do not name MVP vendors in audit or `lane_registry.json` before `mvp_lane_approval.json` has `approved: true`.
- Do not start Phase 3 if Phase 2 proof or approval failed.
- Do not create directories without a listed consumer in §4.
- Do not use superseded drafts as authority.
- Do not cite `future_modules/stock_module/` as the canonical home for the eight MDs in execution text — use `CANON_INDEX.md` after Tranche 1.

---

## Hard self-sufficiency statement

This lock is **self-contained**: obsolete framing is **§5**; exit criteria are **§6** and reference only sections present here. **No** stock_module path appears as normative canon location. **No** wildcard identifies a required Tranche 1–3 file — **§4** and **§7** enumerate exact names. Execution control = `**THE_FADE_PHASE0_FINAL_LOCK.md`** + eight canon files (paths via `**CANON_INDEX.md`**) + `\*\*JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md\*\` order.

---

_End of THE FADE Phase 0 final lock._
