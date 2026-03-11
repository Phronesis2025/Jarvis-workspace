# FILE REGISTRY

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
This markdown file is the human-readable view.

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
| JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | doc | source_of_truth | user | High-level product requirements for Jarvis rebuild | user | Core planning doc |
| JARVIS_SYSTEM_DOCUMENTATION_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_DOCUMENTATION_v3.md | doc | source_of_truth | user | Detailed architecture and operating documentation | user | Core planning doc |
| JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | doc | source_of_truth | user | Current authoritative decisions and system rules | user | Most important design reference |
| master_backlog.json | C:\dev\jarvis-workspace\state\master_backlog.json | state | source_of_truth | user | Machine-readable task backlog | user / jarvis_script | Primary backlog source |
| MASTER_BACKLOG.md | C:\dev\jarvis-workspace\state\MASTER_BACKLOG.md | state | generated | jarvis_script | Human-readable backlog table | render_master_backlog.py | Rendered from master_backlog.json |
| DAILY_REVIEW.md | C:\dev\jarvis-workspace\state\DAILY_REVIEW.md | state | source_of_truth | user | Daily execution log and summary | user / jarvis_script | Reconcile appends entries |
| DAILY_PLAN.md | C:\dev\jarvis-workspace\state\DAILY_PLAN.md | state | source_of_truth | user | Current planned work for the day | user | Lightly used so far |
| PROJECT_STATUS_WCS.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_WCS.md | state | source_of_truth | user | Human-readable WCS project status | user / jarvis_script | May later be rendered |
| PROJECT_STATUS_N8N.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_N8N.md | state | source_of_truth | user | Human-readable n8n project status | user | n8n worker deferred |
| file_registry.json | C:\dev\jarvis-workspace\state\file_registry.json | state | source_of_truth | user | Machine-readable file registry | user / jarvis_script | Source for this markdown file |
| FILE_REGISTRY.md | C:\dev\jarvis-workspace\state\FILE_REGISTRY.md | state | generated | jarvis_script | Human-readable file registry | user / future renderer | This file |
| render_master_backlog.py | C:\dev\jarvis-workspace\scripts\render_master_backlog.py | script | source_of_truth | jarvis_script | Renders MASTER_BACKLOG.md from backlog JSON | user | Working |
| update_master_backlog.ps1 | C:\dev\jarvis-workspace\scripts\update_master_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for backlog renderer | user | Convenience wrapper |
| generate_task_packet.py | C:\dev\jarvis-workspace\scripts\generate_task_packet.py | script | source_of_truth | jarvis_script | Creates task packet files and blank result files | user | Working |
| generate_task_packet.ps1 | C:\dev\jarvis-workspace\scripts\generate_task_packet.ps1 | script | source_of_truth | user | PowerShell wrapper for task generator | user | Convenience wrapper |
| reconcile_task_outcome.py | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.py | script | source_of_truth | jarvis_script | Reconciles worker + QA results into backlog state | user | Working |
| reconcile_task_outcome.ps1 | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.ps1 | script | source_of_truth | user | PowerShell wrapper for reconciler | user | Convenience wrapper |
| cursor_completion_contract.txt | C:\dev\jarvis-workspace\scripts\cursor_completion_contract.txt | template | source_of_truth | user | Forces structured Cursor completion summaries | user | Used in worker prompts |
| overnight_health_check.py | C:\dev\jarvis-workspace\scripts\overnight_health_check.py | script | source_of_truth | jarvis_script | Read-only overnight system health watcher | user | Working |
| run_overnight_health_check.ps1 | C:\dev\jarvis-workspace\scripts\run_overnight_health_check.ps1 | script | source_of_truth | user | Wrapper for overnight health watcher | user | Used for manual or scheduled runs |
| register_overnight_health_task.txt | C:\dev\jarvis-workspace\scripts\register_overnight_health_task.txt | doc | source_of_truth | user | Task Scheduler command notes | user | Scheduling helper |
| run_wcs_scout.py | C:\dev\jarvis-workspace\scripts\run_wcs_scout.py | script | source_of_truth | jarvis_script | Runs public WCS scout and stores results | user | Working after env-var fixes |
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
| *_escalation.json | C:\dev\jarvis-workspace\logs\*_escalation.json | log | runtime_output | jarvis_script | Escalation record for blocked/escalated tasks | user / jarvis_script | May be blank for many tasks |
| overnight_health_*.json | C:\dev\jarvis-workspace\logs\overnight_health_*.json | log | runtime_output | jarvis_script | Machine-readable overnight health output | overnight_health_check.py | Working |
| overnight_health_*.txt | C:\dev\jarvis-workspace\logs\overnight_health_*.txt | log | runtime_output | jarvis_script | Human-readable overnight health summary | overnight_health_check.py | Working |
| public_scout_results.json | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\public_scout_results.json | log | runtime_output | scout_runner | Structured route scout results | run_wcs_scout.py / public_scout.spec.ts | Latest run currently PASS |
| public_scout_summary.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\public_scout_summary.txt | log | runtime_output | scout_runner | Human-readable scout summary | run_wcs_scout.py | Latest run currently PASS |
| playwright_stdout.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\playwright_stdout.txt | log | runtime_output | scout_runner | Raw Playwright stdout from scout run | run_wcs_scout.py | Debug support |
| playwright_stderr.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\playwright_stderr.txt | log | runtime_output | scout_runner | Raw Playwright stderr from scout run | run_wcs_scout.py | Debug support |
| public_scout.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\public_scout.spec.ts | repo_test | source_of_truth | playwright | Public route scout spec for WCS | user | Working after noise filtering |
| home.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\home.spec.ts | repo_test | source_of_truth | playwright | Smoke QA spec for home page | user | Added by WCS-011 |
| global-setup.ts | C:\dev\wcsv2.0-new\tests\e2e\helpers\global-setup.ts | repo_test | source_of_truth | playwright | Shared Playwright startup and readiness logic | user | Updated in WCS-011 |
| package.json | C:\dev\wcsv2.0-new\package.json | repo_test | source_of_truth | user | Repo scripts including test:e2e:smoke | user | WCS repo-side dependency |
| normalize_scout_to_backlog.py | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.py | script | source_of_truth | jarvis_script | Normalizes scout defects into backlog-ready tasks and updates backlog state | user | Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md |
| normalize_scout_to_backlog.ps1 | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for scout defect normalizer | user | Convenience wrapper |
| scout_noise_rules.json | C:\dev\jarvis-workspace\config\scout_noise_rules.json | config | source_of_truth | user | Known scout noise filtering rules for backlog normalization | user | Used by normalize_scout_to_backlog.py |