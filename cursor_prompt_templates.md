# Cursor Prompt Templates

## Live Doc Status
- Last reviewed: 2026-03-14
- Last updated: 2026-03-14 (doc pass: worker-result command-evidence hardening for draft_worker_result_from_evidence.py)
- Status: active reusable template set for common Jarvis/Cursor actions

## Purpose

This file stores standard Cursor prompt templates for recurring Jarvis rebuild tasks so prompt structure stays tight, consistent, and resistant to Cursor overreach.

**Workflow helper:** `build_cursor_handoff.py --task WCS-XXX` generates a handoff file under `scratch/cursor_handoffs/` whose Cursor prompt body matches the bounded style of Template 4 (WCS task implementation). The script fails (no file written) when bounded file scope cannot be derived from the task packet. Use the generated handoff as the copy/paste prompt when starting work on a task.

**Workflow helper:** `build_task_cycle_summary.py --task WCS-XXX` generates a human-readable markdown summary under `scratch/task_cycle_summaries/` that describes the current task/worker/QA evidence for a single WCS task cycle. Use that summary when reviewing a task, preparing a handoff, or deciding the next bounded operator action.

**Workflow helper:** `run_guarded_task_cycle.py --task WCS-XXX --mode pre_worker|post_worker|full` runs the existing guarded task-cycle scripts in order and stops on the first failure. Optional for post_worker/full: add `--draft-qa-result` plus QA evidence (e.g. `--build-status pass --smoke-status pass --manual-status pass --manual-check "Manual browser verification of /about"`) to have the flow run `draft_qa_result_from_evidence.py --write` before pre-stamp QA validation; without `--draft-qa-result`, QA result JSON must already exist. Use only as an orchestrator; it does not replace helper logic, execute worker code directly, or schedule tasks.

**Workflow helper:** `select_next_ready_task.py [--project WCS] [--limit N]` selects the next eligible ready task from the backlog using the progression ladder (execution_lane, test_phase, selector_rank) when present; read-only, does not mutate state.

**Workflow helper:** `build_daily_execution_prep.py [--project WCS] [--task WCS-XXX] [--output <path>]` prepares a daily execution prep package (selection, packet if missing, handoff, summary) and writes a prep markdown file; does not execute tasks or mutate state beyond approved helper outputs.

**Workflow helper:** `run_cursor_worker.py --task WCS-XXX [--workspace <path>] [--handoff <path>]` is the Cursor invocation bridge: runs Agent (or cursor launcher) against the task repo workspace from the packet (`repo_path`); uses `--trust` for non-interactive Agent execution; reports PASS/BLOCKED/FAIL honestly; does not prove completion or write worker_complete; operator still verifies completion and finalizes worker-result evidence.

**Workflow helper:** `draft_worker_result_from_evidence.py --task WCS-XXX [--workspace <path>] [--executor <label>] [--mode working_tree|head_auto] --command "<truthful step>" [--command "<truthful step>"] [--write]` drafts a truthful worker result JSON from task packet and repo evidence (branch, changed files). Explicit `--command` values populate `commands_run`; entries are trimmed, empty values are dropped, and placeholder-only values like `todo`, `tbd`, and `placeholder` are rejected. For `worker_complete`, at least one meaningful `--command` is required or the draft fails. Does not stamp or fabricate completion; operator should review before post-worker.

**Worker-result drafting example:** `python scripts/draft_worker_result_from_evidence.py --task WCS-XXX --command "Implemented bounded change on task branch jarvis-task-wcs-xxx" [--write]`

**Workflow helper:** `draft_qa_result_from_evidence.py --task WCS-XXX [--workspace <path>] [--build-status pass|fail|skip|unknown] [--smoke-status ...] [--manual-status ...] [--manual-check <text>] [--artifact <path>] [--note <text>] [--write]` drafts a truthful pre-stamp QA result JSON from operator-supplied evidence. Dry-run by default; does not stamp, reconcile, or fabricate evidence; operator should review before post-worker.

## Core rules for all Cursor prompts

Use these rules in every prompt unless a specific template intentionally overrides them:

- This is not a theory rewrite.
- Be surgical.
- Do not broaden scope.
- Do not modify unrelated files.
- Do not invent new capabilities.
- Keep architecture intent intact.
- Preserve current live contracts unless the task explicitly changes them.
- Use current live docs / handoff bundle / current workspace state as source of truth.
- Return a concise summary of:
  - files changed
  - exact corrections made
  - assumptions or edge cases
  - anything intentionally left unchanged and why
- Refresh timestamps on every touched doc.

### Hardening rules for proof and contracts

Apply these when a task asks for proof, hard contracts, or doc/registry updates:

1. **Proof rule**  
   When proof is requested, return: actual command run, actual output, actual exit code, and actual PASS/FAIL result. Do not return expected output, suggested proof only, or hypothetical PASS shape.

2. **Hard contract rule**  
   When a prompt says fail bluntly, do not invent scope, do not broaden scope, do not mutate state (or similar), treat it literally. Do not add permissive fallback behavior unless the prompt explicitly authorizes it.

3. **Timestamp rule**  
   If any doc or registry surface is touched: refresh the timestamp, never move timestamps backward, and keep all touched live docs aligned to the current hardening date.

---

## Template 1 — Documentation alignment pass

### Use when
- Live truth changed and docs need to catch up.
- A task proof status changed.
- A script moved from planned to live.
- A doc is stale or overclaiming.

### Template

```text
Update documentation/state surfaces only for the live Jarvis rebuild workspace.

This is a documentation alignment task only.
Do NOT modify Python logic.
Do NOT modify WCS app code.
Do NOT rewrite architecture broadly.
Be surgical and accurate.

Primary source of truth:
- current live workspace state
- current handoff bundle / anchor / live process docs

What changed in live truth:
- [INSERT LIVE TRUTH CHANGES]

Files to update:
- [INSERT FILE LIST]

Rules:
- Every touched file must get a refreshed timestamp.
- Keep wording tight and operational.
- Do not overclaim beyond what is actually proven.
- Correct stale or misleading wording.
- Preserve historical context only where it is still useful.

Specific corrections required:
- [INSERT REQUIRED CORRECTIONS BY FILE]

Return at the end:
1. files changed
2. exact corrections made in each
3. any files intentionally left unchanged and why
4. confirmation that every touched file had its timestamp refreshed
```

---

## Template 2 — New hardening script build

### Use when
- Adding a new validator, gate, helper, or bounded script.
- Hardening the current task loop.

### Template

```text
Build the next hardening script for the live Jarvis rebuild.

This is a code + doc update task.
Do not redesign the architecture.
Do not touch WCS app code.
Do not mutate backlog or other state during validation unless explicitly required.
Keep it boring, local-first, and bounded.

Source of truth:
- current live handoff bundle
- current live docs already in the workspace

Deliverables:
1. Create:
- [INSERT SCRIPT PATH]

2. Update docs/registry with refreshed timestamps:
- [INSERT DOC/REGISTRY FILES]

3. Follow the style/CLI/output conventions of existing validators/gates where possible.

Required behavior:
- [INSERT REQUIRED BEHAVIOR]

Required CLI:
- [INSERT CLI CONTRACT]

Output contract:
- [INSERT PASS/FAIL SHAPE]

Safety / boundedness rules:
- [INSERT READ-ONLY OR SAFE BEHAVIOR RULES]

Documentation updates required:
- [INSERT DOC CHANGES]

Return:
1. files changed
2. concise explanation of what the new script validates or does
3. exact commands to run for a local proof
4. assumptions or edge cases handled
5. whether the docs were updated to reflect the new live state
```

---

## Template 3 — Existing script hardening/refactor pass

### Use when
- Tightening an existing Jarvis script.
- Improving guardrails without changing the broader architecture.
- Fixing contract drift or adding stricter validation.

### Template

```text
Harden an existing Jarvis script without broad redesign.

Scope:
- target script: [INSERT SCRIPT PATH]

This is a bounded hardening/refactor task.
Do not redesign the system.
Do not add unrelated features.
Do not modify WCS app code.
Keep the script’s role intact.

Source of truth:
- current live workspace state
- current handoff bundle / process docs

Required improvements:
- [INSERT HARDENING GOALS]

Rules:
- preserve existing valid contract behavior unless explicitly changing it
- prefer smaller changes over broad rewrites
- keep CLI/output style consistent with nearby scripts
- update docs/registry only if behavior or contract changed
- refresh timestamps on touched docs

Return:
1. files changed
2. exact hardening changes made
3. any contract changes introduced
4. local proof commands
5. any risks or edge cases to watch
```

---

## Template 4 — WCS task implementation prompt

### Use when
- Cursor is acting as the worker for a bounded WCS task.
- A task packet already exists.

### Template

```text
Implement the assigned WCS task in a bounded way.

Task:
- [INSERT TASK ID]

Source of truth:
- task packet
- current repo state
- existing code patterns in the WCS repo

Rules:
- do only the assigned task
- do not broaden scope
- do not refactor unrelated files
- preserve current architecture unless the task explicitly requires otherwise
- keep changes bounded to expected task file scope
- do not claim QA was run unless it was actually run

Required output:
1. files changed
2. concise summary of implementation
3. any assumptions made
4. any issues/blockers encountered
5. any follow-up concerns that should become a separate task instead of being folded into this one
```

---

## Template 5 — QA or defect follow-up task creation

### Use when
- A real failure needs to become a new backlog task.
- QA uncovered a separate issue that should not be folded into the current task.

### Template

```text
Create a clean follow-up task proposal from the failure evidence below.

This is a task-definition/doc task only.
Do not modify code.
Do not fix the issue directly.

Evidence:
- [INSERT FAILURE OUTPUT / CONTEXT]

Goal:
Produce a bounded follow-up task that can enter the Jarvis backlog cleanly.

Include:
- task title
- task intent
- likely scope/files
- why this should be separate from the current task
- suggested acceptance criteria
- risks / unknowns

Rules:
- keep it narrow
- do not merge multiple problems into one task unless clearly connected
- do not invent implementation details without evidence

Return:
1. proposed task title
2. proposed task summary
3. suggested file scope
4. suggested acceptance criteria
5. any unknowns needing later validation
```

---

## Template 6 — QA failure triage analysis

### Use when
- QA failed and you want Cursor to classify the failure without lying about status.
- You want a bounded next-step recommendation.

### Template

```text
Analyze this QA failure and classify it without rewriting reality.

This is an analysis task only.
Do not modify code.
Do not rewrite result files.
Do not turn a failure into a pass.

Failure evidence:
- [INSERT QA OUTPUT]

Classify the failure as one of:
- environment/setup failure
- test harness failure
- application regression
- ambiguous / needs more evidence

Return:
1. likely failure class
2. probable root cause
3. confidence level (high / medium / low)
4. bounded next action
5. whether a follow-up backlog task is warranted
6. if a task is warranted, a concise suggested task title
```

---

## Template 7 — Branch-safe doc update pass

### Use when
- You want docs updated without Cursor touching code.
- You need a low-risk housekeeping pass.

### Template

```text
Update documentation only in this workspace.

Do not edit Python files.
Do not edit WCS app code.
Do not edit task/result JSON unless explicitly listed.

Source of truth:
- [INSERT LIVE SOURCE]

Files allowed to change:
- [INSERT ALLOWED FILES]

Required updates:
- [INSERT DOC UPDATES]

Rules:
- no scope creep
- refresh timestamps on every touched file
- preserve existing formatting patterns where practical

Return:
1. files changed
2. exact doc changes made
3. any stale docs found but left untouched
```

---

## Template 8 — Proof-summary request after a successful loop

### Use when
- A task completed a meaningful proof path.
- You want Cursor to update docs or write a concise status summary.

### Template

```text
Use the successful task evidence below to update proof/status documentation.

Evidence:
- [INSERT TERMINAL OUTPUTS / RESULT SUMMARY]

Goal:
Update the approved live docs so proof status matches reality.

Rules:
- do not overclaim
- distinguish partial proof from full completed/reconciled loop proof
- refresh timestamps on every touched file

Return:
1. files changed
2. what proof status changed
3. exact wording updates made
4. anything intentionally left unchanged and why
```

---

## Recommended standard sections for future templates

Use this section order whenever practical:

1. Purpose / task type
2. Scope boundaries
3. Source of truth
4. Required deliverables
5. Rules / non-goals
6. Specific required changes
7. Output format required from Cursor

This keeps prompts consistent and makes it easier to spot when Cursor ignored something.

---

## Next templates to add later

Add more only when they become recurring enough to justify standardization:

- backlog/task packet generation prompt
- reconcile/review prompt
- new chat handoff/context-anchor prompt
- QA reliability hardening prompt
- agent/module spec drafting prompt

