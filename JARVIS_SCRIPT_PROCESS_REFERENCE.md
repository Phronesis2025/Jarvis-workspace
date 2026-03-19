````md
# JARVIS_SCRIPT_PROCESS_REFERENCE_v2.md

## Live Doc Status
- Last reviewed: 2026-03-19
- Last updated: 2026-03-19 (Pathfinder optional LLM synthesis fallback path proven)
- Status: aligned to current live hardening state (hardened loop with validation gates, commit gate, stamping, file-registry checker, packet lifecycle/status cleanup during reconcile, a thin operator-facing WCS wrapper for prep/post, and stricter launch-safety auditing on the Cursor bridge path)
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Proof: Real guarded end-to-end task cycles succeeded on WCS-042, WCS-043, WCS-041, WCS-046, WCS-061, and WCS-008. On WCS-043, reconcile safely proved that task packet JSON and task packet markdown now sync to the terminal outcome instead of remaining misleadingly `ready`. On WCS-041, the strict real-Agent `--launch-cursor` success path is proved. On WCS-046, the one-command single-task wrapper (`run_one_task_cycle.py`) is proved through prep, Agent CLI launch, and completion; task completion still required operator commit, QA, manual verification, and post-worker truth. On WCS-061 and WCS-008, the full-cycle wrapper (`run_one_task_full_cycle.py`) is proved; wrapper family can truthfully close a single task end-to-end via mechanical path plus `--finalize`; screenshot artifact support and `--finalize` proven on WCS-008.

## Current local state / follow-up
- Option B V1 is live via `scripts/run_wcs_operator_entrypoint.py` for operator-facing `prep` and `post`.
- `prep --launch-cursor` now uses strict post-launch auditing through `run_cursor_worker.py --require-auditable-delta`.
- Strict launch failure is now honestly proven: launch can exit `0` and still fail overall when no immediate auditable in-scope repo delta exists.
- Blocked/timeout behavior is also honestly proven: the real Agent CLI path returns `BLOCKED` when the agent does not finish before the configured timeout.
- Strict real-Agent success is proven on `WCS-041` and `WCS-046`. One-command single-task wrapper (`run_one_task_cycle.py`) is proven on `WCS-046`. Full-cycle wrapper (`run_one_task_full_cycle.py`) is proven on `WCS-061` and `WCS-008`; wrapper can close a single task end-to-end; no batching or autonomy exaggeration. WCS-033 was a bad proof target; do not present as proof. Sequential runner (`run_task_sequence.py`) is proven on WCS-028. Page-specific smoke support is implemented and proven on WCS-032 for `/schedules`; overall smoke coverage still limited. Pathfinder v1 is proven: `run_pathfinder.py` accepts minimal intake or full task packet, gathers bounded context from workspace artifacts and WCS repo files, produces structured result with optional draft backlog candidate; read-only only. Optional LLM synthesis fallback path proven 2026-03-19; result includes `synthesis_source` and `llm_skipped_reason`; LLM path not yet proven.

## Post-milestone doc audit (live workflow rule)

After each meaningful milestone, explicitly check: Did live state update? Did file registry update? Did handoff/current-state docs update? Does this change require canon-doc updates (source-of-truth, PRD), or should those remain unchanged? If canon docs are unchanged, state that explicitly. This is a doc-audit checkpoint for live execution, not a product architecture rule. Use it before recommending commit/push after a milestone.

## Purpose

This document defines the **current live Jarvis WCS task execution process** and the **intended future process** the system is being hardened toward.

It is a working reference for:

- how the process works now
- what each script currently does
- what is still manual or semi-manual
- what contracts must be satisfied
- what parts are intended to be automated later
- what guardrails already exist
- what guardrails are still being built

This document is meant to orient a new chat or operator to the **real operating process**, not an idealized version.

---

# System Intent

Jarvis is a **local-first Python foreman/orchestrator**.

Jarvis is **not** the primary coding agent.

The active project is the **WCS website**.

The current Phase 1 architecture is intentionally simple:

- local Python scripts
- JSON as source-of-truth
- Markdown as rendered human-readable view
- the WCS worker as the current coding worker for WCS tasks
- Cursor as the current execution surface for that WCS worker
- Playwright as the QA layer
- one bounded task at a time
- Git branch correctness enforced as part of task completion

The intended long-term direction is a more automated local-first multi-agent system, but without weakening auditability, branch correctness, or source-of-truth discipline.

---

# Current Operating Truth

## Current WCS loop

The current **proven live WCS task loop** is:

1. Run `jarvis.py` (or `jarvis.py --force` when an intentional fresh selection is required).
2. Jarvis validates selected task execution eligibility from JSON state.
3. Jarvis validates packet/result placeholder contracts and shapes.
4. Jarvis writes/updates daily plan and run-log state.
5. Jarvis generates or reuses task packet artifacts.
6. Jarvis prepares the correct WCS task branch.
7. Jarvis verifies final branch state after prep and reports it.
8. Worker performs a bounded implementation in the WCS repo.
9. Operator verifies the diff and confirms scope is correct.
10. `worker_change_check.py` is run as a read-only worker-boundary validator before commit/finalization.
11. A commit is created on the correct task branch with a clean worktree afterward.
12. `commit_gate_check.py --task WCS-XXX` is run as a read-only commit-state gate for the task branch and HEAD.
13. The worker result JSON is finalized truthfully (placeholders replaced with factual data).
14. `worker_result_validate.py --task WCS-XXX --mode pre-stamp` is run as a read-only worker-result schema validator.
15. QA is run in the WCS repo using:
    - `npm run build`
    - `npm run test:e2e:smoke` (Playwright config now starts the local dev server via `webServer` when no E2E_BASE_URL/NEXT_PUBLIC_BASE_URL is set)
16. The QA result JSON is finalized truthfully (placeholders replaced with factual data). Optionally, the operator can use `draft_qa_result_from_evidence.py --task WCS-XXX` (with build/smoke/manual status and `--write`) to draft a truthful pre-stamp QA result from CLI evidence before validation; the script does not stamp, reconcile, or fabricate evidence.
17. `qa_result_validate.py --task WCS-XXX --mode pre-stamp` is run as a read-only QA-result schema validator.
18. `stamp_guard_check.py --task WCS-XXX` is run as a read-only pre-stamp guardrail to confirm worker and QA results are both present, pre-stamp, and not obvious placeholders.
19. `stamp_result_timestamp.py` is run once per file: pass the **file path** to the worker result JSON, then the **file path** to the QA result JSON (e.g. `results/WCS-XXX_worker_result.json` and `qa/WCS-XXX_qa_result.json`).
20. `pre_reconcile_check.py` is run as a read-only readiness gate.
21. `reconcile_task_outcome.py --task WCS-XXX` is run.
22. Reconcile verifies:
    - valid worker result
    - valid QA result
    - expected branch == current branch
    - task branch has committed work and is ahead of `main`
    - repo/task evidence is sufficient
22. Backlog JSON and rendered Markdown are updated from reconcile output.
23. If task packet artifacts exist, reconcile also syncs task packet JSON and task packet markdown to the same terminal outcome (`done`, `blocked`, or `escalated`) so packet files do not remain misleadingly `ready`.
24. Backlog/state remains authoritative; task packet artifacts remain generated/operator-facing views that are kept aligned during reconcile.
25. `post_reconcile_validate.py` is run as a read-only validator of final state surfaces.

WCS-019 is now a full completed/reconciled live loop proof under this hardened process. The hardened live WCS loop is currently proven across WCS-016, WCS-017, WCS-018, and WCS-019, including:
- correct task/branch activation
- `worker_change_check.py` PASS
- `commit_gate_check.py` PASS
- `worker_result_validate.py` PASS
- real QA rerun PASS
- `qa_result_validate.py` PASS
- worker result stamped
- QA result stamped
- `pre_reconcile_check.py` PASS
- `reconcile_task_outcome.py` success
- `post_reconcile_validate.py` PASS

For operator-facing consolidation, `run_wcs_operator_entrypoint.py --task WCS-XXX --workspace <path> prep|post ...` is now live as a thin wrapper over the existing validated helpers. In **prep**, it ensures the task packet exists (delegating to `generate_task_packet.py` only when missing), then delegates to `run_guarded_task_cycle.py --mode pre_worker`, and prints the key artifact paths for the packet, Cursor handoff, and task-cycle summary. In **post**, it delegates to `run_guarded_task_cycle.py --mode post_worker` and passes worker/QA evidence flags through unchanged. It does not select tasks automatically, create commits, run build/Playwright itself, invent evidence, schedule work, or run an autonomous full loop. Fresh proof succeeded on `WCS-044` for the wrapper's **prep** and **post** paths. In the current live build, `prep --launch-cursor` now opts into strict post-launch auditing through `run_cursor_worker.py --require-auditable-delta`; it also supports optional real-Agent timeout passthrough via `--agent-timeout-seconds <n>`. Launch may report success only when the branch remains correct, an immediate working-tree delta exists, and changed files stay within packet scope. This still does not prove task completion, semantic correctness, commit readiness, QA completion, or finalized worker evidence.

After QA failures or ambiguous results, `qa_failure_triage.py --task WCS-XXX` can be run as a strictly read-only helper to classify the failure (`environment_setup_failure`, `test_harness_failure`, `application_regression`, or `ambiguous`) and recommend the next bounded action without mutating any state.

For hardening-surface checks (not part of the core task loop), `file_registry_check.py --workspace <path>` can be run as a read-only file-registry drift/coverage checker: it verifies that `file_registry.json` and `FILE_REGISTRY.md` exist, parse, and list the core hardening scripts and docs; it does not modify the registry. `naming_drift_check.py --workspace <path>` can be run as a read-only naming-drift helper to detect obvious name mismatches between core scripts/docs and the file registry; it does not rename or rewrite anything. `render_file_registry.py --workspace <path>` can be run as the renderer that takes `state/file_registry.json` as source-of-truth and writes `state/FILE_REGISTRY.md` in the approved registry format. `critical_surface_health_check.py --workspace <path>` can be run as a read-only sanity checker for the critical hardening surface: it verifies critical scripts/docs/registry exist, critical helpers compile, and `file_registry_check` plus `naming_drift_check` pass; it does not run the full task loop or mutate state. For workflow support, `build_cursor_handoff.py --task WCS-XXX [--workspace <path>] [--output <path>]` builds a bounded, copy/paste-ready Cursor handoff file from the task packet (writes to `scratch/cursor_handoffs/` by default); it does not execute the task, modify WCS code, or mutate backlog/state. `build_task_cycle_summary.py --task WCS-XXX [--workspace <path>] [--output <path>]` builds a human-readable markdown summary of the current task cycle from existing task/worker/QA artifacts (writes to `scratch/task_cycle_summaries/` by default); it does not execute the task, change task status, or mutate backlog/state. `run_guarded_task_cycle.py --task WCS-XXX [--workspace <path>] [--mode pre_worker|post_worker|full] [--draft-worker-result] [--worker-command <text>] [--worker-executor <text>] [--draft-qa-result] [--build-status pass|fail|skip|unknown] [--smoke-status ...] [--manual-status ...] [--manual-check <text>] [--artifact <path>] [--qa-note <text>]` is a workflow/orchestration helper that runs the existing guarded task-cycle scripts in order and stops on the first failure. **pre_worker** mode is unchanged. In **post_worker** and **full** modes, when `--draft-worker-result` is supplied, the flow inserts an optional step named `draft_worker_result_from_evidence` immediately before `worker_result_validate.py --mode pre-stamp`; that step runs `draft_worker_result_from_evidence.py --write`, passes through repeatable `--worker-command` values as `--command`, passes `--worker-executor` as `--executor` when supplied, and still fails honestly if meaningful worker command evidence is missing. Missing worker-result JSON is tolerated only when `--draft-worker-result` is supplied; otherwise the run fails with the explicit missing-worker-result message. In **post_worker** and **full** modes, when `--draft-qa-result` is supplied, the flow still inserts an optional step that runs `draft_qa_result_from_evidence.py --write` with the supplied QA evidence args **before** `qa_result_validate.py --mode pre-stamp`; that QA wiring was not changed in this step. The flow still stops on the first failed step. It does not replace helper logic, execute worker code directly, run build/Playwright automatically, or schedule tasks. `select_next_ready_task.py [--workspace <path>] [--project WCS] [--limit N]` is a read-only workflow helper that selects the next eligible ready task from the backlog; when progression ladder fields are present it uses execution_lane (fake_reversible, real_easy, real_investigative), test_phase (phase_a–d), and selector_rank (lower first), then fallback (priority, risk, task id); it does not mutate backlog, daily plan, or any state. `build_daily_execution_prep.py [--workspace <path>] [--project WCS] [--task WCS-XXX] [--output <path>]` is a workflow helper that prepares an operator-facing daily execution prep package by chaining select_next_ready_task (when --task is omitted), ensuring task packet availability by invoking `generate_task_packet.py` when needed, then build_cursor_handoff and build_task_cycle_summary; it writes a prep markdown file and helper outputs only, does not execute the task itself, and does not mutate backlog/state beyond approved helper outputs (e.g. packet generation when missing).

## Current process reality

### Automated now
- task selection
- daily plan updates
- run log updates
- task packet generation
- WCS branch preparation
- master backlog rendering
- scout normalization into backlog
- timestamp stamping
- reconcile state updates
- branch verification during reconcile

### Semi-manual now
- WCS worker implementation through Cursor or by direct operator action
- worker result JSON content fill-in
- QA command execution
- QA result JSON content fill-in
- Git commit creation in the WCS repo
- terminal output review and go/no-go decisioning

### Not yet fully automated
- direct Python QA entrypoint in the live workspace
- automatic worker result generation from actual implementation activity
- automatic QA result generation from actual test output
- full pre-reconcile readiness checking before script execution
- richer operator-safety prompts and recovery guidance
- unattended end-to-end execution

### Cursor invocation bridge (live)

`run_cursor_worker.py` is live as a **Cursor invocation bridge**: it prefers the **real Cursor Agent CLI** (`agent`) when available; if not, it falls back to the **desktop cursor launcher**. Execution runs against the **task repo workspace** (from the task packet), not the Jarvis workspace; Agent uses `--trust` for non-interactive use. It reports PASS / BLOCKED / FAIL honestly. In its stricter launch-safety mode, `--require-auditable-delta`, a successful external launch exit is followed by an immediate working-tree audit: current branch must still match the expected branch, a real working-tree delta must exist, and changed files must stay within packet scope. If any of those checks fail, the launch now fails honestly instead of reporting a misleading PASS. It still does not by itself prove task completion or write a truthful worker_complete result. The operator still verifies completion and finalizes worker-result evidence. The system remains **operator-assisted at the worker completion/evidence stage**; full autonomy is not achieved.

---

# Governing Rules

## Completion rule

A task must **not** be marked done unless all of the following are true:

1. a worker result file exists
2. the worker result file is truthful and final
3. the worker result status is valid
4. a QA result file exists
5. the QA result file is truthful and final
6. the QA result status is valid and passing
7. the repo changes are committed
8. the repo is on the correct task branch
9. reconcile branch verification passes
10. reconcile completes successfully

## Source-of-truth rule

Where JSON exists, JSON is authoritative for machine decisions.

Markdown is the paired human-readable rendered view.

Logs are evidence and history. Logs are **not** source-of-truth.

## Result timestamp rule

Worker and QA result files should keep `completed_at` blank until their content is final.

The local timestamp helper stamps the real local timestamp afterward.

## Process documentation rule

Whenever a new process change, guardrail, contract, or script behavior is **locked in and live**, the corresponding working process and hardening documentation files in this workspace **must be updated immediately** to match the new reality.

## One-task rule

Phase 1 remains a one-task-at-a-time loop.

The system does not widen scope merely because the repo is already open.

## Contract rule

Result files must use the actual system contracts, not invented statuses.

Placeholder files are not proof of execution.

---

# Core Process Scripts

## 1. `scripts/jarvis.py`

### Role
Phase-1 foreman / orchestrator.

### Current behavior
The current hardened `jarvis.py` foreman loop:

- reads `state/master_backlog.json`
- reads `state/project_status_wcs.json`
- checks whether a task is already selected for the current day
- reuses the selected task unless a forced reselection is requested
- deterministically selects one valid WCS task when selection is needed
- validates that the selected task is currently eligible for execution based on backlog and project status
- validates that task packet/result placeholders exist and are in the expected contract shape (not treated as evidence)
- records durable escalation state when hard failures occur in state loading, selection, packet validation, or branch preparation/verification
- writes/updates:
  - `state/daily_plan.json`
  - `state/DAILY_PLAN.md`
  - `state/run_log.json`
  - `state/RUN_LOG.md`
- triggers task packet generation (or reuse) for the selected task
- triggers task branch preparation for the WCS repo
- verifies final branch state after prep (expected branch, current branch, cleanliness) and records the result
- skips packet regeneration if the artifacts already exist unless force behavior is used

### Current operator-facing output

The current operator-safe output from `jarvis.py` is intended to:

- clearly state whether it reused an existing task or selected a new one (and when `--force` was respected)
- print the selected task id and title
- summarize which plan/log files were updated
- state whether task packet artifacts were generated or reused
- show branch-prep mode, target task branch, and repo path
- show the final branch verification result after prep (expected branch, current branch, dirty/clean)
- warn that generated worker/QA result files are placeholders and **not** proof of execution
- remind the operator of the worker/QA result contracts and allowed statuses
- print an explicit **“TASK IS NOT COMPLETE YET”** handoff block
- print next-step commands for worker implementation, QA, stamping, and reconcile
- remind that process/docs must be updated whenever a new hardening rule or behavior is locked in
- mention when an escalation record was written on hard failure, including paths to `state/escalations.json` and `state/ESCALATIONS.md`

### Escalation state surfaces

`jarvis.py` now maintains durable escalation state:

- `state/escalations.json` — authoritative machine-readable escalation list
- `state/ESCALATIONS.md` — rendered human-readable escalation view

Whenever a hard failure occurs during `jarvis.py` execution (for example invalid JSON state, invalid selected task, partial packet artifacts, packet/placeholder contract mismatch, branch preparation failure, or post-branch-prep branch verification failure), Jarvis appends a new escalation record with:

- timestamp
- task id (when known)
- project
- phase (e.g. `jarvis_state_load`, `jarvis_selection`, `jarvis_packet_validation`, `jarvis_branch_preparation`, `jarvis_branch_verification`)
- severity (`error`)
- status (`open`)
- human_action_required (`true`)
- reason_code (e.g. `invalid_json_state`, `invalid_selected_task`, `partial_packet_artifacts`, `packet_contract_mismatch`, `branch_prepare_failed`, `branch_verification_failed`, `repo_inspection_failed`)
- summary
- details
- recommended next action

`ESCALATIONS.md` is always rendered from `escalations.json`; JSON remains source-of-truth.

### What Jarvis does not currently do
- it does not perform the code change
- it does not run Cursor
- it does not run QA commands
- it does not finalize worker result content
- it does not finalize QA result content
- it does not create Git commits
- it does not stamp timestamps
- it does not reconcile completion by itself

### Current operator reality
If a task was already selected for the day, `jarvis.py` will usually reuse it.

If a fresh selection is intentionally needed, `jarvis.py --force` is required.

### Intended future build direction
Future work for `jarvis.py` is focused on:
- even stronger preflight validation before selection and branch prep
- richer escalation and human-action-required recording into durable state surfaces
- optional automatic generation of worker and QA handoff prompts
- clearer pause/stop behavior when guardrails fail instead of relying on operator memory

---

## 2. `scripts/generate_task_packet.py`

### Role
Task packet generator.

### Current behavior
When a backlog item has optional `implementation_instruction`, it is copied into the task packet for use by `build_cursor_handoff.py` to make the Cursor prompt more explicit.

For a task like `WCS-016`, it generates:
- `tasks/WCS-016_task.json`
- `tasks/WCS-016_task.md`

It also generates placeholder files:
- `results/WCS-016_worker_result.json`
- `qa/WCS-016_qa_result.json`
- `logs/WCS-016_escalation.json`

### Important current truth
The worker and QA result files generated here are placeholders.

Their existence does **not** mean:
- work has been implemented
- QA has been performed
- a task is reconcile-ready

### What this script does not currently do
- it does not fill factual worker result content
- it does not fill factual QA result content
- it does not stamp timestamps
- it does not validate Git state
- it does not prove completion

### Intended future build direction
- stronger packet schema validation
- stronger warnings that placeholder files are not execution proof
- packet generation checks for obvious task/repo baseline mismatch

---

## 3. `scripts/prepare_wcs_task_branch.py`

### Role
Pre-execution Git branch safety step for the WCS repo.

### Current behavior
- reads the configured WCS repo path
- checks current repo branch
- checks dirty state
- refuses unsafe switching when the repo is dirty on the wrong branch
- switches to the correct task branch if it exists
- creates the correct task branch from `main` when needed
- reports:
  - mode
  - current branch
  - target branch
  - dirty state
  - repo path

### Why it exists
This reduces the risk of doing the right task on the wrong branch.

### What this script does not currently prove
- that a commit later exists
- that the worker result is valid
- that reconcile should succeed
- that the repo stayed correct after subsequent operator actions

### Current operator reality
The operator still manually verifies:
- `git branch --show-current`
- `git status`

before implementation begins.

### Intended future build direction
- stronger explicit failure reasons
- optional post-switch verification summary
- better operator messaging when switching away from a previous task branch

---

## 4. `scripts/reconcile_task_outcome.py`

### Role
Final evidence validator and backlog reconciler.

### Current behavior
- requires an explicit task id via `--task WCS-XXX`
- reads the task packet
- reads worker result JSON
- reads QA result JSON
- validates result contracts
- verifies final reconcile conditions
- verifies repo branch state
- verifies task branch commit state
- updates backlog/state if all conditions pass
- re-renders the backlog markdown view
- syncs existing task packet JSON and task packet markdown to the reconciled terminal outcome when packet artifacts exist
- updates review output where applicable

### Current required worker result statuses
Allowed worker statuses are:
- `worker_complete`
- `blocked`
- `escalated`

Any other worker status is invalid.

### Current required QA result statuses
Allowed QA statuses are:
- `qa_pass`
- `qa_fail`
- `escalated`

Any other QA status is invalid or non-final.

### Current done-path hardening behavior
For a done-path reconcile, the script verifies:
- expected branch matches current branch
- repo path is valid
- branch verification passes
- the task branch has committed work
- the task branch is ahead of `main`
- the worker and QA files satisfy the expected contracts

### Current write behavior
Typically updates:
- `state/master_backlog.json`
- `state/MASTER_BACKLOG.md`
- `tasks/WCS-XXX_task.json` (status + updated_at when packet exists)
- `tasks/WCS-XXX_task.md` (re-rendered from the updated packet when packet exists)
- `state/DAILY_REVIEW.md`

Backlog/state remains the authoritative source of truth. Task packet artifacts remain generated/operator-facing surfaces that are kept aligned after reconcile so they do not lie about terminal status.

### What this script does not currently do
- it does not guess the task if `--task` is omitted
- it does not create commits
- it does not finalize placeholder result files for the operator
- it does not excuse contract violations
- it does not replace operator review of terminal output

### Current operator reality
Reconcile is only run after:
- work is implemented
- work is committed
- worker result is truthful and final
- QA result is truthful and final
- both results are stamped
- the repo is still on the correct task branch

### Intended future build direction
- pre-reconcile readiness checks before full reconcile (now partially satisfied by `scripts/pre_reconcile_check.py`)
- clearer contract error output
- explicit placeholder-shape rejection earlier in the flow
- optional dry-run / explain mode
- stronger operator-safety guidance before state mutation

---

## 5. `scripts/pre_reconcile_check.py`

### Role

Read-only pre-reconcile readiness gate for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- verifies that `tasks/WCS-XXX_task.json` exists
- verifies that `results/WCS-XXX_worker_result.json` exists
- verifies that `qa/WCS-XXX_qa_result.json` exists
- validates worker result JSON:
  - parses successfully
  - has matching `task_id`
  - uses an allowed status: `worker_complete | blocked | escalated`
  - status is not `draft`
  - `completed_at` is present and non-blank
- validates QA result JSON:
  - parses successfully
  - has matching `task_id`
  - uses an allowed status: `qa_pass | qa_fail | escalated`
  - status is not `draft`
  - `completed_at` is present and non-blank
- reads `state/project_status_wcs.json` for the WCS repo path
- verifies:
  - repo path exists
  - `git branch --show-current` works
  - expected branch is `jarvis-task-wcs-XXX`
  - current branch matches the expected branch
  - `git status --porcelain` is clean
  - the task branch is ahead of `main` (or `master` when `main` is missing) by at least one commit

### Output and behavior

- prints `PRE-RECONCILE CHECK: PASS` or `PRE-RECONCILE CHECK: FAIL`
- prints the task id
- on PASS, prints:
  - repo path
  - expected branch
  - current branch
  - commits ahead of main/master
  - a concise list of passed checks
- on FAIL, prints a `Failures:` section listing all failed prerequisites
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only gate that can be run before `reconcile_task_outcome.py` to confirm that artifacts and repo state appear ready, without mutating any state.

---

## 6. `scripts/post_reconcile_validate.py`

### Role

Read-only post-reconcile validation for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- verifies state files exist:
  - `state/master_backlog.json`
  - `state/MASTER_BACKLOG.md`
  - `state/DAILY_REVIEW.md`
- validates backlog JSON:
  - parses successfully
  - root is a list
  - exactly one backlog record exists for the task id
  - that record has `project == "WCS"` and `status == "done"`
- validates rendered backlog markdown:
  - file exists and is readable
  - contains the task id
  - contains the task title (if present in backlog JSON)
  - contains a simple, visible “done” indicator on a line that also contains the task id
- validates `DAILY_REVIEW.md`:
  - file exists and is readable
  - contains the task id
- validates worker result and QA result files:
  - `results/WCS-XXX_worker_result.json` exists and parses
  - `qa/WCS-XXX_qa_result.json` exists and parses
  - both `task_id` fields match the requested task id
  - worker status is one of: `worker_complete | blocked | escalated`
  - QA status is one of: `qa_pass | qa_fail | escalated`
  - both `completed_at` fields are present and non-blank

### Output and behavior

- prints `POST-RECONCILE VALIDATION: PASS` or `POST-RECONCILE VALIDATION: FAIL`
- prints `Task: WCS-XXX`
- on PASS, prints:
  - task title (when available)
  - backlog status
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only validator that can be run after `reconcile_task_outcome.py` to confirm that the intended task is actually marked done and visible in the expected state surfaces.

---

## 7. `scripts/stamp_result_timestamp.py`

---

## 8. `scripts/worker_change_check.py`

### Role

Read-only worker change boundary validator for a single WCS task before commit/finalization.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- reads `tasks/WCS-XXX_task.json` to determine expected file scope using a simple Phase 1 rule:
  - prefers an explicit `target_files` or `suspected_files` list when present
  - otherwise uses a single `target_file` / `file_path` / `file` field when present
  - as a last resort, uses a `notes` field that looks like a single path
- fails bluntly when it cannot determine expected file scope from the task packet
- reads `state/project_status_wcs.json` to resolve the WCS repo path
- verifies the repo path exists
- verifies:
  - `git status --short` works
  - `git diff --name-only` works (and when working tree is clean, `git diff --name-only HEAD~1 HEAD`)
  - `git branch --show-current` works
  - expected branch is `jarvis-task-wcs-XXX`
  - current branch matches the expected branch
- gathers changed files: from working tree (`git status` and `git diff`) when there are uncommitted changes; when the working tree is clean, from the HEAD commit (`git diff --name-only HEAD~1 HEAD`) so the check works both before and after the task commit and aligns with the post_worker flow
- validates changed files:
  - at least one changed file exists
  - every changed file is within the expected file scope derived from the task packet
- validates diff sanity:
  - runs `git diff --unified=0` (working tree) or `git diff --unified=0 HEAD~1 HEAD` (when using HEAD commit) for each changed file
  - counts simple changed lines per file
  - fails if more than 3 files are changed
  - fails if any single file has more than 40 changed lines (adds+deletes)

### Output and behavior

- prints `WORKER CHANGE CHECK: PASS` or `WORKER CHANGE CHECK: FAIL`
- prints `Task: WCS-XXX`
- on PASS, prints:
  - repo path
  - expected branch
  - current branch
  - expected file scope
  - actual changed files
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not create commits
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only worker-boundary validator that can be run before commit/finalization to catch obvious scope drift and suspiciously large diffs for a bounded WCS task.

---

## 8b. `scripts/run_cursor_worker.py`

### Role

Cursor execution bridge for the WCS worker: prefers the real Cursor Agent CLI (`agent`) when available; falls back to the desktop cursor launcher. Execution runs against the **task repo workspace** (from the task packet), not the Jarvis workspace. Does not by itself prove task completion or write a truthful worker_complete result; operator still verifies completion and finalizes worker-result evidence.

### Current behavior

- requires `--task WCS-XXX`
- optional `--workspace` (default: Jarvis workspace root), optional `--handoff` (default: `scratch/cursor_handoffs/<task>_cursor_handoff.md`), optional `--require-auditable-delta`, optional `--agent-timeout-seconds <n>` for the real Agent CLI path only, optional `--agent-model <id>` (e.g. composer-1.5) passed as `--model <value>` to the Agent CLI when provided
- validates: task id, Jarvis workspace, handoff file exists, task packet exists; **reads and validates `repo_path` from task packet** (required; must exist and be a directory; FAIL if missing or invalid)
- **Agent CLI detection (Windows-hardened):** tries `shutil.which("agent")`, then `agent.cmd`, `agent.exe`, `agent.bat`; on Windows only, if none found, runs `where agent` / `where agent.cmd` and uses first existing path, then tries PowerShell `Get-Command agent`. If Agent CLI still cannot be found in the process environment, falls back to cursor and reports which path was used.
- **Execution target:** Agent and desktop launcher both use the **task repo workspace** (`repo_path` from packet): Agent is run with `--workspace <repo_path>`, `--trust` (non-interactive trust for that repo), and subprocess cwd = `repo_path`; desktop launcher subprocess cwd = `repo_path`. Handoff file remains in Jarvis workspace; execution context is the task repo.
- **Execution priority:** (1) if `agent` CLI is detected, runs `agent [--model <id>] --print --workspace <repo_path> --trust "<prompt>"` with cwd = repo_path; the full task spec (preamble + handoff) is written to `scratch/agent_prompts/<task>_prompt.txt`, and a short CLI-safe instruction is passed as the prompt (telling the agent to read that file), avoiding Windows command-line truncation/escaping of long multi-line prompts; uses `--agent-timeout-seconds` (default `600`) for the subprocess timeout, and passes `--model <value>` when `--agent-model` is supplied; (2) else if `cursor` launcher is on PATH, runs `cursor <handoff_path>` with cwd = repo_path; (3) if neither found, exits BLOCKED (exit 2). When agent returns non-zero and stderr mentions authentication, a hint suggests running `agent login`.
- **Agent output artifact:** when the real Agent CLI path runs, stdout and stderr are written to `scratch/agent_outputs/<task>_agent_output.txt` for operator review; the path is printed on PASS, BLOCKED (non-zero exit), and FAIL (strict audit). Helps debug when exit is 0 but no in-scope delta is found.
- **Strict post-launch audit mode:** when `--require-auditable-delta` is supplied and the external launch exits `0`, the script immediately inspects the task repo **working tree only** and requires all of the following:
  - current branch still matches the expected branch
  - a real working-tree delta exists
  - changed files remain within the task packet scope
  If any of those checks fail, the script returns FAIL instead of a misleading PASS.
- does not fabricate worker completion; does not write a worker result unless execution is truthfully successful (scripted execution does not provide completion evidence; operator must finalize the worker result)
- exit codes: 0 PASS (launch succeeded and, when strict mode is used, the immediate audit also passed), 2 BLOCKED (neither agent nor cursor found, or the real Agent path did not complete before timeout, or process failed), 1 FAIL (malformed input, missing handoff/packet, missing or invalid repo_path, or strict audit failure)

### Output

- On PASS: `RUN CURSOR WORKER: PASS`, task id, **Jarvis workspace**, **Task repo workspace**, handoff path, whether **Real Agent CLI** or **Desktop launcher fallback** was used, path to `scratch/agent_outputs/<task>_agent_output.txt` (Agent path only), and when strict mode is active, explicit post-launch audit output (branch after launch, changed files detected, and in-scope result)
- On BLOCKED: `RUN CURSOR WORKER: BLOCKED`, reason, **Jarvis workspace**, **Task repo workspace**, path to agent output artifact (Agent path only), worker result not written. For the real Agent path this includes timeout output when the agent does not finish before `--agent-timeout-seconds`.
- On FAIL: `RUN CURSOR WORKER: FAIL`, reason (e.g. handoff file does not exist; task packet has no repo_path; repo path does not exist or is not a directory; no auditable working-tree delta detected after launch; branch drift; or changed files outside task scope), path to agent output artifact (Agent path only when audit failed after exit 0)

### Why it exists

This script is the Cursor invocation bridge for the current WCS worker execution surface: it runs Agent (or cursor launcher) against the task repo workspace from the packet, with non-interactive trust for that repo when using Agent. The new strict audit mode makes the launch surface more trustworthy by refusing PASS when the immediate repo state is not auditable. It still does not prove task completion or write a truthful worker_complete result; the operator still verifies completion and finalizes worker-result evidence. The system remains operator-assisted at the worker completion/evidence stage.

---

## 8ba. `scripts/run_wcs_operator_entrypoint.py`

### Role

Thin operator-facing wrapper for the current Phase 1 WCS lane.

### Current behavior

- uses argparse subcommands: `prep` and `post`
- requires `--task WCS-XXX`; accepts optional `--workspace`
- **prep**:
  - checks whether `tasks/WCS-XXX_task.json` exists
  - if missing, delegates to `generate_task_packet.py --task WCS-XXX`
  - delegates to `run_guarded_task_cycle.py --mode pre_worker`
  - prints the key artifact paths for task packet JSON, task packet markdown, Cursor handoff, and task-cycle summary
  - may optionally attempt `--launch-cursor` by delegating to `run_cursor_worker.py --require-auditable-delta`
  - supports optional passthrough `--agent-timeout-seconds <n>` and `--agent-model <id>` for the real Agent CLI path when `--launch-cursor` is used
- **post**:
  - delegates to `run_guarded_task_cycle.py --mode post_worker`
  - passes worker/QA evidence flags through unchanged, including:
    - `--draft-worker-result`
    - `--worker-command`
    - `--worker-executor`
    - `--draft-qa-result`
    - `--build-status`
    - `--smoke-status`
    - `--manual-status`
    - `--manual-check`
    - `--artifact`
    - `--qa-note`
- prints the exact delegated helper command and does not hide helper output
- stops on the first failed delegated step and reports FAIL honestly

### Important current truth

This wrapper is **not** a new engine. The existing validated helpers remain the true execution logic underneath. The wrapper is only an operator-facing consolidation layer for the already-proven prep/post path.

Fresh proof succeeded on `WCS-044` for:

- `prep`
- `post`

The optional `prep --launch-cursor` path remains operator-assisted. It now uses strict post-launch auditing so the wrapper fails honestly when launch is not immediately auditable, and it can pass through `--agent-timeout-seconds <n>` and `--agent-model <id>`. The strict failure path is safely proved. Blocked/timeout behavior is also proved. The strict real-Agent success path is proved on `WCS-041` and `WCS-046`. The one-command single-task wrapper (`run_one_task_cycle.py`) is proved on `WCS-046`; task completion still requires operator commit, QA, manual verification, and post-worker truth. The full-cycle wrapper (`run_one_task_full_cycle.py`) is proved on `WCS-061` and `WCS-008`; wrapper family can truthfully close a single task end-to-end via mechanical path plus `--finalize`. Screenshot artifact support and `--finalize` proven on WCS-008. `--finalize`: resume mode for task already committed and smoke-tested; skips prep/launch/commit/build/smoke; delegates to post only; requires `--task` and `--manual-check`; optional `--artifact` for screenshot path(s). Current smoke test still limited; page-specific task coverage should be improved later.

### What this script does not currently do

- it does not select tasks automatically
- it does not create commits
- it does not run QA commands itself
- it does not invent worker or QA evidence
- it does not schedule work
- it does not run an autonomous full loop
- it does not claim task completion, semantic correctness, commit readiness, QA completion, or finalized worker evidence from launch alone
- it does not replace `generate_task_packet.py`, `run_guarded_task_cycle.py`, or `run_cursor_worker.py`

### Why it exists

It reduces operator glue for the current WCS lane while preserving the validated helper contracts and guardrails already in place.

---

## 8bb. `scripts/run_one_task_cycle.py`

### Role

Thin operator-facing wrapper for exactly one bounded WCS task cycle.

### Current behavior

- accepts either:
  - `--task WCS-XXX`
  - `--select-ready` to select exactly one eligible ready WCS task through `select_next_ready_task.py`
- accepts optional `--workspace`
- accepts optional `--launch-cursor`
- accepts optional `--agent-timeout-seconds <n>` and `--agent-model <id>` and passes them through only when `--launch-cursor` is used
- delegates task selection to `select_next_ready_task.py` when `--select-ready` is used
- delegates prep and optional strict launch to `run_wcs_operator_entrypoint.py prep`
- stops immediately and reports FAIL honestly when selection, prep, or strict launch fails/blocks
- after a successful prep path, prints a clean operator next-actions block for:
  - git diff review
  - `git add` / `git commit`
  - `npm run build`
  - `npm run test:e2e:smoke`
  - manual verification
  - `run_wcs_operator_entrypoint.py post ...`

### Important current truth

This script is still only an operator-facing wrapper. It does not claim that launch success equals task completion. The operator still verifies the diff, creates the commit, runs QA, and finalizes truthful post-worker evidence before reconcile. Proven on `WCS-046` for one-command single-task prep/launch orchestration; task completion still required operator commit, QA, manual verification, and post-worker truth.

### What this script does not currently do

- it does not run multiple tasks
- it does not schedule work
- it does not create commits
- it does not run build/smoke automatically
- it does not finalize worker or QA evidence
- it does not call post-worker automatically
- it does not weaken strict launch audit behavior

### Why it exists

It reduces operator glue for exactly one bounded WCS task while preserving the already-proven helper contracts and the one-task-at-a-time Phase 1 stance.

---

## 8bc. `scripts/run_task_sequence.py`

### Role

Sequential multi-task runner. Runs multiple WCS tasks one after another by reusing `run_one_task_full_cycle.py`. Proven on WCS-028 (one-task sequential proof) and WCS-029 + WCS-030 (multi-task back-to-back in one live session with honest operator checkpoints preserved between tasks).

### Current behavior

- selects exactly one next ready task via `select_next_ready_task.py` at the start of each iteration
- runs the full-cycle path for that exact task (pins task identity; no internal reselection)
- operator checkpoint for commit; operator checkpoint for manual verification note
- finalizes that same task; only then advances to the next task
- stops immediately on failure, block, abort, or gate failure
- uses explicit checkpoint exit codes from `run_one_task_full_cycle.py` (EXIT_STOP_COMMIT=10, EXIT_STOP_MANUAL=11) instead of fragile stdout parsing
- `--max-tasks` (default 3); pass-through of launch/dev-server/screenshot flags

### Important current truth

The operator-gated sequential runner is now proven for multiple tasks back-to-back in one live session. Proof was completed on WCS-029 and WCS-030 using `run_task_sequence.py` with honest operator checkpoints preserved between tasks. The system remains sequential only. No scheduling, unattended mode, concurrency, or session persistence. Current smoke coverage is still limited and should be improved later, especially for broader route/page coverage.

### What this script does not currently do

- it does not schedule work
- it does not run unattended
- it does not run tasks concurrently
- it does not persist session state

### Why it exists

Provides a thin wrapper to run multiple tasks sequentially using the proven single-task flow, with honest operator checkpoints preserved.

---

## 8c. `scripts/draft_worker_result_from_evidence.py`

### Role

Worker-result drafting helper: builds a truthful `worker_result.json` from real task-packet and repo evidence (branch, changed files), plus explicit operator-supplied command evidence. Does not stamp, reconcile, or fabricate completion; operator should review the drafted result before guarded post-worker if appropriate.

### Current behavior

- `--task WCS-XXX` required; `--workspace`, `--executor` (default `cursor_agent`), `--mode` (default `head_auto`: working tree if changed, else HEAD commit), repeatable `--command <text>`, `--write` (optional; without it, dry-run only)
- Loads task packet; requires valid `repo_path` and expected branch; requires current branch matches expected task branch
- Derives expected file scope from packet (target_files, suspected_files, notes, etc.); determines changed files from working tree or HEAD commit per `--mode`
- Fails if no changed files or if any changed file is outside expected scope; does not guess `files_changed`
- Normalizes `--command` entries by trimming whitespace, dropping empty values, and rejecting obvious placeholders such as `todo`, `tbd`, and `placeholder`
- Drafts JSON with `task_id`, `status` (worker_complete when evidence present), `executor`, `summary` (evidence-based), `files_changed` (from repo), `commands_run` (from explicit meaningful `--command` values only), `issues_encountered` ([]), `notes` (evidence source), `completed_at` (left blank; script does not stamp)
- For `worker_complete`, requires one or more meaningful `--command` values or fails clearly before writing; this closes the practical gap where `worker_result_validate.py --mode pre-stamp` could pass but `stamp_guard_check.py` could still fail on empty `commands_run`
- Does not auto-infer or fabricate commands from `evidence_source`; `commands_run` only reflects operator-supplied `--command` text
- Without `--write`: prints PASS and drafted JSON to stdout, reports `Written: no`. With `--write`: writes `results/WCS-XXX_worker_result.json`

### Output

- On success: `DRAFT WORKER RESULT: PASS`, task, workspace, repo path, expected/current branch, evidence source, output path, written yes/no, then the drafted JSON
- On failure: `DRAFT WORKER RESULT: FAIL`, reason (e.g. missing packet, wrong branch, no changed files, file outside scope, or missing meaningful `--command` evidence for `worker_complete`)

### Why it exists

Provides a single helper to draft a truthful worker result from repo evidence plus explicit command evidence so the operator does not have to hand-write it every time. Does not fabricate completion, commands, or QA/build claims; operator still reviews before post-worker.

---

## 8d. `scripts/draft_qa_result_from_evidence.py`

### Role

QA-result drafting helper: drafts a truthful `qa_result.json` from operator-supplied evidence (build/smoke/manual status via CLI). Dry-run by default; `--write` to persist. Pre-stamp only: does not stamp `completed_at`, does not reconcile, does not fabricate checks or artifacts. Operator should review the drafted result before guarded post-worker if appropriate.

### Current behavior

- `--task WCS-XXX` required; `--workspace` optional; `--write` optional (without it, dry-run only)
- `--build-status`, `--smoke-status`, `--manual-status` with choices `pass|fail|skip|unknown`; `--manual-check` (repeatable); `--artifact` (repeatable; paths must exist or script fails); `--note` (repeatable)
- Reads task packet; fails if missing or invalid. Artifact paths must exist or script fails bluntly.
- Builds `checks_run` / `checks_passed` / `checks_failed` from evidence; sets `status` to `qa_pass`, `qa_fail`, or `escalated` per evidence; leaves `completed_at` blank (pre-stamp only)
- Output JSON matches validator contract (task_id, status, qa_tool, summary, checks_run, checks_passed, checks_failed, artifacts, notes, completed_at). v1 is CLI-evidence-driven; does not auto-parse build/test logs.
- Without `--write`: prints PASS and drafted JSON to stdout, reports `Written: no`. With `--write`: writes `qa/WCS-XXX_qa_result.json`

### Output

- On success: `DRAFT QA RESULT: PASS`, task, workspace, output path, written yes/no, then the drafted JSON
- On failure: `DRAFT QA RESULT: FAIL`, reason (e.g. missing packet, artifact path does not exist)

### Why it exists

QA-side twin of `draft_worker_result_from_evidence.py`: drafts truthful pre-stamp QA result JSON from evidence so the operator can avoid hand-writing it when evidence is from CLI. Does not stamp, reconcile, or fabricate; operator still reviews before post-worker. Validator-proven (e.g. qa_result_validate.py --mode pre-stamp for WCS-042).

---

## 9. `scripts/worker_result_validate.py`

### Role

Read-only worker-result schema validator for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- supports `--mode pre-stamp` (default) and `--mode post-stamp`
- reads `results/WCS-XXX_worker_result.json` and validates:
  - file exists
  - JSON parses and root is an object
  - `task_id` matches the requested task id
  - `status` is one of: `worker_complete | blocked | escalated`
  - `status` is not `draft`
- requires the following fields to exist:
  - `task_id`
  - `status`
  - `executor`
  - `summary`
  - `files_changed`
  - `commands_run`
  - `issues_encountered`
  - `notes`
  - `completed_at`
- validates field content:
  - `executor` is non-blank
  - `summary` is non-blank
  - `files_changed` is a list
  - `commands_run` is a list
  - `issues_encountered` is a list
  - `notes` field exists (content may be blank or non-blank)
  - `files_changed` contains at least one entry when `status == worker_complete`
  - every `files_changed` entry is a non-blank string
- optionally reads `tasks/WCS-XXX_task.json` and derives expected file scope using the same simple Phase 1 rule as `worker_change_check.py`:
  - `target_files` list when present
  - otherwise a single `target_file` / `file_path` / `file`
  - otherwise a `notes` field that clearly looks like a single repo-relative path
- when expected file scope is available, requires every `files_changed` entry to be within that scope; if expected scope cannot be determined, it skips this consistency check instead of failing
- validates `completed_at` based on mode:
  - in `pre-stamp` mode, `completed_at` must be blank
  - in `post-stamp` mode, `completed_at` must be non-blank

### Output and behavior

- prints `WORKER RESULT VALIDATION: PASS` or `WORKER RESULT VALIDATION: FAIL`
- prints `Task: WCS-XXX`
- prints `Mode: pre-stamp` or `Mode: post-stamp`
- on PASS, prints:
  - executor
  - status
  - files_changed
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only worker-result schema validator that can be run before and after timestamp stamping to catch missing or malformed worker-result fields and simple task-scope inconsistencies.

---

## 10. `scripts/qa_result_validate.py`

### Role

Read-only QA-result schema validator for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- supports `--mode pre-stamp` (default) and `--mode post-stamp`
- reads `qa/WCS-XXX_qa_result.json` and validates:
  - file exists
  - JSON parses and root is an object
  - `task_id` matches the requested task id
  - `status` is one of: `qa_pass | qa_fail | escalated`
  - `status` is not `draft`
- requires the following fields to exist:
  - `task_id`
  - `status`
  - `qa_tool`
  - `summary`
  - `checks_run`
  - `checks_passed`
  - `checks_failed`
  - `artifacts`
  - `notes`
  - `completed_at`
- validates field content:
  - `qa_tool` is non-blank
  - `summary` is non-blank
  - `checks_run` is a list
  - `checks_passed` is a list
  - `checks_failed` is a list
  - `artifacts` is a list
  - `notes` field exists (content may be blank or non-blank)
  - `checks_run` contains at least one entry when `status` is `qa_pass` or `qa_fail`
  - every entry in `checks_run`, `checks_passed`, `checks_failed`, and `artifacts` is a non-blank string
- validates simple internal consistency:
  - when `status == qa_pass`:
    - `checks_failed` is empty
    - `checks_passed` contains at least one entry
  - when `status == qa_fail`:
    - `checks_failed` contains at least one entry
  - when `status == escalated`:
    - does not require non-empty `checks_passed` or `checks_failed` beyond type/shape checks
- validates `completed_at` based on mode:
  - in `pre-stamp` mode, `completed_at` must be blank
  - in `post-stamp` mode, `completed_at` must be non-blank

### Output and behavior

- prints `QA RESULT VALIDATION: PASS` or `QA RESULT VALIDATION: FAIL`
- prints `Task: WCS-XXX`
- prints `Mode: pre-stamp` or `Mode: post-stamp`
- on PASS, prints:
  - `qa_tool`
  - status
  - checks_run
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only QA-result schema validator that can be run before and after timestamp stamping to catch missing or malformed QA-result fields and simple internal inconsistencies.

### Role
Local result finalization helper.

### Current behavior
- accepts a file path argument
- stamps a timestamp into a result JSON field
- defaults to `completed_at` unless another field is specified

### Actual current usage pattern
```powershell
python .\stamp_result_timestamp.py ..\results\WCS-016_worker_result.json
python .\stamp_result_timestamp.py ..\qa\WCS-016_qa_result.json
````

### Important current truth

This script does **not** take `--task-id`.

It stamps one file at a time.

### What this script does not currently do

* it does not validate task semantics
* it does not validate allowed statuses
* it does not reconcile
* it does not repair bad result content

### Current operator reality

This helper is used only after the result file is already finalized and truthful.

### Intended future build direction

* wrapper that stamps worker and QA files together by task id
* optional validation that the file is no longer in draft/template shape before stamping

---

## 6. `scripts/render_master_backlog.py`

### Role

Backlog renderer.

### Current behavior

* reads `state/master_backlog.json`
* renders `state/MASTER_BACKLOG.md`

### Why it exists

This enforces the rule that JSON is authoritative and Markdown follows.

### What this script does not currently do

* it does not select tasks
* it does not reconcile completion
* it does not independently change backlog truth

### Current operator reality

The normal path is:

1. update `master_backlog.json`
2. run the renderer
3. let `MASTER_BACKLOG.md` update from JSON

### Intended future build direction

* automatic render on approved backlog edits
* schema validation before render
* clearer drift detection when rendered markdown is stale

---

## 7. `scripts/run_wcs_scout.py`

### Role

Public-route WCS scout runner.

### Current behavior

* runs the public scout loop
* writes timestamped scout outputs
* feeds scout findings into normalization

### Typical outputs

Under timestamped scout folders:

* public results JSON
* public summary text
* Playwright stdout
* Playwright stderr
* normalization reports

### Why it exists

This turns public-route failures into discoverable backlog work.

### What this script does not currently do

* it does not fix code
* it does not close tasks
* it does not verify worker task completion

### Intended future build direction

* better route-specific grouping
* stronger duplicate suppression
* better scheduled/scored reporting

---

## 7b. `scripts/run_pathfinder.py`

### Role

Pathfinder v1: bounded read-only WCS intake/investigation worker. Accepts minimal intake or full task packet, gathers context from workspace artifacts and WCS repo suspected files, produces structured result with synthesis and optional draft backlog candidate, or escalation when blocked.

### Current behavior

* CLI: `python scripts/run_pathfinder.py --packet <path-to-json>` [ `--no-llm` ] [ `--model <model-id>` ] [ `--out <path>` ]
* `--no-llm`: skip optional LLM synthesis; use rule-based synthesis only
* `--model`: model ID for LLM synthesis when enabled (default from env or synthesis module)
* Validates packet (minimal or full task packet)
* Resolves paths: workspace-relative for evidence; workspace then WCS repo for suspected files
* Rule-based synthesis always runs first: normalized issue type, evidence summary, missing context, likely next action, confidence
* Optional LLM synthesis: when not `--no-llm`, imports and uses `pathfinder_llm_synthesis.py` if available; safe fallback to rule-based when module unavailable, package missing, API key missing, or synthesis fails; records `llm_skipped_reason` when skipped
* Result output includes `synthesis_source` (e.g. `rule_based` or `llm`) and, when applicable, `llm_skipped_reason` (e.g. `no_llm`, `validation_failure`)
* Writes result to `scratch/pathfinder/` or `--out` path

### What this script does not do

* does not edit production code
* does not run git commands
* does not schedule or run unattended
* does not crawl the repo broadly
* does not autonomously create backlog items (draft candidate requires operator review)
* does not become a broad autonomous agent (LLM synthesis is optional enrichment only)

### Proof

Proven 2026-03-18 with `--packet future_modules/pathfinder/examples/pathfinder_intake.example.json`. Fallback path proven 2026-03-19: `--no-llm` run produced `synthesis_source=rule_based`, `llm_skipped_reason=no_llm`; LLM-enabled run fell back with `synthesis_source=rule_based`, `llm_skipped_reason=validation_failure`. LLM path not yet proven.

---

## 7c. `scripts/export_dashboard_data.py`

### Role

One-way export of local Jarvis source-of-truth files into Supabase dashboard tables. Populates the read model for the Jarvis Dashboard v1 (deployed on Vercel).

### Current behavior

* CLI: `python scripts/export_dashboard_data.py`
* Requires env: `SUPABASE_URL` (or `NEXT_PUBLIC_SUPABASE_URL`), `SUPABASE_SERVICE_KEY` (or `SUPABASE_SERVICE_ROLE_KEY`)
* Reads: `state/master_backlog.json`, `state/escalations.json`, `tasks/*_task.json`, `results/*_worker_result.json`, `scratch/pathfinder/*.json`, `scratch/pathfinder_ab/*.json`
* Upserts into: `dashboard_task_state`, `dashboard_runs`, `dashboard_module_status`, `dashboard_pathfinder_cases`
* Never mutates Jarvis truth files

### What this script does not do

* does not edit local JSON/Markdown
* does not run the dashboard app
* does not provide automatic/scheduled sync (manual runs only)

---

## 8. `scripts/normalize_scout_to_backlog.py`

### Role

Scout defect normalizer.

### Current behavior

* reads scout outputs
* applies noise filtering
* suppresses duplicates already represented in backlog
* inserts new findings into `state/master_backlog.json`
* re-renders `state/MASTER_BACKLOG.md`
* writes normalization output

### Why it exists

It converts scout findings into bounded backlog tasks.

### What this script does not currently do

* it does not implement fixes
* it does not commit repo changes
* it does not mark tasks done

### Intended future build direction

* stronger deduplication
* more robust issue bucketing
* confidence scoring for scout-generated tasks

---

## 9. `scripts/overnight_health_check.py`

### Role

Read-only workspace/repo health check.

### Current behavior

Checks:

* workspace path
* repo path
* dirty repo state
* key tool availability
* basic health conditions

### Why it exists

It provides a low-risk sanity check of the environment.

### What this script does not currently do

* it does not repair failures
* it does not select tasks
* it does not reconcile tasks

### Intended future build direction

* richer guardrail reporting
* escalation/pause integration
* scheduled health polling once the manual loop is more stable
- automatically update the working process/documentation files whenever a new process change, guardrail, contract, or script behavior is locked in
---

# Current QA Reality

## Live workspace truth

The broader source-of-truth documents may still reference a phase-1 Python QA script like `run_wcs_qa.py`, but in the current live workspace the QA path is still effectively operator-driven.

What is actually present and used is:

* saved QA command references
* WCS repo build command
* WCS repo Playwright smoke command
* manual interpretation of test results
* manual update of the QA result JSON

## Current QA flow

The live QA flow is:

1. run:

   * `npm run build`
2. run:

   * `npm run test:e2e:smoke`
3. inspect terminal output
4. update `qa/WCS-XXX_qa_result.json`
5. stamp `completed_at`

## Current QA truth

QA is currently **semi-manual evidence capture**, not a fully automated Python QA runner.

---

# Main WCS Task Loop

## Current proven loop

### Step 1 — Decide task reuse vs fresh selection

* run `jarvis.py`
* or run `jarvis.py --force` if intentional fresh reselection is required

### Step 2 — Generate packet artifacts

Usually triggered by `jarvis.py`

Artifacts include:

* task JSON
* task markdown
* placeholder worker result JSON
* placeholder QA result JSON
* placeholder escalation JSON

### Step 3 — Prepare the task branch

Usually triggered by `jarvis.py`

The goal is to place the WCS repo on:

* `jarvis-task-wcs-XXX`

### Step 4 — Manually verify Git state

In the WCS repo:

* `git branch --show-current`
* `git status`

The repo should be:

* on the correct task branch
* clean before work begins

### Step 5 — Perform worker implementation

The WCS worker implementation currently runs through Cursor or by direct operator action.

The code change must stay bounded to the task scope.

### Step 6 — Verify the diff

The operator inspects the diff to confirm:

* the change is small and in-scope
* unrelated logic was not removed
* the task intent matches the actual file change

### Step 7 — Commit gate

In the WCS repo:

* stage the intended file changes
* commit on the correct task branch
* verify the worktree is clean after commit

### Step 8 — Finalize worker result

The worker result JSON is filled truthfully.

It must include:

* correct task id
* valid worker status
* factual summary
* actual file changes
* actual issues encountered
* `completed_at` still blank until stamping

### Step 9 — Run QA

The operator currently runs:

* `npm run build`
* `npm run test:e2e:smoke`

### Step 10 — Finalize QA result

The QA result JSON is filled truthfully.

It must include:

* correct task id
* valid QA status
* checks actually run
* actual passed/failed items
* notes tied to actual evidence
* `completed_at` still blank until stamping

### Step 11 — Stamp result timestamps

The timestamp helper is run once for the worker result file and once for the QA result file.

### Step 12 — Reconcile the task

The operator runs:

* `reconcile_task_outcome.py --task WCS-XXX`

Reconcile is responsible for final state transition only if all contract and branch checks pass.

### Step 13 — Verify final state

The operator verifies:

* the correct task changed state
* `state/master_backlog.json` is correct
* `state/MASTER_BACKLOG.md` was rendered correctly
* review output was updated as expected

---

# Files Commonly Touched in the Process

## State files

* `state/master_backlog.json`
* `state/MASTER_BACKLOG.md`
* `state/daily_plan.json`
* `state/DAILY_PLAN.md`
* `state/run_log.json`
* `state/RUN_LOG.md`
* `state/DAILY_REVIEW.md`
* `state/project_status_wcs.json`

**Local machine-state handling:** `state/project_status_wcs.json` is machine-specific local state and should normally stay out of commits. To suppress Git status noise from local path/config differences, you can run:

```text
git update-index --skip-worktree .\state\project_status_wcs.json
```

When you intentionally need to edit or commit this file later, restore tracking with:

```text
git update-index --no-skip-worktree .\state\project_status_wcs.json
```

## Packet and result files

* `tasks/WCS-XXX_task.json`
* `tasks/WCS-XXX_task.md`
* `results/WCS-XXX_worker_result.json`
* `qa/WCS-XXX_qa_result.json`
* `logs/WCS-XXX_escalation.json`

## WCS repo files

* bounded source files under `C:\dev\wcsv2.0-new`
* repo tests and test artifacts where applicable

---

# Result File Contracts

## Worker result JSON

### Allowed statuses

* `worker_complete`
* `blocked`
* `escalated`

### Current truth requirement

A valid worker result must be factual and should include:

* correct task id
* actual execution summary
* real changed file list
* real commands run if tracked
* real issues encountered
* empty `completed_at` until stamped

### Current invalid examples

* `status: "completed"`
* blank placeholder values treated as final
* fake Cursor attribution when the operator actually did the work

---

## QA result JSON

### Allowed statuses

* `qa_pass`
* `qa_fail`
* `escalated`

### Current truth requirement

A valid QA result must be factual and should include:

* correct task id
* actual checks run
* actual pass/fail outcome
* actual notes
* empty `completed_at` until stamped

### Current invalid examples

* default placeholder JSON treated as evidence
* claimed pass with no build/test evidence
* invented artifacts

---

# Current Guardrails

## Already in place

* one-task-per-cycle process
* JSON source-of-truth discipline
* rendered markdown views
* branch-prep before worker execution
* operator verification of branch and clean repo state
* timestamp stamping kept local
* reconcile status contract enforcement
* reconcile branch verification
* reconcile commit-ahead-of-main verification

## Still weak or still manual

* worker-result truthfulness depends on operator discipline
* QA-result truthfulness depends on operator discipline
* current QA execution is not wrapped by a dedicated Python entrypoint
* some docs still describe planned artifacts more than live ones
* task text may drift from actual repo baseline if backlog maintenance is sloppy

---

# Intended Final Automation Map

## Processes intended to be automated later

### Selection and routing

* task eligibility validation
* safer reuse vs force decisioning
* clearer next-step instructions after selection
* stronger backlog/packet contract checks

### Worker handoff

* structured worker prompt generation
* changed-file sanity checks
* allowed-scope enforcement
* worker result schema validation before stamping

### QA handoff

* direct QA command orchestration
* automatic QA result generation from actual build/test outputs
* artifact linking from test outputs
* explicit fail/escalate routing

### Completion controls

* task-level dual-file timestamp stamping
* pre-reconcile readiness validation
* reconcile dry-run or explain mode
* clearer state transition enforcement
* stronger rejection of draft/template evidence

### Safety and reporting

* stronger operator-facing summaries
* pause-after-failure behavior
* daily review improvements
* more robust backlog/render drift checks

## Processes not intended to be fully automated until later

* broad autonomous coding
* vague multi-task execution
* voice-first execution flow
* unattended expansion into other worker domains
* any automation that weakens auditability, source-of-truth discipline, or branch correctness

---

# Process Direction

## What the system is now

The current system is:

* local-first
* partly automated
* partly operator-driven
* auditable
* contract-based
* getting safer through hardening

## What the system is being built toward

The intended final system is:

* more automated
* still local-first
* still auditable
* still branch-safe
* still source-of-truth driven
* more explicit about prerequisites
* less dependent on operator memory
* more resistant to false completion

---

# Bottom Line

The process only counts as progress when it produces **truthful evidence**.

That means:

* the right task was selected
* the right branch was used
* the bounded code change was committed
* the worker result is factual
* the QA result is factual
* timestamps were applied after finalization
* reconcile verified branch and commit state
* backlog truth changed only after all of that passed

Anything weaker than that is not completion. It is noise.

```
```
