# FILE REGISTRY

## Live Doc Status
- Last reviewed: 2026-03-13
- Last updated: 2026-03-13
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Status: aligned to current live hardening state; registry mirrors file_registry.json and is rendered by render_file_registry.py

## Purpose

This file is the human-readable registry of the Jarvis local build system.

It exists to prevent drift between:
- design documents
- live scripts
- state files
- generated task artifacts
- scout outputs
- WCS repo-side test files

JSON is the machine-readable source for later automation.
This markdown file is the human-readable view rendered from file_registry.json.

---

## Conventions

### Source Type
- `source_of_truth` = primary authoritative file
- `generated` = derived from another file
- `template` = reusable starter structure
- `runtime_output` = produced by scripts or test runs

### Categories
- `doc`
- `state`
- `script`
- `config`
- `template`
- `task_packet`
- `worker_result`
- `qa_result`
- `log`
- `repo_test`

### Owners
- `user`
- `jarvis_script`
- `cursor_worker`
- `playwright`
- `scout_runner`

---

## Registry

| File | Path | Category | Source Type | Owner | Purpose | Updated By | Notes |
|---|---|---|---|---|---|---|---|

| JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | doc | source_of_truth | user | High-level product requirements for Jarvis rebuild | user | Core planning doc (design-era; some sections are historical baseline rather than current live operating truth) |
| JARVIS_SYSTEM_DOCUMENTATION_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_DOCUMENTATION_v3.md | doc | source_of_truth | user | Detailed architecture and operating documentation | user | Core planning doc (design-era; some sections are historical baseline rather than current live operating truth) |
| JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | doc | source_of_truth | user | Current authoritative decisions and system rules | user | Most important design reference; some areas still describe earlier-phase assumptions and should be read as baseline when they diverge from JARVIS_LIVE_HANDOFF_BUNDLE.md |
| JARVIS_SCRIPT_PROCESS_REFERENCE.md | C:\dev\jarvis-workspace\JARVIS_SCRIPT_PROCESS_REFERENCE.md | doc | source_of_truth | user | Live reference for Jarvis WCS task execution process and hardening helpers | user | Documents current live Jarvis operating loop, guardrails, and helpers such as commit gates and pre-stamp checks |
| master_backlog.json | C:\dev\jarvis-workspace\state\master_backlog.json | state | source_of_truth | user | Machine-readable task backlog | user / jarvis_script | Primary backlog source |
| MASTER_BACKLOG.md | C:\dev\jarvis-workspace\state\MASTER_BACKLOG.md | state | generated | jarvis_script | Human-readable backlog table | render_master_backlog.py | Rendered from master_backlog.json |
| DAILY_REVIEW.md | C:\dev\jarvis-workspace\state\DAILY_REVIEW.md | state | source_of_truth | user | Daily execution log and summary | user / jarvis_script | Reconcile appends entries |
| DAILY_PLAN.md | C:\dev\jarvis-workspace\state\DAILY_PLAN.md | state | source_of_truth | user | Current planned work for the day | user | Lightly used so far |
| PROJECT_STATUS_WCS.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_WCS.md | state | source_of_truth | user | Human-readable WCS project status | user / jarvis_script | May later be rendered |
| PROJECT_STATUS_N8N.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_N8N.md | state | source_of_truth | user | Human-readable n8n project status | user | n8n worker deferred |
| file_registry.json | C:\dev\jarvis-workspace\state\file_registry.json | state | source_of_truth | user | Machine-readable file registry | user / jarvis_script | Source for FILE_REGISTRY.md; aligned to current live hardening state |
| FILE_REGISTRY.md | C:\dev\jarvis-workspace\state\FILE_REGISTRY.md | state | generated | jarvis_script | Human-readable file registry | user / future renderer | Human-readable registry view rendered from file_registry.json by render_file_registry.py; aligned to current live hardening state |
| render_master_backlog.py | C:\dev\jarvis-workspace\scripts\render_master_backlog.py | script | source_of_truth | jarvis_script | Renders MASTER_BACKLOG.md from backlog JSON | user | Working |
| update_master_backlog.ps1 | C:\dev\jarvis-workspace\scripts\update_master_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for backlog renderer | user | Convenience wrapper |
| generate_task_packet.py | C:\dev\jarvis-workspace\scripts\generate_task_packet.py | script | source_of_truth | jarvis_script | Creates task packet files and blank result files | user | Working |
| generate_task_packet.ps1 | C:\dev\jarvis-workspace\scripts\generate_task_packet.ps1 | script | source_of_truth | user | PowerShell wrapper for task generator | user | Convenience wrapper |
| reconcile_task_outcome.py | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.py | script | source_of_truth | jarvis_script | Reconciles worker and QA results into backlog state | user | Working |
| reconcile_task_outcome.ps1 | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.ps1 | script | source_of_truth | user | PowerShell wrapper for reconciler | user | Convenience wrapper |
| cursor_completion_contract.txt | C:\dev\jarvis-workspace\scripts\cursor_completion_contract.txt | template | source_of_truth | user | Forces structured Cursor completion summaries | user | Used in worker prompts |
| overnight_health_check.py | C:\dev\jarvis-workspace\scripts\overnight_health_check.py | script | source_of_truth | jarvis_script | Read-only overnight system health watcher | user | Working |
| run_overnight_health_check.ps1 | C:\dev\jarvis-workspace\scripts\run_overnight_health_check.ps1 | script | source_of_truth | user | Wrapper for overnight health watcher | user | Used for manual or scheduled runs |
| register_overnight_health_task.txt | C:\dev\jarvis-workspace\scripts\register_overnight_health_task.txt | doc | source_of_truth | user | Task Scheduler command notes | user | Scheduling helper |
| run_wcs_scout.py | C:\dev\jarvis-workspace\scripts\run_wcs_scout.py | script | source_of_truth | jarvis_script | Runs public WCS scout and stores results | user | Working |
| wcs_scout_routes.json | C:\dev\jarvis-workspace\config\wcs_scout_routes.json | config | source_of_truth | user | Public routes list for WCS scout | user | /shop and /news removed for now |
| WCS-001_task.md | C:\dev\jarvis-workspace\tasks\WCS-001_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Example completed task |
| WCS-001_task.json | C:\dev\jarvis-workspace\tasks\WCS-001_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Example completed task |
| WCS-002_task.md | C:\dev\jarvis-workspace\tasks\WCS-002_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Example completed task |
| WCS-002_task.json | C:\dev\jarvis-workspace\tasks\WCS-002_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Example completed task |
| WCS-003_task.md | C:\dev\jarvis-workspace\tasks\WCS-003_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Example completed task |
| WCS-003_task.json | C:\dev\jarvis-workspace\tasks\WCS-003_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Example completed task |
| WCS-004_task.md | C:\dev\jarvis-workspace\tasks\WCS-004_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Completed after branch cleanup |
| WCS-004_task.json | C:\dev\jarvis-workspace\tasks\WCS-004_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Completed after branch cleanup |
| WCS-011_task.md | C:\dev\jarvis-workspace\tasks\WCS-011_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | QA infrastructure task |
| WCS-011_task.json | C:\dev\jarvis-workspace\tasks\WCS-011_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | QA infrastructure task |
| *_worker_result.json | C:\dev\jarvis-workspace\results\*_worker_result.json | worker_result | runtime_output | cursor_worker | Worker completion record per task | user / cursor_worker | Reconciler input |
| *_qa_result.json | C:\dev\jarvis-workspace\qa\*_qa_result.json | qa_result | runtime_output | playwright | QA completion record per task | user / playwright | Reconciler input |
| *_escalation.json | C:\dev\jarvis-workspace\logs\*_escalation.json | log | runtime_output | jarvis_script | Escalation record for blocked or escalated tasks | user / jarvis_script | May be blank for many tasks |
| overnight_health_*.json | C:\dev\jarvis-workspace\logs\overnight_health_*.json | log | runtime_output | jarvis_script | Machine-readable overnight health output | overnight_health_check.py | Working |
| overnight_health_*.txt | C:\dev\jarvis-workspace\logs\overnight_health_*.txt | log | runtime_output | jarvis_script | Human-readable overnight health summary | overnight_health_check.py | Working |
| public_scout_results.json | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\public_scout_results.json | log | runtime_output | scout_runner | Structured route scout results | run_wcs_scout.py / public_scout.spec.ts | Latest run currently PASS |
| public_scout_summary.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\public_scout_summary.txt | log | runtime_output | scout_runner | Human-readable scout summary | run_wcs_scout.py | Latest run currently PASS |
| playwright_stdout.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\playwright_stdout.txt | log | runtime_output | scout_runner | Raw Playwright stdout from scout run | run_wcs_scout.py | Debug support |
| playwright_stderr.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\playwright_stderr.txt | log | runtime_output | scout_runner | Raw Playwright stderr from scout run | run_wcs_scout.py | Debug support |
| public_scout.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\public_scout.spec.ts | repo_test | source_of_truth | playwright | Public route scout spec for WCS | user | External WCS repo Playwright spec at C:\dev\wcsv2.0-new\tests\e2e |
| home.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\home.spec.ts | repo_test | source_of_truth | playwright | Smoke QA spec for home page | user | External WCS repo Playwright spec at C:\dev\wcsv2.0-new\tests\e2e |
| global-setup.ts | C:\dev\wcsv2.0-new\tests\e2e\helpers\global-setup.ts | repo_test | source_of_truth | playwright | Shared Playwright startup and readiness logic | user | External WCS repo Playwright helper at C:\dev\wcsv2.0-new\tests\e2e\helpers |
| package.json | C:\dev\wcsv2.0-new\package.json | repo_test | source_of_truth | user | Repo scripts including test:e2e:smoke | user | WCS repo-side dependency in external WCS repo at C:\dev\wcsv2.0-new |
| normalize_scout_to_backlog.py | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.py | script | source_of_truth | jarvis_script | Normalizes scout defects into backlog-ready tasks and updates backlog state | user | Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md |
| normalize_scout_to_backlog.ps1 | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for scout defect normalizer | user | Convenience wrapper |
| scout_noise_rules.json | C:\dev\jarvis-workspace\config\scout_noise_rules.json | config | source_of_truth | user | Known scout noise filtering rules for backlog normalization | user | Used by normalize_scout_to_backlog.py |
| JARVIS_PHASE_CHECKLIST.md | C:\dev\jarvis-workspace\JARVIS_PHASE_CHECKLIST.md | doc | source_of_truth | user | Phase-by-phase rebuild checklist and status for Jarvis workspace | user | Current canonical overview of phases, missing state surfaces, and next priorities |
| JARVIS_AGENT_IDEA_BACKLOG.md | C:\dev\jarvis-workspace\JARVIS_AGENT_IDEA_BACKLOG.md | doc | source_of_truth | user | Idea backlog for short-term modules and longer-term agent business concepts | user | Reusable idea backlog aligned with current Jarvis architecture |
| JARVIS_TASK_EXECUTION_CHECKLIST.md | C:\dev\jarvis-workspace\JARVIS_TASK_EXECUTION_CHECKLIST.md | doc | source_of_truth | user | Live execution checklist for bounded Jarvis WCS tasks | user | Defines current live execution phases for Jarvis-controlled WCS loop, including guardrails and helpers |
| JARVIS_LIVE_HANDOFF_BUNDLE.md | C:\dev\jarvis-workspace\JARVIS_LIVE_HANDOFF_BUNDLE.md | doc | source_of_truth | user | Live handoff bundle describing current Jarvis system truth, hardening state, and helper surfaces | user | Aggregates current live system decisions, hardened loop surfaces, and helper scripts for Jarvis rebuild |
| manual_loop_checklist.md | C:\dev\jarvis-workspace\scripts\manual_loop_checklist.md | doc | source_of_truth | user | Manual proof-loop checklist for running a WCS task through backlog, worker, QA, and reconcile | user | Operator runbook; should be aligned with actual script and state behavior to avoid drift |
| jarvis.py | C:\dev\jarvis-workspace\scripts\jarvis.py | script | source_of_truth | jarvis_script | Phase 3 foreman; reads backlog and project status, validates task eligibility, prepares and verifies WCS task branch, manages task packets, writes daily_plan and run_log, and records durable escalation state on hard failure | user | Does not perform code changes, QA, commits, stamping, or reconcile; acts as local-first foreman/orchestrator with stronger operator-safety output and durable escalation recording |
| prepare_wcs_task_branch.py | C:\dev\jarvis-workspace\scripts\prepare_wcs_task_branch.py | script | source_of_truth | user | Prepares WCS task branch for bounded task work | user | Used in task workflow to create or switch to task branch in WCS repo |
| stamp_result_timestamp.py | C:\dev\jarvis-workspace\scripts\stamp_result_timestamp.py | script | source_of_truth | user | Stamps completed_at (or specified field) on worker and QA result JSON files; takes FILE PATH as positional argument | user | Helper to keep result timestamps consistent; run once per result file with path to that file |
| daily_plan.json | C:\dev\jarvis-workspace\state\daily_plan.json | state | source_of_truth | jarvis_script | Current selected task and plan metadata; machine-readable | jarvis.py | Written by jarvis.py; pairs with DAILY_PLAN.md |
| run_log.json | C:\dev\jarvis-workspace\state\run_log.json | state | source_of_truth | jarvis_script | Append-only machine-readable run history | jarvis.py | Written by jarvis.py when a task is selected |
| RUN_LOG.md | C:\dev\jarvis-workspace\state\RUN_LOG.md | state | source_of_truth | jarvis_script | Append-only human-readable run log | jarvis.py | Written by jarvis.py when a task is selected |
| project_status_wcs.json | C:\dev\jarvis-workspace\state\project_status_wcs.json | state | source_of_truth | user | Machine-readable WCS project status | user | Mirror of PROJECT_STATUS_WCS.md; consumed by jarvis.py and scripts |
| project_status_n8n.json | C:\dev\jarvis-workspace\state\project_status_n8n.json | state | source_of_truth | user | Machine-readable n8n project status | user | Mirror of PROJECT_STATUS_N8N.md; n8n worker deferred |
| escalations.json | C:\dev\jarvis-workspace\state\escalations.json | state | source_of_truth | jarvis_script | Machine-readable escalation records for Jarvis hard failures | jarvis.py | Authoritative live escalation state; rendered to ESCALATIONS.md |
| ESCALATIONS.md | C:\dev\jarvis-workspace\state\ESCALATIONS.md | state | generated | jarvis_script | Human-readable escalation log | jarvis.py | Rendered from escalations.json whenever Jarvis records an escalation; reflects durable, active escalation state |
| pre_reconcile_check.py | C:\dev\jarvis-workspace\scripts\pre_reconcile_check.py | script | source_of_truth | jarvis_script | Read-only pre-reconcile readiness gate for a WCS task | user | Validates task/result/repo prerequisites before running reconcile; strictly read-only guardrail |
| post_reconcile_validate.py | C:\dev\jarvis-workspace\scripts\post_reconcile_validate.py | script | source_of_truth | jarvis_script | Read-only post-reconcile validator for a WCS task | user | Confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, DAILY_REVIEW.md, and result files; strictly read-only validator |
| commit_gate_check.py | C:\dev\jarvis-workspace\scripts\commit_gate_check.py | script | source_of_truth | jarvis_script | Read-only commit-state gate for a WCS task branch and HEAD | user | Validates branch, HEAD, ahead-of-main/master, clean worktree, commit message, and bounded committed-files/line counts before trusting worker/QA results; strictly read-only gate, now proven in a completed/reconciled loop (including WCS-019) |
| playwright.config.ts | C:\dev\wcsv2.0-new\playwright.config.ts | config | source_of_truth | wcs_repo | Local/CI Playwright execution config for WCS smoke QA | user | Local smoke now uses Playwright webServer to start npm run dev automatically when no E2E_BASE_URL / NEXT_PUBLIC_BASE_URL is set; central config for smoke QA server startup/reuse behavior |
| qa_failure_triage.py | C:\dev\jarvis-workspace\scripts\qa_failure_triage.py | script | source_of_truth | jarvis_script | Read-only QA failure triage helper for a WCS task | user | Classifies QA failures into environment_setup_failure, test_harness_failure, application_regression, or ambiguous based on QA result summary/notes; prints evidence-based next-step guidance without mutating any state |
| stamp_guard_check.py | C:\dev\jarvis-workspace\scripts\stamp_guard_check.py | script | source_of_truth | jarvis_script | Read-only pre-stamp guardrail for worker and QA result JSON files | user | Verifies worker and QA result files both exist, parse, have allowed statuses, remain pre-stamp, and are not obvious placeholders before running stamp_result_timestamp.py; strictly read-only and does not stamp or mutate state |
| worker_change_check.py | C:\dev\jarvis-workspace\scripts\worker_change_check.py | script | source_of_truth | jarvis_script | Read-only worker-boundary validator for changed-file scope and simple diff sanity | user | Validates that changed files stay within task scope and diffs are small before commit/finalization; strictly read-only worker-boundary gate |
| worker_result_validate.py | C:\dev\jarvis-workspace\scripts\worker_result_validate.py | script | source_of_truth | jarvis_script | Read-only worker-result schema validator for a WCS task | user | Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes; strictly read-only validator |
| qa_result_validate.py | C:\dev\jarvis-workspace\scripts\qa_result_validate.py | script | source_of_truth | jarvis_script | Read-only QA-result schema validator for a WCS task | user | Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes; strictly read-only validator |
| file_registry_check.py | C:\dev\jarvis-workspace\scripts\file_registry_check.py | script | source_of_truth | jarvis_script | Read-only file-registry drift and core-coverage checker for hardened-loop items | user | Verifies that file_registry.json and FILE_REGISTRY.md exist, parse, and contain entries for critical hardened-loop scripts/docs; strictly read-only and does not modify the registry |
| naming_drift_check.py | C:\dev\jarvis-workspace\scripts\naming_drift_check.py | script | source_of_truth | jarvis_script | Read-only naming drift detector for core hardening scripts/docs/registry entries | user | Checks for obvious name mismatches between core scripts/docs and the file registry; strictly read-only and does not auto-fix names |
| render_file_registry.py | C:\dev\jarvis-workspace\scripts\render_file_registry.py | script | source_of_truth | jarvis_script | Renderer for FILE_REGISTRY.md from file_registry.json | user | Reads state/file_registry.json and writes state/FILE_REGISTRY.md in the approved registry format; keeps the markdown registry rendered from JSON; strictly read-only except for writing FILE_REGISTRY.md |
| critical_surface_health_check.py | C:\dev\jarvis-workspace\scripts\critical_surface_health_check.py | script | source_of_truth | jarvis_script | Read-only sanity checker for critical Jarvis hardening surface | user | Verifies critical scripts/docs/registry exist, critical helpers compile, and file_registry_check + naming_drift_check pass; does not run full task loop or mutate state |
| build_task_cycle_summary.py | C:\dev\jarvis-workspace\scripts\build_task_cycle_summary.py | script | source_of_truth | jarvis_script | Workflow helper: builds human-readable task cycle summaries for a WCS task | user | Reads task packet, optional task markdown, worker result, and QA result (when present) and writes scratch/task_cycle_summaries/<task>_task_cycle_summary.md; does not execute tasks, change task state, or mutate backlog/results |
| run_guarded_task_cycle.py | C:\dev\jarvis-workspace\scripts\run_guarded_task_cycle.py | script | source_of_truth | jarvis_script | Workflow/orchestration helper for guarded WCS task cycles | user | Runs existing guarded task-cycle helpers in sequence for a single WCS task and stops on the first failure; does not replace their logic, execute worker code directly, or schedule tasks |
| select_next_ready_task.py | C:\dev\jarvis-workspace\scripts\select_next_ready_task.py | script | source_of_truth | jarvis_script | Read-only workflow helper: selects next eligible ready task from backlog | user | Reads state/master_backlog.json; reports selected task and ranked candidates; does not mutate backlog, daily plan, or any state |
| build_daily_execution_prep.py | C:\dev\jarvis-workspace\scripts\build_daily_execution_prep.py | script | source_of_truth | jarvis_script | Workflow helper: prepares operator-facing daily execution prep package | user | Chains select_next_ready_task (optional), build_cursor_handoff, and build_task_cycle_summary; writes prep markdown to scratch/daily_execution_prep/; does not execute tasks or mutate backlog/state |
| build_cursor_handoff.py | C:\dev\jarvis-workspace\scripts\build_cursor_handoff.py | script | source_of_truth | jarvis_script | Workflow helper: builds copy/paste-ready Cursor handoff file for a WCS task | user | Reads task packet and writes scratch/cursor_handoffs/<task>_cursor_handoff.md when bounded file scope can be derived; fails (no file written) when scope cannot be derived; does not execute task, modify WCS code, or mutate backlog/state |
