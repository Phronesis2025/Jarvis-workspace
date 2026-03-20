# MODULE_CHECKLISTS

Rendered from `state/module_checklists.json`. Canonical source of truth for per-module build-path checklists.

**Generated at:** 2026-03-20

---

## WCS Code Module

**Purpose:** Prove one bounded WCS task loop; operator-assisted coding worker via Cursor; sequential only.

**Current phase:** Workflow hardening  
**Current step:** workflow_hardening_complete  
**Final version:** Trustworthy sequential WCS task loop: select, prep, worker, commit, QA, reconcile, export; one task at a time; no fabrication.

### Phase 0 — Reset and architecture lock
**Goal:** Lock project shape; WCS as first proof domain.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | Jarvis as foreman/orchestrator, not main coder | done |
| 2 | Local-first; JSON as source of truth | done |
| 3 | WCS as first active proof domain | done |
| 4 | Playwright as QA truth for WCS | done |
| 5 | One bounded task at a time | done |

### Phase 1 — Core file/state foundation
**Goal:** Durable system structure; visible state.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | master_backlog.json + MASTER_BACKLOG.md | done |
| 2 | Task packet generation and reconcile | done |
| 3 | Escalation state (escalations.json / ESCALATIONS.md) | done |
| 4 | File registry and project status | done |

### Phase 2 — WCS semi-manual proof loop
**Goal:** Prove backlog → packet → worker → reconcile → QA loop.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | Backlog rendering; packet generation; reconcile | done |
| 2 | Playwright home smoke path; public scout | done |
| 3 | Defect normalizer; scout noise rules | done |
| 4 | Overnight health check | done |

### Phase 3 — Jarvis foreman and live cycles
**Goal:** jarvis.py selects task; real WCS cycles under Jarvis control.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | jarvis.py foreman; daily plan; run log | done |
| 2 | Commit gate helper; stamp guard; worker/QA result validation | done |
| 3 | run_wcs_operator_entrypoint.py prep/post | done |
| 4 | run_one_task_cycle.py; run_one_task_full_cycle.py | done |
| 5 | run_task_sequence.py; 5-task batch proof | done |
| 6 | Post-task export; cleanup-to-main after success | done |

### Phase 3C — Workflow hardening
**Goal:** Strict launch; page-specific smoke; sequential runner proven.  
**Status:** in_progress

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | run_cursor_worker.py strict post-launch audit | done | |
| 2 | Page-specific smoke for /about, /schedules, /drills | done | |
| 3 | 5-task fake-task batch proof (WCS-037 through WCS-049) | done | |
| 4 | Broader route/page-smoke coverage | not_started | Current smoke test still limited |
| 5 | Record when human/operator action required | not_started | |

### Phase 4 — Controlled autonomy (deferred)
**Goal:** Scheduling, unattended execution — only after Phase 3 stable.  
**Status:** deferred

| # | Item | Status |
|---|------|--------|
| 1 | Limited scheduled cycles | deferred |
| 2 | Unattended end-to-end execution | deferred |

---

## Pathfinder

**Purpose:** Bounded read-only intake/investigation worker for WCS; no code edits, no git actions.

**Current phase:** Proof  
**Current step:** v1_proven  
**Final version:** Trustworthy read-only research scout: intake packet → bounded context → structured result; optional LLM synthesis with safe fallback.

### Phase: Design
**Goal:** Define intake/output contract; read-only scope.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | Intake packet format; minimal or full task packet | done |
| 2 | Output: synthesis, findings, optional draft backlog candidate | done |
| 3 | Read-only only; no code edits, no git | done |

### Phase: Implementation
**Goal:** run_pathfinder.py; bounded context from workspace and WCS repo.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | run_pathfinder.py CLI; config-driven | done |
| 2 | Optional LLM synthesis via pathfinder_llm_synthesis.py | done |
| 3 | Fallback to rule-based when LLM unavailable/API key missing | done |
| 4 | synthesis_source and llm_skipped_reason in result | done |
| 5 | validation_failure:<reason> diagnostics | done |

### Phase: Proof
**Goal:** Live run proven; fallback + LLM path proven.  
**Status:** in_progress

| # | Item | Status |
|---|------|--------|
| 1 | Live run with realistic WCS intake packet | done |
| 2 | --no-llm => rule_based/no_llm proof | done |
| 3 | LLM-enabled success path proven | done |
| 4 | Confidence normalization hardening | done |
| 5 | Broader Pathfinder expansion | deferred |

---

## Jarvis Dashboard

**Purpose:** Read-only web dashboard for Jarvis system progress; Supabase as read model.

**Current phase:** Deployment and verification  
**Current step:** v1_live_on_vercel  
**Final version:** Trustworthy read-only dashboard: Overview, Task Board, Recent Runs, Pathfinder; live data from exporter; no write-back, no scheduling, no automatic sync.

### Phase: Setup
**Goal:** Next.js app; Supabase schema; mock data fallback.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | dashboard_task_state, dashboard_runs, dashboard_module_status | done |
| 2 | Mock data when Supabase env vars absent | done |
| 3 | RLS policies for anon read | done |

### Phase: Implementation
**Goal:** Overview, Task Board, Recent Runs, Pathfinder pages.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | Overview: module status, metrics, next steps | done |
| 2 | WCS trust metrics (B/S/P) in Overview and Recent Runs | done |
| 3 | B1 module section and B1 process chart on Overview | done |
| 4 | Exporter health surface on Overview | done |
| 5 | fetchCache force-no-store for live Overview data | done |

### Phase: Deployment and verification
**Goal:** Vercel live; lint passes; build proof.  
**Status:** in_progress

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Deploy to Vercel | done | |
| 2 | Lint passes | done | |
| 3 | Build proof (npm run build) | blocked | Environment-blocked on some Windows setups: EPERM on Next trace file |

---

## B1 Local Website Defect Watcher

**Purpose:** Read-only watcher: route checks, evidence capture, proposed defect packets for operator review.

**Current phase:** Proof  
**Current step:** v1_proven  
**Final version:** Trustworthy v1 watcher: config-driven; Watcher Config → Route Checks → Evidence Capture → Noise Filter/Dedupe → Proposed Defect Packets → Operator Review; no operator approval workflow in v1.

### Phase: Implementation
**Goal:** run_local_website_defect_watcher.py; Playwright; config-driven.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | CLI: --config <path>; first site wcsbasketball.site | done |
| 2 | Route checks; direct reachability; no nav-link clicking | done |
| 3 | Evidence: run_result, screenshots, console_errors, evidence_manifest | done |
| 4 | Proposed defect packets; dedupe in state | done |
| 5 | Signal hardening: Supabase/WebSocket/realtime noise filtered | done |

### Phase: Proof
**Goal:** Fresh proof run; 0 findings after signal hardening.  
**Status:** in_progress

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Fresh proof run: 0 findings, 0 proposed packets, 4 screenshots | done | |
| 2 | Operator approval workflow | deferred | Watcher creates proposed packets only; not implemented |

---

## Dashboard Exporter

**Purpose:** One-way export of local Jarvis state to Supabase dashboard tables; never mutates Jarvis truth files.

**Current phase:** Verification  
**Current step:** dry_run_proven  
**Final version:** Trustworthy one-way sync: master_backlog, results, Pathfinder outputs → dashboard tables; WCS trust metrics from qa_result/worker_result; dry-run and live export both proven.

### Phase: Implementation
**Goal:** export_dashboard_data.py; gather and upsert.  
**Status:** done

| # | Item | Status |
|---|------|--------|
| 1 | Gather task state from master_backlog + task packets | done |
| 2 | Gather runs from logs; Pathfinder cases from outputs | done |
| 3 | WCS trust metrics: build, smoke, page-smoke, route, stop_reason | done |
| 4 | operator_checkpoints from qa_result | done |
| 5 | dashboard_export_log for Last dashboard update | done |

### Phase: Verification
**Goal:** Dry-run available; live export separate proof surface.  
**Status:** in_progress

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | --dry-run for payload/env health without writes | done | |
| 2 | Live export connectivity/write success | in_progress | Separate proof surface; post-task export hook runs when env vars present |
