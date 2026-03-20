# JARVIS_REBUILD_PHASE_CHECKLIST.md

## Live Doc Status
- Last reviewed: 2026-03-20
- Last updated: 2026-03-20 (workflow-hardening milestone: 5-task fake-task batch proof)
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Status: aligned to current live hardening state (escalation surfaces live; commit gate helper live and proven; file registry drift/coverage checker live; QA result drafting helper live and validator-proven; packet lifecycle/status cleanup keeps reconciled task packet artifacts aligned; Option B V1 wrapper live; one-task cycle wrapper proven on WCS-046; full-cycle wrapper proven on WCS-061 and WCS-008; sequential runner run_task_sequence.py proven on WCS-028, WCS-029+WCS-030, and 5-task batch WCS-037 through WCS-049; workflow-hardening milestone complete enough for current phase: 5-task fake-task batch passed, live export after each completed task passed, WCS returns to clean main after success; sequence non-interactive passthrough live; post-task export live; post-success cleanup-to-main live; blocked/excluded specimen semantics cleanup deferred; page-specific smoke support implemented and proven; Pathfinder v1 proven; Pathfinder optional LLM synthesis fallback + LLM path proven; broader Pathfinder expansion deferred; Jarvis Dashboard v1 live on Vercel as read-only Supabase-backed dashboard; exporter working; WCS trust-metrics lane implemented; broader route/page-smoke coverage and unattended execution remain later work; no write-back, scheduling, or automatic sync; overall smoke coverage still limited)

## Purpose

This checklist summarizes the Jarvis rebuild from the beginning through roughly Phase 3–4, using the project decisions we already locked:

- local-first
- Jarvis as foreman/orchestrator, not main coder
- JSON as machine truth
- Markdown as rendered human view
- WCS as the first active project
- WCS worker as the current coding worker, executed through Cursor in this phase
- Playwright as the QA layer
- parent login deferred
- voice deferred
- n8n worker deferred until later

---

# Current broad position

**Current reality:**  
We are **past the reset/foundation stage** and **well into the WCS proof-loop stage**.

### Rough progress by phase
- **Phase 0 — reset / architecture lock:** mostly complete
- **Phase 1 — file/state/script foundation:** mostly complete
- **Phase 2 — WCS semi-manual proof loop:** strong progress, mostly working
- **Phase 3 — true Jarvis foreman loop:** foreman built; daily plan/run log active; live cycles; escalation surfaces (`escalations.json` / `ESCALATIONS.md`) are live and in use
- **Phase 4 — controlled autonomy / more workers:** future

### Short version
We have built a lot of the rails.  
The central Jarvis foreman (`jarvis.py`) is **built and in use**; remaining Phase 3 work is state completeness and proving live Jarvis-controlled cycles.

---

# Phase 0 — Reset and architecture lock

## Goal
Stop chasing fake autonomy and lock the real project shape.

## Checklist
- [x] Decide Jarvis is a **foreman/orchestrator**, not the main coding worker
- [x] Decide the system is **local-first**
- [x] Decide WCS is the **first active proof domain**
- [x] Decide the WCS worker remains the current coding worker and Cursor remains the current execution surface for that worker
- [x] Decide Playwright is the QA truth for WCS
- [x] Decide phase 1 uses **Python scripts**, not heavy orchestration frameworks
- [x] Decide state uses **JSON as source of truth** and **Markdown as human view**
- [x] Defer parent login area for now
- [x] Defer voice for later phases
- [x] Defer n8n worker until WCS foundation is stronger
- [x] Lock “one bounded task at a time” as the phase-1 operating rule

## Deliverable outcome
- Project direction stopped being vague
- Scope was reduced to something boring and buildable
- The rebuild stopped pretending to be fully autonomous on day one

---

# Phase 1 — Core file/state foundation

## Goal
Create the minimum durable system structure so the project can operate on visible state instead of chat memory.

## Checklist
- [x] Create core source-of-truth docs
- [x] Create machine-readable backlog state
- [x] Create human-readable backlog render
- [x] Establish file registry concept
- [x] Establish project status concept
- [x] Establish logs folder structure
- [x] Establish scripts/config/state folder pattern
- [x] Define WCS backlog categories
- [x] Define “do not mark done without evidence” rule
- [x] Define escalation/pause philosophy
- [x] Initialize local Git repo for `C:\dev\jarvis-workspace`

## Expected files / concepts in this phase
- `master_backlog.json`
- `MASTER_BACKLOG.md`
- `file_registry.json`
- `FILE_REGISTRY.md`
- `project_status_wcs.json`
- `PROJECT_STATUS_WCS.md`
- workspace logs structure
- source-of-truth docs

## Deliverable outcome
- The system has visible state
- The project can now operate from files instead of vague discussion
- The workspace now has basic version history via Git

---

# Phase 2 — WCS semi-manual proof loop

## Goal
Prove one boring loop works cleanly before building more agents.

## Core loop to prove
1. backlog item exists
2. task packet is generated
3. Cursor executes the work
4. result is recorded/reconciled
5. QA runs
6. task becomes done or escalated
7. state updates correctly

---

## Phase 2A — Backlog and packet mechanics

### Checklist
- [x] Build `render_master_backlog.py`
- [x] Confirm `MASTER_BACKLOG.md` renders from `master_backlog.json`
- [x] Build `generate_task_packet.py`
- [x] Build `reconcile_task_outcome.py`
- [x] Confirm task packet generation works
- [x] Confirm reconcile flow works
- [x] Confirm multiple WCS tasks have already moved through the loop successfully

### Deliverable outcome
- The backlog-to-packet-to-reconcile loop is real
- WCS tasks are not just conceptual; they are moving

---

## Phase 2B — QA and scout layer

### Checklist
- [x] Stabilize Playwright home smoke path
- [x] Confirm `WCS-011` QA plumbing is in main
- [x] Build public scout route config
- [x] Build `public_scout.spec.ts`
- [x] Build `run_wcs_scout.py`
- [x] Run public scout successfully
- [x] Filter false positives so Public Scout v1 returns PASS correctly

### Deliverable outcome
- WCS now has a repeatable route-checking and defect-detection layer
- QA/intake is stronger than before
- Public Scout v1 is working

---

## Phase 2C — Defect-to-backlog normalization

### Checklist
- [x] Design defect normalizer in same style as current system
- [x] Build `normalize_scout_to_backlog.py`
- [x] Build `normalize_scout_to_backlog.ps1`
- [x] Build `scout_noise_rules.json`
- [x] Prove clean-run no-op behavior
- [x] Prove synthetic failure insertion behavior
- [x] Prove duplicate suppression behavior
- [x] Integrate normalizer into `run_wcs_scout.py`
- [x] Confirm integrated scout -> normalizer run works cleanly
- [x] Log normalizer output into same timestamped scout log folder

### Deliverable outcome
- Real scout failures can now become backlog-ready tasks
- Known noise can be filtered
- Duplicate tasks can be suppressed
- Defect intake is now partially automated

---

## Phase 2D — Health and operational guardrails

### Checklist
- [x] Build `overnight_health_check.py`
- [x] Run overnight health check successfully
- [x] Confirm overnight health check reports PASS/WARN honestly
- [x] Confirm warning handling is visible and useful
- [x] Keep health check read-only instead of pretending it “fixes” things

### Deliverable outcome
- The system has a basic operational self-check
- Shutdown/startup confidence is better
- Guardrails are present

---

## Phase 2 overall status
### Status: **Mostly complete / strongly working**

### What is proven
- Backlog rendering works
- Task packet generation works
- Reconcile works
- Public scout works
- Overnight health check works
- Defect normalization works
- Several WCS tasks have already been completed successfully

### What is still missing in Phase 2
- More live WCS tasks should continue moving through the loop
- State files still need continued cleanup and consistency work
- Some original planned phase-1 scripts were replaced by practical equivalents and may still need naming cleanup

---

# Phase 3 — Build the true Jarvis foreman

## Goal
Stop relying on manual glue between scripts and create the actual Jarvis planning/orchestration script.

## Status: foreman built and in use

### Checklist
- [x] Build `jarvis.py`
- [x] Have `jarvis.py` load backlog + WCS project status
- [x] Have `jarvis.py` choose exactly **one valid bounded WCS task**
- [x] Enforce pull rules for allowed WCS task categories
- [x] Write a valid task packet automatically
- [x] Write/update `DAILY_PLAN.md`
- [x] Write/update `daily_plan.json`
- [x] Append to `RUN_LOG.md`
- [x] Append to `run_log.json`
- [x] Record the selected task, reason, and timestamp
- [x] Prevent selecting blocked, done, or invalid tasks
- [x] Prevent selecting more than one task per cycle
- [x] Respect initial “max 1 WCS task per day” rule
- [ ] Record when human/operator action is required
- [x] Make Jarvis operate from files/state instead of chat memory

## Optional companion cleanup in Phase 3
- [ ] Decide whether current working scripts keep their present names
- [ ] Or wrap/re-map them to the original planned script naming model
- [ ] Clean drift between “working system” and “planned system” terminology

## Deliverable outcome
- Jarvis becomes a real foreman script
- The system no longer depends on manual operator stitching between every step
- The architecture finally matches the core promise of the project

---

# Phase 3B — Complete the missing state model

## Goal
Finish the state surfaces the docs originally assumed would exist.

### Checklist
- [x] Make `daily_plan.json` real and active
- [x] Make `RUN_LOG.md` real and active
- [x] Make `run_log.json` real and active
- [x] Make `escalations.json` real and active
- [x] Make `ESCALATIONS.md` real and active
- [x] Make `project_status_n8n.json` real even if deferred
- [x] Tighten task packet lifecycle/status consistency so reconciled packet JSON + markdown no longer remain misleadingly `ready`; safely proved on WCS-043 (`tasks/WCS-043_task.json` now shows `status: done`, `tasks/WCS-043_task.md` now shows `Status: done`)
- [ ] Make `AGENT_REGISTRY.md` real if still part of the intended system
- [ ] Make `OPERATING_RULES.md` real if still part of the intended system
- [ ] Ensure all state files have a clear source-of-truth relationship
- [ ] Ensure no state file is lying or stale

## Deliverable outcome
- The file-based operating model becomes complete
- The system becomes more self-explanatory and durable

---

# Phase 3C — Live Jarvis-controlled WCS cycles

## Goal
Run real WCS work through Jarvis control, not just supporting scripts.

### Checklist
- [x] Jarvis selects a real WCS task
- [x] Jarvis writes a valid packet
- [x] Human executes task in Cursor
- [x] Worker result is captured cleanly
- [x] QA runs against the changed work
- [x] Task becomes done or escalated based on evidence
- [x] Run log updates correctly
- [ ] Project status updates correctly
- [x] Repeat successfully across multiple real tasks (currently proven for WCS-016, WCS-017, WCS-018, and WCS-019 as full completed/reconciled loops)
- [ ] Prove longer-run consecutive-task stability beyond the current four-task proof

## Deliverable outcome
- The boring core loop is now proven for multiple real WCS tasks under Jarvis control (currently WCS-016, WCS-017, WCS-018, WCS-019)

---

# Phase 4 — Controlled autonomy and expansion

## Goal
Only after Phase 3 is stable, turn on more automation carefully.

## Phase 4A — Scheduling / timed runs

### Checklist
- [ ] Enable very limited scheduled cycles
- [ ] Start with one run at a time
- [ ] Prevent overlapping cycles
- [ ] Respect pause/escalation conditions
- [ ] Confirm scheduling does not create duplicate or conflicting work
- [ ] Confirm scheduled runs preserve logs and state correctly

## Deliverable outcome
- Jarvis starts acting on a clock, not just manual launch
- Still boring, controlled, and auditable

---

## Phase 4B — Additional worker types

### Checklist
- [x] Add research scout for debugging support — Pathfinder v1 proven (bounded read-only WCS intake; manual CLI; 2026-03-18)
- [x] Pathfinder optional LLM synthesis — fallback + LLM path proven; `--no-llm` and `--model`; safe fallback to rule-based when module/API key absent or synthesis fails; result includes `synthesis_source` and `llm_skipped_reason`; validation diagnostics preserve `validation_failure:<reason>`; broader Pathfinder expansion deferred; confidence normalization hardening complete, stable enough for broader testing
- [x] B1 v1 Local Website Defect Watcher — design + implementation + proof complete; first site https://www.wcsbasketball.site/; Playwright; CLI/config-driven; read-only; writes run_result, screenshots, console_errors, evidence_manifest, proposed_defect_packets; dedupe in state/local_website_defect_watcher_dedupe.json; signal hardening complete; fresh proof 0 findings; operator approval workflow not implemented; v1 does not click nav links
- [ ] Add research scout for topic/content gathering if still valuable
- [ ] Revisit n8n improvement worker once rubric is machine-checkable
- [ ] Add truth-mapping helpers for other projects if needed
- [ ] Add additional bounded workers only when packet + output + QA path are clear
- [ ] Refuse to add “cool” workers that do not have a strict contract

## Deliverable outcome
- Jarvis grows from one proof loop into a true multi-worker system
- Expansion happens from stable contracts, not hype

---

## Phase 4C — System hardening and renderer cleanup

### Checklist
- [x] Build `render_file_registry.py`
- [x] Stop hand-maintaining `FILE_REGISTRY.md` (now rendered from file_registry.json by render_file_registry.py)
- [x] Add health checks for new critical scripts/configs — **live via `critical_surface_health_check.py`** (read-only sanity check: existence, compile, and file_registry_check + naming_drift_check pass)
- [x] WCS trust-metrics dashboard surfacing — **live**; exporter derives build/smoke/page-smoke/route/stop_reason from local evidence; Overview and Recent Runs show trust signals; current route/page-smoke trust is better surfaced but broader coverage remains later work; full-system sweep mostly passed with bounded blockers; dashboard lint passes; dashboard build proof remains environment-blocked on Windows (EPERM on Next trace file); exporter safe dry-run mode now complete
- [x] Dashboard stale-data/cache fix — **complete**; Overview route uses `fetchCache = "force-no-store"`; after restart and export refresh, Overview shows live data (Last dashboard update, What happened today, Recent activity, WCS task totals); build env blocker separate and still open
- [x] Dashboard update for B1/operator visibility — **complete**; Overview now surfaces B1 module section (bounded, read-only, first site, proof summary), separate B1 process chart (Watcher Config → Route Checks → Evidence Capture → Noise Filter/Dedupe → Proposed Defect Packets → Operator Review), and exporter health surface (dry-run available, dry-run proof, live export separate proof surface); B1 surfaced on Overview only; no dedicated B1 page or nav item; no new Supabase-backed B1 data model; no write-back or control-plane additions; operator approval workflow and nav-link checking remain out of scope
- [x] Workflow-hardening milestone — **complete enough for current phase**; 5-task fake-task batch passed (WCS-037 through WCS-049); live export after each completed task passed; WCS returns to clean `main` after success; sequence non-interactive passthrough (`--confirm-commit`, `--manual-check`) live; post-task export hook live; post-success cleanup-to-main live; future cleanup of blocked/excluded specimen semantics deferred
- [ ] Harden all script wrappers
- [ ] Standardize output log locations
- [ ] Reduce naming drift across docs/state/scripts
- [ ] Further improve evidence reporting and human review surfaces

## Deliverable outcome
- The system becomes easier to maintain and trust over time

---

# Later phases — not now

## These are explicitly later, not current focus
- [ ] voice interface
- [ ] parent login / private family workflows in WCS
- [ ] autonomous n8n worker path
- [ ] broader multi-project scheduling
- [ ] larger agent fleet
- [ ] advanced mission-control dashboards
- [ ] robot/device coordination layers

---

# Practical current checkpoint

## Completed successfully
- [x] Core architecture decisions locked
- [x] WCS chosen as phase-1 proof domain
- [x] Backlog state exists in JSON + Markdown
- [x] Task packet generation works
- [x] Reconcile works
- [x] Playwright QA layer is active
- [x] Public Scout v1 works
- [x] Defect normalizer works
- [x] Overnight health check works
- [x] Local Git repo created for `jarvis-workspace`
- [x] Build `jarvis.py` (foreman selects task, writes daily plan and run log, generates packet, prepares branch)
- [x] Daily plan and run log state files real and active

## Next real priorities
- [x] Complete escalation state files (`escalations.json` / `ESCALATIONS.md`) and any remaining state surfaces — **live**
- [x] Run real Jarvis-controlled WCS cycles and prove consecutive-task stability (currently proven for WCS-016, WCS-017, WCS-018, and WCS-019)
- [x] Harden commit gate helper (commit-state enforcement around worker/QA completion and reconcile) — **live via `commit_gate_check.py`, proven in completed/reconciled loop**
- [x] QA execution reliability hardening for local WCS smoke QA (Playwright `webServer` now starts `npm run dev` when no E2E_BASE_URL/NEXT_PUBLIC_BASE_URL is set)
- [x] Build `qa_failure_triage.py` as a read-only helper to classify QA failures and suggest bounded next actions without mutating state
- [x] Build `stamp_guard_check.py` as a read-only pre-stamp guardrail to prevent stamping placeholder/draft/incomplete worker/QA results
- [x] Build `file_registry_check.py` as a read-only file-registry drift/coverage checker (helper/hardening surface, not in core task loop) — **live**
- [x] Build `naming_drift_check.py` as a read-only naming-drift helper for core hardening scripts/docs/registry entries (helper/hardening surface, not in core task loop) — **live**
- [x] Build `critical_surface_health_check.py` as a read-only sanity checker for the critical hardening surface (existence, compile, and registry/naming helper runs) — **live**
- [x] Build `build_cursor_handoff.py` as a workflow helper that prepares bounded Cursor handoff files from task packets — **live**
- [x] Build `build_task_cycle_summary.py` as a workflow helper that summarizes current task/worker/QA evidence into a human-readable task-cycle markdown file without executing tasks or mutating state — **live**
- [x] Build `run_guarded_task_cycle.py` as a workflow/orchestration helper that runs existing guarded task-cycle scripts in order and stops on first failure without changing their logic — **live**
- [x] Build `run_wcs_operator_entrypoint.py` as a thin operator-facing WCS wrapper over existing helpers with `prep` and `post` only; `prep` and `post` are freshly proven on `WCS-044`
- [x] Build `run_one_task_cycle.py` as a one-task-only operator wrapper that either accepts `--task WCS-XXX` or selects one ready bounded WCS task, delegates prep/optional strict launch to existing wrappers, and prints the remaining operator steps without claiming completion — **live and proven on WCS-046**
- [x] Build `run_one_task_full_cycle.py` as a full one-command single-task closeout wrapper (prep, strict launch, commit, build, managed dev server, smoke, screenshot capture, honest manual-check stop, --finalize for post); requires `--confirm-commit` and `--manual-check`; wrapper family can truthfully close a single task end-to-end — **live and proven on WCS-061 and WCS-008** (screenshot artifact support and --finalize proven on WCS-008; current smoke test still limited; page-specific task coverage should be improved later)
- [x] Wire optional QA-result drafting into guarded post_worker/full via `run_guarded_task_cycle.py --draft-qa-result` and QA evidence passthrough; draft step runs before `qa_result_validate.py --mode pre-stamp`; without `--draft-qa-result`, QA result JSON still required — **live**
- [x] Wire optional worker-result drafting into guarded post_worker/full via `run_guarded_task_cycle.py --draft-worker-result` plus truthful repeatable `--worker-command <text>` (and optional `--worker-executor` passthrough); inserted worker-draft step runs immediately before `worker_result_validate.py --mode pre-stamp`, pre_worker remains unchanged, and WCS-042 proved the safe boundary through worker draft PASS + worker pre-stamp validation PASS before intentionally stopping ahead of stamp/reconcile — **live**
- [x] Build `select_next_ready_task.py` as a read-only workflow helper that selects the next eligible ready task from backlog/planning surfaces using progression ladder (execution_lane, test_phase, selector_rank) when present, without mutating state — **live**
- [x] Build `build_daily_execution_prep.py` as a workflow helper that prepares operator-facing daily execution prep by ensuring packet availability (invoking `generate_task_packet.py` when needed), then chaining handoff and summary helpers, without executing tasks or mutating state beyond approved helper outputs — **live**
- [x] **Next major milestone:** Build Cursor invocation bridge (`run_cursor_worker.py`) — prefers real Agent CLI (`agent`) when available (Windows-hardened detection: which/where/PowerShell), falls back to desktop cursor launcher; attempts execution of generated handoff; reports PASS/BLOCKED/FAIL honestly; does not prove completion or write worker_complete; operator still verifies completion and finalizes worker-result evidence; system remains operator-assisted at the worker completion/evidence stage — **live**
- [x] Harden launch safety on the Cursor bridge/operator-wrapper path so `run_cursor_worker.py --require-auditable-delta` now fails honestly when branch drift occurs, no immediate working-tree delta exists, or changed files fall outside task scope; `run_wcs_operator_entrypoint.py prep --launch-cursor` now uses that strict audit mode; strict failure path safely proved, blocked/timeout path also honestly proved, and strict real-Agent success path is now proved on `WCS-041` and `WCS-046`
- [x] Add configurable real-Agent timeout control for the strict launch path via `run_cursor_worker.py --agent-timeout-seconds` with passthrough from `run_wcs_operator_entrypoint.py prep --launch-cursor`; strict audit truth remains unchanged
- [x] Build `draft_worker_result_from_evidence.py` as a worker-result drafting helper from task packet and repo evidence (branch, changed files); does not stamp, reconcile, or fabricate completion; operator reviews draft before post-worker — **live**
- [x] Harden `draft_worker_result_from_evidence.py` so `worker_complete` drafting requires one or more meaningful repeatable `--command <text>` entries, populates `commands_run` from those explicit values only, rejects placeholder-only command evidence, and closes the validator/stamp-guard `commands_run` gap — **live and proven on WCS-042** (`worker_result_validate.py --mode pre-stamp` PASS, `stamp_guard_check.py` PASS)
- [x] Real guarded end-to-end task cycle succeeded on WCS-042 (Agent-first run_cursor_worker, task repo workspace, draft_worker_result_from_evidence, stamp, QA, reconcile)
- [x] Build `draft_qa_result_from_evidence.py` as a QA-result drafting helper from operator-supplied evidence (CLI: build/smoke/manual status); dry-run by default, `--write` to persist; pre-stamp only; does not stamp, reconcile, or fabricate evidence; operator reviews draft before post-worker — **live** (validator-proven, e.g. WCS-042 pre-stamp)
- [ ] Only then consider scheduling
- [ ] Only after that consider more workers

---

# Bottom line

We are **not** at the beginning anymore.

We are also **not** at “Jarvis complete.”

We are roughly here:

- **Foundation:** mostly done
- **WCS support loop:** working
- **QA and defect intake:** strong
- **True Jarvis foreman/orchestrator:** built and in use (`jarvis.py` selects task, writes plan/run log, packet, branch)
- **Scheduling and additional workers:** future

That means the next serious step is not more idea generation.

It is:

## **Run real Jarvis-controlled WCS cycles and complete remaining state (escalations, etc.).**