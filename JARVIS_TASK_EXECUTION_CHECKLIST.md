````md
# JARVIS_TASK_EXECUTION_CHECKLIST_v2.md

## Live Doc Status
- Last reviewed: 2026-03-19
- Last updated: 2026-03-19 (Pathfinder fallback + LLM path proven)
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Status: aligned to current live hardening state (phases match handoff bundle; completed_at blank until stamping; stamp takes FILE PATH; validators/gates read-only; commit gate helper live and proven in completed/reconciled loop; thin operator-facing wrappers live for prep/post and one-task cycle flow; full-cycle wrapper proven on WCS-061 and WCS-008; sequential runner proven on WCS-028; post-milestone doc-audit checkpoint added; WCS trust visibility now live in dashboard Overview and Recent Runs; Pathfinder optional LLM synthesis fallback + LLM path proven; broader Pathfinder expansion still pending; current smoke test still limited; launch path supports strict post-launch auditing; scheduling and unattended execution remain deferred)

## Purpose

This checklist defines the **current live execution steps** for a bounded Jarvis WCS task and the **future direction** the process is being hardened toward.

It is intended to be used during task execution.

It is not the architecture reference.  
It is the **operator checklist** for running the loop correctly.

---

# Core Rule

A task is **not complete** unless all of the following are true:

1. Jarvis selected or reused the correct task intentionally
2. The WCS repo is on the correct task branch
3. The code change was made in bounded scope
4. The code change was committed on the correct branch
5. The worker result JSON is truthful and final
6. The QA result JSON is truthful and final
7. Both result files were timestamp-stamped after finalization
8. Reconcile passed
9. Backlog state reflects the correct completed task

---

# Current Live Execution Checklist

## Phase 0 — Decide whether to reuse or force a new task

### Current action
Decide whether today’s already-selected task should be reused or whether a fresh task selection is intentionally needed.

### Current commands
Normal reuse path:
```powershell
python .\jarvis.py
````

Forced reselection path:

```powershell
python .\jarvis.py --force
```

### Current success condition

* Jarvis either intentionally reuses the current day’s task
* or intentionally selects a new one

### Current failure condition

* operator assumes a fresh selection occurred when Jarvis actually reused the existing task
* operator starts work on the wrong task because `--force` was not used when needed

### Current verification

Read the terminal output carefully and confirm:

* whether Jarvis reused or newly selected
* the exact task id
* the exact task title

### Intended future automation

* explicit reuse-vs-force warning output
* stronger pre-selection operator guidance
* safer fresh-selection confirmation path

---

## Phase 1 — Run Jarvis and inspect its output

### Current action

Run Jarvis and confirm it completed the foreman portion of the loop.

### Current success condition

Jarvis should:

* identify the active task
* update daily plan and run log state
* generate or reuse task packet artifacts
* prepare the correct WCS task branch

### Current failure condition

Stop if:

* the wrong task is selected
* packet generation errors occur
* branch-prep errors occur (and escalations are recorded)
* output is ambiguous about what task is active

### Current verification

The terminal output should clearly identify:

* task id
* task title
* packet generation status
* branch-prep result
* target task branch
* whether an escalation record was written and where to find `state/escalations.json` and `state/ESCALATIONS.md`

### Intended future automation

* stronger summary output
* explicit next-step guidance after task selection
* automatic handoff package generation for worker and QA

---

## Phase 1B — Optional operator wrapper for prep/post

### Current action

Use `run_wcs_operator_entrypoint.py` when you want a tighter operator entrypoint for the current WCS lane without replacing the real helper scripts underneath.

### Current commands

Prep example:

```powershell
python .\scripts\run_wcs_operator_entrypoint.py prep --task WCS-XXX
```

Strict launch example:

```powershell
python .\scripts\run_wcs_operator_entrypoint.py prep --task WCS-XXX --launch-cursor
```

Strict launch with longer Agent timeout example:

```powershell
python .\scripts\run_wcs_operator_entrypoint.py prep --task WCS-XXX --launch-cursor --agent-timeout-seconds 1200
```

Post example:

```powershell
python .\scripts\run_wcs_operator_entrypoint.py post --task WCS-XXX --draft-worker-result --worker-command "Implemented bounded change on task branch jarvis-task-wcs-xxx" --draft-qa-result --build-status pass --smoke-status pass --manual-status pass --manual-check "Manual browser verification of the targeted change"
```

### Important current truth

- `prep` ensures the packet exists when missing, delegates to guarded `pre_worker`, and prints key artifact paths
- when `prep --launch-cursor` is used, the wrapper now calls `run_cursor_worker.py` with strict post-launch audit enabled
- optional `--agent-timeout-seconds <n>` and `--agent-model <id>` can be passed through during strict launch (timeout gives the real Agent CLI path more time; agent-model selects the model, e.g. composer-1.5 when default Opus hits usage limit)
- `post` delegates to guarded `post_worker` and passes worker/QA evidence through unchanged
- existing helpers remain the true engines underneath
- the wrapper does not run build or smoke itself, does not create commits, does not select tasks automatically, and does not invent evidence
- launch still does not prove task completion, semantic correctness, commit readiness, QA completion, or finalized worker evidence
- strict launch failure is acceptable and expected when launch is not immediately auditable, for example when no working-tree delta exists or changed files fall outside scope
- blocked/timeout launch is also an honest outcome when the real Agent CLI does not finish before the configured timeout
- strict real-Agent success is proven on `WCS-041` and `WCS-046`; one-command single-task wrapper is proven on `WCS-046`; operator review, commit, QA, and post-worker truthfulness are still required after launch

### Current success condition

* the wrapper delegates to the expected helper command
* helper output remains visible
* the delegated step passes honestly

### Current failure condition

Stop if:

* the wrapper hides a helper failure
* the wrapper reinterprets evidence instead of passing it through
* the wrapper is treated as autonomous execution rather than operator-assisted orchestration

---

## Phase 1C — One-task cycle wrapper

### Current action

Use `run_one_task_cycle.py` when you want one command to drive exactly one bounded WCS task through selection-or-explicit-task plus prep/optional strict launch, while still keeping commit/QA/post-worker truth operator-assisted.

### Current commands

Explicit task example:

```powershell
python .\scripts\run_one_task_cycle.py --task WCS-XXX
```

Select-one-ready example:

```powershell
python .\scripts\run_one_task_cycle.py --select-ready
```

Strict launch example:

```powershell
python .\scripts\run_one_task_cycle.py --task WCS-XXX --launch-cursor --agent-timeout-seconds 1200
```

Strict launch with explicit Agent model (e.g. when default Opus hits usage limit):

```powershell
python .\scripts\run_one_task_cycle.py --task WCS-XXX --launch-cursor --agent-timeout-seconds 1200 --agent-model composer-1.5
```

### Important current truth

- this wrapper still handles exactly one task only
- it delegates selection to `select_next_ready_task.py` when `--select-ready` is used
- it delegates prep and optional strict launch to `run_wcs_operator_entrypoint.py prep`
- it stops on first failed or blocked delegated step
- after a successful prep path, it prints the exact remaining operator steps for diff review, commit, QA, manual verification, and `post`
- launch success still does not equal completion
- the operator still owns diff review, commit creation, QA truth, manual verification, and post-worker truthfulness

### Current failure condition

Stop if:

* selection fails or returns no eligible task
* delegated prep fails
* strict launch fails or blocks
* the wrapper is treated as a multi-task or autonomous loop tool

---

## Phase 1D — Full one-task closeout wrapper

### Current action

Use `run_one_task_full_cycle.py` when you want one command to run the full single-task cycle: prep, optional strict launch, commit, build, smoke, manual verification, and post. Requires operator confirmation flags; does not fabricate evidence. Proven on WCS-061 and WCS-008; wrapper family can truthfully close a single task end-to-end via mechanical path plus `--finalize`; screenshot artifact support and `--finalize` proven on WCS-008.

### Current commands

Prep and launch only (stops before commit; review diff first):

```powershell
python .\scripts\run_one_task_full_cycle.py --task WCS-XXX --launch-cursor --agent-timeout-seconds 1200 --agent-model composer-1.5
```

Full closeout with managed dev server and optional screenshot:

```powershell
python .\scripts\run_one_task_full_cycle.py --task WCS-XXX --launch-cursor --agent-timeout-seconds 1200 --agent-model composer-1.5 --manage-dev-server --confirm-commit --manual-check "Verified the targeted change locally in the browser for WCS-XXX."
```

With screenshot capture (saves to qa/artifacts/<TASK_ID>_manual_check.png; does NOT imply manual pass):

```powershell
python .\scripts\run_one_task_full_cycle.py --task WCS-048 --launch-cursor --manage-dev-server --capture-screenshot --manual-url "http://localhost:3000/schedules" --confirm-commit --manual-check "Verified calendar emoji on schedules page."
```

Resume/finalize mode (task already committed and smoke-tested; skip prep/launch/commit/build/smoke):

```powershell
python .\scripts\run_one_task_full_cycle.py --finalize --task WCS-XXX --manual-check "Verified the targeted change locally in the browser for WCS-XXX."
```

With optional screenshot artifact (if captured in prior run):

```powershell
python .\scripts\run_one_task_full_cycle.py --finalize --task WCS-XXX --manual-check "Verified ..." --artifact qa/artifacts/WCS-XXX_manual_check.png
```

### Important current truth

- one task only; no batching or scheduling; operator-truthful
- reuses `run_wcs_operator_entrypoint.py prep` and `post`; does not duplicate business logic
- `--confirm-commit` required to proceed past diff review; commit is idempotent if working tree already clean
- `--manual-check "..."` required to run post; operator must provide truthful verification note
- `--manage-dev-server`: reuses existing server on `--dev-port` if in use; `--force-restart-dev-server` kills only process on that port; only kills on exit if wrapper started the server
- `--capture-screenshot` saves to qa/artifacts/<TASK_ID>_manual_check.png and wires into QA artifacts; does NOT imply manual verification passed
- runs `npm run build` and `npm run test:e2e:smoke`; current smoke test is limited and should be improved later, especially for page-specific task coverage
- `--finalize`: resume mode for task already committed and smoke-tested; skips prep/launch/commit/build/smoke; delegates to post only; requires `--task` and `--manual-check`; optional `--artifact` for screenshot path(s)
- stops immediately on prep/launch/build/smoke failure; no fabrication of worker/QA/manual evidence

### Current failure condition

Stop if:

* selection fails or returns no eligible task
* delegated prep fails
* strict launch fails or blocks
* git add/commit fails (when --confirm-commit used)
* npm run build fails
* npm run test:e2e:smoke fails
* post delegation fails

---

## Phase 2 — Verify branch and repo cleanliness before touching code

### Current action

Go to the WCS repo and verify the repo is on the correct task branch and clean before implementation begins.

### Current commands

```powershell
git branch --show-current
git status
```

### Current success condition

* current branch matches the selected task branch
* working tree is clean

### Current failure condition

Stop if:

* branch is not the expected task branch
* repo is dirty before the task starts
* unrelated changes are present
* repo is in merge/rebase/conflict state

### Current verification

The repo should show:

* the correct `jarvis-task-wcs-XXX` branch
* nothing to commit
* working tree clean

### Intended future automation

* post-branch-prep automatic verification
* stronger script-side warnings for dirty state
* clearer recovery instructions when branch state is unsafe

---

## Phase 3 — Review the task packet before implementation

### Current action

Read the task packet so the implementation stays bounded.

### Current files to review

* `tasks/WCS-XXX_task.json`
* `tasks/WCS-XXX_task.md`

### Current success condition

The packet clearly defines:

* task id
* task title
* intended scope
* target file(s) or area(s)

### Current failure condition

Stop if:

* task scope is unclear
* task title does not match the actual repo baseline
* packet appears stale or misleading
* the requested change is broader than intended

### Current verification

Confirm:

* the implementation target is understood
* the desired change matches the actual current repo state
* the task is still bounded and safe

### Intended future automation

* packet/repo mismatch detection
* packet validation before worker handoff
* explicit allowed-scope enforcement

---

## Phase 4 — Perform the worker implementation

### Current action

Perform the bounded code change in Cursor or by direct operator edit.

### Current success condition

* only the intended file(s) are changed
* the change stays within task scope
* no unrelated cleanup or refactor work is introduced
* the implementation actually matches the task intent

### Current failure condition

Stop if:

* unrelated logic is removed
* multiple unrelated files change
* the task drifts into broader work
* the implementation direction no longer matches the task definition

### Current operator reality

The worker implementation is currently semi-manual.

Cursor may help perform the change, but the operator still validates the result.

### Intended future automation

* structured worker prompts generated from the task packet
* scope-limited changed-file validation
* automated detection of suspiciously broad diffs
* contract-safe worker result generation

---

## Phase 5 — Verify the diff before commit

### Current action

Inspect the diff before staging or committing.

### Current commands

Examples:

```powershell
git status --short
git diff -- path\to\target_file
git diff --unified=5 -- path\to\target_file
```

### Current success condition

* diff is bounded
* only expected file(s) changed
* no unrelated behavior was removed
* the task intent matches the actual code change

### Current failure condition

Stop if:

* diff is much larger than expected
* unrelated code was changed
* the file was partially broken by tool output
* the implementation does not match the selected task

### Current verification

Confirm:

* file count is correct
* changed lines are correct
* no hidden accidental refactor slipped in

### Intended future automation

* automated diff sanity checks (now partially available via `worker_change_check.py`)
* stronger changed-file allowlist validation
* suspicious-diff warning output

---

## Phase 6 — Run worker change boundary check (read-only)

### Current action

Run the read-only worker change boundary validator before committing, to confirm the changed files and diff size stay within the intended task scope.

### Current command

```powershell
python .\worker_change_check.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `WORKER CHANGE CHECK: PASS`
* current branch matches the expected task branch
* expected file scope matches the task packet
* the actual changed files are within the expected file scope
* the number of changed files is small and each diff is within the allowed size limit

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* it cannot determine expected file scope from the task packet
* any changed file is outside the expected task scope
* too many files are changed
* any single file has too many changed lines
* the current branch does not match the expected task branch

### Current verification

Confirm:

* the printed task id matches the intended task
* repo path and branch are correct
* expected file scope matches the task’s true intent
* actual changed files list matches what you meant to touch

### Intended future automation

* tighter integration with the commit gate
* clearer reporting when scope drift is detected

---

## Phase 7 — Commit gate

### Current action

Stage and commit the bounded change on the correct task branch.

### Current commands

Examples:

```powershell
git add .\path\to\changed_file
git commit -m "WCS-XXX concise factual message"
git status
```

### Current success condition

* the commit is created on the correct task branch
* the commit message references the task id
* the worktree is clean after commit

### Current failure condition

Stop if:

* nothing is committed
* the commit occurs on the wrong branch
* unrelated files are included
* the worktree remains dirty afterward

### Current verification

Confirm:

* commit succeeded
* current branch is still correct
* `git status` shows a clean worktree after commit

### Intended future automation

* tighter integration between commit_state checks and worker/QA result finalization
* stronger branch/commit summaries

----

## Phase 7B — Run commit gate check (read-only)

### Current action

Run the read-only commit gate helper after commit, before treating worker/QA results as trusted evidence.

### Current command

```powershell
python .\commit_gate_check.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `COMMIT GATE CHECK: PASS`
* current branch matches the expected task branch
* HEAD commit exists and is ahead of `main`/`master`
* worktree is clean after commit
* HEAD commit message references the task id
* committed files and changed lines are within bounded scope for the task

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* the task packet or repo path is missing
* branch or HEAD cannot be determined
* the branch is not ahead of `main`/`master`
* the worktree is dirty after commit
* the commit message omits the task id
* committed files fall outside expected task file scope

### Current verification

Confirm:

* the printed task id matches the intended task
* repo path, expected branch, current branch, base branch, and commits-ahead count look correct
* committed files in HEAD match the true task scope

### Intended future automation

* tighter integration with commit creation and worker/QA result finalization
* clearer summaries when the gate fails and how to recover

----

## Phase 7 — Finalize the worker result JSON truthfully

### Current action

Replace the placeholder worker result with factual execution data.

### Current file

* `results/WCS-XXX_worker_result.json`

### Current required worker statuses

Allowed values:

* `worker_complete`
* `blocked`
* `escalated`

### Current success condition

The worker result is truthful and includes:

* correct task id
* valid worker status
* honest executor identity
* factual summary
* actual files changed
* real commands run if tracked
* real issues encountered
* `completed_at` left blank for now (pre-stamp)

### Current failure condition

Stop if:

* status is invalid such as `completed`
* the file is still a blank placeholder
* changed files are missing or false
* executor attribution is false
* `completed_at` is stamped too early

### Current verification

Read the JSON and confirm:

* it matches what actually happened
* it uses a valid worker status
* it still has `completed_at: ""`

### Intended future automation

* direct generation of worker results from validated activity
* automatic rejection of placeholder-shaped worker results

---

## Phase 8 — Validate worker result schema (read-only)

### Current action

Run the read-only worker-result schema validator to confirm the worker result JSON has the required fields and shape.

### Current commands

Pre-stamp mode (before timestamps are applied):

```powershell
python .\worker_result_validate.py --task WCS-XXX --mode pre-stamp
```

Post-stamp mode (after timestamps are applied):

```powershell
python .\worker_result_validate.py --task WCS-XXX --mode post-stamp
```

### Current success condition

* the script exits with code `0`
* output shows `WORKER RESULT VALIDATION: PASS`
* executor and summary are non-blank
* files_changed, commands_run, and issues_encountered are lists
* files_changed is non-empty when status is `worker_complete`
* completed_at matches the expected mode (blank in pre-stamp, non-blank in post-stamp)

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any required worker-result fields are missing
* executor or summary are blank
* list fields have the wrong type
* completed_at does not match the expected mode

### Current verification

Confirm:

* the printed task id matches the intended task
* the printed executor and status match what actually happened
* the printed files_changed list matches the real changed files

### Intended future automation

* tighter integration with the worker completion path
* clearer reporting when schema violations are detected

---

## Phase 9 — Run QA

### Current action

Run the live QA commands for the WCS repo.

### Current live QA commands

```powershell
npm run build
npm run test:e2e:smoke
```

The Playwright config is hardened so that, for local runs without `E2E_BASE_URL` or `NEXT_PUBLIC_BASE_URL` set, `npm run test:e2e:smoke` automatically starts `npm run dev` via `webServer`, waits for readiness, and reuses an existing server when already running.

### Current success condition

* build passes
* smoke QA passes
* the terminal output clearly supports a pass decision

### Current failure condition

Stop if:

* build fails
* smoke tests fail
* no tests are found unexpectedly
* browsers/dependencies are missing
* output is ambiguous or broken

### Current operator reality

QA is currently semi-manual.

The operator runs the commands and interprets the terminal results.

### Intended future automation

* dedicated Python QA entrypoint
* direct capture of build/test results into QA artifacts
* automatic pass/fail/escalate routing

---

## Phase 9 — Finalize the QA result JSON truthfully

### Current action

Replace the placeholder QA result with factual QA evidence.

### Current file

* `qa/WCS-XXX_qa_result.json`

### Current required QA statuses

Allowed values:

* `qa_pass`
* `qa_fail`
* `escalated`

### Current success condition

The QA result is truthful and includes:

* correct task id
* valid QA status
* actual checks run
* actual checks passed
* actual checks failed
* factual notes
* `completed_at` left blank for now (pre-stamp)

### Current failure condition

Stop if:

* the QA result is still a placeholder
* QA status is invalid
* the claimed checks do not match what was run
* pass/fail reporting is invented
* `completed_at` is stamped too early

### Current verification

Read the JSON and confirm:

* it matches actual QA activity
* it uses a valid QA status
* it still has `completed_at: ""`

### Intended future automation

* direct generation of QA result content from actual command output
* stronger evidence linking from test runs

---

## Phase 10 — Validate QA result schema (read-only)

### Current action

Run the read-only QA-result schema validator to confirm the QA result JSON has the required fields and shape.

### Current commands

Pre-stamp mode (before timestamps are applied):

```powershell
python .\qa_result_validate.py --task WCS-XXX --mode pre-stamp
```

Post-stamp mode (after timestamps are applied):

```powershell
python .\qa_result_validate.py --task WCS-XXX --mode post-stamp
```

### Current success condition

* the script exits with code `0`
* output shows `QA RESULT VALIDATION: PASS`
* qa_tool and summary are non-blank
* checks_run, checks_passed, checks_failed, and artifacts are lists
* checks_run is non-empty when status is `qa_pass` or `qa_fail`
* internal consistency between status, checks_passed, and checks_failed is satisfied
* completed_at matches the expected mode (blank in pre-stamp, non-blank in post-stamp)

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any required QA-result fields are missing
* qa_tool or summary are blank
* list fields have the wrong type
* checks_run is empty for `qa_pass` or `qa_fail`
* status-specific checks for checks_passed/checks_failed fail
* completed_at does not match the expected mode

### Current verification

Confirm:

* the printed task id matches the intended task
* the printed qa_tool and status match what actually happened
* the printed checks_run list matches the real checks that were run

### Intended future automation

* tighter integration with the QA execution path
* clearer reporting when schema violations are detected

---

## Phase 10B — Triage QA failures (read-only helper)

### Current action

When QA fails or produces ambiguous evidence, optionally run the read-only QA failure triage helper to classify the failure and suggest the next bounded action.

### Current command

```powershell
python .\qa_failure_triage.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `QA TRIAGE: CLASSIFIED` or `QA TRIAGE: UNABLE TO CLASSIFY`
* output prints:
  * task id
  * reviewed QA status
  * failure class (`environment_setup_failure`, `test_harness_failure`, `application_regression`, or `ambiguous`)
  * confidence (`high`, `medium`, or `low`)
  * likely cause
  * whether a follow-up task is recommended
  * suggested follow-up task title when applicable

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* the task id is malformed
* the workspace path does not exist

### Current verification

Confirm:

* the printed task id matches the intended task
* the reviewed QA status matches the actual QA result
* the failure class and likely cause align with the evidence in the QA summary/notes

### Important current truth

`qa_failure_triage.py` is a **helper**, not an authority:

* it does not rewrite QA results
* it does not change backlog or state
* it does not mark tasks done or escalated
* it does not call reconcile
* it does not convert failed QA into passes

---

## Phase 11 — Guard pre-stamp readiness (read-only)

### Current action

Run the read-only stamp guard helper to confirm both worker and QA result files exist, parse, have allowed statuses, remain pre-stamp, and are not obvious placeholders before stamping.

### Current command

```powershell
python .\stamp_guard_check.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `STAMP GUARD CHECK: PASS`
* worker and QA result files are present and parse as objects
* both have allowed statuses for their kind
* both have `completed_at` blank (pre-stamp)
* summaries and key fields are present and not placeholder-shaped

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* either result file is missing or malformed
* status is invalid or `draft`
* `completed_at` is already non-blank
* summaries or required list fields look like placeholders when statuses imply real evidence should exist

### Current verification

Confirm:

* the printed task id matches the intended task
* the printed paths match the intended result files
* failures (when present) clearly describe why stamping should be blocked

---

## Phase 12 — Stamp finalized result timestamps

### Current action

Stamp the finalized worker result and QA result files with real local timestamps. `stamp_result_timestamp.py` takes a **FILE PATH** (positional argument) to the result JSON to stamp; run it once per file.

### Current commands

```powershell
python .\stamp_result_timestamp.py ..\results\WCS-XXX_worker_result.json
python .\stamp_result_timestamp.py ..\qa\WCS-XXX_qa_result.json
```

### Current success condition

* both files are stamped successfully
* both files now contain real `completed_at` values

### Current failure condition

Stop if:

* file path is wrong
* JSON is malformed
* stamping is attempted before the file is final
* only one file is stamped and the other is forgotten

### Current verification

Read both files and confirm:

* timestamps are present
* all other fields remain intact
* stamped content is still truthful

### Intended future automation

* task-level dual stamping helper
* refusal to stamp draft/template-shaped files
* stronger output when stamping succeeds or should be blocked

---

## Process documentation rule

Whenever a new process change, guardrail, contract, or script behavior is **locked in and live**, the corresponding working process and checklist documentation in this workspace **must be updated immediately** so execution checklists stay aligned with the real loop.

## Phase 11 — Run pre-reconcile readiness check (read-only)

### Current action

Run the read-only pre-reconcile gate for the selected task to confirm artifacts and repo state look ready before reconcile.

### Current command

```powershell
python .\pre_reconcile_check.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `PRE-RECONCILE CHECK: PASS`
* repo path, expected branch, current branch, and commits ahead of main/master are printed
* all listed readiness checks are reported as passed

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any failures are listed for artifacts, worker result, QA result, or repo/branch state

### Current verification

Confirm:

* the printed task id matches the intended task
* repo path and branch match what you expect
* commits-ahead count is at least 1

### Intended future automation

* tighter integration with reconcile
* optional enforcement that reconcile may only run after a passing pre-reconcile check

---

## Phase 12 — Reconcile the task

### Current action

Run reconcile explicitly for the task.

### Current command

```powershell
python .\reconcile_task_outcome.py --task WCS-XXX
```

### Current success condition

Reconcile should:

* accept the worker result contract
* accept the QA result contract
* verify the repo path
* verify the expected branch
* verify the current branch
* verify committed work exists
* verify the task branch is ahead of `main`
* update backlog state
* render backlog markdown
* update review output where applicable

### Current failure condition

Stop if:

* task id is missing
* worker status is invalid
* QA status is invalid
* result files are missing or malformed
* branch verification fails
* commit verification fails
* reconcile reports an error

### Current verification

Read the terminal output and confirm:

* the correct task was reconciled
* branch verification passed
* commit-ahead-of-main check passed
* state files were updated

### Intended future automation

* dry-run / explain mode
* richer contract error messages
* stronger rejection of placeholder evidence before deep reconcile

---

## Phase 13 — Verify final backlog and rendered state

### Current action

Inspect the resulting state files after reconcile.

### Current files to inspect

* `state/master_backlog.json`
* `state/MASTER_BACKLOG.md`
* `state/DAILY_REVIEW.md`

### Current success condition

* the correct task changed state
* the task is marked appropriately
* no wrong task was mutated
* backlog markdown reflects the JSON truth
* review output is updated as expected

### Current failure condition

Stop if:

* the wrong task changed state
* the task remained in the wrong status after reported success
* backlog JSON and Markdown drift
* state files appear malformed

### Current verification

Confirm:

* selected task id matches the updated done task
* neighboring tasks remain unchanged unless intentionally affected
* rendered markdown matches the JSON update

### Intended future automation

* JSON/Markdown drift detection
* stronger review summary generation

---

## Phase 14 — Run post-reconcile validation (read-only)

### Current action

Run the read-only post-reconcile validator for the reconciled task to confirm that backlog, rendered markdown, review output, and result files all reflect the intended done state.

### Current command

```powershell
python .\post_reconcile_validate.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `POST-RECONCILE VALIDATION: PASS`
* the printed task title and backlog status match expectations
* the passed-checks list indicates backlog JSON, rendered markdown, review, worker result, and QA result are all consistent

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any failures are listed for backlog JSON, MASTER_BACKLOG.md, DAILY_REVIEW.md, worker result, or QA result

### Current verification

Confirm:

* the printed task id matches the reconciled task
* backlog JSON shows the task as done for project WCS
* MASTER_BACKLOG.md and DAILY_REVIEW.md both include the task
* worker and QA results are present, have allowed statuses, and non-blank completed_at

### Intended future automation

* tighter integration with reconcile outcome reporting
* automatic drift detection when backlog JSON and rendered markdown disagree

---

## Phase 15 — Post-milestone doc audit (checkpoint)

### Current action

Before recommending commit/push after a meaningful milestone, run the doc-audit checkpoint:

- Did live state update? (backlog, DAILY_REVIEW, task packets, results)
- Did file registry update? (state/file_registry.json, state/FILE_REGISTRY.md)
- Did handoff/current-state docs update? (JARVIS_LIVE_HANDOFF_BUNDLE, JARVIS_NEW_CHAT_HANDOFF_BUNDLE, JARVIS_PHASE_CHECKLIST, JARVIS_SCRIPT_PROCESS_REFERENCE)
- Does this change require canon-doc updates (source-of-truth, PRD), or should those remain unchanged?
- If canon docs are unchanged, state that explicitly.

This is a doc-audit checkpoint for live execution, not a product architecture rule.

---

# Current Result Contracts

## Worker result contract

### Allowed worker statuses

* `worker_complete`
* `blocked`
* `escalated`

### Minimum truth requirements

* correct `task_id`
* truthful `status`
* truthful `executor`
* factual `summary`
* real `files_changed`
* actual `commands_run` if tracked
* real `issues_encountered`
* truthful `notes`
* blank `completed_at` until stamping

### Invalid examples

* `status: "completed"`
* blank placeholder treated as final
* fake executor attribution
* fake changed-file reporting

---

## QA result contract

### Allowed QA statuses

* `qa_pass`
* `qa_fail`
* `escalated`

### Minimum truth requirements

* correct `task_id`
* truthful `status`
* truthful `qa_tool`
* factual `summary`
* actual `checks_run`
* actual `checks_passed`
* actual `checks_failed`
* truthful `notes`
* blank `completed_at` until stamping

### Invalid examples

* placeholder JSON treated as final evidence
* pass claim without actual build/test support
* invented artifacts or notes

---

# Current Manual or Semi-Manual Areas

The current process still relies on operator discipline in these areas:

* deciding when to use `--force`
* confirming the selected task is the intended one
* verifying branch and repo cleanliness after branch prep
* validating the actual code diff
* creating the correct Git commit
* filling worker result JSON truthfully
* running build and smoke QA manually
* filling QA result JSON truthfully
* confirming reconcile terminal output is actually correct
* validating final backlog state
* reviewing new entries in `state/ESCALATIONS.json` / `state/ESCALATIONS.md` when Jarvis reports a hard failure

---

# Processes Being Built Toward

## Worker-side improvements

* structured worker handoff prompt generation
* bounded-scope validation before implementation
* automated changed-file sanity checking
* direct worker-result generation from validated execution activity

## QA-side improvements

* dedicated Python QA runner
* automated build/test orchestration
* direct QA-result generation from actual command output
* stronger fail/escalate routing

## Safety improvements

* reuse-vs-force guardrails
* stronger preflight repo checks
* stronger rejection of placeholder result files
* clearer branch/commit status summaries
* pre-reconcile readiness validation

## State and reporting improvements

* WCS trust visibility in dashboard (build, smoke, page-smoke, route, stop reason) — **live**; exporter populates operator_checkpoints and stop_reason from local evidence; Overview and Recent Runs surface trust signals
* Pathfinder optional LLM synthesis — **fallback + LLM path proven**; `run_pathfinder.py` supports `--no-llm` and `--model`; safe fallback to rule-based when module/API key absent or synthesis fails; result includes `synthesis_source` and `llm_skipped_reason`; validation failure diagnostics preserve `validation_failure:<reason>`; broader Pathfinder expansion still pending
* more explicit terminal guidance after each stage
* better daily review reporting
* stronger JSON/Markdown drift detection
* clearer operator-facing failure messages
* less dependence on operator memory

---

# Processes Not Intended to Be Fully Automated Yet

These are not current Phase-1 goals:

* broad autonomous coding
* vague multi-task execution
* unattended scope expansion
* voice-first execution flow
* any automation that weakens auditability
* any automation that weakens branch correctness
* any automation that weakens JSON source-of-truth discipline

---

# Current Execution Mindset

The process is considered correct only when:

* the right task is active
* the right branch is active
* the code change is bounded
* the code change is committed
* the worker result is factual
* the QA result is factual
* timestamps are applied after finalization
* reconcile verifies branch and commit state
* backlog truth changes only after all of that passes

Anything less is not completion.

```
```
