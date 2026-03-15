# JARVIS PATHFINDER REVIEW BUNDLE

## 1. Bundle Metadata

- Generated timestamp: 2026-03-14T18:44:23-05:00
- Branch: `main`
- Purpose: Aggregate the exact current Jarvis files and real example artifacts needed for Pathfinder contract-pack planning/review against the live implementation.
- Note: This bundle is for Pathfinder contract-pack planning only, not activation.

## 2. Live Example Artifacts (highest priority)

### WCS-043_task.json

- Exact path: `C:\dev\jarvis-workspace\tasks\WCS-043_task.json`
- Status: active
- Short purpose: Real current task packet JSON example from the completed WCS-043 loop.
- Note: Most recent real current task packet JSON example.

```json
{
  "task_id": "WCS-043",
  "project": "WCS",
  "title": "Fake test: add visible TEST: prefix to drills page heading",
  "bucket": "ugly",
  "priority": "P3",
  "risk": "low",
  "status": "done",
  "repo_path": "C:\\dev\\wcsv2.0-new",
  "branch_name": "jarvis-task-wcs-043",
  "problem_summary": "Fake test: add visible TEST: prefix to drills page heading.",
  "goal": "Resolve: Fake test: add visible TEST: prefix to drills page heading, with the smallest safe change that satisfies QA.",
  "suspected_files": [
    "src/app/drills/page.tsx"
  ],
  "acceptance_criteria": [
    "The scoped issue is resolved: Fake test: add visible TEST: prefix to drills page heading",
    "App builds successfully with npm run build",
    "Local app can be opened for verification",
    "Targeted change is visible or behaves correctly on the relevant page/flow",
    "Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated"
  ],
  "qa_plan": [
    "Run npm run build",
    "Start local app with npm run dev",
    "Run Playwright smoke QA if available",
    "Verify the targeted change locally in the browser"
  ],
  "system_impact": "Low risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: src/app/drills/page.tsx.",
  "stop_conditions": [
    "Required file cannot be found",
    "Build fails for unrelated reasons",
    "Task scope expands beyond the targeted fix"
  ],
  "notes": "src/app/drills/page.tsx",
  "created_at": "2026-03-14T18:01:23-05:00",
  "updated_at": "2026-03-14T18:25:38-05:00"
}
```

### WCS-043_worker_result.json

- Exact path: `C:\dev\jarvis-workspace\results\WCS-043_worker_result.json`
- Status: active
- Short purpose: Real current worker result JSON example from the completed WCS-043 loop.
- Note: Most recent real current worker result JSON example.

```json
{
  "task_id": "WCS-043",
  "status": "worker_complete",
  "executor": "cursor_agent",
  "summary": "Implemented bounded changes for WCS-043 in src/app/drills/page.tsx on branch jarvis-task-wcs-043.",
  "files_changed": [
    "src/app/drills/page.tsx"
  ],
  "commands_run": [
    "Implemented bounded TEST: heading change in src/app/drills/page.tsx on task branch jarvis-task-wcs-043"
  ],
  "issues_encountered": [],
  "notes": "Evidence from head_commit. Drafted by script; operator should review before post-worker.",
  "completed_at": "2026-03-14T18:10:52-05:00"
}
```

### WCS-043_qa_result.json

- Exact path: `C:\dev\jarvis-workspace\qa\WCS-043_qa_result.json`
- Status: active
- Short purpose: Real current QA result JSON example from the completed WCS-043 loop.
- Note: Most recent real current QA result JSON example.

```json
{
  "task_id": "WCS-043",
  "status": "qa_pass",
  "qa_tool": "manual operator QA via Next build and Playwright smoke and manual browser verification",
  "summary": "Build passed, Playwright smoke passed, manual verification passed for the targeted change.",
  "checks_run": [
    "npm run build",
    "npm run test:e2e:smoke",
    "Manual browser verification of /drills confirmed visible TEST: Practice Drills heading on localhost:3000"
  ],
  "checks_passed": [
    "npm run build",
    "npm run test:e2e:smoke",
    "Manual browser verification of /drills confirmed visible TEST: Practice Drills heading on localhost:3000"
  ],
  "checks_failed": [],
  "artifacts": [],
  "notes": "Drafted by script from CLI evidence. Operator should review before guarded post-worker flow.",
  "completed_at": "2026-03-14T18:10:52-05:00"
}
```

### WCS-043_cursor_handoff.md

- Exact path: `C:\dev\jarvis-workspace\scratch\cursor_handoffs\WCS-043_cursor_handoff.md`
- Status: active
- Short purpose: Real current bounded Cursor handoff generated for WCS-043.
- Note: Most recent real current Cursor handoff output.

````md
# Cursor handoff: WCS-043

## Task
- **ID:** WCS-043
- **Title:** Fake test: add visible TEST: prefix to drills page heading
- **Summary:** Fake test: add visible TEST: prefix to drills page heading.
- **Goal:** Resolve: Fake test: add visible TEST: prefix to drills page heading, with the smallest safe change that satisfies QA.

## Expected file scope
- src/app/drills/page.tsx

## Branch context
- **Expected branch:** jarvis-task-wcs-043
- **Current branch:** jarvis-task-wcs-043

## Acceptance criteria
- The scoped issue is resolved: Fake test: add visible TEST: prefix to drills page heading
- App builds successfully with npm run build
- Local app can be opened for verification
- Targeted change is visible or behaves correctly on the relevant page/flow
- Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated

## Stop conditions / constraints
- Required file cannot be found
- Build fails for unrelated reasons
- Task scope expands beyond the targeted fix

## System impact
Low risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: src/app/drills/page.tsx.

---

## Cursor implementation prompt

Implement the assigned WCS task in a bounded way.

**Task:** WCS-043

**Source of truth:**
- This handoff and the task packet
- Current repo state and existing code patterns in the WCS repo

**Rules:**
- Do only the assigned task; do not broaden scope.
- Do not refactor unrelated files.
- Preserve current architecture unless the task explicitly requires otherwise.
- Keep changes bounded to the expected file scope above.
- Do not claim QA was run unless it was actually run; do not fabricate status or evidence.

**Required output from Cursor:**
1. Files changed
2. Concise implementation summary
3. Assumptions made
4. Blockers/issues encountered (if any)
5. Follow-up concerns that should be separate tasks (if any)

Do not pad with theory or broad redesign. Be surgical and bounded.
````

### WCS-043_task_cycle_summary.md

- Exact path: `C:\dev\jarvis-workspace\scratch\task_cycle_summaries\WCS-043_task_cycle_summary.md`
- Status: active
- Short purpose: Real current human-readable task cycle summary generated for WCS-043.
- Note: Most recent real current task cycle summary output.

````md
# Task cycle summary: WCS-043

## Task
- **ID:** WCS-043
- **Title:** Fake test: add visible TEST: prefix to drills page heading
- **Goal/summary:** Resolve: Fake test: add visible TEST: prefix to drills page heading, with the smallest safe change that satisfies QA.

## Branch context
- **Expected branch:** jarvis-task-wcs-043
- **Current branch:** jarvis-task-wcs-043

## Evidence presence
- **Task packet JSON:** yes
- **Task packet markdown:** yes
- **Worker result JSON:** yes
- **QA result JSON:** yes

## Worker result
- **Status:** worker_complete
- **Completed at:** 2026-03-14T18:10:52-05:00

## QA result
- **Status:** qa_pass
- **Completed at:** 2026-03-14T18:10:52-05:00

## Cycle assessment
Worker and QA results present with completed timestamps; task appears fully cycled based on current artifacts.

## Next likely step
Next likely step: confirm backlog/reconcile state reflects this completed cycle.

## Notes
- Worker summary: Implemented bounded changes for WCS-043 in src/app/drills/page.tsx on branch jarvis-task-wcs-043.
- QA summary: Build passed, Playwright smoke passed, manual verification passed for the targeted change.
````

## 3. Current Contract / Flow Scripts

### run_guarded_task_cycle.py

- Exact path: `C:\dev\jarvis-workspace\scripts\run_guarded_task_cycle.py`
- Status: active
- Short purpose: Workflow/orchestration helper for guarded WCS task cycles; optional worker and QA drafting in post_worker/full

```python
"""
Run a guarded WCS task cycle for a single task.
Orchestrates existing helpers; stops immediately on the first failure.
Does not execute worker code, run QA directly, or invent new task logic.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a guarded WCS task cycle by orchestrating existing helpers. "
            "Stops immediately on first failure."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-019")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre_worker", "post_worker", "full"],
        default="post_worker",
        help="Cycle mode: pre_worker, post_worker, or full (default: post_worker).",
    )
    parser.add_argument(
        "--draft-worker-result",
        action="store_true",
        help="Optional: run draft_worker_result_from_evidence.py with --write before worker validation (post_worker/full only).",
    )
    parser.add_argument(
        "--worker-command",
        action="append",
        default=[],
        metavar="TEXT",
        help="Worker evidence: repeatable truthful command/step text (used only with --draft-worker-result).",
    )
    parser.add_argument(
        "--worker-executor",
        metavar="TEXT",
        help="Optional worker executor label passthrough (used only with --draft-worker-result).",
    )
    parser.add_argument(
        "--draft-qa-result",
        action="store_true",
        help="Optional: run draft_qa_result_from_evidence.py with --write before QA validation (post_worker/full only).",
    )
    parser.add_argument(
        "--build-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: build outcome (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--smoke-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: smoke outcome (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--manual-status",
        choices=["pass", "fail", "skip", "unknown"],
        help="QA evidence: manual verification outcome (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--manual-check",
        action="append",
        default=[],
        metavar="TEXT",
        help="QA evidence: repeatable manual check description (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        metavar="PATH",
        help="QA evidence: repeatable artifact path (used only with --draft-qa-result).",
    )
    parser.add_argument(
        "--qa-note",
        action="append",
        default=[],
        metavar="TEXT",
        help="QA evidence: repeatable note line (used only with --draft-qa-result).",
    )
    return parser.parse_args()


def normalize_task_id(raw: str) -> str:
    t = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_step(
    name: str,
    cmd: List[str],
    cwd: Path,
) -> Tuple[bool, str]:
    """Run a single orchestration step. Return (ok, output_text)."""
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )
    combined = ""
    if proc.stdout:
        combined += proc.stdout
    if proc.stderr:
        if combined:
            combined += "\n"
        combined += proc.stderr
    ok = proc.returncode == 0
    return ok, combined.strip()


def task_paths(workspace: Path, task_id: str) -> Dict[str, Path]:
    return {
        "packet_json": workspace / "tasks" / f"{task_id}_task.json",
        "worker_result": workspace / "results" / f"{task_id}_worker_result.json",
        "qa_result": workspace / "qa" / f"{task_id}_qa_result.json",
    }


def ensure_workspace_and_packet(workspace: Path, task_id: str) -> Optional[str]:
    if not workspace.exists():
        return "Workspace path does not exist."
    paths = task_paths(workspace, task_id)
    if not paths["packet_json"].is_file():
        return f"Task packet not found: {paths['packet_json']}"
    try:
        data = read_json(paths["packet_json"])
    except Exception as e:  # noqa: BLE001
        return f"Could not read or parse task packet: {e}"
    if not isinstance(data, Dict):
        return "Task packet root must be an object."
    return None


def build_pre_worker_steps(
    workspace: Path,
    task_id: str,
) -> List[Tuple[str, List[str]]]:
    scripts_dir = workspace / "scripts"
    py = sys.executable
    steps: List[Tuple[str, List[str]]] = []

    steps.append(
        (
            "prepare_wcs_task_branch",
            [
                py,
                str(scripts_dir / "prepare_wcs_task_branch.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "build_cursor_handoff",
            [
                py,
                str(scripts_dir / "build_cursor_handoff.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "build_task_cycle_summary",
            [
                py,
                str(scripts_dir / "build_task_cycle_summary.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    return steps


def build_draft_qa_result_cmd(
    workspace: Path,
    task_id: str,
    args: argparse.Namespace,
) -> List[str]:
    """Build command line for draft_qa_result_from_evidence.py with --write and QA evidence passthrough."""
    scripts_dir = workspace / "scripts"
    py = sys.executable
    cmd: List[str] = [
        py,
        str(scripts_dir / "draft_qa_result_from_evidence.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
        "--write",
    ]
    if args.build_status is not None:
        cmd.extend(["--build-status", args.build_status])
    if args.smoke_status is not None:
        cmd.extend(["--smoke-status", args.smoke_status])
    if args.manual_status is not None:
        cmd.extend(["--manual-status", args.manual_status])
    for v in args.manual_check or []:
        cmd.extend(["--manual-check", v])
    for v in args.artifact or []:
        cmd.extend(["--artifact", v])
    for v in args.qa_note or []:
        cmd.extend(["--note", v])
    return cmd


def build_draft_worker_result_cmd(
    workspace: Path,
    task_id: str,
    args: argparse.Namespace,
) -> List[str]:
    """Build command line for draft_worker_result_from_evidence.py with --write and worker evidence passthrough."""
    scripts_dir = workspace / "scripts"
    py = sys.executable
    cmd: List[str] = [
        py,
        str(scripts_dir / "draft_worker_result_from_evidence.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
        "--write",
    ]
    if args.worker_executor is not None:
        cmd.extend(["--executor", args.worker_executor])
    for v in args.worker_command or []:
        cmd.extend(["--command", v])
    return cmd


def build_post_worker_steps(
    workspace: Path,
    task_id: str,
    draft_worker_result: bool = False,
    draft_worker_args: Optional[argparse.Namespace] = None,
    draft_qa_result: bool = False,
    draft_qa_args: Optional[argparse.Namespace] = None,
) -> List[Tuple[str, List[str]]]:
    scripts_dir = workspace / "scripts"
    py = sys.executable
    paths = task_paths(workspace, task_id)

    worker_path = paths["worker_result"]
    qa_path = paths["qa_result"]

    steps: List[Tuple[str, List[str]]] = []

    steps.append(
        (
            "worker_change_check",
            [
                py,
                str(scripts_dir / "worker_change_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "commit_gate_check",
            [
                py,
                str(scripts_dir / "commit_gate_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    if draft_worker_result and draft_worker_args is not None:
        steps.append(
            (
                "draft_worker_result_from_evidence",
                build_draft_worker_result_cmd(workspace, task_id, draft_worker_args),
            )
        )
    steps.append(
        (
            "worker_result_validate_pre_stamp",
            [
                py,
                str(scripts_dir / "worker_result_validate.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
                "--mode",
                "pre-stamp",
            ],
        )
    )
    if draft_qa_result and draft_qa_args is not None:
        steps.append(
            (
                "draft_qa_result_from_evidence",
                build_draft_qa_result_cmd(workspace, task_id, draft_qa_args),
            )
        )
    steps.append(
        (
            "qa_result_validate_pre_stamp",
            [
                py,
                str(scripts_dir / "qa_result_validate.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
                "--mode",
                "pre-stamp",
            ],
        )
    )
    steps.append(
        (
            "stamp_guard_check",
            [
                py,
                str(scripts_dir / "stamp_guard_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )

    steps.append(
        (
            "stamp_worker_result",
            [
                py,
                str(scripts_dir / "stamp_result_timestamp.py"),
                str(worker_path),
            ],
        )
    )
    steps.append(
        (
            "stamp_qa_result",
            [
                py,
                str(scripts_dir / "stamp_result_timestamp.py"),
                str(qa_path),
            ],
        )
    )
    steps.append(
        (
            "pre_reconcile_check",
            [
                py,
                str(scripts_dir / "pre_reconcile_check.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "reconcile_task_outcome",
            [
                py,
                str(scripts_dir / "reconcile_task_outcome.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "post_reconcile_validate",
            [
                py,
                str(scripts_dir / "post_reconcile_validate.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )
    steps.append(
        (
            "build_task_cycle_summary",
            [
                py,
                str(scripts_dir / "build_task_cycle_summary.py"),
                "--task",
                task_id,
                "--workspace",
                str(workspace),
            ],
        )
    )

    return steps


def run_steps_sequence(
    workspace: Path,
    task_id: str,
    mode: str,
    steps: List[Tuple[str, List[str]]],
) -> int:
    print("RUN GUARDED TASK CYCLE: START")
    print(f"Task: {task_id}")
    print(f"Mode: {mode}")
    print(f"Workspace: {workspace}")
    print("")

    executed: List[str] = []

    for name, cmd in steps:
        print(f"Running step: {name}")
        print(f"Command: {' '.join(cmd)}")
        ok, output = run_step(name, cmd, cwd=workspace)
        executed.append(name)
        if output:
            print("--- step output begin ---")
            print(output)
            print("--- step output end ---")
        if not ok:
            print("")
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(f"Failed step: {name}")
            print(f"Failed command: {' '.join(cmd)}")
            return 1
        print(f"Step {name}: PASS")
        print("")

    print("RUN GUARDED TASK CYCLE: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {mode}")
    print(f"Workspace: {workspace}")
    if executed:
        print("Steps run (in order):")
        for name in executed:
            print(f"- {name} (PASS)")
    return 0


def main() -> int:
    args = parse_args()

    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("RUN GUARDED TASK CYCLE: FAIL")
        print(f"Task: {args.task!r}")
        print(f"Mode: {args.mode}")
        print(f"Workspace: {args.workspace or '(default)'}")
        print(f"Reason: {e}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        workspace = Path(__file__).resolve().parent.parent

    err = ensure_workspace_and_packet(workspace, task_id)
    if err:
        print("RUN GUARDED TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print(f"Workspace: {workspace}")
        print(f"Reason: {err}")
        return 1

    paths = task_paths(workspace, task_id)

    mode = args.mode
    steps: List[Tuple[str, List[str]]] = []
    draft_worker = getattr(args, "draft_worker_result", False)
    draft_qa = getattr(args, "draft_qa_result", False)

    if mode == "pre_worker":
        steps = build_pre_worker_steps(workspace, task_id)
    elif mode == "post_worker":
        if not paths["worker_result"].is_file() and not draft_worker:
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(
                "Reason: worker result JSON must exist for post_worker mode (or use --draft-worker-result to create it from evidence)."
            )
            return 1
        if not paths["qa_result"].is_file() and not draft_qa:
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(
                "Reason: QA result JSON must exist for post_worker mode (or use --draft-qa-result to create it from evidence)."
            )
            return 1
        steps = build_post_worker_steps(
            workspace,
            task_id,
            draft_worker_result=draft_worker,
            draft_worker_args=args if draft_worker else None,
            draft_qa_result=draft_qa,
            draft_qa_args=args if draft_qa else None,
        )
    elif mode == "full":
        pre = build_pre_worker_steps(workspace, task_id)
        steps.extend(pre)
        if not paths["worker_result"].is_file() and not draft_worker:
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(
                "Reason: worker result JSON must exist for post-worker steps in full mode (or use --draft-worker-result to create it from evidence)."
            )
            return 1
        if not paths["qa_result"].is_file() and not draft_qa:
            print("RUN GUARDED TASK CYCLE: FAIL")
            print(f"Task: {task_id}")
            print(f"Mode: {mode}")
            print(f"Workspace: {workspace}")
            print(
                "Reason: QA result JSON must exist for post-worker steps in full mode (or use --draft-qa-result to create it from evidence)."
            )
            return 1
        post = build_post_worker_steps(
            workspace,
            task_id,
            draft_worker_result=draft_worker,
            draft_worker_args=args if draft_worker else None,
            draft_qa_result=draft_qa,
            draft_qa_args=args if draft_qa else None,
        )
        steps.extend(post)
    else:
        print("RUN GUARDED TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print(f"Workspace: {workspace}")
        print("Reason: unsupported mode.")
        return 1

    return run_steps_sequence(workspace, task_id, mode, steps)


if __name__ == "__main__":
    raise SystemExit(main())
```

### run_cursor_worker.py

- Exact path: `C:\dev\jarvis-workspace\scripts\run_cursor_worker.py`
- Status: active
- Short purpose: Agent-first Cursor execution bridge for the current WCS worker surface; prefers agent CLI, then cursor launcher

```python
"""
Cursor worker execution wrapper for the Jarvis WCS task loop.
Prefers the real Cursor Agent CLI when available; falls back to the desktop cursor launcher.
Attempts to run the generated Cursor handoff; fails or blocks clearly if execution is unavailable.
Does not fabricate worker completion. Bridge between pre-worker prep and post-worker validation.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Worker execution wrapper: attempt to run the generated Cursor handoff for a WCS task. "
            "Fails or blocks clearly if Cursor execution is not available in this environment."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-040")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--handoff",
        help=(
            "Path to handoff markdown file. "
            "Default: scratch/cursor_handoffs/<task>_cursor_handoff.md"
        ),
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    t = normalize_text(raw).upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_git(repo_path: Path, args: List[str]) -> Tuple[int, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(repo_path),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=10,
    )
    out = (proc.stdout or "").strip()
    if proc.stderr:
        out = f"{out}\n{proc.stderr.strip()}" if out else proc.stderr.strip()
    return proc.returncode, out


def main() -> int:
    args = parse_args()

    try:
        task_id = validate_task_id(args.task)
    except ValueError as e:
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {normalize_text(args.task).upper() or '(missing)'}")
        print("Reason: Invalid task id.")
        print(f"Detail: {e}")
        return 1

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent
    if not workspace.exists():
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Workspace path does not exist.")
        return 1

    handoff_path: Path
    if args.handoff:
        handoff_path = Path(args.handoff).resolve()
    else:
        handoff_path = workspace / "scratch" / "cursor_handoffs" / f"{task_id}_cursor_handoff.md"

    if not handoff_path.is_file():
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print(f"Handoff path: {handoff_path}")
        print("Reason: Handoff file does not exist.")
        return 1

    task_packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not task_packet_path.is_file():
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Task packet does not exist.")
        print(f"Expected: {task_packet_path}")
        return 1

    try:
        packet = read_json(task_packet_path)
    except Exception as e:
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Reason: Could not read task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet must be a JSON object.")
        return 1

    expected_branch = normalize_text(packet.get("branch_name") or "")
    if not expected_branch:
        expected_branch = f"jarvis-task-{task_id.lower()}"

    raw_repo = normalize_text(packet.get("repo_path") or "")
    if not raw_repo:
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Task packet has no repo_path. Execution requires a valid task repo workspace.")
        print(f"Expected: repo_path in {task_packet_path}")
        return 1
    repo_path = Path(raw_repo).resolve()
    if not repo_path.exists():
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print(f"Repo path from packet: {repo_path}")
        print("Reason: Task repo path does not exist.")
        return 1
    if not repo_path.is_dir():
        print("RUN CURSOR WORKER: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print(f"Repo path from packet: {repo_path}")
        print("Reason: Task repo path is not a directory.")
        return 1

    current_branch: Optional[str] = None
    try:
        code, out = run_git(repo_path, ["branch", "--show-current"])
        if code == 0 and out:
            current_branch = out.strip()
    except Exception:
        pass

    agent_cmd = _find_agent_cli()
    if agent_cmd is not None:
        return _run_via_agent(
            agent_cmd=agent_cmd,
            workspace=workspace,
            handoff_path=handoff_path,
            task_id=task_id,
            expected_branch=expected_branch,
            current_branch=current_branch,
            repo_path=repo_path,
        )
    cursor_cmd = _find_cursor_cli()
    if cursor_cmd is not None:
        return _run_via_cursor_launcher(
            cursor_cmd=cursor_cmd,
            workspace=workspace,
            handoff_path=handoff_path,
            task_id=task_id,
            expected_branch=expected_branch,
            current_branch=current_branch,
            repo_path=repo_path,
        )
    print("RUN CURSOR WORKER: BLOCKED")
    print(f"Task: {task_id}")
    print(f"Jarvis workspace: {workspace}")
    print(f"Task repo workspace: {repo_path}")
    print(f"Handoff path: {handoff_path}")
    print("Reason: Cursor execution is not available in the current environment.")
    print("Detail: Neither 'agent' CLI nor 'cursor' launcher found on PATH. Install Cursor Agent CLI or Cursor CLI, or run the handoff manually in the IDE.")
    print("Worker result: not written (no execution performed).")
    return 2


def _run_via_agent(
    agent_cmd: str,
    workspace: Path,
    handoff_path: Path,
    task_id: str,
    expected_branch: str,
    current_branch: Optional[str],
    repo_path: Path,
) -> int:
    """Run handoff via real Cursor Agent CLI (agent --print --workspace <repo_path> --trust ...)."""
    # Prefer passing handoff content directly when small enough (Windows cmd limit ~8191)
    max_prompt_chars = 6000
    try:
        content = handoff_path.read_text(encoding="utf-8")
        if len(content) <= max_prompt_chars:
            prompt = content
        else:
            prompt = (
                f"Read and execute the 'Cursor implementation prompt' section from the handoff file at: {handoff_path}. "
                "Implement the WCS task described there; stay bounded to the expected file scope and rules in the handoff."
            )
    except OSError:
        prompt = (
            f"Read and execute the 'Cursor implementation prompt' section from the handoff file at: {handoff_path}. "
            "Implement the WCS task described there; stay bounded to the expected file scope and rules in the handoff."
        )
    args = [
        agent_cmd,
        "--print",
        "--workspace", str(repo_path),
        "--trust",
        prompt,
    ]
    timeout_seconds = 600
    try:
        proc = subprocess.run(
            args,
            cwd=str(repo_path),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        print("RUN CURSOR WORKER: BLOCKED")
        print(f"Task: {task_id}")
        print(f"Jarvis workspace: {workspace}")
        print(f"Task repo workspace: {repo_path}")
        print(f"Handoff path: {handoff_path}")
        print("Reason: Real Agent CLI did not finish within timeout.")
        print(f"Detail: agent command timed out after {timeout_seconds}s.")
        print("Worker result: not written (execution did not complete).")
        return 2
    except Exception as e:
        print("RUN CURSOR WORKER: BLOCKED")
        print(f"Task: {task_id}")
        print(f"Jarvis workspace: {workspace}")
        print(f"Task repo workspace: {repo_path}")
        print(f"Handoff path: {handoff_path}")
        print("Reason: Real Agent CLI invocation failed.")
        print(f"Detail: {e}")
        print("Worker result: not written (no execution performed).")
        return 2
    if proc.returncode != 0:
        print("RUN CURSOR WORKER: BLOCKED")
        print(f"Task: {task_id}")
        print(f"Jarvis workspace: {workspace}")
        print(f"Task repo workspace: {repo_path}")
        print(f"Handoff path: {handoff_path}")
        print("Reason: Real Agent CLI returned non-zero exit code.")
        print(f"Exit code: {proc.returncode}")
        if proc.stderr:
            stderr_snippet = proc.stderr.strip()[:500]
            print(f"Stderr: {stderr_snippet}")
            if "Authentication required" in proc.stderr or "agent login" in proc.stderr:
                print("Hint: If authentication is required, run `agent login` and retry.")
        print("Worker result: not written (execution did not complete successfully).")
        return 2
    print("RUN CURSOR WORKER: PASS")
    print(f"Task: {task_id}")
    print(f"Jarvis workspace: {workspace}")
    print(f"Task repo workspace: {repo_path}")
    print(f"Handoff path: {handoff_path}")
    print("Cursor execution: Real Agent CLI attempted (exited 0).")
    print("Worker result: not written (scripted Agent does not provide completion evidence; operator must verify and finalize worker result after reviewing agent output).")
    if expected_branch:
        print(f"Expected branch: {expected_branch}")
    if current_branch:
        print(f"Current branch: {current_branch}")
    print("Summary: Handoff was passed to Cursor Agent CLI with task repo workspace. Verify task completion and run post_worker flow (e.g. run_guarded_task_cycle --mode post_worker) to finalize worker result.")
    return 0


def _run_via_cursor_launcher(
    cursor_cmd: str,
    workspace: Path,
    handoff_path: Path,
    task_id: str,
    expected_branch: str,
    current_branch: Optional[str],
    repo_path: Path,
) -> int:
    """Run handoff via desktop cursor launcher (cursor <handoff_path>); cwd is task repo."""
    proc = subprocess.run(
        [cursor_cmd, str(handoff_path)],
        cwd=str(repo_path),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    if proc.returncode != 0:
        print("RUN CURSOR WORKER: BLOCKED")
        print(f"Task: {task_id}")
        print(f"Jarvis workspace: {workspace}")
        print(f"Task repo workspace: {repo_path}")
        print(f"Handoff path: {handoff_path}")
        print("Reason: Desktop launcher process returned non-zero exit code.")
        print(f"Failed command: {cursor_cmd} {handoff_path}")
        print(f"Exit code: {proc.returncode}")
        if proc.stderr:
            print(f"Stderr: {proc.stderr.strip()[:500]}")
        print("Worker result: not written (execution did not complete successfully).")
        return 2
    print("RUN CURSOR WORKER: PASS")
    print(f"Task: {task_id}")
    print(f"Jarvis workspace: {workspace}")
    print(f"Task repo workspace: {repo_path}")
    print(f"Handoff path: {handoff_path}")
    print("Cursor execution: Desktop launcher fallback attempted (exited 0).")
    print("Worker result: not written (scripted Cursor does not provide completion evidence; operator must finalize worker result after completing the task in the IDE).")
    if expected_branch:
        print(f"Expected branch: {expected_branch}")
    if current_branch:
        print(f"Current branch: {current_branch}")
    print("Summary: Handoff was passed to Cursor. Complete the task in the IDE (task repo workspace), then run the post_worker flow (e.g. run_guarded_task_cycle --mode post_worker).")
    return 0


def _find_agent_cli() -> Optional[str]:
    """Prefer real Cursor Agent CLI when available. Uses Windows-aware detection."""
    # Try shutil.which with multiple names (works on all platforms)
    for name in ("agent", "agent.cmd", "agent.exe", "agent.bat"):
        path = shutil.which(name)
        if path:
            return path
    # On Windows, shutil.which often misses commands that work in PowerShell/cmd
    if sys.platform == "win32":
        path = _find_agent_cli_via_where()
        if path:
            return path
    return None


def _find_agent_cli_via_where() -> Optional[str]:
    """Windows fallback: use 'where agent' / 'where agent.cmd' to find first valid path."""
    for name in ("agent", "agent.cmd"):
        try:
            proc = subprocess.run(
                ["cmd", "/c", "where", name],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=5,
            )
            if proc.returncode != 0:
                continue
            for line in (proc.stdout or "").strip().splitlines():
                candidate = line.strip()
                if not candidate or candidate.upper().startswith("INFO:"):
                    continue
                if Path(candidate).exists():
                    return candidate
        except (subprocess.TimeoutExpired, OSError, ValueError):
            continue
    # PowerShell sometimes sees agent when cmd/which do not (e.g. profile PATH)
    try:
        proc = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "(Get-Command agent -ErrorAction SilentlyContinue).Source",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        if proc.returncode == 0 and proc.stdout:
            candidate = proc.stdout.strip().splitlines()[0].strip()
            if candidate and Path(candidate).exists():
                return candidate
    except (subprocess.TimeoutExpired, OSError, ValueError):
        pass
    return None


def _find_cursor_cli() -> Optional[str]:
    cursor = shutil.which("cursor")
    if cursor:
        return cursor
    cursor = shutil.which("Cursor")
    if cursor:
        return cursor
    if sys.platform == "win32":
        for name in ("cursor.cmd", "Cursor.cmd", "cursor.exe", "Cursor.exe"):
            c = shutil.which(name)
            if c:
                return c
    return None


if __name__ == "__main__":
    raise SystemExit(main())
```

### build_daily_execution_prep.py

- Exact path: `C:\dev\jarvis-workspace\scripts\build_daily_execution_prep.py`
- Status: active
- Short purpose: Workflow helper: prepares operator-facing daily execution prep package

```python
"""
Build an operator-facing daily execution prep package by chaining existing helpers.
Read-only with respect to backlog/state; writes prep markdown and helper outputs only.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare a daily execution prep package by chaining selection, handoff, and summary helpers. "
            "Does not execute tasks or mutate backlog/state."
        )
    )
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--project",
        default="WCS",
        help="Project filter for automatic selection (default: WCS).",
    )
    parser.add_argument(
        "--task",
        help="Task id to use directly (e.g. WCS-019). If omitted, select via select_next_ready_task.py.",
    )
    parser.add_argument(
        "--output",
        help=(
            "Output prep file path. Default: "
            "scratch/daily_execution_prep/<task>_daily_execution_prep.md"
        ),
    )
    return parser.parse_args()


def normalize_task_id(raw: str) -> str:
    t = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def run_helper(
    name: str,
    cmd: List[str],
    cwd: Path,
) -> Tuple[int, str]:
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )
    out = (proc.stdout or "").strip()
    if proc.stderr:
        out = out + "\n" + proc.stderr.strip() if out else proc.stderr.strip()
    return proc.returncode, out


def select_task_via_helper(workspace: Path, project: str) -> Tuple[Optional[str], int, str]:
    """
    Run select_next_ready_task.py; return (task_id_or_none, exit_code, output).
    """
    scripts_dir = workspace / "scripts"
    cmd = [
        sys.executable,
        str(scripts_dir / "select_next_ready_task.py"),
        "--workspace",
        str(workspace),
        "--project",
        project,
    ]
    code, out = run_helper("select_next_ready_task", cmd, workspace)
    task_id = None
    if code == 0:
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("Selected task id:"):
                task_id = line.split(":", 1)[1].strip().upper()
                break
    return task_id, code, out


def build_prep_content(
    task_id: str,
    title: str,
    project: str,
    expected_branch: str,
    current_branch: Optional[str],
    handoff_path: Path,
    summary_path: Path,
) -> str:
    current_branch_line = current_branch if current_branch else "(unable to resolve — check repo)"
    lines = [
        f"# Daily execution prep: {task_id}",
        "",
        f"- **Task ID:** {task_id}",
        f"- **Title:** {title or '(see task packet)'}",
        f"- **Project:** {project}",
        f"- **Expected branch:** {expected_branch}",
        f"- **Current branch:** {current_branch_line}",
        "",
        "## Generated artifacts",
        f"- **Cursor handoff:** {handoff_path}",
        f"- **Task-cycle summary:** {summary_path}",
        "",
        "## Next action",
        "1. Open the Cursor handoff file and use it as the copy/paste prompt for implementation.",
        "2. After worker implementation and commit, run post-worker guards and QA as per the task cycle.",
        "3. Use the task-cycle summary to confirm evidence and next steps.",
        "",
        "---",
        "",
        "*This prep was generated by build_daily_execution_prep.py. It prepares execution but does not execute tasks or mutate backlog/state.*",
        "",
    ]
    return "\n".join(lines)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def get_repo_path(workspace: Path) -> Optional[Path]:
    state_file = workspace / "state" / "project_status_wcs.json"
    if not state_file.is_file():
        return None
    try:
        data = read_json(state_file)
        return Path(data.get("repo_path", "")).resolve() if data.get("repo_path") else None
    except Exception:
        return None


def get_current_branch(repo_path: Path) -> Optional[str]:
    try:
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip()
    except Exception:
        pass
    return None


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace).resolve() if args.workspace else Path(__file__).resolve().parent.parent
    project = (args.project or "WCS").strip()
    task_arg = args.task.strip() if args.task else None

    if not workspace.exists():
        print("DAILY EXECUTION PREP: FAIL")
        print(f"Workspace: {workspace}")
        print(f"Project: {project}")
        print("Failed step: (validation)")
        print("Reason: Workspace path does not exist.")
        return 1

    task_id: Optional[str] = None
    task_supplied = False

    if task_arg:
        try:
            task_id = normalize_task_id(task_arg)
            task_supplied = True
        except ValueError as e:
            print("DAILY EXECUTION PREP: FAIL")
            print(f"Workspace: {workspace}")
            print(f"Project: {project}")
            print("Failed step: (validation)")
            print(f"Reason: {e}")
            return 1
    else:
        task_id, sel_code, sel_out = select_task_via_helper(workspace, project)
        if sel_code == 2:
            print("DAILY EXECUTION PREP: FAIL")
            print(f"Workspace: {workspace}")
            print(f"Project: {project}")
            print("Failed step: select_next_ready_task")
            print("Reason: No eligible task found (NO MATCH).")
            return 2
        if sel_code != 0 or not task_id:
            print("DAILY EXECUTION PREP: FAIL")
            print(f"Workspace: {workspace}")
            print(f"Project: {project}")
            print("Failed step: select_next_ready_task")
            print("Failed command: select_next_ready_task.py --workspace ... --project ...")
            print(f"Reason: Selection failed (exit {sel_code}) or could not parse selected task id.")
            return 1

    scripts_dir = workspace / "scripts"
    packet_path = workspace / "tasks" / f"{task_id}_task.json"
    packet_status = "already present"
    if not packet_path.is_file():
        gen_cmd = [
            sys.executable,
            str(scripts_dir / "generate_task_packet.py"),
            "--task",
            task_id,
            "--workspace",
            str(workspace),
        ]
        g_code, g_out = run_helper("generate_task_packet", gen_cmd, workspace)
        if g_code != 0:
            print("DAILY EXECUTION PREP: FAIL")
            print(f"Workspace: {workspace}")
            print(f"Project: {project}")
            print("Failed step: generate_task_packet")
            print(f"Failed command: {' '.join(gen_cmd)}")
            print(f"Reason: Packet generation failed (exit {g_code}).")
            return 1
        packet_status = "generated during this run"

    # Build handoff
    handoff_cmd = [
        sys.executable,
        str(scripts_dir / "build_cursor_handoff.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
    ]
    h_code, h_out = run_helper("build_cursor_handoff", handoff_cmd, workspace)
    if h_code != 0:
        print("DAILY EXECUTION PREP: FAIL")
        print(f"Workspace: {workspace}")
        print(f"Project: {project}")
        print("Failed step: build_cursor_handoff")
        print(f"Failed command: {' '.join(handoff_cmd)}")
        print(f"Reason: Handoff build failed (exit {h_code}).")
        return 1

    # Default handoff path
    handoff_path = workspace / "scratch" / "cursor_handoffs" / f"{task_id}_cursor_handoff.md"

    # Build task-cycle summary
    summary_cmd = [
        sys.executable,
        str(scripts_dir / "build_task_cycle_summary.py"),
        "--task",
        task_id,
        "--workspace",
        str(workspace),
    ]
    s_code, s_out = run_helper("build_task_cycle_summary", summary_cmd, workspace)
    if s_code != 0:
        print("DAILY EXECUTION PREP: FAIL")
        print(f"Workspace: {workspace}")
        print(f"Project: {project}")
        print("Failed step: build_task_cycle_summary")
        print(f"Failed command: {' '.join(summary_cmd)}")
        print(f"Reason: Task-cycle summary build failed (exit {s_code}).")
        return 1

    summary_path = workspace / "scratch" / "task_cycle_summaries" / f"{task_id}_task_cycle_summary.md"

    # Resolve title and branch for prep file
    title = ""
    if packet_path.is_file():
        try:
            packet = read_json(packet_path)
            if isinstance(packet, dict):
                title = (packet.get("title") or packet.get("task_id") or "").strip()
        except Exception:
            pass
    expected_branch = f"jarvis-task-{task_id.lower()}"
    repo_path = get_repo_path(workspace)
    current_branch = get_current_branch(repo_path) if repo_path and repo_path.exists() else None

    # Output prep file
    if args.output:
        prep_path = Path(args.output).resolve()
    else:
        prep_dir = workspace / "scratch" / "daily_execution_prep"
        prep_dir.mkdir(parents=True, exist_ok=True)
        prep_path = prep_dir / f"{task_id}_daily_execution_prep.md"

    content = build_prep_content(
        task_id=task_id,
        title=title,
        project=project,
        expected_branch=expected_branch,
        current_branch=current_branch,
        handoff_path=handoff_path,
        summary_path=summary_path,
    )
    try:
        prep_path.parent.mkdir(parents=True, exist_ok=True)
        prep_path.write_text(content, encoding="utf-8")
    except Exception as e:
        print("DAILY EXECUTION PREP: FAIL")
        print(f"Workspace: {workspace}")
        print(f"Project: {project}")
        print("Failed step: write prep file")
        print(f"Reason: Could not write prep file: {e}")
        return 1

    print("DAILY EXECUTION PREP: PASS")
    print(f"Workspace: {workspace}")
    print(f"Project: {project}")
    print(f"Selected task id: {task_id}")
    print(f"Task packet: {packet_status}")
    print(f"Output prep file: {prep_path}")
    print(f"Handoff file: {handoff_path}")
    print(f"Task-cycle summary: {summary_path}")
    print(f"Task selection: {'supplied explicitly (--task)' if task_supplied else 'automatic (select_next_ready_task)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### build_cursor_handoff.py

- Exact path: `C:\dev\jarvis-workspace\scripts\build_cursor_handoff.py`
- Status: active
- Short purpose: Workflow helper: builds copy/paste-ready Cursor handoff file for a WCS task

```python
"""
Build a copy/paste-ready Cursor handoff file for a selected WCS task.
Reads task packet and optional prompt templates; writes a bounded handoff markdown.
Does not execute the task, modify WCS code, or mutate backlog/state.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare a bounded Cursor handoff file for a WCS task from its task packet. "
            "Does not execute the task or mutate state."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-019")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--output",
        help="Output file path. Default: scratch/cursor_handoffs/<task>_cursor_handoff.md",
    )
    return parser.parse_args()


def normalize_task_id(raw: str) -> str:
    t = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e


def get_repo_path(packet: Dict[str, Any], workspace: Path) -> Optional[Path]:
    repo = packet.get("repo_path")
    if repo:
        return Path(repo).resolve()
    state_file = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(state_file)
        return Path(data["repo_path"]).resolve()
    except Exception:
        return None


def get_current_branch(repo_path: Path) -> Optional[str]:
    try:
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip()
    except Exception:
        pass
    return None


def derive_scope(packet: Dict[str, Any]) -> List[str]:
    """Derive expected file scope from packet. Prefer explicit list fields."""
    # Prefer structured list
    suspected = packet.get("suspected_files")
    if isinstance(suspected, list) and suspected:
        return [str(x).strip() for x in suspected if x]
    target_files = packet.get("target_files")
    if isinstance(target_files, list) and target_files:
        return [str(x).strip() for x in target_files if x]
    # Single file fields
    for key in ("target_file", "file_path", "file"):
        val = packet.get(key)
        if val and isinstance(val, str) and val.strip():
            return [val.strip()]
    # notes as last resort if it looks like a single path
    notes = packet.get("notes")
    if isinstance(notes, str) and notes.strip():
        n = notes.strip()
        if "/" in n or n.endswith(".tsx") or n.endswith(".ts") or n.endswith(".jsx") or n.endswith(".js"):
            return [n]
    return []


def build_handoff_content(
    task_id: str,
    packet: Dict[str, Any],
    scope: List[str],
    expected_branch: str,
    current_branch: Optional[str],
) -> str:
    """Build handoff markdown. scope must be non-empty (caller must validate)."""
    title = packet.get("title") or packet.get("task_id") or task_id
    goal = packet.get("goal") or packet.get("problem_summary") or ""
    summary = packet.get("problem_summary") or packet.get("summary") or goal
    acceptance = packet.get("acceptance_criteria")
    if not isinstance(acceptance, list):
        acceptance = []
    stop_conditions = packet.get("stop_conditions")
    if not isinstance(stop_conditions, list):
        stop_conditions = []
    system_impact = packet.get("system_impact") or ""

    scope_section = "\n".join(f"- {f}" for f in scope)

    current_branch_line = current_branch if current_branch else "(unable to resolve — check repo)"

    acceptance_text = "\n".join(f"- {a}" for a in acceptance) if acceptance else "- (see task packet)"
    stop_text = "\n".join(f"- {s}" for s in stop_conditions) if stop_conditions else "- (see task packet)"

    content = f"""# Cursor handoff: {task_id}

## Task
- **ID:** {task_id}
- **Title:** {title}
- **Summary:** {summary}
- **Goal:** {goal}

## Expected file scope
{scope_section}

## Branch context
- **Expected branch:** {expected_branch}
- **Current branch:** {current_branch_line}

## Acceptance criteria
{acceptance_text}

## Stop conditions / constraints
{stop_text}
"""
    if system_impact:
        content += f"\n## System impact\n{system_impact}\n"

    content += """
---

## Cursor implementation prompt

Implement the assigned WCS task in a bounded way.

**Task:** """ + task_id + """

**Source of truth:**
- This handoff and the task packet
- Current repo state and existing code patterns in the WCS repo

**Rules:**
- Do only the assigned task; do not broaden scope.
- Do not refactor unrelated files.
- Preserve current architecture unless the task explicitly requires otherwise.
- Keep changes bounded to the expected file scope above.
- Do not claim QA was run unless it was actually run; do not fabricate status or evidence.

**Required output from Cursor:**
1. Files changed
2. Concise implementation summary
3. Assumptions made
4. Blockers/issues encountered (if any)
5. Follow-up concerns that should be separate tasks (if any)

Do not pad with theory or broad redesign. Be surgical and bounded.
"""
    return content


def main() -> int:
    args = parse_args()
    failures: List[str] = []

    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        workspace = Path(__file__).resolve().parent.parent

    if not workspace.exists():
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print("- Workspace path does not exist.")
        return 1

    packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not packet_path.is_file():
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print(f"- Task packet not found: {packet_path}")
        return 1

    try:
        packet = read_json(packet_path)
    except Exception as e:
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print(f"- Could not read or parse task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print("- Task packet root must be an object.")
        return 1

    if not packet.get("title") and not packet.get("goal") and not packet.get("problem_summary"):
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print("- Task packet has no title, goal, or problem_summary; cannot build a bounded handoff.")
        return 1

    scope = derive_scope(packet)
    if not scope:
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print("- Unable to derive bounded file scope from task packet.")
        return 1

    expected_branch = f"jarvis-task-{task_id.lower()}"
    repo_path = get_repo_path(packet, workspace)
    current_branch = get_current_branch(repo_path) if repo_path and repo_path.exists() else None

    if args.output:
        out_path = Path(args.output).resolve()
    else:
        handoffs_dir = workspace / "scratch" / "cursor_handoffs"
        handoffs_dir.mkdir(parents=True, exist_ok=True)
        out_path = handoffs_dir / f"{task_id}_cursor_handoff.md"

    try:
        content = build_handoff_content(task_id, packet, scope, expected_branch, current_branch)
    except Exception as e:
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print(f"- Failed to build handoff content: {e}")
        return 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        out_path.write_text(content, encoding="utf-8")
    except Exception as e:
        print("CURSOR HANDOFF BUILD: FAIL")
        print("Failures:")
        print(f"- Could not write handoff file: {e}")
        return 1

    print("CURSOR HANDOFF BUILD: PASS")
    print(f"Task: {task_id}")
    print(f"Output: {out_path}")
    print(f"Expected branch: {expected_branch}")
    print(f"Current branch: {current_branch if current_branch else '(unable to resolve)'}")
    print("Summary: handoff includes task id, title, goal, file scope, acceptance criteria, branch context, and bounded Cursor prompt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### build_task_cycle_summary.py

- Exact path: `C:\dev\jarvis-workspace\scripts\build_task_cycle_summary.py`
- Status: active
- Short purpose: Workflow helper: builds human-readable task cycle summaries for a WCS task

```python
"""
Build a human-readable summary for a single WCS task cycle.
Reads task, worker, and QA artifacts; writes a markdown summary.
Does not execute the task, modify WCS code, or mutate backlog/state.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build a human-readable summary of a WCS task cycle from current evidence. "
            "Does not execute tasks or mutate state."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-019")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--output",
        help=(
            "Output file path. Default: "
            "scratch/task_cycle_summaries/<task>_task_cycle_summary.md"
        ),
    )
    return parser.parse_args()


def normalize_task_id(raw: str) -> str:
    t = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e


def get_repo_path(packet: Dict[str, Any], workspace: Path) -> Optional[Path]:
    repo = packet.get("repo_path")
    if repo:
        return Path(repo).resolve()
    state_file = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(state_file)
        return Path(data["repo_path"]).resolve()
    except Exception:
        return None


def get_current_branch(repo_path: Path) -> Optional[str]:
    try:
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip()
    except Exception:
        pass
    return None


def load_optional_json(path: Path, failures: List[str]) -> Optional[Dict[str, Any]]:
    if not path.is_file():
        return None
    try:
        data = read_json(path)
    except Exception as e:
        failures.append(f"Could not read or parse JSON file {path}: {e}")
        return None
    if not isinstance(data, dict):
        failures.append(f"JSON root must be an object in {path}.")
        return None
    return data


def build_cycle_assessment(
    has_worker: bool,
    has_qa: bool,
    worker_completed_at: Optional[str],
    qa_completed_at: Optional[str],
) -> str:
    if not has_worker and not has_qa:
        return "Task packet only: no worker or QA results present."
    if has_worker and not has_qa:
        if worker_completed_at:
            return (
                "Worker result present and completed; QA result not yet recorded."
            )
        return "Worker result present but appears pre-stamp (no completed_at); QA result missing."
    if has_worker and has_qa:
        if worker_completed_at and qa_completed_at:
            return (
                "Worker and QA results present with completed timestamps; "
                "task appears fully cycled based on current artifacts."
            )
        return (
            "Worker and QA results present, but at least one appears pre-stamp "
            "(missing completed_at)."
        )
    # Should not reach here, but keep a safe default.
    return "Cycle state could not be classified from current artifacts."


def infer_next_step(
    has_worker: bool,
    has_qa: bool,
    worker_completed_at: Optional[str],
    qa_completed_at: Optional[str],
) -> str:
    if not has_worker and not has_qa:
        return (
            "Next likely step: prepare a bounded worker handoff and run the worker task."
        )
    if has_worker and not has_qa:
        if worker_completed_at:
            return "Next likely step: perform QA for this task and record a QA result."
        return "Next likely step: finalize the worker implementation and then perform QA."
    if has_worker and has_qa:
        if worker_completed_at and qa_completed_at:
            return (
                "Next likely step: confirm backlog/reconcile state reflects this completed cycle."
            )
        return (
            "Next likely step: complete stamping or reconciliation steps for worker/QA results."
        )
    return "Next likely step: review artifacts manually to decide the safest next action."


def summarize_notes(text: str, max_len: int = 240) -> str:
    t = text.strip()
    if len(t) <= max_len:
        return t
    return t[: max_len - 3] + "..."


def build_summary_markdown(
    task_id: str,
    packet: Dict[str, Any],
    packet_md_present: bool,
    worker: Optional[Dict[str, Any]],
    qa: Optional[Dict[str, Any]],
    expected_branch: str,
    current_branch: Optional[str],
) -> Tuple[str, str]:
    """Return (content, evidence_summary_line)."""
    title = packet.get("title") or packet.get("task_id") or task_id
    goal = packet.get("goal") or packet.get("problem_summary") or packet.get("summary") or ""

    has_worker = worker is not None
    has_qa = qa is not None

    worker_status = worker.get("status") if worker else None
    worker_completed_at = worker.get("completed_at") if worker else None
    worker_summary = worker.get("summary") if worker else None

    qa_status = qa.get("status") if qa else None
    qa_completed_at = qa.get("completed_at") if qa else None
    qa_summary = qa.get("summary") if qa else None

    assessment = build_cycle_assessment(
        has_worker=has_worker,
        has_qa=has_qa,
        worker_completed_at=worker_completed_at,
        qa_completed_at=qa_completed_at,
    )
    next_step = infer_next_step(
        has_worker=has_worker,
        has_qa=has_qa,
        worker_completed_at=worker_completed_at,
        qa_completed_at=qa_completed_at,
    )

    current_branch_line = current_branch if current_branch else "(unable to resolve — check repo)"

    evidence_bits = []
    evidence_bits.append("task packet JSON")
    if packet_md_present:
        evidence_bits.append("task markdown")
    if has_worker:
        evidence_bits.append("worker result")
    if has_qa:
        evidence_bits.append("QA result")
    evidence_summary = ", ".join(evidence_bits)

    packet_present_text = "yes"
    worker_present_text = "yes" if has_worker else "no"
    qa_present_text = "yes" if has_qa else "no"
    packet_md_text = "yes" if packet_md_present else "no"

    content_lines = [
        f"# Task cycle summary: {task_id}",
        "",
        "## Task",
        f"- **ID:** {task_id}",
        f"- **Title:** {title}",
        f"- **Goal/summary:** {goal}" if goal else "- **Goal/summary:** (not specified)",
        "",
        "## Branch context",
        f"- **Expected branch:** {expected_branch}",
        f"- **Current branch:** {current_branch_line}",
        "",
        "## Evidence presence",
        f"- **Task packet JSON:** {packet_present_text}",
        f"- **Task packet markdown:** {packet_md_text}",
        f"- **Worker result JSON:** {worker_present_text}",
        f"- **QA result JSON:** {qa_present_text}",
        "",
        "## Worker result",
        f"- **Status:** {worker_status or '(not present)'}",
        f"- **Completed at:** {worker_completed_at or '-'}",
        "",
        "## QA result",
        f"- **Status:** {qa_status or '(not present)'}",
        f"- **Completed at:** {qa_completed_at or '-'}",
        "",
        "## Cycle assessment",
        assessment,
        "",
        "## Next likely step",
        next_step,
        "",
        "## Notes",
    ]

    if worker_summary:
        content_lines.append(
            f"- Worker summary: {summarize_notes(str(worker_summary))}"
        )
    if qa_summary:
        content_lines.append(
            f"- QA summary: {summarize_notes(str(qa_summary))}"
        )
    if not worker_summary and not qa_summary:
        content_lines.append(
            "- No worker/QA summaries available; review source artifacts if needed."
        )

    content = "\n".join(content_lines) + "\n"
    return content, evidence_summary


def main() -> int:
    args = parse_args()
    failures: List[str] = []

    try:
        task_id = normalize_task_id(args.task)
    except ValueError as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        workspace = Path(__file__).resolve().parent.parent

    if not workspace.exists():
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print("- Workspace path does not exist.")
        return 1

    tasks_dir = workspace / "tasks"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"

    packet_path = tasks_dir / f"{task_id}_task.json"
    if not packet_path.is_file():
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Task packet not found: {packet_path}")
        return 1

    try:
        packet = read_json(packet_path)
    except Exception as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Could not read or parse task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print("- Task packet root must be an object.")
        return 1

    packet_md_path = tasks_dir / f"{task_id}_task.md"
    packet_md_present = packet_md_path.is_file()

    worker_path = results_dir / f"{task_id}_worker_result.json"
    qa_path = qa_dir / f"{task_id}_qa_result.json"

    worker = load_optional_json(worker_path, failures)
    qa = load_optional_json(qa_path, failures)

    expected_branch = f"jarvis-task-{task_id.lower()}"
    repo_path = get_repo_path(packet, workspace)
    current_branch = get_current_branch(repo_path) if repo_path and repo_path.exists() else None

    if args.output:
        out_path = Path(args.output).resolve()
    else:
        summaries_dir = workspace / "scratch" / "task_cycle_summaries"
        summaries_dir.mkdir(parents=True, exist_ok=True)
        out_path = summaries_dir / f"{task_id}_task_cycle_summary.md"

    if failures:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        for f in failures:
            print(f"- {f}")
        return 1

    try:
        content, evidence_summary = build_summary_markdown(
            task_id=task_id,
            packet=packet,
            packet_md_present=packet_md_present,
            worker=worker,
            qa=qa,
            expected_branch=expected_branch,
            current_branch=current_branch,
        )
    except Exception as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Failed to build summary content: {e}")
        return 1

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
    except Exception as e:
        print("TASK CYCLE SUMMARY BUILD: FAIL")
        print("Failures:")
        print(f"- Unable to write summary file: {e}")
        return 1

    print("TASK CYCLE SUMMARY BUILD: PASS")
    print(f"Task: {task_id}")
    print(f"Output: {out_path}")
    if current_branch:
        print(f"Current branch: {current_branch}")
    else:
        print("Current branch: (unable to resolve — check repo)")
    print(f"Summary: included {evidence_summary}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### select_next_ready_task.py

- Exact path: `C:\dev\jarvis-workspace\scripts\select_next_ready_task.py`
- Status: active
- Short purpose: Read-only workflow helper: selects next eligible ready task from backlog

```python
"""
Select the next eligible ready task from the Jarvis/WCS backlog.
Read-only: does not modify backlog, daily plan, or any state.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Progression ladder (preferred when present in backlog)
EXECUTION_LANE_ORDER = {"fake_reversible": 1, "real_easy": 2, "real_investigative": 3}
TEST_PHASE_ORDER = {"phase_a": 1, "phase_b": 2, "phase_c": 3, "phase_d": 4}
# Fallback order (align with jarvis.py when ladder fields absent)
PRIORITY_ORDER = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
ELIGIBLE_BUCKETS_WCS = {"broken", "ugly"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Select the next eligible ready task from the backlog. "
            "Read-only; does not mutate state."
        )
    )
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--project",
        default="WCS",
        help="Project filter (default: WCS).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Max candidate tasks to show in ranked output (default: 10).",
    )
    return parser.parse_args()


def normalize(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def parse_task_number(task_id: str) -> int:
    t = normalize(task_id).upper()
    if not t.startswith("WCS-"):
        return 999999
    suffix = t.split("-", 1)[1]
    if not suffix.isdigit():
        return 999999
    return int(suffix)


def execution_lane_rank(task: Dict[str, Any]) -> int:
    return EXECUTION_LANE_ORDER.get(normalize(task.get("execution_lane")).lower(), 999)


def test_phase_rank(task: Dict[str, Any]) -> int:
    return TEST_PHASE_ORDER.get(normalize(task.get("test_phase")).lower(), 999)


def selector_rank_val(task: Dict[str, Any]) -> int:
    v = task.get("selector_rank")
    if v is None:
        return 999999
    try:
        return int(v)
    except (TypeError, ValueError):
        return 999999


def priority_rank(task: Dict[str, Any]) -> int:
    return PRIORITY_ORDER.get(normalize(task.get("priority")).upper(), 999)


def risk_rank(task: Dict[str, Any]) -> int:
    return RISK_ORDER.get(normalize(task.get("risk")).lower(), 999)


def sort_key(task: Dict[str, Any]) -> Tuple[int, int, int, int, int, int]:
    """Order: execution_lane, test_phase, selector_rank, then fallback priority, risk, task id."""
    return (
        execution_lane_rank(task),
        test_phase_rank(task),
        selector_rank_val(task),
        priority_rank(task),
        risk_rank(task),
        parse_task_number(normalize(task.get("task_id", ""))),
    )


def is_eligible(task: Any, project: str) -> bool:
    if not isinstance(task, dict):
        return False
    proj = normalize(task.get("project")).upper()
    if proj != project.upper():
        return False
    status = normalize(task.get("status")).lower()
    if status != "ready":
        return False
    bucket = normalize(task.get("bucket")).lower()
    if project.upper() == "WCS" and bucket not in ELIGIBLE_BUCKETS_WCS:
        return False
    tid = normalize(task.get("task_id")).upper()
    if not tid.startswith("WCS-"):
        return False
    return True


def load_backlog(workspace: Path) -> List[Dict[str, Any]]:
    path = workspace / "state" / "master_backlog.json"
    if not path.is_file():
        raise FileNotFoundError(f"Backlog not found: {path}")
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"Backlog root must be a JSON array: {path}")
    return raw


def select_and_rank(
    backlog: List[Dict[str, Any]],
    project: str,
) -> Tuple[List[Dict[str, Any]], List[Tuple[Dict[str, Any], str]]]:
    """
    Return (eligible_sorted, skipped_with_reasons).
    eligible_sorted is sorted by priority, risk, task_id.
    skipped_with_reasons are ineligible tasks with a short reason (e.g. first N we considered).
    """
    eligible: List[Dict[str, Any]] = []
    skipped: List[Tuple[Dict[str, Any], str]] = []

    for task in backlog:
        if not isinstance(task, dict):
            continue
        proj = normalize(task.get("project")).upper()
        status = normalize(task.get("status")).lower()
        bucket = normalize(task.get("bucket")).lower()
        tid = normalize(task.get("task_id")).upper()

        if proj != project.upper():
            skipped.append((task, "wrong project"))
            continue
        if status != "ready":
            skipped.append((task, f"status not ready ({status})"))
            continue
        if project.upper() == "WCS" and bucket not in ELIGIBLE_BUCKETS_WCS:
            skipped.append((task, f"bucket not eligible ({bucket})"))
            continue
        if not tid.startswith("WCS-"):
            skipped.append((task, "invalid task id"))
            continue
        eligible.append(task)

    eligible.sort(key=sort_key)
    return eligible, skipped


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace).resolve() if args.workspace else Path(__file__).resolve().parent.parent
    project = normalize(args.project) or "WCS"
    limit = max(1, min(args.limit, 100))

    if not workspace.exists():
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print("- Workspace path does not exist.")
        return 1

    try:
        backlog = load_backlog(workspace)
    except FileNotFoundError as e:
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1
    except json.JSONDecodeError as e:
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print(f"- Invalid JSON in backlog: {e}")
        return 1
    except ValueError as e:
        print("SELECT NEXT READY TASK: FAIL")
        print("Failures:")
        print(f"- {e}")
        return 1

    eligible, skipped = select_and_rank(backlog, project)

    if not eligible:
        print("SELECT NEXT READY TASK: NO MATCH")
        print(f"Workspace: {workspace}")
        print(f"Project: {project}")
        if skipped:
            status_reasons = {}
            for _, reason in skipped[:20]:
                status_reasons[reason] = status_reasons.get(reason, 0) + 1
            summary = "; ".join(f"{r}: {c}" for r, c in sorted(status_reasons.items()))
            print(f"Reason: no eligible ready task. Sample skip reasons: {summary}")
        else:
            print("Reason: no tasks in backlog for this project or backlog empty.")
        return 2

    selected = eligible[0]
    task_id = normalize(selected.get("task_id")).upper()
    title = normalize(selected.get("title")) or task_id
    priority = normalize(selected.get("priority"))
    bucket = normalize(selected.get("bucket"))
    risk = normalize(selected.get("risk"))
    status = normalize(selected.get("status"))
    execution_lane = normalize(selected.get("execution_lane"))
    test_phase = normalize(selected.get("test_phase"))
    sel_rank = selected.get("selector_rank")

    print("SELECT NEXT READY TASK: PASS")
    print(f"Workspace: {workspace}")
    print(f"Project: {project}")
    print(f"Selected task id: {task_id}")
    print(f"Selected title: {title}")
    print(f"Priority: {priority}  Bucket: {bucket}  Risk: {risk}  Status: {status}")
    if execution_lane:
        print(f"Execution lane: {execution_lane}")
    if test_phase:
        print(f"Test phase: {test_phase}")
    if sel_rank is not None:
        print(f"Selector rank: {sel_rank}")
    if execution_lane or test_phase or sel_rank is not None:
        print(
            "Reason selected: first eligible ready task by progression ladder "
            "(execution_lane, test_phase, selector_rank), then fallback (priority, risk, task id)."
        )
    else:
        print(
            "Reason selected: first eligible ready task by deterministic order "
            "(priority, then risk, then task id)."
        )
    print(f"Reviewed candidate count: {len(eligible)}")
    print("")
    print("Ranked candidates (up to limit):")
    for i, t in enumerate(eligible[:limit], 1):
        tid = normalize(t.get("task_id")).upper()
        tit = normalize(t.get("title")) or tid
        pr = normalize(t.get("priority"))
        rk = normalize(t.get("risk"))
        lane = normalize(t.get("execution_lane"))
        phase = normalize(t.get("test_phase"))
        sr = t.get("selector_rank")
        extra = ""
        if lane or phase or sr is not None:
            parts = [f"lane={lane}" if lane else "", f"phase={phase}" if phase else "", f"rank={sr}" if sr is not None else ""]
            extra = "  " + " ".join(p for p in parts if p)
        print(f"  {i}. {tid}  {pr}  {rk}{extra}  {tit[:50]}{'...' if len(tit) > 50 else ''}")

    # Skipped section: show a few near-candidates or common skip reasons
    print("")
    print("Skipped (sample):")
    shown = 0
    for task, reason in skipped[:15]:
        if shown >= 8:
            break
        tid = normalize(task.get("task_id")).upper()
        st = normalize(task.get("status")).lower()
        print(f"  - {tid}: {reason}")
        shown += 1
    if not skipped:
        print("  (none; all non-ready tasks excluded from eligibility)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### prepare_wcs_task_branch.py

- Exact path: `C:\dev\jarvis-workspace\scripts\prepare_wcs_task_branch.py`
- Status: active
- Short purpose: Prepares WCS task branch for bounded task work

```python
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class BranchPrepError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BranchPrepError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BranchPrepError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def normalize_task_id(task_id: str) -> str:
    task_id = task_id.strip().upper()
    if not task_id.startswith("WCS-"):
        raise BranchPrepError(f"Expected task id like WCS-009. Got: {task_id}")
    return task_id


def target_branch_name(task_id: str) -> str:
    return f"jarvis-task-{task_id.lower()}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare the correct WCS task branch before execution."
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-009")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root. Defaults to script grandparent directory.",
    )
    parser.add_argument(
        "--repo",
        help="Override WCS repo path. If omitted, use state/project_status_wcs.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"

    task_id = normalize_task_id(args.task)
    target_branch = target_branch_name(task_id)

    if args.repo:
        repo_path = Path(args.repo).resolve()
    else:
        project_status = read_json(state_dir / "project_status_wcs.json")
        repo_path = Path(project_status["repo_path"]).resolve()

    if not repo_path.exists():
        raise BranchPrepError(f"WCS repo path does not exist: {repo_path}")

    git_dir = repo_path / ".git"
    if not git_dir.exists():
        raise BranchPrepError(f"Path is not a git repo: {repo_path}")

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise BranchPrepError(current_branch_result.stderr.strip() or "Failed to detect current branch.")

    current_branch = current_branch_result.stdout.strip()

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise BranchPrepError(status_result.stderr.strip() or "Failed to inspect repo status.")

    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    is_dirty = bool(dirty_lines)

    if current_branch == target_branch:
        mode = "already_on_target_dirty" if is_dirty else "already_on_target_clean"
        print(f"MODE: {mode}")
        print(f"CURRENT_BRANCH: {current_branch}")
        print(f"TARGET_BRANCH: {target_branch}")
        print(f"DIRTY: {'true' if is_dirty else 'false'}")
        if dirty_lines:
            print("DIRTY_FILES:")
            for line in dirty_lines:
                print(line)
        return 0

    if is_dirty:
        raise BranchPrepError(
            "Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.\n"
            f"Current branch: {current_branch}\n"
            f"Target branch: {target_branch}\n"
            "Dirty files:\n" + "\n".join(dirty_lines)
        )

    branch_exists_result = run_git(repo_path, ["branch", "--list", target_branch])
    if branch_exists_result.returncode != 0:
        raise BranchPrepError(branch_exists_result.stderr.strip() or "Failed to inspect branch list.")

    target_exists = bool(branch_exists_result.stdout.strip())

    if target_exists:
        switch_result = run_git(repo_path, ["switch", target_branch])
        if switch_result.returncode != 0:
            raise BranchPrepError(switch_result.stderr.strip() or f"Failed to switch to {target_branch}.")
        mode = "switched_to_existing_target"
    else:
        main_exists_result = run_git(repo_path, ["branch", "--list", "main"])
        if main_exists_result.returncode != 0:
            raise BranchPrepError(main_exists_result.stderr.strip() or "Failed to inspect main branch.")
        if not main_exists_result.stdout.strip():
            raise BranchPrepError("Cannot create target branch because local 'main' branch was not found.")

        create_result = run_git(repo_path, ["switch", "-c", target_branch, "main"])
        if create_result.returncode != 0:
            raise BranchPrepError(create_result.stderr.strip() or f"Failed to create {target_branch} from main.")
        mode = "created_new_target_from_main"

    print(f"MODE: {mode}")
    print(f"CURRENT_BRANCH: {current_branch}")
    print(f"TARGET_BRANCH: {target_branch}")
    print("DIRTY: false")
    print(f"REPO_PATH: {repo_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BranchPrepError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
```

### worker_change_check.py

- Exact path: `C:\dev\jarvis-workspace\scripts\worker_change_check.py`
- Status: active
- Short purpose: Read-only worker-boundary validator for changed-file scope and simple diff sanity

```python
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


class WorkerChangeError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise WorkerChangeError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerChangeError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker change boundary check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerChangeError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerChangeError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path, failures: List[str]) -> Set[str]:
    try:
        data = read_json(task_json_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return set()

    if not isinstance(data, dict):
        failures.append(f"Task packet must be a JSON object: {task_json_path}")
        return set()

    expected: Set[str] = set()

    for key in ("target_files", "suspected_files"):
        files_val = data.get(key)
        if isinstance(files_val, list):
            for item in files_val:
                path = normalize_text(item)
                if path:
                    expected.add(path.replace("\\", "/"))
            if expected:
                break

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    if not expected:
        failures.append(
            f"Unable to determine expected file scope from task packet: {task_json_path}"
        )

    return expected


def resolve_repo_path(workspace: Path, failures: List[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    raw = normalize_text(data.get("repo_path"))
    if not raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def gather_changed_files(repo_path: Path, failures: List[str]) -> Tuple[Set[str], bool]:
    """
    Return (changed_file_paths, from_head_commit).
    If working tree has changes, use those and from_head_commit=False.
    If working tree is clean, use files changed in HEAD commit and from_head_commit=True.
    """
    changed: Set[str] = set()

    status_result = run_git(repo_path, ["status", "--short"])
    if status_result.returncode != 0:
        failures.append(
            f"git status --short failed in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in status_result.stdout.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(maxsplit=1)
            if len(parts) == 2:
                changed.add(parts[1].replace("\\", "/"))

    diff_result = run_git(repo_path, ["diff", "--name-only"])
    if diff_result.returncode != 0:
        failures.append(
            f"git diff --name-only failed in {repo_path}: "
            f"{diff_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in diff_result.stdout.splitlines():
            path = normalize_text(line)
            if path:
                changed.add(path.replace("\\", "/"))

    if changed:
        return changed, False

    head_diff = run_git(repo_path, ["diff", "--name-only", "HEAD~1", "HEAD"])
    if head_diff.returncode == 0:
        for line in head_diff.stdout.splitlines():
            path = normalize_text(line)
            if path:
                changed.add(path.replace("\\", "/"))

    return changed, bool(changed)


def check_branch(repo_path: Path, task_id: str, failures: List[str]) -> Tuple[str, str | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"git branch --show-current failed in {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    return expected_branch, current_branch


def check_diff_sanity(
    repo_path: Path,
    changed_files: Set[str],
    failures: List[str],
    from_head_commit: bool = False,
) -> None:
    if len(changed_files) > 3:
        failures.append(
            f"Too many changed files for a bounded task. Expected at most 3, found {len(changed_files)}."
        )

    for path in sorted(changed_files):
        if from_head_commit:
            diff_result = run_git(repo_path, ["diff", "--unified=0", "HEAD~1", "HEAD", "--", path])
        else:
            diff_result = run_git(repo_path, ["diff", "--unified=0", "--", path])
        if diff_result.returncode != 0:
            failures.append(
                f"git diff --unified=0 failed for {path} in {repo_path}: "
                f"{diff_result.stderr.strip() or '(no stderr output)'}"
            )
            continue

        total_changes = 0
        for line in diff_result.stdout.splitlines():
            if not line:
                continue
            if line.startswith("@@"):
                continue
            if line.startswith("+++ ") or line.startswith("--- "):
                continue
            if line[0] in {"+", "-"}:
                total_changes += 1

        if total_changes > 40:
            failures.append(
                f"File {path} has too many changed lines for a bounded task. "
                f"Found {total_changes}, limit is 40."
            )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER CHANGE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerChangeError as exc:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json_path = workspace / "tasks" / f"{task_id}_task.json"
    expected_files = determine_expected_files(task_json_path, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = ""
    current_branch: str | None = None

    changed_files: Set[str] = set()
    from_head_commit = False
    if repo_path is not None:
        expected_branch, current_branch = check_branch(repo_path, task_id, failures)
        changed_files, from_head_commit = gather_changed_files(repo_path, failures)

        if not changed_files:
            failures.append(
                "No changed files detected in the WCS repo (working tree or HEAD commit)."
            )

        if expected_files:
            for path in sorted(changed_files):
                if path not in expected_files:
                    failures.append(
                        f"Changed file {path} is outside the expected task scope: {sorted(expected_files)}."
                    )

        if changed_files:
            check_diff_sanity(repo_path, changed_files, failures, from_head_commit)

    if failures:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("WORKER CHANGE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch and current_branch:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
    if expected_files:
        print(f"Expected file scope: {', '.join(sorted(expected_files))}")
    print(f"Actual changed files: {', '.join(sorted(changed_files))}")
    print("Passed checks:")
    print("- repo path and current branch resolved correctly")
    print("- changed files exist and are within expected task scope")
    print("- number of changed files is within the allowed limit")
    print("- per-file diff size is within the allowed limit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### commit_gate_check.py

- Exact path: `C:\dev\jarvis-workspace\scripts\commit_gate_check.py`
- Status: active
- Short purpose: Read-only commit-state gate for a WCS task branch and HEAD

```python
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


class CommitGateError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CommitGateError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CommitGateError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only commit-state gate for a single WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise CommitGateError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise CommitGateError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path, failures: List[str]) -> Set[str]:
    """
    Derive expected file scope from the task packet.

    Mirrors the Phase-1 logic used in worker_change_check.py:
    - prefer target_files (list)
    - then target_file / file_path / file
    - finally a notes field that looks like a single path
    """
    try:
        data = read_json(task_json_path)
    except CommitGateError as exc:
        failures.append(str(exc))
        return set()

    if not isinstance(data, dict):
        failures.append(f"Task packet must be a JSON object: {task_json_path}")
        return set()

    expected: Set[str] = set()

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    if not expected:
        failures.append(
            f"Unable to determine expected file scope from task packet: {task_json_path}"
        )

    return expected


def resolve_repo_path(workspace: Path, failures: List[str]) -> Optional[Path]:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except CommitGateError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    raw = normalize_text(data.get("repo_path"))
    if not raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def check_branch_and_head(
    repo_path: Path, task_id: str, failures: List[str]
) -> Tuple[str, Optional[str], Optional[str]]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"git branch --show-current failed in {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    head_result = run_git(repo_path, ["rev-parse", "HEAD"])
    if head_result.returncode != 0:
        failures.append(
            f"Failed to resolve HEAD in repo {repo_path}: "
            f"{head_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, current_branch, None

    head_sha = normalize_text(head_result.stdout)
    if not head_sha:
        failures.append(f"HEAD rev-parse returned empty output in repo {repo_path}.")
        head_sha = None

    return expected_branch, current_branch, head_sha


def check_ahead_of_base(
    repo_path: Path, current_branch: Optional[str], failures: List[str]
) -> Tuple[Optional[str], Optional[int]]:
    base_branch: Optional[str] = None
    for candidate in ["main", "master"]:
        rev_parse = run_git(repo_path, ["rev-parse", "--verify", candidate])
        if rev_parse.returncode == 0:
            base_branch = candidate
            break

    if base_branch is None:
        failures.append(f"Neither 'main' nor 'master' branch exists in repo {repo_path}.")
        return None, None

    ahead_result = run_git(
        repo_path,
        ["rev-list", "--count", f"{base_branch}..{current_branch or 'HEAD'}"],
    )
    if ahead_result.returncode != 0:
        failures.append(
            f"Failed to compute commits ahead of {base_branch} in {repo_path}: "
            f"{ahead_result.stderr.strip() or '(no stderr output)'}"
        )
        return base_branch, None

    ahead_str = normalize_text(ahead_result.stdout)
    try:
        ahead_count = int(ahead_str or "0")
    except ValueError:
        failures.append(
            f"Unexpected rev-list output for {base_branch}..{current_branch or 'HEAD'} "
            f"in {repo_path}: {ahead_str}"
        )
        return base_branch, None

    if ahead_count < 1:
        failures.append(
            f"Task branch must be ahead of {base_branch} by at least 1 commit. Found: {ahead_count}."
        )

    return base_branch, ahead_count


def check_worktree_clean(repo_path: Path, failures: List[str]) -> None:
    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        failures.append(
            f"Failed to inspect repo status in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
        return

    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    if dirty_lines:
        failures.append(
            f"Repo working tree is not clean in {repo_path}. "
            f"{len(dirty_lines)} changed path(s) detected after commit."
        )


def is_within_expected_scope(path: str, expected_files: Set[str]) -> bool:
    for expected in expected_files:
        if not expected:
            continue
        prefix = expected.rstrip("/")
        if path == prefix or path.startswith(prefix + "/"):
            return True
    return False


def gather_head_commit_files_and_changes(
    repo_path: Path, failures: List[str]
) -> Tuple[Set[str], Dict[str, int]]:
    """
    Inspect the HEAD commit.

    - Uses git show to list committed files.
    - Uses git diff-tree --numstat to count changed lines per file.
    """
    committed_files: Set[str] = set()
    line_counts: Dict[str, int] = {}

    show_result = run_git(repo_path, ["show", "--pretty=", "--name-only", "HEAD"])
    if show_result.returncode != 0:
        failures.append(
            f"git show --name-only HEAD failed in {repo_path}: "
            f"{show_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in show_result.stdout.splitlines():
            path = normalize_text(line)
            if path:
                norm = path.replace("\\", "/")
                committed_files.add(norm)

    numstat_result = run_git(
        repo_path, ["diff-tree", "--no-commit-id", "--numstat", "-r", "HEAD"]
    )
    if numstat_result.returncode != 0:
        failures.append(
            f"git diff-tree --numstat HEAD failed in {repo_path}: "
            f"{numstat_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in numstat_result.stdout.splitlines():
            parts = line.split("\t")
            if len(parts) != 3:
                continue
            added_raw, deleted_raw, path = parts
            path = normalize_text(path)
            if not path:
                continue
            norm_path = path.replace("\\", "/")
            try:
                added = int(added_raw) if added_raw.isdigit() else 0
                deleted = int(deleted_raw) if deleted_raw.isdigit() else 0
            except ValueError:
                continue
            total = added + deleted
            line_counts[norm_path] = total
            committed_files.add(norm_path)

    return committed_files, line_counts


def check_commit_boundedness(
    committed_files: Set[str],
    line_counts: Dict[str, int],
    expected_files: Set[str],
    failures: List[str],
) -> None:
    if not committed_files:
        failures.append("HEAD commit has no changed files.")
        return

    # Reuse Phase-1 thresholds from worker_change_check.py.
    if len(committed_files) > 3:
        failures.append(
            f"Too many committed files for a bounded task. Expected at most 3, "
            f"found {len(committed_files)}."
        )

    for path in sorted(committed_files):
        if not is_within_expected_scope(path, expected_files):
            failures.append(
                f"Committed file outside expected task scope: {path}. "
                f"Expected scope derived from task packet: {sorted(expected_files) or '(none)'}."
            )

    for path, total_changes in line_counts.items():
        if total_changes > 40:
            failures.append(
                f"File {path} has too many changed lines in HEAD for a bounded task. "
                f"Found {total_changes}, limit is 40."
            )


def check_commit_message(repo_path: Path, task_id: str, failures: List[str]) -> None:
    log_result = run_git(repo_path, ["log", "-1", "--pretty=%B"])
    if log_result.returncode != 0:
        failures.append(
            f"Failed to read HEAD commit message in {repo_path}: "
            f"{log_result.stderr.strip() or '(no stderr output)'}"
        )
        return

    message = normalize_text(log_result.stdout)
    if not message:
        failures.append("HEAD commit message is empty.")
        return

    if task_id.upper() not in message.upper():
        failures.append(
            f"HEAD commit message must contain the task id {task_id}. "
            f"Found: {message!r}."
        )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("COMMIT GATE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except CommitGateError as exc:
        print("COMMIT GATE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json_path = workspace / "tasks" / f"{task_id}_task.json"
    if not task_json_path.exists():
        failures.append(f"Missing task packet JSON: {task_json_path}")
        expected_files: Set[str] = set()
    else:
        expected_files = determine_expected_files(task_json_path, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = ""
    current_branch: Optional[str] = None
    head_sha: Optional[str] = None
    base_branch: Optional[str] = None
    ahead_count: Optional[int] = None
    committed_files: Set[str] = set()
    line_counts: Dict[str, int] = {}

    if repo_path is not None:
        expected_branch, current_branch, head_sha = check_branch_and_head(
            repo_path, task_id, failures
        )
        base_branch, ahead_count = check_ahead_of_base(
            repo_path, current_branch, failures
        )
        check_worktree_clean(repo_path, failures)
        committed_files, line_counts = gather_head_commit_files_and_changes(
            repo_path, failures
        )
        if expected_files:
            check_commit_boundedness(
                committed_files, line_counts, expected_files, failures
            )
        else:
            failures.append(
                "Unable to determine expected file scope; commit gate cannot validate "
                "that HEAD is bounded to the selected task."
            )
        check_commit_message(repo_path, task_id, failures)

    if failures:
        print("COMMIT GATE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("COMMIT GATE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None:
        print(f"Repo: {repo_path}")
    print(f"Expected branch: {expected_branch or '(unknown)'}")
    print(f"Current branch: {current_branch or '(unknown)'}")
    print(f"Base branch: {base_branch or '(none)'}")
    if ahead_count is not None:
        print(f"Commits ahead of {base_branch}: {ahead_count}")
    print(f"HEAD: {head_sha or '(unknown)'}")

    if committed_files:
        print("Committed files in HEAD:")
        for path in sorted(committed_files):
            changes = line_counts.get(path)
            if changes is not None:
                print(f"- {path} (changed lines: {changes})")
            else:
                print(f"- {path}")

    print("Checks:")
    print("- task packet exists and parses")
    print("- WCS repo path exists")
    print("- current branch matches expected task branch")
    print("- HEAD commit exists")
    print("- branch is ahead of main/master by at least 1 commit")
    print("- worktree is clean after commit")
    print("- HEAD commit message references the task id")
    print("- committed files are within expected task file scope")
    print("- committed file count and changed-line counts are within bounded thresholds")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### draft_worker_result_from_evidence.py

- Exact path: `C:\dev\jarvis-workspace\scripts\draft_worker_result_from_evidence.py`
- Status: active
- Short purpose: Draft truthful worker result JSON from task packet and repo evidence

```python
"""
Draft a truthful worker_result.json from real repo/task evidence.
Does not stamp, reconcile, or fabricate completion.
Operator should review the drafted result before guarded post-worker if appropriate.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Optional, Set, Tuple


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Draft a truthful worker result JSON from task packet and repo evidence. "
            "Does not stamp or fabricate completion."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-042")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--executor",
        default="cursor_agent",
        help="Executor label (default: cursor_agent).",
    )
    parser.add_argument(
        "--mode",
        choices=["working_tree", "head_auto"],
        default="head_auto",
        help=(
            "working_tree: use uncommitted diff only; "
            "head_auto: working tree if changed, else HEAD commit (default)."
        ),
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write results/WCS-XXX_worker_result.json; without this, dry-run only.",
    )
    parser.add_argument(
        "--command",
        action="append",
        default=[],
        metavar="TEXT",
        help="Truthful command or step run (repeatable). Required when drafting worker_complete result.",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    t = normalize_text(raw).upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_git(repo_path: Path, args: List[str], timeout: int = 10) -> Tuple[int, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(repo_path),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    out = (proc.stdout or "").strip()
    if proc.stderr:
        out = f"{out}\n{proc.stderr.strip()}" if out else proc.stderr.strip()
    return proc.returncode, out


def get_expected_scope(packet: dict) -> Set[str]:
    """Derive expected file scope from task packet (same spirit as worker_result_validate)."""
    expected: Set[str] = set()
    target_files = packet.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))
    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(packet.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break
    if not expected:
        suspected = packet.get("suspected_files")
        if isinstance(suspected, list):
            for item in suspected:
                path = normalize_text(item)
                if path:
                    expected.add(path.replace("\\", "/"))
    if not expected:
        notes = normalize_text(packet.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))
    return expected


def get_changed_files_working_tree(repo_path: Path) -> List[str]:
    """Files changed in working tree vs HEAD (repo-relative, forward slashes)."""
    code, out = run_git(repo_path, ["diff", "--name-only", "HEAD"])
    if code != 0:
        return []
    lines = [ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()]
    return lines


def get_changed_files_head_commit(repo_path: Path) -> List[str]:
    """Files changed in HEAD commit (repo-relative, forward slashes)."""
    code, out = run_git(repo_path, ["diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"])
    if code != 0:
        return []
    lines = [ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()]
    return lines


PLACEHOLDER_COMMANDS = {"todo", "tbd", "placeholder"}


def normalize_commands(raw: List[str]) -> List[str]:
    """Trim, drop empty, and drop obvious placeholders. Does not invent or derive."""
    out: List[str] = []
    for item in raw:
        s = normalize_text(item)
        if not s:
            continue
        if s.lower() in PLACEHOLDER_COMMANDS:
            continue
        out.append(s)
    return out


def main() -> int:
    args = parse_args()
    try:
        task_id = validate_task_id(args.task)
    except ValueError as e:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {normalize_text(args.task).upper() or '(missing)'}")
        print(f"Reason: {e}")
        return 1

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent
    if not workspace.exists():
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Workspace path does not exist.")
        return 1

    task_packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not task_packet_path.is_file():
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Task packet does not exist.")
        print(f"Expected: {task_packet_path}")
        return 1

    try:
        packet = read_json(task_packet_path)
    except Exception as e:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Reason: Could not read task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet must be a JSON object.")
        return 1

    raw_repo = normalize_text(packet.get("repo_path") or "")
    if not raw_repo:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet has no repo_path.")
        return 1
    repo_path = Path(raw_repo).resolve()
    if not repo_path.exists() or not repo_path.is_dir():
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print("Reason: Task repo path does not exist or is not a directory.")
        return 1

    expected_branch = normalize_text(packet.get("branch_name") or "")
    if not expected_branch:
        expected_branch = f"jarvis-task-{task_id.lower()}"

    code, branch_out = run_git(repo_path, ["branch", "--show-current"])
    if code != 0 or not branch_out:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print("Reason: Could not determine current branch.")
        return 1
    current_branch = branch_out.strip()
    if current_branch != expected_branch:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        print("Reason: Current branch does not match expected task branch.")
        return 1

    expected_scope = get_expected_scope(packet)
    if not expected_scope:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Could not derive expected file scope from task packet.")
        return 1

    evidence_source: Optional[str] = None
    changed: List[str] = []

    if args.mode == "working_tree":
        changed = get_changed_files_working_tree(repo_path)
        evidence_source = "working_tree" if changed else None
    else:
        changed = get_changed_files_working_tree(repo_path)
        if changed:
            evidence_source = "working_tree"
        else:
            changed = get_changed_files_head_commit(repo_path)
            evidence_source = "head_commit" if changed else None

    if not changed:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        print("Reason: No changed files detected (no working tree changes and no HEAD commit changes in head_auto mode).")
        return 1

    if evidence_source is None:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: No evidence source for changed files.")
        return 1

    for f in changed:
        norm = f.replace("\\", "/")
        if norm not in expected_scope:
            print("DRAFT WORKER RESULT: FAIL")
            print(f"Task: {task_id}")
            print(f"Repo path: {repo_path}")
            print(f"Expected scope: {sorted(expected_scope)}")
            print(f"Changed files: {changed}")
            print(f"Reason: Changed file {norm!r} is outside expected task scope.")
            return 1

    summary = (
        f"Implemented bounded changes for {task_id} in {', '.join(sorted(changed))} on branch {current_branch}."
    )

    notes = f"Evidence from {evidence_source}. Drafted by script; operator should review before post-worker."

    commands_run = normalize_commands(args.command or [])

    draft = {
        "task_id": task_id,
        "status": "worker_complete",
        "executor": normalize_text(args.executor) or "cursor_agent",
        "summary": summary,
        "files_changed": sorted(changed),
        "commands_run": commands_run,
        "issues_encountered": [],
        "notes": notes,
        "completed_at": "",
    }

    if draft["status"] == "worker_complete" and not commands_run:
        print("DRAFT WORKER RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print(
            "Reason: Worker result status is worker_complete; at least one meaningful --command is required for stamp guard. "
            "Provide one or more --command <text> with actual commands run."
        )
        return 1

    out_path = workspace / "results" / f"{task_id}_worker_result.json"
    written = False
    if args.write:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(draft, indent=2) + "\n", encoding="utf-8")
        written = True

    print("DRAFT WORKER RESULT: PASS")
    print(f"Task: {task_id}")
    print(f"Workspace: {workspace}")
    print(f"Repo path: {repo_path}")
    print(f"Expected branch: {expected_branch}")
    print(f"Current branch: {current_branch}")
    print(f"Evidence source: {evidence_source}")
    print(f"Output path: {out_path}")
    print(f"Written: {'yes' if written else 'no'}")
    print("")
    print(json.dumps(draft, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### draft_qa_result_from_evidence.py

- Exact path: `C:\dev\jarvis-workspace\scripts\draft_qa_result_from_evidence.py`
- Status: active
- Short purpose: Draft truthful QA result JSON from operator-supplied evidence (CLI: build/smoke/manual status)

```python
"""
Draft a truthful qa_result.json from CLI evidence (build/smoke/manual status).
Does not stamp, reconcile, or fabricate completion.
Operator should review the drafted result before guarded post-worker if appropriate.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, List


STATUS_CHOICES = ("pass", "fail", "skip", "unknown")


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Draft a truthful QA result JSON from CLI evidence (build/smoke/manual status). "
            "Does not stamp or fabricate completion."
        )
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-042")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write qa/WCS-XXX_qa_result.json; without this, dry-run only.",
    )
    parser.add_argument(
        "--build-status",
        choices=STATUS_CHOICES,
        help="Build (npm run build) outcome: pass, fail, skip, or unknown.",
    )
    parser.add_argument(
        "--smoke-status",
        choices=STATUS_CHOICES,
        help="Playwright smoke (npm run test:e2e:smoke) outcome: pass, fail, skip, or unknown.",
    )
    parser.add_argument(
        "--manual-status",
        choices=STATUS_CHOICES,
        help="Manual verification outcome: pass, fail, skip, or unknown.",
    )
    parser.add_argument(
        "--manual-check",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable: description of a manual check (e.g. 'Manual browser verification of /about').",
    )
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        metavar="PATH",
        help="Repeatable: path to an artifact file; must exist or script fails.",
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        metavar="TEXT",
        help="Repeatable: note line to append to notes.",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    t = normalize_text(raw).upper()
    if not re.match(r"^WCS-\d+$", t):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return t


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_artifact_path(workspace: Path, raw: str) -> Path:
    p = Path(raw)
    if not p.is_absolute():
        p = workspace / raw
    return p.resolve()


def main() -> int:
    args = parse_args()

    try:
        task_id = validate_task_id(args.task)
    except ValueError as e:
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {normalize_text(args.task).upper() or '(missing)'}")
        print(f"Reason: {e}")
        return 1

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent
    if not workspace.exists():
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Workspace path does not exist.")
        return 1

    task_packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not task_packet_path.is_file():
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Workspace: {workspace}")
        print("Reason: Task packet does not exist.")
        print(f"Expected: {task_packet_path}")
        return 1

    try:
        packet = read_json(task_packet_path)
    except Exception as e:
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print(f"Reason: Could not read task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("DRAFT QA RESULT: FAIL")
        print(f"Task: {task_id}")
        print("Reason: Task packet must be a JSON object.")
        return 1

    # Artifact paths must exist or we fail
    artifacts_resolved: List[str] = []
    for raw in args.artifact or []:
        p = resolve_artifact_path(workspace, raw)
        if not p.exists():
            print("DRAFT QA RESULT: FAIL")
            print(f"Task: {task_id}")
            print(f"Workspace: {workspace}")
            print(f"Reason: Artifact path does not exist: {p}")
            print(f"Supplied: {raw!r}")
            return 1
        artifacts_resolved.append(str(p))

    # Build checks from CLI evidence
    checks_run: List[str] = []
    checks_passed: List[str] = []
    checks_failed: List[str] = []

    if args.build_status in ("pass", "fail"):
        checks_run.append("npm run build")
        if args.build_status == "pass":
            checks_passed.append("npm run build")
        else:
            checks_failed.append("npm run build")

    if args.smoke_status in ("pass", "fail"):
        checks_run.append("npm run test:e2e:smoke")
        if args.smoke_status == "pass":
            checks_passed.append("npm run test:e2e:smoke")
        else:
            checks_failed.append("npm run test:e2e:smoke")

    manual_checks: List[str] = []
    if args.manual_status in ("pass", "fail"):
        manual_checks = [normalize_text(c) for c in (args.manual_check or []) if normalize_text(c)]
        if not manual_checks:
            manual_checks = ["Manual browser verification"]
        for c in manual_checks:
            checks_run.append(c)
            if args.manual_status == "pass":
                checks_passed.append(c)
            else:
                checks_failed.append(c)

    # Determine status: qa_fail if any failed; escalated if no usable checks; else qa_pass
    if checks_failed:
        status = "qa_fail"
    elif not checks_run:
        status = "escalated"
    else:
        status = "qa_pass"

    # qa_tool: truthful text only
    parts: List[str] = []
    if args.build_status in ("pass", "fail"):
        parts.append("Next build")
    if args.smoke_status in ("pass", "fail"):
        parts.append("Playwright smoke")
    if args.manual_status in ("pass", "fail"):
        parts.append("manual browser verification")
    qa_tool = "manual operator QA via " + " and ".join(parts) if parts else "manual operator QA (evidence incomplete; drafted as escalated)"

    # summary: evidence-based, formulaic
    if status == "qa_pass" and checks_run:
        bits = []
        if "npm run build" in checks_passed:
            bits.append("Build passed")
        if "npm run test:e2e:smoke" in checks_passed:
            bits.append("Playwright smoke passed")
        if any(c not in ("npm run build", "npm run test:e2e:smoke") for c in checks_passed):
            bits.append("manual verification passed")
        summary = ", ".join(bits) + " for the targeted change." if bits else "QA checks passed for the targeted change."
    elif status == "qa_fail" and checks_failed:
        bits = []
        if "npm run build" in checks_failed:
            bits.append("Build failed")
        if "npm run test:e2e:smoke" in checks_failed:
            bits.append("Playwright smoke failed")
        if any(c not in ("npm run build", "npm run test:e2e:smoke") for c in checks_failed):
            bits.append("manual verification failed")
        summary = ", ".join(bits) + " during QA for the targeted change." if bits else "QA failed for the targeted change."
    else:
        summary = "QA evidence was incomplete or inconclusive; result drafted as escalated for operator review."

    # notes
    notes_parts = [
        "Drafted by script from CLI evidence. Operator should review before guarded post-worker flow."
    ]
    if args.manual_status in ("skip", "unknown") and (args.build_status or args.smoke_status) in ("pass", "fail"):
        notes_parts.append("Manual verification was skipped or not evidenced.")
    if not checks_run and status == "escalated":
        notes_parts.append("No usable checks ran; evidence incomplete or only skip/unknown supplied.")
    for n in args.note or []:
        t = normalize_text(n)
        if t:
            notes_parts.append(t)
    notes = " ".join(notes_parts)

    draft = {
        "task_id": task_id,
        "status": status,
        "qa_tool": qa_tool,
        "summary": summary,
        "checks_run": checks_run,
        "checks_passed": checks_passed,
        "checks_failed": checks_failed,
        "artifacts": artifacts_resolved,
        "notes": notes,
        "completed_at": "",
    }

    out_path = workspace / "qa" / f"{task_id}_qa_result.json"
    written = False
    if args.write:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(draft, indent=2) + "\n", encoding="utf-8")
        written = True

    print("DRAFT QA RESULT: PASS")
    print(f"Task: {task_id}")
    print(f"Workspace: {workspace}")
    print(f"Output path: {out_path}")
    print(f"Written: {'yes' if written else 'no'}")
    print("")
    print(json.dumps(draft, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### worker_result_validate.py

- Exact path: `C:\dev\jarvis-workspace\scripts\worker_result_validate.py`
- Status: active
- Short purpose: Read-only worker-result schema validator for a WCS task

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List, Set


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}


class WorkerResultError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise WorkerResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path) -> Set[str]:
    expected: Set[str] = set()
    try:
        data = read_json(task_json_path)
    except WorkerResultError:
        return expected

    if not isinstance(data, dict):
        return expected

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    return expected


def check_worker_result(
    worker_path: Path,
    task_id: str,
    mode: str,
    expected_files: Set[str],
    failures: List[str],
) -> None:
    try:
        data = read_json(worker_path)
    except WorkerResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    # Required fields
    required_fields = [
        "task_id",
        "status",
        "executor",
        "summary",
        "files_changed",
        "commands_run",
        "issues_encountered",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"Worker result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    executor = normalize_text(data.get("executor"))
    if not executor:
        failures.append("Worker result executor must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("Worker result summary must be present and non-blank.")

    files_changed = data.get("files_changed")
    if not isinstance(files_changed, list):
        failures.append("Worker result files_changed must be a list.")
        files_changed_list: List[str] = []
    else:
        files_changed_list = [normalize_text(x) for x in files_changed]

    commands_run = data.get("commands_run")
    if not isinstance(commands_run, list):
        failures.append("Worker result commands_run must be a list.")

    issues_encountered = data.get("issues_encountered")
    if not isinstance(issues_encountered, list):
        failures.append("Worker result issues_encountered must be a list.")

    # notes field must exist (already checked) but may be blank or non-blank; no extra content rule

    if status == "worker_complete":
        if not files_changed_list:
            failures.append(
                "Worker result files_changed must contain at least one entry when status is worker_complete."
            )

    for entry in files_changed_list:
        if not entry:
            failures.append("Worker result files_changed contains a blank entry.")

    # Simple task-scope consistency if expected scope is known
    if expected_files:
        for entry in files_changed_list:
            normalized_entry = entry.replace("\\", "/")
            if normalized_entry and normalized_entry not in expected_files:
                failures.append(
                    f"Worker result files_changed entry {normalized_entry} is outside expected task scope: {sorted(expected_files)}."
                )

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, worker result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, worker result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerResultError as exc:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    task_json_path = workspace / "tasks" / f"{task_id}_task.json"

    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")

    expected_files = determine_expected_files(task_json_path)

    if worker_path.exists():
        check_worker_result(worker_path, task_id, args.mode, expected_files, failures)

    if failures:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    # Best-effort display of key fields on pass
    data = read_json(worker_path)
    executor = normalize_text(data.get("executor"))
    status = normalize_text(data.get("status"))
    files_changed = data.get("files_changed") or []
    files_changed_display = [normalize_text(x) for x in files_changed if normalize_text(x)]

    print("WORKER RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"Executor: {executor}")
    print(f"Status: {status}")
    print(f"Files changed: {', '.join(files_changed_display) if files_changed_display else '(none)'}")
    print("Passed checks:")
    print("- worker result JSON exists and parses")
    print("- required worker result fields are present")
    print("- executor and summary are non-blank")
    print("- list fields (files_changed, commands_run, issues_encountered) have the correct types")
    print("- files_changed is non-empty for worker_complete (if applicable)")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")
    if expected_files:
        print("- files_changed entries are within expected task scope")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### qa_result_validate.py

- Exact path: `C:\dev\jarvis-workspace\scripts\qa_result_validate.py`
- Status: active
- Short purpose: Read-only QA-result schema validator for a WCS task

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List


ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class QaResultError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise QaResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise QaResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only QA result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise QaResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise QaResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_qa_result(
    qa_path: Path,
    task_id: str,
    mode: str,
    failures: List[str],
) -> None:
    try:
        data = read_json(qa_path)
    except QaResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    required_fields = [
        "task_id",
        "status",
        "qa_tool",
        "summary",
        "checks_run",
        "checks_passed",
        "checks_failed",
        "artifacts",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"QA result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    qa_tool = normalize_text(data.get("qa_tool"))
    if not qa_tool:
        failures.append("QA result qa_tool must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("QA result summary must be present and non-blank.")

    checks_run = data.get("checks_run")
    checks_passed = data.get("checks_passed")
    checks_failed = data.get("checks_failed")
    artifacts = data.get("artifacts")

    if not isinstance(checks_run, list):
        failures.append("QA result checks_run must be a list.")
        checks_run_list: List[str] = []
    else:
        checks_run_list = [normalize_text(x) for x in checks_run]

    if not isinstance(checks_passed, list):
        failures.append("QA result checks_passed must be a list.")
        checks_passed_list: List[str] = []
    else:
        checks_passed_list = [normalize_text(x) for x in checks_passed]

    if not isinstance(checks_failed, list):
        failures.append("QA result checks_failed must be a list.")
        checks_failed_list: List[str] = []
    else:
        checks_failed_list = [normalize_text(x) for x in checks_failed]

    if not isinstance(artifacts, list):
        failures.append("QA result artifacts must be a list.")
        artifacts_list: List[str] = []
    else:
        artifacts_list = [normalize_text(x) for x in artifacts]

    # notes must exist (checked above) but can be blank or non-blank; no extra content rule

    if status in {"qa_pass", "qa_fail"} and not checks_run_list:
        failures.append(
            "QA result checks_run must contain at least one entry when status is qa_pass or qa_fail."
        )

    for arr_name, arr in [
        ("checks_run", checks_run_list),
        ("checks_passed", checks_passed_list),
        ("checks_failed", checks_failed_list),
        ("artifacts", artifacts_list),
    ]:
        for entry in arr:
            if not isinstance(entry, str):
                failures.append(f"QA result {arr_name} contains a non-string entry.")
            elif not entry:
                failures.append(f"QA result {arr_name} contains a blank entry.")

    # Simple internal consistency
    if status == "qa_pass":
        if checks_failed_list:
            failures.append("QA result checks_failed must be empty when status is qa_pass.")
        if not checks_passed_list:
            failures.append("QA result checks_passed must contain at least one entry when status is qa_pass.")
    elif status == "qa_fail":
        if not checks_failed_list:
            failures.append("QA result checks_failed must contain at least one entry when status is qa_fail.")
    # status == escalated: no extra requirements for checks_passed / checks_failed beyond type and content shape

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, QA result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, QA result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("QA RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except QaResultError as exc:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")

    if qa_path.exists():
        check_qa_result(qa_path, task_id, args.mode, failures)

    if failures:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    data = read_json(qa_path)
    qa_tool = normalize_text(data.get("qa_tool"))
    status = normalize_text(data.get("status"))
    checks_run = data.get("checks_run") or []
    checks_run_display = [normalize_text(x) for x in checks_run if normalize_text(x)]

    print("QA RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"QA tool: {qa_tool}")
    print(f"Status: {status}")
    print(f"Checks run: {', '.join(checks_run_display) if checks_run_display else '(none)'}")
    print("Passed checks:")
    print("- QA result JSON exists and parses")
    print("- required QA result fields are present")
    print("- qa_tool and summary are non-blank")
    print("- list fields (checks_run, checks_passed, checks_failed, artifacts) have the correct types")
    print("- checks_run is non-empty for qa_pass/qa_fail (if applicable)")
    print("- internal consistency between status, checks_passed, and checks_failed")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### stamp_guard_check.py

- Exact path: `C:\dev\jarvis-workspace\scripts\stamp_guard_check.py`
- Status: active
- Short purpose: Read-only pre-stamp guardrail for worker and QA result JSON files

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class StampGuardError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise StampGuardError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise StampGuardError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only pre-stamp guardrail for worker and QA result JSON files."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise StampGuardError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise StampGuardError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def load_result(path: Path, kind: str, failures: List[str]) -> Dict[str, Any] | None:
    try:
        data = read_json(path)
    except StampGuardError as exc:
        failures.append(str(exc))
        return None
    if not isinstance(data, dict):
        failures.append(f"{kind} result must be a JSON object: {path}")
        return None
    return data


def check_completed_at_pre_stamp(
    data: Dict[str, Any], kind: str, failures: List[str]
) -> str:
    completed_raw = normalize_text(data.get("completed_at"))
    if completed_raw:
        failures.append(
            f"{kind} result completed_at must be blank before stamping; "
            f"found: {completed_raw!r}."
        )
    return completed_raw


def check_worker_pre_stamp(
    data: Dict[str, Any],
    task_id: str,
    failures: List[str],
) -> None:
    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft' before stamping.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. "
            f"Found: {status or '(blank)'}."
        )

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    summary = normalize_text(data.get("summary"))
    if not summary or summary.lower() in {"todo", "tbd", "placeholder"}:
        failures.append(
            "Worker result summary must be present, non-blank, and not a placeholder before stamping."
        )

    executor = normalize_text(data.get("executor"))
    if not executor:
        failures.append(
            "Worker result executor must be present and non-blank before stamping."
        )

    files_changed = data.get("files_changed")
    if not isinstance(files_changed, list):
        failures.append("Worker result files_changed must be a list before stamping.")
        files_changed_list: List[str] = []
    else:
        files_changed_list = [normalize_text(x) for x in files_changed]

    if status == "worker_complete" and not files_changed_list:
        failures.append(
            "Worker result files_changed must contain at least one entry when status is worker_complete before stamping."
        )

    commands_run = data.get("commands_run")
    if not isinstance(commands_run, list):
        failures.append("Worker result commands_run must be a list before stamping.")
        commands_run_list: List[str] = []
    else:
        commands_run_list = [normalize_text(x) for x in commands_run]

    if status == "worker_complete":
        meaningful_commands = [
            cmd
            for cmd in commands_run_list
            if cmd and cmd.lower() not in {"todo", "tbd", "placeholder"}
        ]
        if not meaningful_commands:
            failures.append(
                "Worker result commands_run should contain at least one meaningful entry when status is worker_complete before stamping."
            )


def check_qa_pre_stamp(
    data: Dict[str, Any],
    task_id: str,
    failures: List[str],
) -> None:
    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft' before stamping.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. "
            f"Found: {status or '(blank)'}."
        )

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    summary = normalize_text(data.get("summary"))
    if not summary or summary.lower() in {"todo", "tbd", "placeholder"}:
        failures.append(
            "QA result summary must be present, non-blank, and not a placeholder before stamping."
        )

    qa_tool = normalize_text(data.get("qa_tool"))
    if not qa_tool:
        failures.append(
            "QA result qa_tool must be present and non-blank before stamping."
        )

    notes = normalize_text(data.get("notes"))
    if notes and notes.lower() in {"todo", "tbd", "placeholder"}:
        failures.append(
            "QA result notes must not be an obvious placeholder before stamping."
        )

    checks_run = data.get("checks_run")
    if not isinstance(checks_run, list):
        failures.append("QA result checks_run must be a list before stamping.")
        checks_run_list: List[str] = []
    else:
        checks_run_list = [normalize_text(x) for x in checks_run]

    checks_failed = data.get("checks_failed")
    if not isinstance(checks_failed, list):
        failures.append("QA result checks_failed must be a list before stamping.")
        checks_failed_list: List[str] = []
    else:
        checks_failed_list = [normalize_text(x) for x in checks_failed]

    if status in {"qa_pass", "qa_fail"} and not checks_run_list:
        failures.append(
            "QA result checks_run must contain at least one entry when status is qa_pass or qa_fail before stamping."
        )

    if status == "qa_pass" and checks_failed_list:
        failures.append(
            "QA result checks_failed must be empty when status is qa_pass before stamping."
        )

    checks_passed = data.get("checks_passed")
    if not isinstance(checks_passed, list):
        failures.append("QA result checks_passed must be a list before stamping.")
        checks_passed_list: List[str] = []
    else:
        checks_passed_list = [normalize_text(x) for x in checks_passed]

    if status == "qa_pass" and not checks_passed_list:
        failures.append(
            "QA result checks_passed must contain at least one entry when status is qa_pass before stamping."
        )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("STAMP GUARD CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except StampGuardError as exc:
        print("STAMP GUARD CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    worker_data = load_result(worker_path, "Worker", failures)
    qa_data = load_result(qa_path, "QA", failures)

    worker_completed_raw = ""
    qa_completed_raw = ""

    if worker_data is not None:
        worker_completed_raw = check_completed_at_pre_stamp(
            worker_data, "Worker", failures
        )
        check_worker_pre_stamp(worker_data, task_id, failures)
    if qa_data is not None:
        qa_completed_raw = check_completed_at_pre_stamp(qa_data, "QA", failures)
        check_qa_pre_stamp(qa_data, task_id, failures)

    # Detect uneven / split-stamp states explicitly.
    if worker_data is not None and qa_data is not None:
        worker_completed = bool(worker_completed_raw)
        qa_completed = bool(qa_completed_raw)
        if worker_completed != qa_completed:
            failures.append(
                "Worker and QA results are in a split-stamp state: "
                f"worker completed_at={worker_completed_raw!r}, "
                f"QA completed_at={qa_completed_raw!r}. "
                "Both must be blank before stamping or both stamped consistently."
            )

    # Both artifacts must be present and ready before stamping.
    if worker_data is None or qa_data is None:
        failures.append(
            "Both worker and QA result files must exist and parse successfully before stamping."
        )

    if failures:
        print("STAMP GUARD CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("STAMP GUARD CHECK: PASS")
    print(f"Task: {task_id}")
    print("Worker and QA results are present, pre-stamp, and appear ready for timestamping.")
    print(f"- Worker result: {worker_path}")
    print(f"- QA result: {qa_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### stamp_result_timestamp.py

- Exact path: `C:\dev\jarvis-workspace\scripts\stamp_result_timestamp.py`
- Status: active
- Short purpose: Stamps completed_at (or specified field) on worker and QA result JSON files; takes FILE PATH as positional argument

```python
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class StampError(Exception):
    pass


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise StampError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise StampError(f"Invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stamp a result JSON file with the current local ISO timestamp in completed_at."
    )
    parser.add_argument("file", help="Path to the JSON result file to stamp")
    parser.add_argument(
        "--field",
        default="completed_at",
        help="Field name to stamp. Defaults to completed_at.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing non-empty timestamp.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.file).resolve()

    data = read_json(path)
    if not isinstance(data, dict):
        raise StampError(f"Expected a JSON object in {path}, got {type(data).__name__}")

    field_name = args.field
    existing_value = data.get(field_name)

    if existing_value and not args.force:
        print(f"SKIPPED: {path}")
        print(f"Reason: {field_name} already has a value: {existing_value}")
        print("Use --force if you intentionally want to overwrite it.")
        return 0

    stamped_value = now_local_iso()
    data[field_name] = stamped_value
    write_json(path, data)

    print(f"STAMPED: {path}")
    print(f"{field_name}: {stamped_value}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except StampError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
```

### pre_reconcile_check.py

- Exact path: `C:\dev\jarvis-workspace\scripts\pre_reconcile_check.py`
- Status: active
- Short purpose: Read-only pre-reconcile readiness gate for a WCS task

```python
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Tuple


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class CheckError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CheckError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CheckError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only pre-reconcile readiness check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016.",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id: str) -> str:
    task_id_norm = normalize_text(task_id).upper()
    if not task_id_norm.startswith("WCS-"):
        raise CheckError(f"Invalid task id (expected WCS-XXX): {task_id_norm}")
    suffix = task_id_norm.split("-", 1)[1]
    if not suffix.isdigit():
        raise CheckError(f"Invalid task id suffix (expected numeric): {task_id_norm}")
    return task_id_norm


def check_artifacts(workspace: Path, task_id: str, failures: list[str]) -> Tuple[Path, Path, Path]:
    task_json = workspace / "tasks" / f"{task_id}_task.json"
    worker_result = workspace / "results" / f"{task_id}_worker_result.json"
    qa_result = workspace / "qa" / f"{task_id}_qa_result.json"

    if not task_json.exists():
        failures.append(f"Missing task packet JSON: {task_json}")
    if not worker_result.exists():
        failures.append(f"Missing worker result JSON: {worker_result}")
    if not qa_result.exists():
        failures.append(f"Missing QA result JSON: {qa_result}")

    return task_json, worker_result, qa_result


def check_worker_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def resolve_repo_path(workspace: Path, failures: list[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except CheckError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    repo_raw = normalize_text(data.get("repo_path"))
    if not repo_raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(repo_raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def check_repo_state(repo_path: Path, task_id: str, failures: list[str]) -> tuple[str | None, str | None, int | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"Failed to read current branch in repo {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        failures.append(
            f"Failed to inspect repo status in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
        if dirty_lines:
            failures.append(
                f"Repo working tree is not clean in {repo_path}. {len(dirty_lines)} changed path(s) detected."
            )

    base_branch = None
    for candidate in ["main", "master"]:
        rev_parse = run_git(repo_path, ["rev-parse", "--verify", candidate])
        if rev_parse.returncode == 0:
            base_branch = candidate
            break

    if base_branch is None:
        failures.append(f"Neither 'main' nor 'master' branch exists in repo {repo_path}.")
        return expected_branch, current_branch, None

    ahead_result = run_git(repo_path, ["rev-list", "--count", f"{base_branch}..{current_branch or 'HEAD'}"])
    if ahead_result.returncode != 0:
        failures.append(
            f"Failed to compute commits ahead of {base_branch} in {repo_path}: "
            f"{ahead_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, current_branch, None

    ahead_str = normalize_text(ahead_result.stdout)
    try:
        ahead_count = int(ahead_str or "0")
    except ValueError:
        failures.append(
            f"Unexpected rev-list output for {base_branch}..{current_branch or 'HEAD'} in {repo_path}: {ahead_str}"
        )
        return expected_branch, current_branch, None

    if ahead_count < 1:
        failures.append(
            f"Task branch must be ahead of {base_branch} by at least 1 commit. Found: {ahead_count}."
        )

    return expected_branch, current_branch, ahead_count


def main() -> int:
    args = parse_args()

    if not args.task:
        print("PRE-RECONCILE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except CheckError as exc:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json, worker_result, qa_result = check_artifacts(workspace, task_id, failures)

    if worker_result.exists():
        check_worker_result(worker_result, task_id, failures)

    if qa_result.exists():
        check_qa_result(qa_result, task_id, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = None
    current_branch = None
    ahead_count: int | None = None

    if repo_path is not None:
        expected_branch, current_branch, ahead_count = check_repo_state(
            repo_path, task_id, failures
        )

    if failures:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("PRE-RECONCILE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch is not None and current_branch is not None:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        if ahead_count is not None:
            print(f"Commits ahead of main/master: {ahead_count}")
    print("Passed checks:")
    print("- task, worker result, and QA result artifacts present")
    print("- worker result contract and completed_at valid")
    print("- QA result contract and completed_at valid")
    print("- repo path, branch, and clean working tree valid")
    print("- task branch ahead of main/master by at least 1 commit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### reconcile_task_outcome.py

- Exact path: `C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.py`
- Status: active
- Short purpose: Reconciles worker and QA results into backlog state

```python
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from generate_task_packet import build_packet_markdown

FINAL_STATUSES = {
    "done",
    "blocked",
    "escalated",
    "worker_complete",
    "qa_fail",
}


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class ReconcileError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ReconcileError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReconcileError(f"Invalid JSON in {path}: {exc}") from exc


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def escape_md(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def normalize_text(value: Any) -> str:
    return str(value or "").strip()


def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(item.get("task_id", "")),
                    escape_md(item.get("project", "")),
                    escape_md(item.get("bucket", "")),
                    escape_md(item.get("priority", "")),
                    escape_md(item.get("risk", "")),
                    escape_md(item.get("status", "")),
                    escape_md(item.get("title", "")),
                    escape_md(item.get("notes", "")),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def normalize_status(value: str) -> str:
    return str(value or "").strip().lower()


def decide_final_status(worker: dict[str, Any], qa: dict[str, Any], escalation: dict[str, Any]) -> str:
    worker_status = normalize_status(worker.get("status", ""))
    qa_status = normalize_status(qa.get("status", ""))
    escalation_status = normalize_status(escalation.get("status", ""))

    if escalation_status == "escalated":
        return "escalated"
    if worker_status == "escalated":
        return "escalated"
    if worker_status == "blocked":
        return "blocked"

    if worker_status != "worker_complete":
        raise ReconcileError(
            f"Worker result must have status 'worker_complete', 'blocked', or 'escalated'. Found: {worker_status or '<blank>'}"
        )

    if qa_status == "qa_pass":
        return "done"
    if qa_status == "qa_fail":
        return "blocked"
    if qa_status == "escalated":
        return "escalated"

    raise ReconcileError(
        f"QA result must have status 'qa_pass', 'qa_fail', or 'escalated'. Found: {qa_status or '<blank>'}"
    )


def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, final_status: str) -> dict[str, Any]:
    for item in backlog_items:
        if str(item.get("task_id", "")).upper() == task_id.upper():
            item["status"] = final_status
            return item
    raise ReconcileError(f"Task {task_id} not found in backlog")


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def load_repo_path_for_project(workspace: Path, project: str) -> Path:
    project_upper = normalize_text(project).upper()
    if project_upper == "WCS":
        status_path = workspace / "state" / "project_status_wcs.json"
    else:
        raise ReconcileError(f"Repo verification is not defined for project: {project_upper or '<blank>'}")

    status = load_json(status_path)
    if not isinstance(status, dict):
        raise ReconcileError(f"Expected JSON object in {status_path}")

    raw_repo_path = normalize_text(status.get("repo_path"))
    if not raw_repo_path:
        raise ReconcileError(f"Missing repo_path in {status_path}")

    repo_path = Path(raw_repo_path)
    if not repo_path.exists():
        raise ReconcileError(f"Configured repo path does not exist: {repo_path}")
    if not (repo_path / ".git").exists():
        raise ReconcileError(f"Configured repo path is not a git repository: {repo_path}")
    return repo_path


def detect_baseline_branch(repo_path: Path) -> str | None:
    for candidate in ("main", "master"):
        result = run_git(repo_path, ["branch", "--list", candidate])
        if result.returncode != 0:
            raise ReconcileError(result.stderr.strip() or f"Failed to inspect git branches in {repo_path}")
        if result.stdout.strip():
            return candidate
    return None


def verify_done_repo_state(workspace: Path, task: dict[str, Any]) -> dict[str, Any]:
    task_id = normalize_text(task.get("task_id")).upper()
    project = normalize_text(task.get("project")).upper()
    repo_path = load_repo_path_for_project(workspace, project)
    expected_branch = task_branch_name(task_id)

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise ReconcileError(current_branch_result.stderr.strip() or "Failed to detect current git branch.")
    current_branch = current_branch_result.stdout.strip()

    if current_branch != expected_branch:
        raise ReconcileError(
            "Refusing to mark task done because repo is on the wrong branch. "
            f"Current branch: {current_branch or '<blank>'}. Expected: {expected_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise ReconcileError(status_result.stderr.strip() or "Failed to inspect git status.")
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    if dirty_lines:
        raise ReconcileError(
            "Refusing to mark task done because repo has uncommitted changes.\n"
            + "\n".join(dirty_lines)
        )

    baseline_branch = detect_baseline_branch(repo_path)
    commits_ahead = None
    if baseline_branch:
        ahead_result = run_git(repo_path, ["rev-list", "--count", f"{baseline_branch}..HEAD"])
        if ahead_result.returncode != 0:
            raise ReconcileError(
                ahead_result.stderr.strip()
                or f"Failed to compare {expected_branch} against {baseline_branch}."
            )
        try:
            commits_ahead = int(ahead_result.stdout.strip() or "0")
        except ValueError as exc:
            raise ReconcileError(
                f"Unexpected rev-list output while comparing {expected_branch} against {baseline_branch}: {ahead_result.stdout!r}"
            ) from exc

        if commits_ahead < 1:
            raise ReconcileError(
                "Refusing to mark task done because the task branch has no commits ahead of "
                f"{baseline_branch}. Expected at least one committed task change on {expected_branch}."
            )

    head_commit_result = run_git(repo_path, ["rev-parse", "--short", "HEAD"])
    if head_commit_result.returncode != 0:
        raise ReconcileError(head_commit_result.stderr.strip() or "Failed to read HEAD commit.")

    return {
        "repo_path": str(repo_path),
        "expected_branch": expected_branch,
        "current_branch": current_branch,
        "baseline_branch": baseline_branch or "",
        "commits_ahead_of_baseline": commits_ahead,
        "head_commit": head_commit_result.stdout.strip(),
        "verified_at": now_local(),
    }


def build_daily_review_entry(
    task: dict[str, Any],
    worker: dict[str, Any],
    qa: dict[str, Any],
    final_status: str,
    repo_verification: dict[str, Any] | None = None,
) -> str:
    task_id = task.get("task_id", "")
    title = task.get("title", "")
    worker_summary = (worker.get("summary") or "").strip()
    qa_summary = (qa.get("summary") or "").strip()
    files_changed = worker.get("files_changed") or []
    commands_run = worker.get("commands_run") or []

    lines = [
        f"### {task_id} — {final_status}",
        f"- Title: {title}",
    ]
    if worker_summary:
        lines.append(f"- Worker: {worker_summary}")
    if qa_summary:
        lines.append(f"- QA: {qa_summary}")
    if files_changed:
        lines.append(f"- Files changed: {', '.join(map(str, files_changed))}")
    if commands_run:
        lines.append(f"- Commands run: {', '.join(map(str, commands_run))}")
    if repo_verification:
        lines.append(f"- Repo path: {repo_verification.get('repo_path', '')}")
        lines.append(f"- Verified branch: {repo_verification.get('current_branch', '')}")
        baseline_branch = normalize_text(repo_verification.get("baseline_branch"))
        if baseline_branch:
            lines.append(
                f"- Commits ahead of {baseline_branch}: {repo_verification.get('commits_ahead_of_baseline', '')}"
            )
        lines.append(f"- HEAD commit: {repo_verification.get('head_commit', '')}")
        lines.append(f"- Branch verified at: {repo_verification.get('verified_at', '')}")
    lines.append(f"- Reconciled at: {now_local()}")
    lines.append("")
    return "\n".join(lines)


def append_daily_review(
    review_path: Path,
    task: dict[str, Any],
    worker: dict[str, Any],
    qa: dict[str, Any],
    final_status: str,
    repo_verification: dict[str, Any] | None = None,
) -> None:
    entry = build_daily_review_entry(task, worker, qa, final_status, repo_verification=repo_verification)
    if review_path.exists():
        existing = review_path.read_text(encoding="utf-8")
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        existing = f"# DAILY_REVIEW\n\nDate: {today}\n\nSummary\n\nWins\n\nFailures / blockers\n\nNext step\n\n"

    task_id = str(task.get("task_id", ""))
    if f"### {task_id} —" in existing:
        return

    content = existing.rstrip() + "\n\n" + entry
    review_path.write_text(content, encoding="utf-8")


def sync_task_packet_artifacts(tasks_dir: Path, task_id: str, final_status: str) -> list[Path]:
    task_json_path = tasks_dir / f"{task_id}_task.json"
    if not task_json_path.exists():
        return []

    packet = load_json(task_json_path)
    if not isinstance(packet, dict):
        raise ReconcileError(f"Expected JSON object in {task_json_path}")

    packet["status"] = final_status
    packet["updated_at"] = now_local()
    save_json(task_json_path, packet)

    task_md_path = tasks_dir / f"{task_id}_task.md"
    task_md_path.write_text(build_packet_markdown(packet), encoding="utf-8")
    return [task_json_path, task_md_path]


CURSOR_COMPLETION_CONTRACT = """When you finish the task, return your summary in this exact structure:

1. What changed
- Files changed:
- Short description of each change:

2. Commands run
- List each command exactly as run

3. Result
- Build result:
- Test result:
- QA result:

4. Issues encountered
- None
or
- List each issue clearly

5. Stop conditions
- State whether any stop condition was hit

6. Recommended worker_result.json fields
{
  \"status\": \"worker_complete\",
  \"summary\": \"...\",
  \"files_changed\": [\"...\"],
  \"commands_run\": [\"...\"],
  \"issues_encountered\": [],
  \"notes\": \"...\"
}

Do not add extra sections. Do not give broad advice unless asked."""


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconcile task outcome from worker and QA JSON files")
    parser.add_argument("--task", required=False, help="Task ID to reconcile, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--skip-review", action="store_true", help="Do not append an entry to DAILY_REVIEW.md")
    parser.add_argument("--print-cursor-contract", action="store_true", help="Print the recommended Cursor completion contract and exit")
    args = parser.parse_args()

    if args.print_cursor_contract:
        print(CURSOR_COMPLETION_CONTRACT)
        return 0

    if not args.task:
        parser.error("--task is required unless --print-cursor-contract is used")

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"
    tasks_dir = workspace / "tasks"

    task_id = args.task.strip().upper()
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"
    daily_review_path = state_dir / "DAILY_REVIEW.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise ReconcileError(f"Expected a JSON array in {backlog_json_path}")

    task = next((item for item in backlog if str(item.get("task_id", "")).upper() == task_id), None)
    if not task:
        raise ReconcileError(f"Task {task_id} not found in backlog")

    worker = load_json(worker_result_path)
    qa = load_json(qa_result_path)
    escalation = load_json(escalation_path) if escalation_path.exists() else {"status": "draft"}

    if str(worker.get("task_id", "")).upper() != task_id:
        raise ReconcileError(f"Worker result task_id mismatch in {worker_result_path}")
    if str(qa.get("task_id", "")).upper() != task_id:
        raise ReconcileError(f"QA result task_id mismatch in {qa_result_path}")

    final_status = decide_final_status(worker, qa, escalation)
    repo_verification = verify_done_repo_state(workspace, task) if final_status == "done" else None

    updated_task = update_backlog_status(backlog, task_id, final_status)
    save_json(backlog_json_path, backlog)
    backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")
    updated_packet_paths = sync_task_packet_artifacts(tasks_dir, task_id, final_status)

    if not args.skip_review:
        append_daily_review(daily_review_path, updated_task, worker, qa, final_status, repo_verification=repo_verification)

    print(f"FINAL STATUS: {final_status}")
    if repo_verification:
        print("BRANCH VERIFIED: yes")
        print(f"REPO PATH: {repo_verification['repo_path']}")
        print(f"EXPECTED BRANCH: {repo_verification['expected_branch']}")
        print(f"CURRENT BRANCH: {repo_verification['current_branch']}")
        if repo_verification.get("baseline_branch"):
            print(
                f"COMMITS AHEAD OF {repo_verification['baseline_branch'].upper()}: "
                f"{repo_verification['commits_ahead_of_baseline']}"
            )
        print(f"HEAD COMMIT: {repo_verification['head_commit']}")
    print(f"UPDATED: {backlog_json_path}")
    print(f"RENDERED: {backlog_md_path}")
    for updated_packet_path in updated_packet_paths:
        label = "RENDERED" if updated_packet_path.suffix.lower() == ".md" else "UPDATED"
        print(f"{label}: {updated_packet_path}")
    if not args.skip_review:
        print(f"UPDATED: {daily_review_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReconcileError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
```

### post_reconcile_validate.py

- Exact path: `C:\dev\jarvis-workspace\scripts\post_reconcile_validate.py`
- Status: active
- Short purpose: Read-only post-reconcile validator for a WCS task

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class ValidationError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ValidationError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only post-reconcile validation for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id_raw: str) -> str:
    task_id = normalize_text(task_id_raw).upper()
    if not task_id.startswith("WCS-"):
        raise ValidationError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise ValidationError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_state_files_exist(workspace: Path, failures: list[str]) -> dict[str, Path]:
    state_dir = workspace / "state"
    paths = {
        "backlog_json": state_dir / "master_backlog.json",
        "backlog_md": state_dir / "MASTER_BACKLOG.md",
        "daily_review_md": state_dir / "DAILY_REVIEW.md",
    }
    for key, path in paths.items():
        if not path.exists():
            failures.append(f"Missing state file: {path}")
    return paths


def check_backlog_json(backlog_json_path: Path, task_id: str, failures: list[str]) -> dict[str, Any] | None:
    try:
        data = read_json(backlog_json_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, list):
        failures.append(f"master_backlog.json root must be a list: {backlog_json_path}")
        return None

    matches: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if normalize_text(item.get("task_id")).upper() == task_id:
            matches.append(item)

    if len(matches) == 0:
        failures.append(f"No backlog entry found for task {task_id} in master_backlog.json.")
        return None
    if len(matches) > 1:
        failures.append(f"Expected exactly one backlog entry for {task_id}, found {len(matches)}.")
        return None

    record = matches[0]
    project = normalize_text(record.get("project")).upper()
    status = normalize_text(record.get("status")).lower()

    if project != "WCS":
        failures.append(
            f"Backlog entry for {task_id} has wrong project. Expected WCS, found {project or '(blank)'}."
        )
    if status != "done":
        failures.append(
            f"Backlog entry for {task_id} must have status 'done'. Found {status or '(blank)'}."
        )

    return record


def check_backlog_markdown(
    backlog_md_path: Path,
    task_id: str,
    title: str | None,
    failures: list[str],
) -> None:
    try:
        text = backlog_md_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing backlog markdown file: {backlog_md_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read backlog markdown {backlog_md_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in MASTER_BACKLOG.md.")

    if title:
        if title not in text:
            failures.append(f"Task title not found in MASTER_BACKLOG.md: {title}")

    # Simple done indicator: look for a line containing both the task id and 'done' (case-insensitive).
    done_line_found = False
    for line in text.splitlines():
        if task_id in line and "done" in line.lower():
            done_line_found = True
            break
    if not done_line_found:
        failures.append(
            f"MASTER_BACKLOG.md does not show a simple 'done' indicator on the same line as {task_id}."
        )


def check_daily_review(daily_review_path: Path, task_id: str, failures: list[str]) -> None:
    try:
        text = daily_review_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing DAILY_REVIEW.md: {daily_review_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read DAILY_REVIEW.md {daily_review_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in DAILY_REVIEW.md.")


def check_worker_result(worker_path: Path, task_id: str, failures: list[str]) -> None:
    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")
        return

    try:
        data = read_json(worker_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(qa_path: Path, task_id: str, failures: list[str]) -> None:
    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")
        return

    try:
        data = read_json(qa_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("POST-RECONCILE VALIDATION: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except ValidationError as exc:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    paths = check_state_files_exist(workspace, failures)

    backlog_record: dict[str, Any] | None = None
    title: str | None = None

    backlog_json_path = paths["backlog_json"]
    backlog_md_path = paths["backlog_md"]
    daily_review_path = paths["daily_review_md"]

    if backlog_json_path.exists():
        backlog_record = check_backlog_json(backlog_json_path, task_id, failures)
        if backlog_record is not None:
            title = normalize_text(backlog_record.get("title"))

    if backlog_md_path.exists():
        check_backlog_markdown(backlog_md_path, task_id, title, failures)

    if daily_review_path.exists():
        check_daily_review(daily_review_path, task_id, failures)

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    check_worker_result(worker_path, task_id, failures)
    check_qa_result(qa_path, task_id, failures)

    if failures:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    status = ""
    if backlog_record is not None:
        status = normalize_text(backlog_record.get("status"))

    print("POST-RECONCILE VALIDATION: PASS")
    print(f"Task: {task_id}")
    if title:
        print(f"Title: {title}")
    if status:
        print(f"Backlog status: {status}")
    print("Passed checks:")
    print("- backlog JSON contains one WCS backlog entry for this task with status done")
    print("- MASTER_BACKLOG.md shows the task id, title, and a done indicator")
    print("- DAILY_REVIEW.md includes the task id")
    print("- worker result exists with matching task_id, allowed status, and non-blank completed_at")
    print("- QA result exists with matching task_id, allowed status, and non-blank completed_at")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### qa_failure_triage.py

- Exact path: `C:\dev\jarvis-workspace\scripts\qa_failure_triage.py`
- Status: active
- Short purpose: Read-only QA failure triage helper for a WCS task

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class QaTriageError(Exception):
    pass


ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise QaTriageError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise QaTriageError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only QA failure triage helper for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise QaTriageError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise QaTriageError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def load_task_packet(workspace: Path, task_id: str) -> Optional[Dict[str, Any]]:
    path = workspace / "tasks" / f"{task_id}_task.json"
    try:
        data = read_json(path)
    except QaTriageError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def load_qa_result(workspace: Path, task_id: str) -> Optional[Dict[str, Any]]:
    path = workspace / "qa" / f"{task_id}_qa_result.json"
    try:
        data = read_json(path)
    except QaTriageError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def classify_failure(
    qa: Optional[Dict[str, Any]],
) -> Tuple[str, str, str, str, bool, Optional[str]]:
    """
    Return:
      (failure_class, confidence, reviewed_status, likely_cause, follow_up_recommended, follow_up_title)
    """
    if qa is None:
        return (
            "ambiguous",
            "low",
            "(missing)",
            "No QA result JSON found; cannot triage without evidence.",
            True,
            "Investigate missing QA result for WCS task",
        )

    status = normalize_text(qa.get("status")).lower()
    summary = normalize_text(qa.get("summary"))
    notes = normalize_text(qa.get("notes"))

    reviewed_status = status if status in ALLOWED_QA_STATUSES else "(invalid)"

    # Environment / setup signatures
    env_markers = [
        "did not become ready",
        "connection refused",
        "ECONNREFUSED",
        "ERR_CONNECTION_REFUSED",
        "Start the app with 'npm run dev'",
        "start the app with 'npm run dev'",
        "server at http://localhost:3000",
        "server at https://localhost:3000",
    ]

    text = f"{summary} {notes}".lower()

    if any(m.lower() in text for m in env_markers):
        failure_class = "environment_setup_failure"
        confidence = "high"
        likely_cause = (
            "Playwright global setup could not reach the local app server "
            "(e.g. localhost:3000 not running or not ready)."
        )
        follow_up_recommended = True
        follow_up_title = (
            "Stabilize local WCS smoke QA server startup for Playwright (npm run dev readiness)."
        )
        return (
            failure_class,
            confidence,
            reviewed_status,
            likely_cause,
            follow_up_recommended,
            follow_up_title,
        )

    # Test harness failures: runner/setup failing before meaningful app checks
    harness_markers = [
        "playwright test was not found",
        "global setup failed",
        "global teardown failed",
        "cannot find module '@playwright/test'",
        "playwright.config",
        "browserType.launch: Failed to launch",
        "browserType.launch: executable doesn't exist",
        "ENV VAR",
        "missing env var",
    ]

    if any(m.lower() in text for m in harness_markers):
        failure_class = "test_harness_failure"
        confidence = "medium"
        likely_cause = (
            "Playwright test harness or global setup/teardown failed before executing meaningful app assertions."
        )
        follow_up_recommended = True
        follow_up_title = "Investigate Playwright harness/global setup failure for WCS smoke QA"
        return (
            failure_class,
            confidence,
            reviewed_status,
            likely_cause,
            follow_up_recommended,
            follow_up_title,
        )

    # Application regression: app reachable but assertions / locators failed
    app_markers = [
        "expect",
        "locator",
        "to be visible",
        "to contain text",
        "AssertionError",
        "Expected",
        "received:",
        "element not found",
        "timed out waiting for selector",
    ]

    if any(m.lower() in text for m in app_markers):
        failure_class = "application_regression"
        confidence = "medium"
        likely_cause = (
            "The app loaded, but one or more smoke assertions/locators failed, "
            "indicating a likely application regression."
        )
        follow_up_recommended = True
        follow_up_title = "Investigate WCS smoke QA regression (home page assertions/locators failing)"
        return (
            failure_class,
            confidence,
            reviewed_status,
            likely_cause,
            follow_up_recommended,
            follow_up_title,
        )

    # No strong signatures matched
    failure_class = "ambiguous"
    confidence = "low"
    likely_cause = (
        "QA result did not match known environment, harness, or regression signatures. "
        "Manual review of QA logs and artifacts is recommended."
    )
    follow_up_recommended = False
    follow_up_title = None
    return (
        failure_class,
        confidence,
        reviewed_status,
        likely_cause,
        follow_up_recommended,
        follow_up_title,
    )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("QA TRIAGE: UNABLE TO CLASSIFY")
        print("Task: (missing)")
        print("Reason: --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except QaTriageError as exc:
        print("QA TRIAGE: UNABLE TO CLASSIFY")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Reason: {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    if not workspace.exists():
        print("QA TRIAGE: UNABLE TO CLASSIFY")
        print(f"Task: {task_id}")
        print(f"Reason: Workspace path does not exist: {workspace}")
        return 1

    task_packet = load_task_packet(workspace, task_id)
    qa_result = load_qa_result(workspace, task_id)

    # Gate behavior by QA status: only triage non-passing or ambiguous QA evidence.
    status_raw = None
    status = ""
    if qa_result is not None:
        status_raw = qa_result.get("status")
        status = normalize_text(status_raw).lower()

    if status == "qa_pass":
        print("QA TRIAGE: NO FAILURE TO TRIAGE")
        print(f"Task: {task_id}")
        print(f"Reviewed QA status: {status}")
        print(
            "Reason: QA triage is intended for failed/escalated/ambiguous QA evidence, "
            "not for qa_pass results."
        )
        return 0

    (
        failure_class,
        confidence,
        reviewed_status,
        likely_cause,
        follow_up_recommended,
        follow_up_title,
    ) = classify_failure(qa_result)

    if failure_class == "ambiguous":
        print("QA TRIAGE: UNABLE TO CLASSIFY" if qa_result is None else "QA TRIAGE: CLASSIFIED")
    else:
        print("QA TRIAGE: CLASSIFIED")

    print(f"Task: {task_id}")
    print(f"Reviewed QA status: {reviewed_status}")
    print(f"Failure class: {failure_class}")
    print(f"Confidence: {confidence}")

    if task_packet is not None:
        title = normalize_text(task_packet.get("title"))
        if title:
            print(f"Task title: {title}")

    if qa_result is not None:
        summary = normalize_text(qa_result.get("summary"))
        if summary:
            print(f"QA summary: {summary}")
        notes = normalize_text(qa_result.get("notes"))
        if notes:
            print(f"QA notes: {notes}")

    print(f"Likely cause: {likely_cause}")
    print(f"Follow-up task recommended: {'yes' if follow_up_recommended else 'no'}")
    if follow_up_title:
        print(f"Suggested follow-up task title: {follow_up_title}")

    # Exit 0 even when classification is ambiguous, as long as processing succeeded.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### generate_task_packet.py

- Exact path: `C:\dev\jarvis-workspace\scripts\generate_task_packet.py`
- Status: active
- Short purpose: Creates task packet files and blank result files
- Note: Current live task packet generation file; included because it is directly responsible for task packet generation.

```python
from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

VALID_STATUSES = {
    "draft",
    "ready",
    "dispatched",
    "in_progress",
    "worker_complete",
    "qa_pass",
    "qa_fail",
    "blocked",
    "escalated",
    "done",
    "deferred",
}

DEFAULT_PROJECT_CONFIG = {
    "WCS": {
        "repo_path": r"C:\dev\wcsv2.0-new",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Run npm run build",
            "Start local app with npm run dev",
            "Run Playwright smoke QA if available",
            "Verify the targeted change locally in the browser",
        ],
        "default_stop_conditions": [
            "Required file cannot be found",
            "Build fails for unrelated reasons",
            "Task scope expands beyond the targeted fix",
        ],
    },
    "N8N": {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Validate workflow or prompt output against the task rubric",
            "Confirm no malformed JSON or broken node configuration",
        ],
        "default_stop_conditions": [
            "Required workflow file cannot be found",
            "Task scope expands beyond the targeted fix",
            "Quality cannot be verified with the current rubric",
        ],
    },
}

TASK_MD_TEMPLATE = """# TASK PACKET

## Header
- Task ID: {task_id}
- Project: {project}
- Title: {title}
- Bucket: {bucket}
- Priority: {priority}
- Risk: {risk}
- Status: {status}

## Repo
- Repo Path: `{repo_path}`
- Branch Name: `{branch_name}`

## Problem Summary
{problem_summary}

## Goal
{goal}

## Suspected Files
{suspected_files_md}

## Acceptance Criteria
{acceptance_criteria_md}

## QA Plan
{qa_plan_md}

## System Impact
{system_impact}

## Stop Conditions
{stop_conditions_md}

## Notes
{notes}
"""


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class PacketGenerationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PacketGenerationError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PacketGenerationError(f"Invalid JSON in {path}: {exc}") from exc



def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")



def is_path_like(value: str) -> bool:
    """
    Treat only clear repo-path-looking values as bounded file scope.
    Examples: 'src/components/Hero.tsx', 'app/about/page.tsx'.
    """
    v = value.strip()
    if not v:
        return False
    lower = v.lower()
    if "/" in v:
        return True
    for ext in (".tsx", ".ts", ".jsx", ".js", ".css", ".scss", ".md"):
        if lower.endswith(ext):
            return True
    return False



def parse_notes_to_files(notes: str) -> list[str]:
    if not notes:
        return []
    cleaned = notes.replace("`", "").strip()
    parts = [part.strip() for part in re.split(r",|;", cleaned) if part.strip()]
    # Only keep values that clearly look like bounded repo paths.
    return [part for part in parts if is_path_like(part)]



def humanize_title_to_problem(title: str) -> str:
    title = title.strip()
    if not title:
        return "Describe the current issue clearly before execution."
    return f"{title}."



def goal_from_title(title: str) -> str:
    if not title.strip():
        return "Complete the scoped task and verify the result."
    return f"Resolve: {title}, with the smallest safe change that satisfies QA."



def acceptance_from_backlog(item: dict[str, Any], suspected_files: list[str]) -> list[str]:
    project = item.get("project", "")
    title = item.get("title", "")
    criteria = [f"The scoped issue is resolved: {title}"] if title else ["The scoped issue is resolved"]
    if project == "WCS":
        criteria.extend([
            "App builds successfully with npm run build",
            "Local app can be opened for verification",
            "Targeted change is visible or behaves correctly on the relevant page/flow",
        ])
    elif project == "N8N":
        criteria.extend([
            "Workflow or prompt output passes the defined quality/rubric check",
            "No malformed JSON or broken node configuration is introduced",
        ])
    if suspected_files:
        criteria.append("Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated")
    return criteria



def system_impact_from_risk(project: str, risk: str, suspected_files: list[str]) -> str:
    base = {
        "low": "Low risk.",
        "medium": "Medium risk.",
        "high": "High risk.",
    }.get(risk, "Risk level not specified.")
    if suspected_files:
        scope = f" Primary expected scope: {', '.join(suspected_files)}."
    else:
        scope = " Scope should stay tightly bounded to the targeted issue."
    if project == "WCS":
        return base + " This should avoid unrelated production-facing behavior changes unless strictly necessary." + scope
    if project == "N8N":
        return base + " This should avoid unrelated workflow, credential, or publishing changes unless strictly necessary." + scope
    return base + scope



def bulletize(items: list[str], fallback: str) -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)



def build_packet_json(item: dict[str, Any], project_cfg: dict[str, Any], dispatch: bool) -> dict[str, Any]:
    task_id = item["task_id"]
    project = item["project"]
    notes = str(item.get("notes", "") or "")
    suspected_files = parse_notes_to_files(notes)
    if not suspected_files:
        raise PacketGenerationError(
            f"Unable to derive bounded file scope for task packet generation for {task_id}."
        )
    ts = now_local()
    status = "dispatched" if dispatch else str(item.get("status", "ready") or "ready")
    if status not in VALID_STATUSES:
        raise PacketGenerationError(f"Task {task_id} has unsupported status: {status}")

    packet = {
        "task_id": task_id,
        "project": project,
        "title": str(item.get("title", "") or ""),
        "bucket": str(item.get("bucket", "") or ""),
        "priority": str(item.get("priority", "") or ""),
        "risk": str(item.get("risk", "") or ""),
        "status": status,
        "repo_path": project_cfg.get("repo_path", ""),
        "branch_name": f"{project_cfg.get('branch_prefix', 'jarvis-task-')}{task_id.lower()}",
        "problem_summary": humanize_title_to_problem(str(item.get("title", "") or "")),
        "goal": goal_from_title(str(item.get("title", "") or "")),
        "suspected_files": suspected_files,
        "acceptance_criteria": acceptance_from_backlog(item, suspected_files),
        "qa_plan": deepcopy(project_cfg.get("default_qa_plan", [])),
        "system_impact": system_impact_from_risk(project, str(item.get("risk", "") or ""), suspected_files),
        "stop_conditions": deepcopy(project_cfg.get("default_stop_conditions", [])),
        "notes": notes,
        "created_at": ts,
        "updated_at": ts,
    }
    return packet



def build_packet_markdown(packet: dict[str, Any]) -> str:
    suspected_files_md = bulletize(packet.get("suspected_files", []), "Confirm the target files before execution")
    acceptance_md = bulletize(packet.get("acceptance_criteria", []), "Add acceptance criteria before execution")
    qa_plan_md = bulletize(packet.get("qa_plan", []), "Add a QA plan before execution")
    stop_md = bulletize(packet.get("stop_conditions", []), "Add stop conditions before execution")
    notes = packet.get("notes") or "No additional notes."

    return TASK_MD_TEMPLATE.format(
        task_id=packet.get("task_id", ""),
        project=packet.get("project", ""),
        title=packet.get("title", ""),
        bucket=packet.get("bucket", ""),
        priority=packet.get("priority", ""),
        risk=packet.get("risk", ""),
        status=packet.get("status", ""),
        repo_path=packet.get("repo_path", ""),
        branch_name=packet.get("branch_name", ""),
        problem_summary=packet.get("problem_summary", ""),
        goal=packet.get("goal", ""),
        suspected_files_md=suspected_files_md,
        acceptance_criteria_md=acceptance_md,
        qa_plan_md=qa_plan_md,
        system_impact=packet.get("system_impact", ""),
        stop_conditions_md=stop_md,
        notes=notes,
    )



def create_blank_result(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "executor": "",
        "summary": "",
        "files_changed": [],
        "commands_run": [],
        "issues_encountered": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_qa(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "qa_tool": "",
        "summary": "",
        "checks_run": [],
        "checks_passed": [],
        "checks_failed": [],
        "artifacts": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_escalation(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "reason": "",
        "details": "",
        "recommended_next_action": "",
        "created_at": "",
    }



def maybe_write(path: Path, content: str | dict[str, Any], *, force: bool) -> tuple[bool, str]:
    if path.exists() and not force:
        return False, f"SKIPPED (exists): {path}"
    if isinstance(content, str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    else:
        save_json(path, content)
    return True, f"WROTE: {path}"



def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, new_status: str) -> None:
    for item in backlog_items:
        if item.get("task_id") == task_id:
            item["status"] = new_status
            return
    raise PacketGenerationError(f"Task {task_id} not found while updating backlog status")



def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        notes = str(item.get("notes", "") or "")
        lines.append(
            f"| {item.get('task_id','')} | {item.get('project','')} | {item.get('bucket','')} | {item.get('priority','')} | {item.get('risk','')} | {item.get('status','')} | {item.get('title','')} | {notes} |"
        )
    lines.append("")
    return "\n".join(lines)



def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Jarvis task packet files from master_backlog.json")
    parser.add_argument("--task", help="Task ID to generate, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite packet/result/qa/escalation files if they already exist")
    parser.add_argument("--dispatch", action="store_true", help="Mark the backlog item as dispatched when generating files")
    parser.add_argument("--list-ready", action="store_true", help="List ready tasks and exit")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    tasks_dir = workspace / "tasks"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise PacketGenerationError(f"Expected a JSON array in {backlog_json_path}")

    if args.list_ready:
        ready = [item for item in backlog if str(item.get("status", "")).lower() == "ready"]
        if not ready:
            print("No ready tasks found.")
            return 0
        print("Ready tasks:")
        for item in ready:
            print(f"- {item.get('task_id')}: {item.get('title')}")
        return 0

    if not args.task:
        parser.error("--task is required unless --list-ready is used")

    task_id = args.task.strip().upper()
    item = next((row for row in backlog if str(row.get("task_id", "")).upper() == task_id), None)
    if not item:
        raise PacketGenerationError(f"Task {task_id} not found in {backlog_json_path}")

    project = str(item.get("project", "") or "")
    project_cfg = DEFAULT_PROJECT_CONFIG.get(project, {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": ["Run the project-appropriate QA checks"],
        "default_stop_conditions": ["Task scope expands beyond the targeted fix"],
    })

    packet = build_packet_json(item, project_cfg, dispatch=args.dispatch)
    packet_md = build_packet_markdown(packet)

    task_json_path = tasks_dir / f"{task_id}_task.json"
    task_md_path = tasks_dir / f"{task_id}_task.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    outputs = [
        maybe_write(task_json_path, packet, force=args.force),
        maybe_write(task_md_path, packet_md, force=args.force),
        maybe_write(worker_result_path, create_blank_result(task_id), force=args.force),
        maybe_write(qa_result_path, create_blank_qa(task_id), force=args.force),
        maybe_write(escalation_path, create_blank_escalation(task_id), force=args.force),
    ]

    if args.dispatch:
        update_backlog_status(backlog, task_id, "dispatched")
        save_json(backlog_json_path, backlog)
        backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")
        print(f"UPDATED backlog status to dispatched for {task_id}")
        print(f"RENDERED: {backlog_md_path}")

    for _, message in outputs:
        print(message)

    print("\nTask packet generation complete.")
    print(f"Task packet markdown: {task_md_path}")
    print(f"Task packet JSON:     {task_json_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PacketGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
```

### jarvis.py

- Exact path: `C:\dev\jarvis-workspace\scripts\jarvis.py`
- Status: active
- Short purpose: Phase 3 foreman; reads backlog and project status, validates task eligibility, prepares and verifies WCS task branch, manages task packets, writes daily_plan and run_log, and records durable escalation state on hard failure
- Note: Included because the current live foreman also records durable escalation state on hard failure.

```python
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class JarvisError(Exception):
    pass


PRIORITY_ORDER = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
ELIGIBLE_BUCKETS = {"broken", "ugly"}
ALLOWED_PROJECT = "WCS"
REQUIRED_TASK_FIELDS = {"task_id", "project", "bucket", "priority", "risk", "status", "title"}
PLACEHOLDER_STATUS = "draft"


ESCALATIONS_JSON_NAME = "escalations.json"
ESCALATIONS_MD_NAME = "ESCALATIONS.md"


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today_local_date() -> str:
    return datetime.now().astimezone().date().isoformat()


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path, expected_type: type | None = None) -> Any:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise JarvisError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise JarvisError(f"Invalid JSON in {path}: {exc}") from exc

    if expected_type is not None and not isinstance(data, expected_type):
        raise JarvisError(
            f"Expected {expected_type.__name__} in {path}, got {type(data).__name__}"
        )
    return data


def read_optional_json(path: Path, default: Any, expected_type: type | None = None) -> Any:
    if not path.exists():
        return default
    return read_json(path, expected_type=expected_type)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_escalations(escalations_path: Path) -> list[dict[str, Any]]:
    """Load existing escalations, initializing an empty list if the file does not exist."""
    if not escalations_path.exists():
        return []
    data = read_json(escalations_path, expected_type=list)
    # Defensive: ensure list of dict-like items
    cleaned: list[dict[str, Any]] = []
    for item in data:
        if isinstance(item, dict):
            cleaned.append(item)
    return cleaned


def render_escalations_md(records: list[dict[str, Any]]) -> str:
    lines = ["# ESCALATIONS", ""]
    if not records:
        lines.append("_No escalations recorded._")
        return "\n".join(lines)

    for record in records:
        timestamp = normalize_text(record.get("timestamp"))
        reason_code = normalize_text(record.get("reason_code"))
        human_action_required = "yes" if bool(record.get("human_action_required")) else "no"

        lines.extend(
            [
                f"## {timestamp} - {reason_code}",
                "",
                f"- **Task ID:** {normalize_text(record.get('task_id'))}",
                f"- **Project:** {normalize_text(record.get('project'))}",
                f"- **Phase:** {normalize_text(record.get('phase'))}",
                f"- **Severity:** {normalize_text(record.get('severity'))}",
                f"- **Status:** {normalize_text(record.get('status'))}",
                f"- **Human action required:** {human_action_required}",
                f"- **Summary:** {normalize_text(record.get('summary'))}",
                "",
                "- **Details:**",
            ]
        )

        details = record.get("details")
        if isinstance(details, list) and details:
            for detail in details:
                lines.append(f"  - {normalize_text(detail)}")
        else:
            lines.append("  - (none)")

        lines.extend(
            [
                "",
                f"- **Recommended next action:** {normalize_text(record.get('recommended_next_action'))}",
                "",
            ]
        )

    return "\n".join(lines).rstrip()


def append_escalation(
    *,
    state_dir: Path,
    task_id: str,
    phase: str,
    reason_code: str,
    summary: str,
    details: list[str],
    recommended_next_action: str,
) -> None:
    """Append a durable escalation record and render the markdown view."""
    escalations_path = state_dir / ESCALATIONS_JSON_NAME
    escalations_md_path = state_dir / ESCALATIONS_MD_NAME

    records = load_escalations(escalations_path)

    record = {
        "timestamp": now_local_iso(),
        "task_id": normalize_text(task_id).upper(),
        "project": ALLOWED_PROJECT,
        "phase": phase,
        "severity": "error",
        "status": "open",
        "human_action_required": True,
        "reason_code": reason_code,
        "summary": summary,
        "details": details,
        "recommended_next_action": recommended_next_action,
    }
    records.append(record)
    write_json(escalations_path, records)
    write_text(escalations_md_path, render_escalations_md(records))

    print("")
    print("JARVIS: escalation recorded")
    print(f"- JSON: {escalations_path}")
    print(f"- Markdown: {escalations_md_path}")


def parse_task_number(task_id: str) -> int:
    task_id = normalize_text(task_id).upper()
    if not task_id.startswith("WCS-"):
        raise JarvisError(f"Expected task id like WCS-016. Got: {task_id}")
    number_part = task_id.split("-", 1)[1]
    if not number_part.isdigit():
        raise JarvisError(f"Expected numeric WCS task id suffix. Got: {task_id}")
    return int(number_part)


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def priority_rank(task: dict[str, Any]) -> int:
    return PRIORITY_ORDER.get(normalize_text(task.get("priority")).upper(), 999)


def risk_rank(task: dict[str, Any]) -> int:
    return RISK_ORDER.get(normalize_text(task.get("risk")).lower(), 999)


def validate_task_shape(task: dict[str, Any], *, context: str) -> None:
    missing = [field for field in sorted(REQUIRED_TASK_FIELDS) if not normalize_text(task.get(field))]
    if missing:
        raise JarvisError(f"{context}: task is missing required fields: {', '.join(missing)}")

    task_id = normalize_text(task.get("task_id")).upper()
    parse_task_number(task_id)

    project = normalize_text(task.get("project")).upper()
    if project != ALLOWED_PROJECT:
        raise JarvisError(f"{context}: task project must be {ALLOWED_PROJECT}. Found: {project}")

    bucket = normalize_text(task.get("bucket")).lower()
    if bucket not in ELIGIBLE_BUCKETS:
        raise JarvisError(
            f"{context}: task bucket must be one of {sorted(ELIGIBLE_BUCKETS)}. Found: {bucket}"
        )

    status = normalize_text(task.get("status")).lower()
    if status != "ready":
        raise JarvisError(f"{context}: task status must be ready for execution. Found: {status}")

    priority = normalize_text(task.get("priority")).upper()
    if priority not in PRIORITY_ORDER:
        raise JarvisError(f"{context}: invalid priority: {priority}")

    risk = normalize_text(task.get("risk")).lower()
    if risk not in RISK_ORDER:
        raise JarvisError(f"{context}: invalid risk: {risk}")


def validate_backlog_task_uniqueness(backlog: list[dict[str, Any]], task_id: str) -> None:
    normalized = normalize_text(task_id).upper()
    matches = [
        task for task in backlog
        if isinstance(task, dict) and normalize_text(task.get("task_id")).upper() == normalized
    ]
    if len(matches) != 1:
        raise JarvisError(
            f"Backlog must contain exactly one entry for {normalized}. Found: {len(matches)}"
        )


def is_ready_wcs_task(task: dict[str, Any]) -> bool:
    if normalize_text(task.get("project")).upper() != ALLOWED_PROJECT:
        return False
    if normalize_text(task.get("status")).lower() != "ready":
        return False
    if normalize_text(task.get("bucket")).lower() not in ELIGIBLE_BUCKETS:
        return False
    task_id = normalize_text(task.get("task_id")).upper()
    return task_id.startswith("WCS-")


def select_task(backlog: list[dict[str, Any]]) -> dict[str, Any]:
    eligible = [task for task in backlog if isinstance(task, dict) and is_ready_wcs_task(task)]
    if not eligible:
        raise JarvisError("No eligible ready WCS task found in master_backlog.json.")

    try:
        eligible.sort(
            key=lambda task: (
                priority_rank(task),
                risk_rank(task),
                parse_task_number(normalize_text(task.get("task_id"))),
            )
        )
    except JarvisError:
        raise
    except Exception as exc:
        raise JarvisError(f"Failed to sort eligible tasks: {exc}") from exc

    return eligible[0]


def get_backlog_task_by_id(backlog: list[dict[str, Any]], task_id: str) -> dict[str, Any] | None:
    normalized = normalize_text(task_id).upper()
    for task in backlog:
        if not isinstance(task, dict):
            continue
        if normalize_text(task.get("task_id")).upper() == normalized:
            return task
    return None


def task_selected_today(
    daily_plan: dict[str, Any],
    run_log: list[dict[str, Any]],
    current_date: str,
) -> dict[str, Any] | None:
    selected_task = daily_plan.get("selected_task")
    generated_at = normalize_text(daily_plan.get("generated_at"))

    if isinstance(selected_task, dict) and generated_at.startswith(current_date):
        return selected_task

    for entry in reversed(run_log):
        if not isinstance(entry, dict):
            continue
        if normalize_text(entry.get("event")) != "task_selected":
            continue
        timestamp = normalize_text(entry.get("timestamp"))
        if not timestamp.startswith(current_date):
            continue
        task_id = normalize_text(entry.get("task_id"))
        if task_id:
            return {"task_id": task_id}
    return None


def build_daily_plan(selected_task: dict[str, Any], timestamp: str) -> dict[str, Any]:
    return {
        "generated_at": timestamp,
        "selected_task": selected_task,
        "selection_reason": {
            "rule": "priority_risk_task_id",
            "details": (
                "Selected highest-priority eligible ready WCS task using deterministic "
                "ordering (priority, then risk, then numeric task id)."
            ),
        },
    }


def render_daily_plan_md(plan: dict[str, Any]) -> str:
    selected_task = plan.get("selected_task", {})
    selection_reason = plan.get("selection_reason", {})
    lines = [
        "# DAILY PLAN",
        "",
        f"**Generated at:** {normalize_text(plan.get('generated_at'))}",
        "",
        "## Selected Task",
        "",
        f"- **Task ID:** {normalize_text(selected_task.get('task_id'))}",
        f"- **Project:** {normalize_text(selected_task.get('project'))}",
        f"- **Bucket:** {normalize_text(selected_task.get('bucket'))}",
        f"- **Priority:** {normalize_text(selected_task.get('priority'))}",
        f"- **Risk:** {normalize_text(selected_task.get('risk'))}",
        f"- **Status:** {normalize_text(selected_task.get('status'))}",
        f"- **Title:** {normalize_text(selected_task.get('title'))}",
        f"- **Notes:** {normalize_text(selected_task.get('notes'))}",
        "",
        "## Selection Reason",
        "",
        f"- **Rule:** {normalize_text(selection_reason.get('rule'))}",
        f"- **Details:** {normalize_text(selection_reason.get('details'))}",
    ]
    return "\n".join(lines)


def render_run_log_md(run_log: list[dict[str, Any]]) -> str:
    lines = ["# RUN LOG", ""]
    if not run_log:
        lines.append("_No run log entries yet._")
        return "\n".join(lines)

    for entry in run_log:
        lines.extend(
            [
                f"## {normalize_text(entry.get('timestamp'))} — {normalize_text(entry.get('event'))}",
                "",
                f"- **Task ID:** {normalize_text(entry.get('task_id'))}",
                f"- **Project:** {normalize_text(entry.get('project'))}",
                f"- **Title:** {normalize_text(entry.get('title'))}",
                f"- **Summary:** {normalize_text(entry.get('summary'))}",
            ]
        )
        artifacts = entry.get("artifacts")
        if isinstance(artifacts, list) and artifacts:
            lines.append("- **Artifacts:**")
            for artifact in artifacts:
                lines.append(f"  - {normalize_text(artifact)}")
        lines.append("")
    return "\n".join(lines).rstrip()


def build_run_log_entry(
    *,
    event: str,
    selected_task: dict[str, Any],
    timestamp: str,
    summary: str,
    artifacts: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "timestamp": timestamp,
        "event": event,
        "task_id": normalize_text(selected_task.get("task_id")).upper(),
        "project": normalize_text(selected_task.get("project")).upper(),
        "title": normalize_text(selected_task.get("title")),
        "summary": summary,
        "artifacts": artifacts or [],
    }


def append_run_log_entry(
    run_log_json_path: Path,
    run_log_md_path: Path,
    run_log: list[dict[str, Any]],
    entry: dict[str, Any],
) -> None:
    run_log.append(entry)
    write_json(run_log_json_path, run_log)
    write_text(run_log_md_path, render_run_log_md(run_log))


def task_artifact_paths(workspace: Path, task_id: str) -> dict[str, Path]:
    normalized_task_id = normalize_text(task_id).upper()
    return {
        "task_json": workspace / "tasks" / f"{normalized_task_id}_task.json",
        "task_md": workspace / "tasks" / f"{normalized_task_id}_task.md",
        "worker_result": workspace / "results" / f"{normalized_task_id}_worker_result.json",
        "qa_result": workspace / "qa" / f"{normalized_task_id}_qa_result.json",
        "escalation": workspace / "logs" / f"{normalized_task_id}_escalation.json",
    }


def analyze_artifacts(artifact_map: dict[str, Path]) -> tuple[list[Path], list[Path]]:
    existing = []
    missing = []
    for path in artifact_map.values():
        if path.exists():
            existing.append(path)
        else:
            missing.append(path)
    return existing, missing


def run_packet_generator(workspace: Path, task_id: str, *, force_packet: bool) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "generate_task_packet.py"
    if not helper_path.exists():
        raise JarvisError(f"Packet generator not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]
    if force_packet:
        cmd.append("--force")

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def run_branch_preparer(workspace: Path, task_id: str) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "prepare_wcs_task_branch.py"
    if not helper_path.exists():
        raise JarvisError(f"Branch preparer not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def parse_branch_prep_output(stdout: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip().upper()] = value.strip()
    return parsed


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def verify_repo_branch_state(repo_path: Path) -> dict[str, str]:
    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise JarvisError(
            current_branch_result.stderr.strip() or f"Failed to inspect repo branch at {repo_path}"
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise JarvisError(
            status_result.stderr.strip() or f"Failed to inspect repo status at {repo_path}"
        )

    current_branch = current_branch_result.stdout.strip()
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    return {
        "current_branch": current_branch,
        "dirty": "true" if dirty_lines else "false",
        "dirty_count": str(len(dirty_lines)),
    }


def validate_task_json_contract(path: Path, expected_task: dict[str, Any]) -> None:
    data = read_json(path, expected_type=dict)
    expected_id = normalize_text(expected_task.get("task_id")).upper()

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != expected_id:
        raise JarvisError(f"{path}: task_id mismatch. Expected {expected_id}, found {actual_id}")

    required = ["task_id", "title"]
    missing = [field for field in required if not normalize_text(data.get(field))]
    if missing:
        raise JarvisError(f"{path}: missing required task packet fields: {', '.join(missing)}")


def validate_result_placeholder_contract(path: Path, expected_task_id: str, kind: str) -> None:
    data = read_json(path, expected_type=dict)
    actual_id = normalize_text(data.get("task_id")).upper()
    expected_id = normalize_text(expected_task_id).upper()

    if actual_id != expected_id:
        raise JarvisError(f"{path}: {kind} task_id mismatch. Expected {expected_id}, found {actual_id}")

    status = normalize_text(data.get("status")).lower()
    if status != PLACEHOLDER_STATUS:
        raise JarvisError(
            f"{path}: expected placeholder status '{PLACEHOLDER_STATUS}' before execution. Found: {status}"
        )

    completed_at = data.get("completed_at")
    if normalize_text(completed_at):
        raise JarvisError(f"{path}: placeholder completed_at must be blank before execution")

    if kind == "worker_result":
        for field in ["executor", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing worker placeholder field: {field}")
        for list_field in ["files_changed", "commands_run", "issues_encountered"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: worker placeholder field must be a list: {list_field}")

    if kind == "qa_result":
        for field in ["qa_tool", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing QA placeholder field: {field}")
        for list_field in ["checks_run", "checks_passed", "checks_failed", "artifacts"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: QA placeholder field must be a list: {list_field}")


def validate_existing_artifacts(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()

    if not artifact_map["task_md"].exists():
        raise JarvisError(f"Existing packet set is invalid: missing markdown packet: {artifact_map['task_md']}")
    if not artifact_map["escalation"].exists():
        raise JarvisError(
            f"Existing packet set is invalid: missing escalation file: {artifact_map['escalation']}"
        )

    validate_task_json_contract(artifact_map["task_json"], selected_task)
    validate_result_placeholder_contract(artifact_map["worker_result"], task_id, "worker_result")
    validate_result_placeholder_contract(artifact_map["qa_result"], task_id, "qa_result")


def validate_generated_placeholders(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    for path in artifact_map.values():
        if not path.exists():
            raise JarvisError(f"Expected generated artifact not found after packet generation: {path}")

    validate_existing_artifacts(artifact_map, selected_task)


def print_mode_banner(mode: str) -> None:
    print("=" * 72)
    print(f"JARVIS MODE: {mode}")
    print("=" * 72)


def print_packet_placeholder_warning(task_id: str, artifact_map: dict[str, Path], skipped_existing: bool) -> None:
    print("")
    print("JARVIS: artifact safety warning")
    print(
        "These task packet result files are placeholders until the worker result and QA result are filled truthfully."
    )
    print("They are NOT execution proof and do NOT mean the task is reconcile-ready.")
    print(f"- Worker placeholder: {artifact_map['worker_result']}")
    print(f"- QA placeholder:     {artifact_map['qa_result']}")
    print(f"- Escalation file:   {artifact_map['escalation']}")
    if skipped_existing:
        print("")
        print("JARVIS: packet generation was skipped because all artifacts already exist.")
        print("That does NOT mean the task is complete.")
        print("Existing packet/result artifacts were contract-validated before continuing.")
        print("Inspect existing worker/QA result contents before relying on them.")


def print_result_contracts() -> None:
    print("")
    print("JARVIS: result contracts")
    print("- Worker result status must be one of: worker_complete | blocked | escalated")
    print("- QA result status must be one of: qa_pass | qa_fail | escalated")
    print("- Keep completed_at blank in worker/QA result files until stamp_result_timestamp.py runs")


def print_contract_validation_summary(
    selected_task: dict[str, Any],
    packet_validated: bool,
    task_validated: bool,
) -> None:
    print("")
    print("JARVIS: contract validation")
    print(f"- Selected task execution-eligible: {'yes' if task_validated else 'no'}")
    print(f"- Packet/result placeholder contract valid: {'yes' if packet_validated else 'no'}")
    print(f"- Selected task: {normalize_text(selected_task.get('task_id')).upper()}")


def print_next_steps(
    selected_task: dict[str, Any],
    workspace: Path,
    repo_path: Path,
    artifact_map: dict[str, Path],
    branch_name: str,
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()
    print("")
    print("JARVIS: foreman phase complete")
    print("TASK IS NOT COMPLETE YET")
    print("Do NOT run reconcile until code is committed, worker result is final, QA result is final, and both are stamped.")
    print("")
    print("Next steps:")
    print(f"1. Open repo: {repo_path}")
    print("2. Verify git state:")
    print("   - git branch --show-current")
    print("   - git status")
    print(f"3. Confirm branch is: {branch_name}")
    print("4. Review task packet:")
    print(f"   - {artifact_map['task_json']}")
    print(f"   - {artifact_map['task_md']}")
    print("5. Perform the bounded implementation only")
    print("6. Inspect the diff before commit")
    print(f"   - git diff -- {normalize_text(selected_task.get('notes')) or '<target_file>'}")
    print("7. Commit on the correct task branch")
    print(f"8. Finalize worker result JSON: {artifact_map['worker_result']}")
    print("9. Run QA (current live path):")
    print("   - npm run build")
    print("   - npm run test:e2e:smoke")
    print(f"10. Finalize QA result JSON: {artifact_map['qa_result']}")
    print("11. Stamp timestamps:")
    print(f"   - python .\\stamp_result_timestamp.py ..\\results\\{task_id}_worker_result.json")
    print(f"   - python .\\stamp_result_timestamp.py ..\\qa\\{task_id}_qa_result.json")
    print("12. Reconcile only when ready:")
    print(f"   - python .\\reconcile_task_outcome.py --task {task_id}")
    print("")
    print("Working process/documentation files should be updated whenever a new process rule or hardening change is locked in.")
    print(f"Workspace: {workspace}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Jarvis foreman v6: select or reuse one WCS task, validate task/artifact contracts, generate packet artifacts, prepare the correct repo branch, and print operator-safe handoff guidance."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow a new selection even if a WCS task was already selected today.",
    )
    parser.add_argument(
        "--force-packet",
        action="store_true",
        help="Force overwrite of existing task packet/result/qa/escalation files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = script_path.parent.parent
    state_dir = workspace / "state"

    backlog_path = state_dir / "master_backlog.json"
    project_status_path = state_dir / "project_status_wcs.json"
    daily_plan_json_path = state_dir / "daily_plan.json"
    daily_plan_md_path = state_dir / "DAILY_PLAN.md"
    run_log_json_path = state_dir / "run_log.json"
    run_log_md_path = state_dir / "RUN_LOG.md"

    try:
        backlog = read_json(backlog_path, expected_type=list)
        project_status_wcs = read_json(project_status_path, expected_type=dict)
        daily_plan = read_optional_json(daily_plan_json_path, default={}, expected_type=dict)
        run_log = read_optional_json(run_log_json_path, default=[], expected_type=list)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id="",
            phase="jarvis_state_load",
            reason_code="invalid_json_state",
            summary="Jarvis failed to load required JSON state during startup.",
            details=[str(exc)],
            recommended_next_action="Inspect the referenced JSON file, repair or restore it, then rerun jarvis.py.",
        )
        print("JARVIS: hard failure while loading required JSON state.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    current_date = today_local_date()
    current_timestamp = now_local_iso()

    used_existing_selection = False
    mode_banner = "NEW_SELECTION_NO_EXISTING_TODAY_TASK"

    try:
        if not args.force:
            existing_today = task_selected_today(daily_plan, run_log, current_date)
            if existing_today:
                existing_task_id = normalize_text(existing_today.get("task_id"))
                backlog_match = get_backlog_task_by_id(backlog, existing_task_id)
                if not backlog_match:
                    raise JarvisError(
                        f"Daily plan references task {existing_task_id}, but that task was not found in master_backlog.json."
                    )
                selected_task = backlog_match
                used_existing_selection = True
                mode_banner = "REUSING_ALREADY_SELECTED_TASK"
            else:
                selected_task = select_task(backlog)
        else:
            selected_task = select_task(backlog)
            mode_banner = "FORCED_FRESH_SELECTION"

        task_id = normalize_text(selected_task.get("task_id")).upper()
        validate_backlog_task_uniqueness(backlog, task_id)
        validate_task_shape(selected_task, context=f"Selected task {task_id}")
        task_validated = True
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=locals().get("task_id", ""),
            phase="jarvis_selection",
            reason_code="invalid_selected_task",
            summary="Jarvis failed to select a valid execution-eligible WCS task.",
            details=[str(exc)],
            recommended_next_action="Inspect the backlog entry and project status for this task, correct invalid fields or duplicates, then rerun jarvis.py.",
        )
        print("JARVIS: task selection/validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    if not used_existing_selection:
        plan = build_daily_plan(selected_task, current_timestamp)
        selection_entry = build_run_log_entry(
            event="task_selected",
            selected_task=selected_task,
            timestamp=current_timestamp,
            summary="Jarvis selected task for current daily plan.",
        )

        write_json(daily_plan_json_path, plan)
        write_text(daily_plan_md_path, render_daily_plan_md(plan))
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, selection_entry)
    else:
        plan = daily_plan

    artifact_map = task_artifact_paths(workspace, task_id)
    existing_artifacts, missing_artifacts = analyze_artifacts(artifact_map)

    packet_generated = False
    packet_skipped_existing = False
    packet_contract_validated = False

    if existing_artifacts and missing_artifacts and not args.force_packet:
        message = (
            "Partial packet artifact state detected. Some packet files already exist, but not all of them. "
            "Inspect the task artifacts and rerun with --force-packet only if overwrite is intentional.\n"
            + "\n".join(f"- existing: {path}" for path in existing_artifacts)
            + "\n"
            + "\n".join(f"- missing: {path}" for path in missing_artifacts)
        )
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="partial_packet_artifacts",
            summary="Jarvis detected partial packet artifact state for the selected task.",
            details=[message],
            recommended_next_action="Inspect existing/missing packet artifacts, decide whether to clean up or rerun with --force-packet, then rerun jarvis.py.",
        )
        print("JARVIS: partial packet artifact state detected.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    try:
        if existing_artifacts and not missing_artifacts and not args.force_packet:
            validate_existing_artifacts(artifact_map, selected_task)
            packet_contract_validated = True
            packet_skipped_existing = True
        else:
            returncode, packet_stdout, packet_stderr = run_packet_generator(
                workspace,
                task_id,
                force_packet=args.force_packet,
            )

            if returncode != 0:
                append_escalation(
                    state_dir=state_dir,
                    task_id=task_id,
                    phase="jarvis_packet_validation",
                    reason_code="packet_contract_mismatch",
                    summary="Jarvis packet generator reported a non-zero exit code.",
                    details=[
                        f"Return code: {returncode}",
                        f"STDERR: {packet_stderr.strip() or '(no stderr output)'}",
                    ],
                    recommended_next_action="Inspect generate_task_packet.py output, fix the underlying issue, then rerun jarvis.py (optionally with --force-packet).",
                )
                print("JARVIS: packet generation failed.", file=sys.stderr)
                print("An escalation record was written for operator follow-up.", file=sys.stderr)
                raise SystemExit(returncode)

            validate_generated_placeholders(artifact_map, selected_task)
            packet_contract_validated = True
            packet_generated = True
            packet_event = build_run_log_entry(
                event="task_packet_generated",
                selected_task=selected_task,
                timestamp=now_local_iso(),
                summary="Jarvis generated task packet and contract-valid placeholder execution artifacts.",
                artifacts=[str(path) for path in artifact_map.values()],
            )
            append_run_log_entry(run_log_json_path, run_log_md_path, run_log, packet_event)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="packet_contract_mismatch",
            summary="Jarvis detected invalid or mismatched packet/result placeholder contracts.",
            details=[str(exc)],
            recommended_next_action="Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet).",
        )
        print("JARVIS: packet/result placeholder contract validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_returncode, branch_stdout, branch_stderr = run_branch_preparer(workspace, task_id)

    if branch_returncode != 0:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_preparation",
            reason_code="branch_prepare_failed",
            summary="Jarvis branch preparer reported a non-zero exit code.",
            details=[
                f"Return code: {branch_returncode}",
                f"STDERR: {branch_stderr.strip() or '(no stderr output)'}",
            ],
            recommended_next_action="Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py.",
        )
        print("JARVIS: branch preparation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(branch_returncode)

    branch_info = parse_branch_prep_output(branch_stdout)
    target_branch = branch_info.get("TARGET_BRANCH", task_branch_name(task_id))
    repo_path = Path(
        branch_info.get("REPO_PATH") or normalize_text(project_status_wcs.get("repo_path"))
    ).resolve()

    try:
        verified_repo_state = verify_repo_branch_state(repo_path)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="repo_inspection_failed",
            summary="Jarvis failed to inspect the WCS repo branch/status after preparation.",
            details=[str(exc)],
            recommended_next_action="Inspect the WCS repo manually (branch and status), resolve issues, then rerun jarvis.py.",
        )
        print("JARVIS: repo branch/status inspection failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_mode = branch_info.get("MODE", "")
    if branch_mode in {"switched_to_existing_target", "created_new_target_from_main"}:
        branch_event = build_run_log_entry(
            event="task_branch_prepared",
            selected_task=selected_task,
            timestamp=now_local_iso(),
            summary=f"Jarvis prepared repo branch for task execution: {target_branch}",
            artifacts=[target_branch, str(repo_path)],
        )
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, branch_event)

    print_mode_banner(mode_banner)

    if used_existing_selection:
        print("JARVIS: using existing task selected today")
    else:
        print("JARVIS: task selected")
        print(f"Workspace: {workspace}")
        print(f"Priority: {normalize_text(selected_task.get('priority'))}")
        print(f"Risk: {normalize_text(selected_task.get('risk'))}")
        print(f"Bucket: {normalize_text(selected_task.get('bucket'))}")
        print(f"daily_plan.json: {daily_plan_json_path}")
        print(f"DAILY_PLAN.md: {daily_plan_md_path}")
        print(f"run_log.json: {run_log_json_path}")
        print(f"RUN_LOG.md: {run_log_md_path}")

    print(f"Task ID: {task_id}")
    print(f"Title: {normalize_text(selected_task.get('title'))}")

    print("")
    if packet_skipped_existing:
        print("JARVIS: packet generation skipped")
        print("Reason: all packet artifacts already exist for this task. Use --force-packet to overwrite.")
        for path in artifact_map.values():
            print(f"- {path}")
    elif packet_generated:
        print("JARVIS: packet generation complete")
        for path in artifact_map.values():
            print(f"WROTE: {path}")
        print("")
        print("Task packet generation complete.")
        print(f"Task packet markdown: {artifact_map['task_md']}")
        print(f"Task packet JSON:     {artifact_map['task_json']}")

    print("")
    print("JARVIS: branch preparation result")
    for line in branch_stdout.strip().splitlines():
        print(line)

    print("")
    print("JARVIS: final branch verification")
    print(f"VERIFIED_REPO_PATH: {repo_path}")
    print(f"VERIFIED_CURRENT_BRANCH: {verified_repo_state['current_branch']}")
    print(f"VERIFIED_EXPECTED_BRANCH: {target_branch}")
    print(f"VERIFIED_DIRTY: {verified_repo_state['dirty']}")
    print(f"VERIFIED_DIRTY_COUNT: {verified_repo_state['dirty_count']}")

    if verified_repo_state["current_branch"] != target_branch:
        details = [
            "Post-branch-prep verification failed. Repo is not on the expected task branch.",
            f"Expected: {target_branch}",
            f"Actual:   {verified_repo_state['current_branch']}",
        ]
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="branch_verification_failed",
            summary="Jarvis detected a branch mismatch after branch preparation.",
            details=details,
            recommended_next_action="Switch the WCS repo to the expected task branch or repair the branch state, then rerun jarvis.py.",
        )
        print("JARVIS: post-branch-prep branch verification failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    print_contract_validation_summary(selected_task, packet_contract_validated, task_validated)
    print_packet_placeholder_warning(task_id, artifact_map, packet_skipped_existing)
    print_result_contracts()
    print_next_steps(selected_task, workspace, repo_path, artifact_map, target_branch)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except JarvisError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        # Record a generic escalation when a JarvisError bubbles out that was not already
        # handled by a more specific escalation path.
        script_path = Path(__file__).resolve()
        state_dir = script_path.parent.parent / "state"
        try:
            append_escalation(
                state_dir=state_dir,
                task_id="",
                phase="jarvis_preflight",
                reason_code="invalid_json_state",
                summary="Jarvis encountered an unhandled JarvisError.",
                details=[str(exc)],
                recommended_next_action="Inspect the error message and recent changes, repair the underlying issue, then rerun jarvis.py.",
            )
        except Exception:
            # If escalation writing itself fails, avoid masking the original error.
            pass
        print("JARVIS: an escalation record may have been written for this failure.", file=sys.stderr)
        raise SystemExit(1)
```

No separate dedicated pause-handling script was found in the current live workspace. Pause/stop behavior is currently expressed through guard scripts, operator flow, and foreman/escalation behavior rather than a single dedicated pause file.

## 4. Current Templates / Schemas / Contracts

### task_packet.template.json

- Exact path: `C:\dev\jarvis-workspace\templates\task_packet.template.json`
- Status: active
- Short purpose: Formal task packet JSON template.

```json
{
  "task_id": "",
  "project": "WCS",
  "title": "",
  "bucket": "",
  "priority": "",
  "risk": "",
  "status": "ready",
  "repo_path": "C:\\dev\\wcsv2.0-new",
  "branch_name": "",
  "problem_summary": "",
  "goal": "",
  "suspected_files": [],
  "acceptance_criteria": [],
  "qa_plan": [],
  "system_impact": "",
  "stop_conditions": [],
  "notes": "",
  "created_at": "",
  "updated_at": ""
}
```

### task_packet.template.md

- Exact path: `C:\dev\jarvis-workspace\templates\task_packet.template.md`
- Status: active
- Short purpose: Formal task packet markdown template.

````md
# TASK PACKET

## Header
- Task ID:
- Project:
- Title:
- Bucket:
- Priority:
- Risk:
- Status:

## Repo
- Repo Path:
- Branch Name:

## Problem Summary

## Goal

## Suspected Files

## Acceptance Criteria
- 

## QA Plan
- 

## System Impact

## Stop Conditions
- 

## Notes
````

### worker_result.template.json

- Exact path: `C:\dev\jarvis-workspace\templates\worker_result.template.json`
- Status: active
- Short purpose: Formal worker result JSON template.

```json
{
  "task_id": "",
  "status": "worker_complete",
  "executor": "cursor_manual",
  "summary": "",
  "files_changed": [],
  "commands_run": [],
  "issues_encountered": [],
  "notes": "",
  "completed_at": ""
}
```

### qa_result.template.json

- Exact path: `C:\dev\jarvis-workspace\templates\qa_result.template.json`
- Status: active
- Short purpose: Formal QA result JSON template.

```json
{
  "task_id": "",
  "status": "",
  "qa_tool": "playwright",
  "summary": "",
  "checks_run": [],
  "checks_passed": [],
  "checks_failed": [],
  "artifacts": [],
  "notes": "",
  "completed_at": ""
}
```

### escalation_record.template.json

- Exact path: `C:\dev\jarvis-workspace\templates\escalation_record.template.json`
- Status: active
- Short purpose: Formal escalation record JSON template.

```json
{
  "task_id": "",
  "status": "escalated",
  "reason": "",
  "details": "",
  "recommended_next_action": "",
  "created_at": ""
}
```

### cursor_completion_contract.txt

- Exact path: `C:\dev\jarvis-workspace\scripts\cursor_completion_contract.txt`
- Status: active
- Short purpose: Forces structured Cursor completion summaries
- Note: Shared contract text used in current worker prompting/output expectations.

````text
When you finish the task, return your summary in this exact structure:

1. What changed
- Files changed:
- Short description of each change:

2. Commands run
- List each command exactly as run

3. Result
- Build result:
- Test result:
- QA result:

4. Issues encountered
- None
or
- List each issue clearly

5. Stop conditions
- State whether any stop condition was hit

6. Recommended worker_result.json fields
{
  "status": "worker_complete",
  "summary": "...",
  "files_changed": ["..."],
  "commands_run": ["..."],
  "issues_encountered": [],
  "notes": "..."
}

Do not add extra sections. Do not give broad advice unless asked.
````

There is no separate formal standalone schema file for worker-result or QA-result validation beyond the live JSON templates, validators, and real examples included in this bundle.

## 5. Current State / Registry / Source-of-Truth Files

### file_registry.json

- Exact path: `C:\dev\jarvis-workspace\state\file_registry.json`
- Status: active
- Short purpose: Machine-readable file registry

```json
[
  {
    "file": "JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "High-level product requirements for Jarvis rebuild",
    "updated_by": "user",
    "notes": "Core planning doc (design-era baseline; now also records deferred LiveKit and LibreCrawl options without making them current-phase commitments)",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "JARVIS_SYSTEM_DOCUMENTATION_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_SYSTEM_DOCUMENTATION_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Detailed architecture and operating documentation",
    "updated_by": "user",
    "notes": "Core planning doc (design-era baseline; now includes compact deferred notes for future LiveKit voice layering and LibreCrawl audit support)",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Current authoritative decisions and system rules",
    "updated_by": "user",
    "notes": "Most important design reference; some areas still describe earlier-phase assumptions and should be read as baseline when they diverge from JARVIS_LIVE_HANDOFF_BUNDLE.md; deferred LiveKit and LibreCrawl options are parked here as future-only notes",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "JARVIS_SCRIPT_PROCESS_REFERENCE.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_SCRIPT_PROCESS_REFERENCE.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Live reference for Jarvis WCS task execution process and hardening helpers",
    "updated_by": "user",
    "notes": "Documents current live Jarvis operating loop, guardrails, and helpers such as commit gates, pre-stamp checks, and packet-status sync during reconcile",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "master_backlog.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\master_backlog.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable task backlog",
    "updated_by": "user / jarvis_script",
    "notes": "Primary backlog source"
  },
  {
    "file": "MASTER_BACKLOG.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\MASTER_BACKLOG.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable backlog table",
    "updated_by": "render_master_backlog.py",
    "notes": "Rendered from master_backlog.json"
  },
  {
    "file": "DAILY_REVIEW.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\DAILY_REVIEW.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Daily execution log and summary",
    "updated_by": "user / jarvis_script",
    "notes": "Reconcile appends entries"
  },
  {
    "file": "DAILY_PLAN.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\DAILY_PLAN.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Current planned work for the day",
    "updated_by": "user",
    "notes": "Lightly used so far"
  },
  {
    "file": "PROJECT_STATUS_WCS.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\PROJECT_STATUS_WCS.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Human-readable WCS project status",
    "updated_by": "user / jarvis_script",
    "notes": "May later be rendered"
  },
  {
    "file": "PROJECT_STATUS_N8N.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\PROJECT_STATUS_N8N.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Human-readable n8n project status",
    "updated_by": "user",
    "notes": "n8n worker deferred"
  },
  {
    "file": "file_registry.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\file_registry.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable file registry",
    "updated_by": "user / jarvis_script",
    "notes": "Source for FILE_REGISTRY.md; aligned to current live hardening state",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "FILE_REGISTRY.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\FILE_REGISTRY.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable file registry",
    "updated_by": "user / future renderer",
    "notes": "Human-readable registry view rendered from file_registry.json by render_file_registry.py; aligned to current live hardening state",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "render_master_backlog.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\render_master_backlog.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Renders MASTER_BACKLOG.md from backlog JSON",
    "updated_by": "user",
    "notes": "Working; reconcile now also syncs existing task packet artifacts to the reconciled terminal outcome"
  },
  {
    "file": "update_master_backlog.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\update_master_backlog.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for backlog renderer",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "generate_task_packet.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\generate_task_packet.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Creates task packet files and blank result files",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "generate_task_packet.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\generate_task_packet.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for task generator",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "reconcile_task_outcome.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Reconciles worker and QA results into backlog state",
    "updated_by": "user",
    "notes": "Working; reconcile now also syncs existing task packet artifacts to the reconciled terminal outcome"
  },
  {
    "file": "reconcile_task_outcome.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for reconciler",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "cursor_completion_contract.txt",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\cursor_completion_contract.txt",
    "category": "template",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Forces structured Cursor completion summaries",
    "updated_by": "user",
    "notes": "Used in worker prompts"
  },
  {
    "file": "overnight_health_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\overnight_health_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only overnight system health watcher",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "run_overnight_health_check.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_overnight_health_check.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Wrapper for overnight health watcher",
    "updated_by": "user",
    "notes": "Used for manual or scheduled runs"
  },
  {
    "file": "register_overnight_health_task.txt",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\register_overnight_health_task.txt",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Task Scheduler command notes",
    "updated_by": "user",
    "notes": "Scheduling helper"
  },
  {
    "file": "run_wcs_scout.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_wcs_scout.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Runs public WCS scout and stores results",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "wcs_scout_routes.json",
    "path": "C:\\dev\\jarvis-workspace\\config\\wcs_scout_routes.json",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Public routes list for WCS scout",
    "updated_by": "user",
    "notes": "/shop and /news removed for now"
  },
  {
    "file": "WCS-001_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-001_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-001_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-001_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-002_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-002_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-002_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-002_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-003_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-003_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-003_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-003_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-004_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-004_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Completed after branch cleanup"
  },
  {
    "file": "WCS-004_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-004_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Completed after branch cleanup"
  },
  {
    "file": "WCS-011_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-011_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "QA infrastructure task"
  },
  {
    "file": "WCS-011_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-011_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "QA infrastructure task"
  },
  {
    "file": "*_worker_result.json",
    "path": "C:\\dev\\jarvis-workspace\\results\\*_worker_result.json",
    "category": "worker_result",
    "source_type": "runtime_output",
    "owner": "cursor_worker",
    "purpose": "Worker completion record per task",
    "updated_by": "user / cursor_worker",
    "notes": "Reconciler input"
  },
  {
    "file": "*_qa_result.json",
    "path": "C:\\dev\\jarvis-workspace\\qa\\*_qa_result.json",
    "category": "qa_result",
    "source_type": "runtime_output",
    "owner": "playwright",
    "purpose": "QA completion record per task",
    "updated_by": "user / playwright",
    "notes": "Reconciler input"
  },
  {
    "file": "*_escalation.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\*_escalation.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Escalation record for blocked or escalated tasks",
    "updated_by": "user / jarvis_script",
    "notes": "May be blank for many tasks"
  },
  {
    "file": "overnight_health_*.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\overnight_health_*.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Machine-readable overnight health output",
    "updated_by": "overnight_health_check.py",
    "notes": "Working"
  },
  {
    "file": "overnight_health_*.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\overnight_health_*.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Human-readable overnight health summary",
    "updated_by": "overnight_health_check.py",
    "notes": "Working"
  },
  {
    "file": "public_scout_results.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_results.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Structured route scout results",
    "updated_by": "run_wcs_scout.py / public_scout.spec.ts",
    "notes": "Latest run currently PASS"
  },
  {
    "file": "public_scout_summary.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_summary.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Human-readable scout summary",
    "updated_by": "run_wcs_scout.py",
    "notes": "Latest run currently PASS"
  },
  {
    "file": "playwright_stdout.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\playwright_stdout.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Raw Playwright stdout from scout run",
    "updated_by": "run_wcs_scout.py",
    "notes": "Debug support"
  },
  {
    "file": "playwright_stderr.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\playwright_stderr.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Raw Playwright stderr from scout run",
    "updated_by": "run_wcs_scout.py",
    "notes": "Debug support"
  },
  {
    "file": "public_scout.spec.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\public_scout.spec.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Public route scout spec for WCS",
    "updated_by": "user",
    "notes": "External WCS repo Playwright spec at C:\\dev\\wcsv2.0-new\\tests\\e2e"
  },
  {
    "file": "home.spec.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\home.spec.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Smoke QA spec for home page",
    "updated_by": "user",
    "notes": "External WCS repo Playwright spec at C:\\dev\\wcsv2.0-new\\tests\\e2e"
  },
  {
    "file": "global-setup.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\helpers\\global-setup.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Shared Playwright startup and readiness logic",
    "updated_by": "user",
    "notes": "External WCS repo Playwright helper at C:\\dev\\wcsv2.0-new\\tests\\e2e\\helpers"
  },
  {
    "file": "package.json",
    "path": "C:\\dev\\wcsv2.0-new\\package.json",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Repo scripts including test:e2e:smoke",
    "updated_by": "user",
    "notes": "WCS repo-side dependency in external WCS repo at C:\\dev\\wcsv2.0-new"
  },
  {
    "file": "normalize_scout_to_backlog.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\normalize_scout_to_backlog.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Normalizes scout defects into backlog-ready tasks and updates backlog state",
    "updated_by": "user",
    "notes": "Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md"
  },
  {
    "file": "normalize_scout_to_backlog.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\normalize_scout_to_backlog.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for scout defect normalizer",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "scout_noise_rules.json",
    "path": "C:\\dev\\jarvis-workspace\\config\\scout_noise_rules.json",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Known scout noise filtering rules for backlog normalization",
    "updated_by": "user",
    "notes": "Used by normalize_scout_to_backlog.py"
  },
  {
    "file": "JARVIS_PHASE_CHECKLIST.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_PHASE_CHECKLIST.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Phase-by-phase rebuild checklist and status for Jarvis workspace",
    "updated_by": "user",
    "notes": "Current canonical overview of phases, missing state surfaces, and next priorities",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "JARVIS_AGENT_IDEA_BACKLOG.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_AGENT_IDEA_BACKLOG.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Idea backlog for short-term modules and longer-term agent business concepts",
    "updated_by": "user",
    "notes": "Reusable idea backlog aligned with current Jarvis architecture"
  },
  {
    "file": "JARVIS_TASK_EXECUTION_CHECKLIST.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_TASK_EXECUTION_CHECKLIST.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Live execution checklist for bounded Jarvis WCS tasks",
    "updated_by": "user",
    "notes": "Defines current live execution phases for Jarvis-controlled WCS loop, including guardrails and helpers",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "JARVIS_LIVE_HANDOFF_BUNDLE.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_LIVE_HANDOFF_BUNDLE.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Live handoff bundle describing current Jarvis system truth, hardening state, and helper surfaces",
    "updated_by": "user",
    "notes": "Aggregates current live system decisions, hardened loop surfaces, helper scripts, and current packet lifecycle/status cleanup truth for Jarvis rebuild",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "manual_loop_checklist.md",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\manual_loop_checklist.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Manual proof-loop checklist for running a WCS task through backlog, worker, QA, and reconcile",
    "updated_by": "user",
    "notes": "Operator runbook; should be aligned with actual script and state behavior to avoid drift"
  },
  {
    "file": "jarvis.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\jarvis.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Phase 3 foreman; reads backlog and project status, validates task eligibility, prepares and verifies WCS task branch, manages task packets, writes daily_plan and run_log, and records durable escalation state on hard failure",
    "updated_by": "user",
    "notes": "Does not perform code changes, QA, commits, stamping, or reconcile; acts as local-first foreman/orchestrator with stronger operator-safety output and durable escalation recording",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "prepare_wcs_task_branch.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\prepare_wcs_task_branch.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Prepares WCS task branch for bounded task work",
    "updated_by": "user",
    "notes": "Used in task workflow to create or switch to task branch in WCS repo"
  },
  {
    "file": "stamp_result_timestamp.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\stamp_result_timestamp.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Stamps completed_at (or specified field) on worker and QA result JSON files; takes FILE PATH as positional argument",
    "updated_by": "user",
    "notes": "Helper to keep result timestamps consistent; run once per result file with path to that file",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "daily_plan.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\daily_plan.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Current selected task and plan metadata; machine-readable",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py; pairs with DAILY_PLAN.md"
  },
  {
    "file": "run_log.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\run_log.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Append-only machine-readable run history",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py when a task is selected"
  },
  {
    "file": "RUN_LOG.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\RUN_LOG.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Append-only human-readable run log",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py when a task is selected"
  },
  {
    "file": "project_status_wcs.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\project_status_wcs.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable WCS project status",
    "updated_by": "user",
    "notes": "Mirror of PROJECT_STATUS_WCS.md; consumed by jarvis.py and scripts"
  },
  {
    "file": "project_status_n8n.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\project_status_n8n.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable n8n project status",
    "updated_by": "user",
    "notes": "Mirror of PROJECT_STATUS_N8N.md; n8n worker deferred"
  },
  {
    "file": "escalations.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\escalations.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Machine-readable escalation records for Jarvis hard failures",
    "updated_by": "jarvis.py",
    "notes": "Authoritative live escalation state; rendered to ESCALATIONS.md",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "ESCALATIONS.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\ESCALATIONS.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable escalation log",
    "updated_by": "jarvis.py",
    "notes": "Rendered from escalations.json whenever Jarvis records an escalation; reflects durable, active escalation state",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "pre_reconcile_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\pre_reconcile_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only pre-reconcile readiness gate for a WCS task",
    "updated_by": "user",
    "notes": "Validates task/result/repo prerequisites before running reconcile; strictly read-only guardrail",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "post_reconcile_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\post_reconcile_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only post-reconcile validator for a WCS task",
    "updated_by": "user",
    "notes": "Confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, DAILY_REVIEW.md, and result files; strictly read-only validator",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "commit_gate_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\commit_gate_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only commit-state gate for a WCS task branch and HEAD",
    "updated_by": "user",
    "notes": "Validates branch, HEAD, ahead-of-main/master, clean worktree, commit message, and bounded committed-files/line counts before trusting worker/QA results; strictly read-only gate, now proven in a completed/reconciled loop (including WCS-019)",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "playwright.config.ts",
    "path": "C:\\dev\\wcsv2.0-new\\playwright.config.ts",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "wcs_repo",
    "purpose": "Local/CI Playwright execution config for WCS smoke QA",
    "updated_by": "user",
    "notes": "Local smoke now uses Playwright webServer to start npm run dev automatically when no E2E_BASE_URL / NEXT_PUBLIC_BASE_URL is set; central config for smoke QA server startup/reuse behavior",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "qa_failure_triage.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\qa_failure_triage.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only QA failure triage helper for a WCS task",
    "updated_by": "user",
    "notes": "Classifies QA failures into environment_setup_failure, test_harness_failure, application_regression, or ambiguous based on QA result summary/notes; prints evidence-based next-step guidance without mutating any state",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "stamp_guard_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\stamp_guard_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only pre-stamp guardrail for worker and QA result JSON files",
    "updated_by": "user",
    "notes": "Verifies worker and QA result files both exist, parse, have allowed statuses, remain pre-stamp, and are not obvious placeholders before running stamp_result_timestamp.py; strictly read-only and does not stamp or mutate state",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "worker_change_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\worker_change_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only worker-boundary validator for changed-file scope and simple diff sanity",
    "updated_by": "user",
    "notes": "Validates that changed files stay within task scope and diffs are small; uses working tree or HEAD commit when clean so post_worker flow is consistent; strictly read-only worker-boundary gate",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "run_cursor_worker.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_cursor_worker.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Agent-first Cursor execution bridge for the current WCS worker surface; prefers agent CLI, then cursor launcher",
    "updated_by": "user",
    "notes": "Execution targets the task repo (repo_path from packet) as the current Cursor execution surface for the WCS worker; Agent uses --workspace and --trust; handoff content as prompt when small; does not fabricate worker completion; proven on WCS-042",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "draft_worker_result_from_evidence.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\draft_worker_result_from_evidence.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Draft truthful worker result JSON from task packet and repo evidence",
    "updated_by": "user",
    "notes": "Does not stamp, reconcile, or fabricate completion; supports repeatable explicit --command values to populate truthful commands_run, trims/drops empty values, rejects placeholder-only command evidence, and requires at least one meaningful command for worker_complete; operator reviews draft before post-worker; live and proven on WCS-042",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "draft_qa_result_from_evidence.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\draft_qa_result_from_evidence.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Draft truthful QA result JSON from operator-supplied evidence (CLI: build/smoke/manual status)",
    "updated_by": "user",
    "notes": "Pre-stamp only; does not stamp or reconcile; does not fabricate checks/artifacts; operator reviews draft before post-worker; live and validator-proven (e.g. WCS-042)",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "worker_result_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\worker_result_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only worker-result schema validator for a WCS task",
    "updated_by": "user",
    "notes": "Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes; strictly read-only validator",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "qa_result_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\qa_result_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only QA-result schema validator for a WCS task",
    "updated_by": "user",
    "notes": "Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes; strictly read-only validator",
    "last_reviewed": "2026-03-12"
  },
  {
    "file": "file_registry_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\file_registry_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only file-registry drift and core-coverage checker for hardened-loop items",
    "updated_by": "user",
    "notes": "Verifies that file_registry.json and FILE_REGISTRY.md exist, parse, and contain entries for critical hardened-loop scripts/docs; strictly read-only and does not modify the registry",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "naming_drift_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\naming_drift_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only naming drift detector for core hardening scripts/docs/registry entries",
    "updated_by": "user",
    "notes": "Checks for obvious name mismatches between core scripts/docs and the file registry; strictly read-only and does not auto-fix names",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "render_file_registry.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\render_file_registry.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Renderer for FILE_REGISTRY.md from file_registry.json",
    "updated_by": "user",
    "notes": "Reads state/file_registry.json and writes state/FILE_REGISTRY.md in the approved registry format; keeps the markdown registry rendered from JSON; strictly read-only except for writing FILE_REGISTRY.md",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "critical_surface_health_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\critical_surface_health_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only sanity checker for critical Jarvis hardening surface",
    "updated_by": "user",
    "notes": "Verifies critical scripts/docs/registry exist, critical helpers compile, and file_registry_check + naming_drift_check pass; does not run full task loop or mutate state",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "build_task_cycle_summary.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\build_task_cycle_summary.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Workflow helper: builds human-readable task cycle summaries for a WCS task",
    "updated_by": "user",
    "notes": "Reads task packet, optional task markdown, worker result, and QA result (when present) and writes scratch/task_cycle_summaries/<task>_task_cycle_summary.md; does not execute tasks, change task state, or mutate backlog/results",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "run_guarded_task_cycle.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_guarded_task_cycle.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Workflow/orchestration helper for guarded WCS task cycles; optional worker and QA drafting in post_worker/full",
    "updated_by": "user",
    "notes": "Runs existing guarded task-cycle helpers in sequence and stops on first failure. pre_worker is unchanged. In post_worker/full, optional --draft-worker-result plus truthful repeatable --worker-command values (and optional --worker-executor) inserts draft_worker_result_from_evidence.py --write immediately before worker_result_validate pre-stamp; worker result JSON may be missing only when this worker-draft flag is supplied, and missing meaningful worker-command evidence fails at the inserted worker-draft step. Existing optional --draft-qa-result QA wiring remains intact and unchanged in this step. Does not replace helper logic, execute worker code directly, or schedule tasks",
    "last_reviewed": "2026-03-14"
  },
  {
    "file": "select_next_ready_task.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\select_next_ready_task.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only workflow helper: selects next eligible ready task from backlog",
    "updated_by": "user",
    "notes": "Reads state/master_backlog.json; uses progression ladder (execution_lane, test_phase, selector_rank) when present, then fallback priority/risk/task id; reports selected task and ranked candidates; does not mutate backlog, daily plan, or any state",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "build_daily_execution_prep.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\build_daily_execution_prep.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Workflow helper: prepares operator-facing daily execution prep package",
    "updated_by": "user",
    "notes": "Ensures task packet exists by invoking generate_task_packet when needed; chains select_next_ready_task (optional), build_cursor_handoff, and build_task_cycle_summary; writes prep markdown to scratch/daily_execution_prep/; does not execute tasks or mutate backlog/state beyond approved helper outputs",
    "last_reviewed": "2026-03-13"
  },
  {
    "file": "build_cursor_handoff.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\build_cursor_handoff.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Workflow helper: builds copy/paste-ready Cursor handoff file for a WCS task",
    "updated_by": "user",
    "notes": "Reads task packet and writes scratch/cursor_handoffs/<task>_cursor_handoff.md when bounded file scope can be derived; fails (no file written) when scope cannot be derived; does not execute task, modify WCS code, or mutate backlog/state",
    "last_reviewed": "2026-03-13"
  }
]
```

### FILE_REGISTRY.md

- Exact path: `C:\dev\jarvis-workspace\state\FILE_REGISTRY.md`
- Status: active
- Short purpose: Human-readable file registry

````md
# FILE REGISTRY

## Live Doc Status
- Last reviewed: 2026-03-14
- Last updated: 2026-03-14
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

| JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | doc | source_of_truth | user | High-level product requirements for Jarvis rebuild | user | Core planning doc (design-era baseline; now also records deferred LiveKit and LibreCrawl options without making them current-phase commitments) |
| JARVIS_SYSTEM_DOCUMENTATION_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_DOCUMENTATION_v3.md | doc | source_of_truth | user | Detailed architecture and operating documentation | user | Core planning doc (design-era baseline; now includes compact deferred notes for future LiveKit voice layering and LibreCrawl audit support) |
| JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | doc | source_of_truth | user | Current authoritative decisions and system rules | user | Most important design reference; some areas still describe earlier-phase assumptions and should be read as baseline when they diverge from JARVIS_LIVE_HANDOFF_BUNDLE.md; deferred LiveKit and LibreCrawl options are parked here as future-only notes |
| JARVIS_SCRIPT_PROCESS_REFERENCE.md | C:\dev\jarvis-workspace\JARVIS_SCRIPT_PROCESS_REFERENCE.md | doc | source_of_truth | user | Live reference for Jarvis WCS task execution process and hardening helpers | user | Documents current live Jarvis operating loop, guardrails, and helpers such as commit gates, pre-stamp checks, and packet-status sync during reconcile |
| master_backlog.json | C:\dev\jarvis-workspace\state\master_backlog.json | state | source_of_truth | user | Machine-readable task backlog | user / jarvis_script | Primary backlog source |
| MASTER_BACKLOG.md | C:\dev\jarvis-workspace\state\MASTER_BACKLOG.md | state | generated | jarvis_script | Human-readable backlog table | render_master_backlog.py | Rendered from master_backlog.json |
| DAILY_REVIEW.md | C:\dev\jarvis-workspace\state\DAILY_REVIEW.md | state | source_of_truth | user | Daily execution log and summary | user / jarvis_script | Reconcile appends entries |
| DAILY_PLAN.md | C:\dev\jarvis-workspace\state\DAILY_PLAN.md | state | source_of_truth | user | Current planned work for the day | user | Lightly used so far |
| PROJECT_STATUS_WCS.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_WCS.md | state | source_of_truth | user | Human-readable WCS project status | user / jarvis_script | May later be rendered |
| PROJECT_STATUS_N8N.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_N8N.md | state | source_of_truth | user | Human-readable n8n project status | user | n8n worker deferred |
| file_registry.json | C:\dev\jarvis-workspace\state\file_registry.json | state | source_of_truth | user | Machine-readable file registry | user / jarvis_script | Source for FILE_REGISTRY.md; aligned to current live hardening state |
| FILE_REGISTRY.md | C:\dev\jarvis-workspace\state\FILE_REGISTRY.md | state | generated | jarvis_script | Human-readable file registry | user / future renderer | Human-readable registry view rendered from file_registry.json by render_file_registry.py; aligned to current live hardening state |
| render_master_backlog.py | C:\dev\jarvis-workspace\scripts\render_master_backlog.py | script | source_of_truth | jarvis_script | Renders MASTER_BACKLOG.md from backlog JSON | user | Working; reconcile now also syncs existing task packet artifacts to the reconciled terminal outcome |
| update_master_backlog.ps1 | C:\dev\jarvis-workspace\scripts\update_master_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for backlog renderer | user | Convenience wrapper |
| generate_task_packet.py | C:\dev\jarvis-workspace\scripts\generate_task_packet.py | script | source_of_truth | jarvis_script | Creates task packet files and blank result files | user | Working |
| generate_task_packet.ps1 | C:\dev\jarvis-workspace\scripts\generate_task_packet.ps1 | script | source_of_truth | user | PowerShell wrapper for task generator | user | Convenience wrapper |
| reconcile_task_outcome.py | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.py | script | source_of_truth | jarvis_script | Reconciles worker and QA results into backlog state | user | Working; reconcile now also syncs existing task packet artifacts to the reconciled terminal outcome |
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
| JARVIS_LIVE_HANDOFF_BUNDLE.md | C:\dev\jarvis-workspace\JARVIS_LIVE_HANDOFF_BUNDLE.md | doc | source_of_truth | user | Live handoff bundle describing current Jarvis system truth, hardening state, and helper surfaces | user | Aggregates current live system decisions, hardened loop surfaces, helper scripts, and current packet lifecycle/status cleanup truth for Jarvis rebuild |
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
| worker_change_check.py | C:\dev\jarvis-workspace\scripts\worker_change_check.py | script | source_of_truth | jarvis_script | Read-only worker-boundary validator for changed-file scope and simple diff sanity | user | Validates that changed files stay within task scope and diffs are small; uses working tree or HEAD commit when clean so post_worker flow is consistent; strictly read-only worker-boundary gate |
| run_cursor_worker.py | C:\dev\jarvis-workspace\scripts\run_cursor_worker.py | script | source_of_truth | jarvis_script | Agent-first Cursor execution bridge for the current WCS worker surface; prefers agent CLI, then cursor launcher | user | Execution targets the task repo (repo_path from packet) as the current Cursor execution surface for the WCS worker; Agent uses --workspace and --trust; handoff content as prompt when small; does not fabricate worker completion; proven on WCS-042 |
| draft_worker_result_from_evidence.py | C:\dev\jarvis-workspace\scripts\draft_worker_result_from_evidence.py | script | source_of_truth | jarvis_script | Draft truthful worker result JSON from task packet and repo evidence | user | Does not stamp, reconcile, or fabricate completion; supports repeatable explicit --command values to populate truthful commands_run, trims/drops empty values, rejects placeholder-only command evidence, and requires at least one meaningful command for worker_complete; operator reviews draft before post-worker; live and proven on WCS-042 |
| draft_qa_result_from_evidence.py | C:\dev\jarvis-workspace\scripts\draft_qa_result_from_evidence.py | script | source_of_truth | jarvis_script | Draft truthful QA result JSON from operator-supplied evidence (CLI: build/smoke/manual status) | user | Pre-stamp only; does not stamp or reconcile; does not fabricate checks/artifacts; operator reviews draft before post-worker; live and validator-proven (e.g. WCS-042) |
| worker_result_validate.py | C:\dev\jarvis-workspace\scripts\worker_result_validate.py | script | source_of_truth | jarvis_script | Read-only worker-result schema validator for a WCS task | user | Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes; strictly read-only validator |
| qa_result_validate.py | C:\dev\jarvis-workspace\scripts\qa_result_validate.py | script | source_of_truth | jarvis_script | Read-only QA-result schema validator for a WCS task | user | Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes; strictly read-only validator |
| file_registry_check.py | C:\dev\jarvis-workspace\scripts\file_registry_check.py | script | source_of_truth | jarvis_script | Read-only file-registry drift and core-coverage checker for hardened-loop items | user | Verifies that file_registry.json and FILE_REGISTRY.md exist, parse, and contain entries for critical hardened-loop scripts/docs; strictly read-only and does not modify the registry |
| naming_drift_check.py | C:\dev\jarvis-workspace\scripts\naming_drift_check.py | script | source_of_truth | jarvis_script | Read-only naming drift detector for core hardening scripts/docs/registry entries | user | Checks for obvious name mismatches between core scripts/docs and the file registry; strictly read-only and does not auto-fix names |
| render_file_registry.py | C:\dev\jarvis-workspace\scripts\render_file_registry.py | script | source_of_truth | jarvis_script | Renderer for FILE_REGISTRY.md from file_registry.json | user | Reads state/file_registry.json and writes state/FILE_REGISTRY.md in the approved registry format; keeps the markdown registry rendered from JSON; strictly read-only except for writing FILE_REGISTRY.md |
| critical_surface_health_check.py | C:\dev\jarvis-workspace\scripts\critical_surface_health_check.py | script | source_of_truth | jarvis_script | Read-only sanity checker for critical Jarvis hardening surface | user | Verifies critical scripts/docs/registry exist, critical helpers compile, and file_registry_check + naming_drift_check pass; does not run full task loop or mutate state |
| build_task_cycle_summary.py | C:\dev\jarvis-workspace\scripts\build_task_cycle_summary.py | script | source_of_truth | jarvis_script | Workflow helper: builds human-readable task cycle summaries for a WCS task | user | Reads task packet, optional task markdown, worker result, and QA result (when present) and writes scratch/task_cycle_summaries/<task>_task_cycle_summary.md; does not execute tasks, change task state, or mutate backlog/results |
| run_guarded_task_cycle.py | C:\dev\jarvis-workspace\scripts\run_guarded_task_cycle.py | script | source_of_truth | jarvis_script | Workflow/orchestration helper for guarded WCS task cycles; optional worker and QA drafting in post_worker/full | user | Runs existing guarded task-cycle helpers in sequence and stops on first failure. pre_worker is unchanged. In post_worker/full, optional --draft-worker-result plus truthful repeatable --worker-command values (and optional --worker-executor) inserts draft_worker_result_from_evidence.py --write immediately before worker_result_validate pre-stamp; worker result JSON may be missing only when this worker-draft flag is supplied, and missing meaningful worker-command evidence fails at the inserted worker-draft step. Existing optional --draft-qa-result QA wiring remains intact and unchanged in this step. Does not replace helper logic, execute worker code directly, or schedule tasks |
| select_next_ready_task.py | C:\dev\jarvis-workspace\scripts\select_next_ready_task.py | script | source_of_truth | jarvis_script | Read-only workflow helper: selects next eligible ready task from backlog | user | Reads state/master_backlog.json; uses progression ladder (execution_lane, test_phase, selector_rank) when present, then fallback priority/risk/task id; reports selected task and ranked candidates; does not mutate backlog, daily plan, or any state |
| build_daily_execution_prep.py | C:\dev\jarvis-workspace\scripts\build_daily_execution_prep.py | script | source_of_truth | jarvis_script | Workflow helper: prepares operator-facing daily execution prep package | user | Ensures task packet exists by invoking generate_task_packet when needed; chains select_next_ready_task (optional), build_cursor_handoff, and build_task_cycle_summary; writes prep markdown to scratch/daily_execution_prep/; does not execute tasks or mutate backlog/state beyond approved helper outputs |
| build_cursor_handoff.py | C:\dev\jarvis-workspace\scripts\build_cursor_handoff.py | script | source_of_truth | jarvis_script | Workflow helper: builds copy/paste-ready Cursor handoff file for a WCS task | user | Reads task packet and writes scratch/cursor_handoffs/<task>_cursor_handoff.md when bounded file scope can be derived; fails (no file written) when scope cannot be derived; does not execute task, modify WCS code, or mutate backlog/state |
````

### AGENT_REGISTRY.md

- Exact path: `C:\dev\jarvis-workspace\AGENT_REGISTRY.md`
- Status: missing
- Short purpose: Current agent registry file if present.
- Note: Current agent registry file if present.

MISSING FILE: `C:\dev\jarvis-workspace\AGENT_REGISTRY.md`

### master_backlog.json

- Exact path: `C:\dev\jarvis-workspace\state\master_backlog.json`
- Status: active
- Short purpose: Machine-readable task backlog

```json
[
  {
    "task_id": "WCS-001",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "done",
    "title": "Fix testimonial typo in PlayerTestimonials quote",
    "notes": "src/components/PlayerTestimonials.tsx"
  },
  {
    "task_id": "WCS-002",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Fix stats section showing 0 for all metrics",
    "notes": "src/components/StatsSection.tsx"
  },
  {
    "task_id": "WCS-003",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Add timeout/fallback handling for long loading states",
    "notes": "TodaysEvents.tsx, LogoMarquee.tsx"
  },
  {
    "task_id": "WCS-004",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "done",
    "title": "Improve empty Around the WCS state",
    "notes": "src/components/TeamUpdates.tsx"
  },
  {
    "task_id": "WCS-005",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Make footer email signup form functional",
    "notes": "src/components/Footer.tsx"
  },
  {
    "task_id": "WCS-006",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fix hero headline accessibility spacing/aria label",
    "notes": "src/components/Hero.tsx"
  },
  {
    "task_id": "WCS-007",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Hide test site banner in production",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-008",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Clarify navbar Coaches link label for logged-out users",
    "notes": "src/components/Navbar.tsx"
  },
  {
    "task_id": "WCS-009",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "done",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "notes": "src/components/LogoMarquee.tsx"
  },
  {
    "task_id": "WCS-010",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "done",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "notes": "src/components/TodaysEvents.tsx"
  },
  {
    "task_id": "WCS-011",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Stabilize local Playwright smoke QA for home page",
    "notes": "tests/e2e, playwright config, global setup for http://localhost:3000"
  },
  {
    "task_id": "WCS-013",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Hide links to unfinished /shop page",
    "notes": "Public navigation or CTA paths should not expose /shop until the page is built out"
  },
  {
    "task_id": "WCS-014",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Hide links to unfinished /news page",
    "notes": "Public links should not expose /news until the page is built out"
  },
  {
    "task_id": "WCS-015",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "ready",
    "title": "Investigate /schedules Supabase realtime auth console error",
    "notes": "Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials"
  },
  {
    "task_id": "WCS-016",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner background from black to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-017",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner background from white back to black",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-018",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner text color from white to black",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-019",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner text color from black back to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-020",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Normalize public footer copyright year across home/about pages",
    "notes": "Public footer component or page-level footer rendering for / and /about",
    "difficulty": 2,
    "execution_lane": "real_easy",
    "test_phase": "phase_c",
    "selector_rank": 130,
    "reversible": false
  },
  {
    "task_id": "WCS-021",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Fix malformed Coach es label rendering on public team cards",
    "notes": "Public /teams card label rendering",
    "difficulty": 2,
    "execution_lane": "real_easy",
    "test_phase": "phase_c",
    "selector_rank": 140,
    "reversible": false
  },
  {
    "task_id": "WCS-022",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "ready",
    "title": "Fill missing grade labels on public team cards that currently show only Grade",
    "notes": "Public /teams team metadata rendering",
    "difficulty": 3,
    "execution_lane": "real_investigative",
    "test_phase": "phase_d",
    "selector_rank": 180,
    "reversible": false
  },
  {
    "task_id": "WCS-023",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "ready",
    "title": "Correct impossible team grade mappings on public /teams cards",
    "notes": "Public /teams data/rendering for Red, Warriors, and similar bad grade labels",
    "difficulty": 3,
    "execution_lane": "real_investigative",
    "test_phase": "phase_d",
    "selector_rank": 190,
    "reversible": false
  },
  {
    "task_id": "WCS-024",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Remove or rename placeholder WCS Errors team from public teams page",
    "notes": "Public /teams team list or seeded display data",
    "difficulty": 2,
    "execution_lane": "real_easy",
    "test_phase": "phase_c",
    "selector_rank": 150,
    "reversible": false
  },
  {
    "task_id": "WCS-025",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "ready",
    "title": "Investigate and fix duplicated calendar rendering on public /schedules page",
    "notes": "Public /schedules calendar component/layout",
    "difficulty": 3,
    "execution_lane": "real_investigative",
    "test_phase": "phase_d",
    "selector_rank": 200,
    "reversible": false
  },
  {
    "task_id": "WCS-026",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Improve empty-state copy for No events today on schedules page",
    "notes": "Public /schedules today-events empty state",
    "difficulty": 2,
    "execution_lane": "real_easy",
    "test_phase": "phase_c",
    "selector_rank": 160,
    "reversible": false
  },
  {
    "task_id": "WCS-027",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Improve empty-state copy for No drills available on drills page",
    "notes": "Public /drills empty state",
    "difficulty": 2,
    "execution_lane": "real_easy",
    "test_phase": "phase_c",
    "selector_rank": 170,
    "reversible": false
  },
  {
    "task_id": "WCS-028",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add basketball emoji to hero subtitle",
    "notes": "src/components/Hero.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 10,
    "reversible": true
  },
  {
    "task_id": "WCS-029",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add fire emoji to hero CTA button label",
    "notes": "src/components/Hero.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 20,
    "reversible": true
  },
  {
    "task_id": "WCS-030",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary TEST MODE badge below hero headline",
    "notes": "src/components/Hero.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 30,
    "reversible": true
  },
  {
    "task_id": "WCS-031",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add trophy emoji to about page promo heading",
    "notes": "src/app/about/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 40,
    "reversible": true
  },
  {
    "task_id": "WCS-032",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add visible TEST: prefix to schedules empty-state heading",
    "notes": "src/app/schedules/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 50,
    "reversible": true
  },
  {
    "task_id": "WCS-033",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add visible TEST: prefix to drills empty-state heading",
    "notes": "src/app/drills/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 60,
    "reversible": true
  },
  {
    "task_id": "WCS-034",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to public team card label",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 70,
    "reversible": true
  },
  {
    "task_id": "WCS-035",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary highlight border to hero section",
    "notes": "src/components/Hero.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 80,
    "reversible": true
  },
  {
    "task_id": "WCS-036",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add star emoji to about mission heading",
    "notes": "src/app/about/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 90,
    "reversible": true
  },
  {
    "task_id": "WCS-037",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add medal emoji to about page section heading",
    "notes": "src/app/about/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 100,
    "reversible": true
  },
  {
    "task_id": "WCS-038",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add calendar emoji to schedules empty-state message",
    "notes": "src/app/schedules/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 110,
    "reversible": true
  },
  {
    "task_id": "WCS-039",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add basketball emoji to schedules page title or filter label",
    "notes": "src/app/schedules/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 120,
    "reversible": true
  },
  {
    "selector_rank": 130,
    "notes": "src/components/Hero.tsx",
    "test_phase": "phase_a",
    "title": "Style test: change home hero subheading letter spacing",
    "project": "WCS",
    "task_id": "WCS-040",
    "risk": "low",
    "priority": "P3",
    "difficulty": 1,
    "status": "done",
    "reversible": true,
    "execution_lane": "fake_reversible",
    "bucket": "ugly"
  },
  {
    "task_id": "WCS-041",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add trophy emoji to hero CTA button label",
    "notes": "src/components/Hero.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 140,
    "reversible": true
  },
  {
    "task_id": "WCS-042",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "done",
    "title": "Fake test: add temporary TEST MODE badge on about page",
    "notes": "src/app/about/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 150,
    "reversible": true
  },
  {
    "task_id": "WCS-043",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "done",
    "title": "Fake test: add visible TEST: prefix to drills page heading",
    "notes": "src/app/drills/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 160,
    "reversible": true
  },
  {
    "task_id": "WCS-044",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to about page section divider",
    "notes": "src/app/about/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 170,
    "reversible": true
  },
  {
    "task_id": "WCS-045",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary highlight border to about page section",
    "notes": "src/app/about/page.tsx",
    "difficulty": 1,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_a",
    "selector_rank": 180,
    "reversible": true
  },
  {
    "task_id": "WCS-046",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary test badge to one team card",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 190,
    "reversible": true
  },
  {
    "task_id": "WCS-047",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to team card metadata label",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 200,
    "reversible": true
  },
  {
    "task_id": "WCS-048",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add calendar emoji to schedules page empty-state",
    "notes": "src/app/schedules/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 210,
    "reversible": true
  },
  {
    "task_id": "WCS-049",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add visible TEST: to schedules empty-state heading",
    "notes": "src/app/schedules/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 220,
    "reversible": true
  },
  {
    "task_id": "WCS-050",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add drill emoji to drills empty-state heading",
    "notes": "src/app/drills/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 230,
    "reversible": true
  },
  {
    "task_id": "WCS-051",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add visible TEST: to drills empty-state message",
    "notes": "src/app/drills/page.tsx",
    "difficulty": 2,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_b",
    "selector_rank": 240,
    "reversible": true
  },
  {
    "task_id": "WCS-052",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to home section heading",
    "notes": "src/components/Hero.tsx",
    "difficulty": 3,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_c",
    "selector_rank": 250,
    "reversible": true
  },
  {
    "task_id": "WCS-053",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to about section heading",
    "notes": "src/app/about/page.tsx",
    "difficulty": 3,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_c",
    "selector_rank": 260,
    "reversible": true
  },
  {
    "task_id": "WCS-054",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary TEST prefix to team card label",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 3,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_c",
    "selector_rank": 270,
    "reversible": true
  },
  {
    "task_id": "WCS-055",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary highlight border to one team card",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 3,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_c",
    "selector_rank": 280,
    "reversible": true
  },
  {
    "task_id": "WCS-056",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary TEST MODE badge to teams section",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 3,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_c",
    "selector_rank": 290,
    "reversible": true
  },
  {
    "task_id": "WCS-057",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to teams section heading",
    "notes": "src/components/ClientTeams.tsx",
    "difficulty": 3,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_c",
    "selector_rank": 300,
    "reversible": true
  },
  {
    "task_id": "WCS-058",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary bright marker to schedules empty state",
    "notes": "src/app/schedules/page.tsx",
    "difficulty": 4,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_d",
    "selector_rank": 310,
    "reversible": true
  },
  {
    "task_id": "WCS-059",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary bright marker to drills empty state",
    "notes": "src/app/drills/page.tsx",
    "difficulty": 4,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_d",
    "selector_rank": 320,
    "reversible": true
  },
  {
    "task_id": "WCS-060",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary emoji to about page CTA or link",
    "notes": "src/app/about/page.tsx",
    "difficulty": 4,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_d",
    "selector_rank": 330,
    "reversible": true
  },
  {
    "task_id": "WCS-061",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fake test: add temporary TEST MODE text to footer",
    "notes": "src/components/Footer.tsx",
    "difficulty": 4,
    "execution_lane": "fake_reversible",
    "test_phase": "phase_d",
    "selector_rank": 340,
    "reversible": true
  }
]
```

### MASTER_BACKLOG.md

- Exact path: `C:\dev\jarvis-workspace\state\MASTER_BACKLOG.md`
- Status: active
- Short purpose: Human-readable backlog table

````md
# MASTER_BACKLOG

| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |
|---|---|---|---|---|---|---|---|
| WCS-001 | WCS | ugly | P2 | low | done | Fix testimonial typo in PlayerTestimonials quote | src/components/PlayerTestimonials.tsx |
| WCS-002 | WCS | broken | P1 | medium | done | Fix stats section showing 0 for all metrics | src/components/StatsSection.tsx |
| WCS-003 | WCS | broken | P1 | medium | done | Add timeout/fallback handling for long loading states | TodaysEvents.tsx, LogoMarquee.tsx |
| WCS-004 | WCS | ugly | P2 | low | done | Improve empty Around the WCS state | src/components/TeamUpdates.tsx |
| WCS-005 | WCS | broken | P1 | medium | done | Make footer email signup form functional | src/components/Footer.tsx |
| WCS-006 | WCS | ugly | P3 | low | ready | Fix hero headline accessibility spacing/aria label | src/components/Hero.tsx |
| WCS-007 | WCS | ugly | P3 | low | ready | Hide test site banner in production | src/components/TestSiteBanner.tsx |
| WCS-008 | WCS | ugly | P3 | low | ready | Clarify navbar Coaches link label for logged-out users | src/components/Navbar.tsx |
| WCS-009 | WCS | broken | P2 | medium | done | Improve LogoMarquee response.ok handling and fallback | src/components/LogoMarquee.tsx |
| WCS-010 | WCS | broken | P2 | medium | done | Show fallback message instead of hiding TodaysEvents on error | src/components/TodaysEvents.tsx |
| WCS-011 | WCS | broken | P1 | low | done | Stabilize local Playwright smoke QA for home page | tests/e2e, playwright config, global setup for http://localhost:3000 |
| WCS-013 | WCS | broken | P2 | low | ready | Hide links to unfinished /shop page | Public navigation or CTA paths should not expose /shop until the page is built out |
| WCS-014 | WCS | broken | P2 | low | ready | Hide links to unfinished /news page | Public links should not expose /news until the page is built out |
| WCS-015 | WCS | broken | P2 | medium | ready | Investigate /schedules Supabase realtime auth console error | Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials |
| WCS-016 | WCS | ugly | P1 | low | done | Flip TestSiteBanner background from black to white | src/components/TestSiteBanner.tsx |
| WCS-017 | WCS | ugly | P1 | low | done | Flip TestSiteBanner background from white back to black | src/components/TestSiteBanner.tsx |
| WCS-018 | WCS | ugly | P1 | low | done | Flip TestSiteBanner text color from white to black | src/components/TestSiteBanner.tsx |
| WCS-019 | WCS | ugly | P1 | low | done | Flip TestSiteBanner text color from black back to white | src/components/TestSiteBanner.tsx |
| WCS-020 | WCS | broken | P2 | low | ready | Normalize public footer copyright year across home/about pages | Public footer component or page-level footer rendering for / and /about |
| WCS-021 | WCS | broken | P2 | low | ready | Fix malformed Coach es label rendering on public team cards | Public /teams card label rendering |
| WCS-022 | WCS | broken | P2 | medium | ready | Fill missing grade labels on public team cards that currently show only Grade | Public /teams team metadata rendering |
| WCS-023 | WCS | broken | P2 | medium | ready | Correct impossible team grade mappings on public /teams cards | Public /teams data/rendering for Red, Warriors, and similar bad grade labels |
| WCS-024 | WCS | broken | P2 | low | ready | Remove or rename placeholder WCS Errors team from public teams page | Public /teams team list or seeded display data |
| WCS-025 | WCS | broken | P2 | medium | ready | Investigate and fix duplicated calendar rendering on public /schedules page | Public /schedules calendar component/layout |
| WCS-026 | WCS | ugly | P2 | low | ready | Improve empty-state copy for No events today on schedules page | Public /schedules today-events empty state |
| WCS-027 | WCS | ugly | P2 | low | ready | Improve empty-state copy for No drills available on drills page | Public /drills empty state |
| WCS-028 | WCS | ugly | P3 | low | ready | Fake test: add basketball emoji to hero subtitle | src/components/Hero.tsx |
| WCS-029 | WCS | ugly | P3 | low | ready | Fake test: add fire emoji to hero CTA button label | src/components/Hero.tsx |
| WCS-030 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST MODE badge below hero headline | src/components/Hero.tsx |
| WCS-031 | WCS | ugly | P3 | low | ready | Fake test: add trophy emoji to about page promo heading | src/app/about/page.tsx |
| WCS-032 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: prefix to schedules empty-state heading | src/app/schedules/page.tsx |
| WCS-033 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: prefix to drills empty-state heading | src/app/drills/page.tsx |
| WCS-034 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to public team card label | src/components/ClientTeams.tsx |
| WCS-035 | WCS | ugly | P3 | low | ready | Fake test: add temporary highlight border to hero section | src/components/Hero.tsx |
| WCS-036 | WCS | ugly | P3 | low | ready | Fake test: add star emoji to about mission heading | src/app/about/page.tsx |
| WCS-037 | WCS | ugly | P3 | low | ready | Fake test: add medal emoji to about page section heading | src/app/about/page.tsx |
| WCS-038 | WCS | ugly | P3 | low | ready | Fake test: add calendar emoji to schedules empty-state message | src/app/schedules/page.tsx |
| WCS-039 | WCS | ugly | P3 | low | ready | Fake test: add basketball emoji to schedules page title or filter label | src/app/schedules/page.tsx |
| WCS-040 | WCS | ugly | P3 | low | done | Style test: change home hero subheading letter spacing | src/components/Hero.tsx |
| WCS-041 | WCS | ugly | P3 | low | ready | Fake test: add trophy emoji to hero CTA button label | src/components/Hero.tsx |
| WCS-042 | WCS | ugly | P3 | low | done | Fake test: add temporary TEST MODE badge on about page | src/app/about/page.tsx |
| WCS-043 | WCS | ugly | P3 | low | done | Fake test: add visible TEST: prefix to drills page heading | src/app/drills/page.tsx |
| WCS-044 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to about page section divider | src/app/about/page.tsx |
| WCS-045 | WCS | ugly | P3 | low | ready | Fake test: add temporary highlight border to about page section | src/app/about/page.tsx |
| WCS-046 | WCS | ugly | P3 | low | ready | Fake test: add temporary test badge to one team card | src/components/ClientTeams.tsx |
| WCS-047 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to team card metadata label | src/components/ClientTeams.tsx |
| WCS-048 | WCS | ugly | P3 | low | ready | Fake test: add calendar emoji to schedules page empty-state | src/app/schedules/page.tsx |
| WCS-049 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: to schedules empty-state heading | src/app/schedules/page.tsx |
| WCS-050 | WCS | ugly | P3 | low | ready | Fake test: add drill emoji to drills empty-state heading | src/app/drills/page.tsx |
| WCS-051 | WCS | ugly | P3 | low | ready | Fake test: add visible TEST: to drills empty-state message | src/app/drills/page.tsx |
| WCS-052 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to home section heading | src/components/Hero.tsx |
| WCS-053 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to about section heading | src/app/about/page.tsx |
| WCS-054 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST prefix to team card label | src/components/ClientTeams.tsx |
| WCS-055 | WCS | ugly | P3 | low | ready | Fake test: add temporary highlight border to one team card | src/components/ClientTeams.tsx |
| WCS-056 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST MODE badge to teams section | src/components/ClientTeams.tsx |
| WCS-057 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to teams section heading | src/components/ClientTeams.tsx |
| WCS-058 | WCS | ugly | P3 | low | ready | Fake test: add temporary bright marker to schedules empty state | src/app/schedules/page.tsx |
| WCS-059 | WCS | ugly | P3 | low | ready | Fake test: add temporary bright marker to drills empty state | src/app/drills/page.tsx |
| WCS-060 | WCS | ugly | P3 | low | ready | Fake test: add temporary emoji to about page CTA or link | src/app/about/page.tsx |
| WCS-061 | WCS | ugly | P3 | low | ready | Fake test: add temporary TEST MODE text to footer | src/components/Footer.tsx |
````

### project_status_wcs.json

- Exact path: `C:\dev\jarvis-workspace\state\project_status_wcs.json`
- Status: active
- Short purpose: Machine-readable WCS project status

```json
{
  "project": "WCS",
  "repo_path": "C:\\dev\\wcsv2.0-new",
  "install_command": "npm install",
  "dev_command": "npm run dev",
  "build_command": "npm run build",
  "local_url": "http://localhost:3000",
  "deploy_target": "Vercel via GitHub push",
  "priority_routes": ["/", "/about", "/teams"],
  "checks_needed": [
    "python_version",
    "node_version",
    "playwright_installed",
    "testids_present"
  ],

  "scout_defect_intake": {
    "enabled": true,
    "runner": "run_wcs_scout.py",
    "normalizer": "normalize_scout_to_backlog.py",
    "noise_rules": "scout_noise_rules.json",
    "results_path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_results.json",
    "report_path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\scout_normalizer_report.json",
    "backlog_target": "C:\\dev\\jarvis-workspace\\state\\master_backlog.json",
    "backlog_markdown": "C:\\dev\\jarvis-workspace\\state\\MASTER_BACKLOG.md"
  },
  "validation_completed": [
    "public_scout_clean_noop_path",
    "public_scout_synthetic_failure_insertion",
    "public_scout_duplicate_suppression",
    "integrated_scout_to_normalizer_run"
  ]
}
```

### daily_plan.json

- Exact path: `C:\dev\jarvis-workspace\state\daily_plan.json`
- Status: active
- Short purpose: Current selected task and plan metadata; machine-readable

```json
{
  "generated_at": "2026-03-12T15:04:13-05:00",
  "selected_task": {
    "task_id": "WCS-019",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "ready",
    "title": "Flip TestSiteBanner text color from black back to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  "selection_reason": {
    "rule": "priority_risk_task_id",
    "details": "Selected highest-priority eligible ready WCS task using deterministic ordering (priority, then risk, then numeric task id)."
  }
}
```

### DAILY_PLAN.md

- Exact path: `C:\dev\jarvis-workspace\state\DAILY_PLAN.md`
- Status: active
- Short purpose: Current planned work for the day

````md
# DAILY PLAN

**Generated at:** 2026-03-12T15:04:13-05:00

## Selected Task

- **Task ID:** WCS-019
- **Project:** WCS
- **Bucket:** ugly
- **Priority:** P1
- **Risk:** low
- **Status:** ready
- **Title:** Flip TestSiteBanner text color from black back to white
- **Notes:** src/components/TestSiteBanner.tsx

## Selection Reason

- **Rule:** priority_risk_task_id
- **Details:** Selected highest-priority eligible ready WCS task using deterministic ordering (priority, then risk, then numeric task id).
````

### run_log.json

- Exact path: `C:\dev\jarvis-workspace\state\run_log.json`
- Status: active
- Short purpose: Append-only machine-readable run history

```json
[
  {
    "timestamp": "2026-03-11T12:19:02-05:00",
    "event": "task_selected",
    "task_id": "WCS-005",
    "project": "WCS",
    "title": "Make footer email signup form functional",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T13:46:40-05:00",
    "event": "task_selected",
    "task_id": "WCS-009",
    "project": "WCS",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T13:46:40-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-009",
    "project": "WCS",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-009_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-009_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-009_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-009_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-009_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_selected",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-010_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-010_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-010_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-010_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-010_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-010",
    "artifacts": [
      "jarvis-task-wcs-010"
    ]
  },
  {
    "timestamp": "2026-03-11T21:24:48-05:00",
    "event": "task_selected",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T21:24:48-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-016_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-016_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-016_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-016_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-016_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T21:24:49-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-016",
    "artifacts": [
      "jarvis-task-wcs-016"
    ]
  },
  {
    "timestamp": "2026-03-12T10:37:44-05:00",
    "event": "task_selected",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T10:37:44-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-017_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-017_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-017_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-017_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-017_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T10:37:45-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-017",
    "artifacts": [
      "jarvis-task-wcs-017",
      "C:\\dev\\wcsv2.0-new"
    ]
  },
  {
    "timestamp": "2026-03-12T11:16:29-05:00",
    "event": "task_selected",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T12:28:50-05:00",
    "event": "task_selected",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T12:28:50-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis generated task packet and contract-valid placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-018_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-018_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-018_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-018_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-018_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T12:28:51-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-018",
    "artifacts": [
      "jarvis-task-wcs-018",
      "C:\\dev\\wcsv2.0-new"
    ]
  },
  {
    "timestamp": "2026-03-12T13:04:45-05:00",
    "event": "task_selected",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "event": "task_selected",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis generated task packet and contract-valid placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-019_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-019_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-019_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-019_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-019_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T15:04:13-05:00",
    "event": "task_selected",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T15:04:14-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-019",
    "artifacts": [
      "jarvis-task-wcs-019",
      "C:\\dev\\wcsv2.0-new"
    ]
  }
]
```

### RUN_LOG.md

- Exact path: `C:\dev\jarvis-workspace\state\RUN_LOG.md`
- Status: active
- Short purpose: Append-only human-readable run log

````md
# RUN LOG

## 2026-03-11T12:19:02-05:00 — task_selected

- **Task ID:** WCS-005
- **Project:** WCS
- **Title:** Make footer email signup form functional
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T13:46:40-05:00 — task_selected

- **Task ID:** WCS-009
- **Project:** WCS
- **Title:** Improve LogoMarquee response.ok handling and fallback
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T13:46:40-05:00 — task_packet_generated

- **Task ID:** WCS-009
- **Project:** WCS
- **Title:** Improve LogoMarquee response.ok handling and fallback
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-009_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-009_task.md
  - C:\dev\jarvis-workspace\results\WCS-009_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-009_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-009_escalation.json

## 2026-03-11T14:49:02-05:00 — task_selected

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T14:49:02-05:00 — task_packet_generated

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-010_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-010_task.md
  - C:\dev\jarvis-workspace\results\WCS-010_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-010_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-010_escalation.json

## 2026-03-11T14:49:02-05:00 — task_branch_prepared

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-010
- **Artifacts:**
  - jarvis-task-wcs-010

## 2026-03-11T21:24:48-05:00 — task_selected

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T21:24:48-05:00 — task_packet_generated

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-016_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-016_task.md
  - C:\dev\jarvis-workspace\results\WCS-016_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-016_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-016_escalation.json

## 2026-03-11T21:24:49-05:00 — task_branch_prepared

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-016
- **Artifacts:**
  - jarvis-task-wcs-016

## 2026-03-12T10:37:44-05:00 — task_selected

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T10:37:44-05:00 — task_packet_generated

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-017_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-017_task.md
  - C:\dev\jarvis-workspace\results\WCS-017_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-017_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-017_escalation.json

## 2026-03-12T10:37:45-05:00 — task_branch_prepared

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-017
- **Artifacts:**
  - jarvis-task-wcs-017
  - C:\dev\wcsv2.0-new

## 2026-03-12T11:16:29-05:00 — task_selected

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T12:28:50-05:00 — task_selected

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T12:28:50-05:00 — task_packet_generated

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis generated task packet and contract-valid placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-018_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-018_task.md
  - C:\dev\jarvis-workspace\results\WCS-018_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-018_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-018_escalation.json

## 2026-03-12T12:28:51-05:00 — task_branch_prepared

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-018
- **Artifacts:**
  - jarvis-task-wcs-018
  - C:\dev\wcsv2.0-new

## 2026-03-12T13:04:45-05:00 — task_selected

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T14:57:08-05:00 — task_selected

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T14:57:08-05:00 — task_packet_generated

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis generated task packet and contract-valid placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-019_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-019_task.md
  - C:\dev\jarvis-workspace\results\WCS-019_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-019_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-019_escalation.json

## 2026-03-12T15:04:13-05:00 — task_selected

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T15:04:14-05:00 — task_branch_prepared

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-019
- **Artifacts:**
  - jarvis-task-wcs-019
  - C:\dev\wcsv2.0-new
````

### JARVIS_TASK_EXECUTION_CHECKLIST.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_TASK_EXECUTION_CHECKLIST.md`
- Status: active
- Short purpose: Live execution checklist for bounded Jarvis WCS tasks
- Note: Included here because it explicitly defines current worker execution phases, activation expectations, and guardrails.

````md
````md
# JARVIS_TASK_EXECUTION_CHECKLIST_v2.md

## Live Doc Status
- Last reviewed: 2026-03-13
- Last updated: 2026-03-13
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Status: aligned to current live hardening state (phases match handoff bundle; completed_at blank until stamping; stamp takes FILE PATH; validators/gates read-only; commit gate helper live and proven in completed/reconciled loop)

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
````

## 6. Current Live Process / Handoff Docs

### JARVIS_LIVE_HANDOFF_BUNDLE.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_LIVE_HANDOFF_BUNDLE.md`
- Status: active
- Short purpose: Live handoff bundle describing current Jarvis system truth, hardening state, and helper surfaces
- Note: Current live process/handoff bundle.

````md
# JARVIS_LIVE_HANDOFF_BUNDLE.md

## Live Doc Status
- Last reviewed: 2026-03-14
- Last updated: 2026-03-14 (doc pass: packet lifecycle/status cleanup live)
- Status: active live handoff bundle for current Jarvis hardening state

## Current local state / follow-up
- No special local follow-up is required for the packet lifecycle/status cleanup beyond normal review and commit discipline.

## Recent live truth
- Option A packet lifecycle/status cleanup is now live.
- `scripts/reconcile_task_outcome.py` now syncs existing task packet JSON and task packet markdown to the reconciled terminal outcome when those packet artifacts exist.
- Backlog/state remains authoritative; task packet artifacts remain generated/operator-facing views that are kept aligned after reconcile.
- Safe proof: completed `WCS-043` now shows `status: done` in `tasks/WCS-043_task.json` and `Status: done` in `tasks/WCS-043_task.md` after reconcile, instead of lingering at `ready`.

## FILE: JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3
````md
# JARVIS Multi-Agent Development System
## System Source of Truth

**Version:** v3.0  
**Date:** March 9, 2026  
**Status:** Current authoritative decisions  
**Use:** Final reference for architecture, constraints, and phase-1 rules

---

## 1. Purpose of This Document

This file records the hard decisions that govern the Jarvis rebuild.

It exists so the project does not drift every time a new idea sounds exciting.

If another note, prompt, or conversation conflicts with this file, this file wins until it is intentionally revised.

---

## 2. Core Identity

Jarvis is a **local-first development foreman** for one operator.

Jarvis is not the main builder.
Jarvis is the coordinator that turns project state into bounded work.

The system is meant to help move real projects forward through:

- planning
- packet generation
- worker routing
- verification
- logging
- escalation

The system succeeds by creating **trustworthy progress**, not by sounding autonomous.

---

## 3. Governing Rule

> **Small verified progress beats large speculative progress.**

Everything below follows from that rule.

---

## 4. Architecture Verdict

### 4.1 Phase-1 runtime
**Chosen:** simple Python orchestration script

### 4.2 Phase-1 state model
**Chosen:** markdown + JSON sidecars

### 4.3 Phase-1 coding execution truth
**Chosen:** WCS worker as the coding worker for WCS, executed semi-manually through Cursor in this phase

### 4.4 Phase-1 verification truth
**Chosen:** Playwright for WCS

### 4.5 Phase-1 activation scope
**Chosen:** WCS planning and proof loop first

### 4.6 Deferred elements
- LangGraph
- project leads
- fully automated coding worker
- n8n autonomous worker
- voice interface
- machine maintenance worker
- dashboard-first work

---

## 5. Phase-1 Mission

The mission of phase 1 is **not** to build the full Jarvis dream.

The mission is to prove one boring loop:

1. state exists
2. Jarvis reads it
3. Jarvis chooses one bounded WCS task
4. Jarvis writes a valid packet
5. task is executed in Cursor
6. result is recorded
7. Playwright QA runs
8. task becomes done or escalated
9. status and logs update correctly

If that loop is not trustworthy, nothing else should be added.

---

## 6. Current Project Priority

### Priority 1
**WCS stabilization and cleanup**

Reason:
- visible value
- bounded UI issues
- clear acceptance criteria
- Playwright is a strong QA path

### Priority 2
**n8n quality improvement design**

Reason:
- important project
- current workflow exists
- quality criteria still too subjective for real automation

### Priority 3
**Future workers**

Only after phase-1 loop stability.

---

## 7. WCS Truth

### 7.1 WCS is the first active build domain
This is the first project where the system must prove it can generate and move real tasks.

### 7.2 WCS task sourcing
Initial WCS backlog categories:

1. Broken
2. Ugly
3. Incomplete
4. Optimization

### 7.3 WCS phase-1 pull rule
Jarvis only pulls from:

- Broken
- Ugly

### 7.4 WCS task size rule
No phase-1 WCS task should require:

- broad redesign
- multi-route change
- database migration
- dependency upgrade
- auth flow rewrite

If it does, the task is too big or wrongly framed.

---

## 8. n8n Truth

### 8.1 n8n is real but deferred
The n8n project matters, but it is not phase-1 execution priority.

### 8.2 Why it is deferred
The system does not yet have a machine-checkable rubric for “better output.”

### 8.3 Activation requirement
Before n8n becomes an active worker path, the build must define:

- output schema
- scoreable quality rubric
- required blocks
- regression tests
- fail conditions

Until then, n8n planning can exist, but n8n automation cannot be trusted.

---

## 9. Worker Truth

### 9.1 Worker rule
Every worker must have:

- purpose
- scope
- input packet
- output contract
- QA path
- escalation rules

### 9.2 No undefined workers
If a worker cannot state those five things clearly, it is not a worker yet. It is just an idea.

### 9.3 No self-grading
No worker may certify final success for its own work.

---

## 10. WCS Worker Truth

### 10.1 Current reality
The WCS worker is **semi-manual**.

### 10.2 What that means
- Jarvis writes the packet
- the operator executes the packet in Cursor
- the result is captured back into the system
- QA verifies independently

### 10.3 Why this is correct
It matches current habits, current tooling, and current reliability.

Pretending phase 1 is fully autonomous coding would be fake autonomy.

---

## 11. State Truth

### 11.1 Markdown remains mandatory
The operator must be able to inspect and edit state directly.

### 11.2 JSON remains mandatory
Scripts must not depend on scraping prose only.

### 11.3 No premature database
SQLite is not phase-1 state.

If markdown + JSON sidecars become genuinely painful in real use, database adoption can be reconsidered later.

### 11.4 Source-of-truth stance
In phase 1, markdown and JSON sidecars are the official state pair.

---

## 12. File Truth

### Mandatory markdown files

- `MASTER_BACKLOG.md`
- `DAILY_PLAN.md`
- `RUN_LOG.md`
- `PROJECT_STATUS_WCS.md`
- `PROJECT_STATUS_N8N.md`
- `ESCALATIONS.md`
- `AGENT_REGISTRY.md`
- `OPERATING_RULES.md`

### Mandatory JSON files

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Mandatory template files

- `task_packet.template.json`
- `worker_result.template.json`
- `qa_result.template.json`
- `escalation_record.template.json`

---

## 13. Script Truth

### Scripts that must exist in phase 1

1. `jarvis.py`
2. `truth_map_wcs.py`
3. `seed_backlog_wcs.py`
4. `record_worker_result.py`
5. `run_wcs_qa.py`
6. `escalate_task.py`

### What does not need to exist yet

- LangGraph graph definitions
- lead-manager scripts
- voice loop scripts
- machine cleanup scripts
- scheduler-first infrastructure
- dashboard-first infrastructure

---

## 14. Task Packet Truth

Every executable task packet must include:

- task ID
- project
- worker
- title
- problem
- goal
- scope
- suspected files
- acceptance criteria
- QA method
- risk level
- system impact
- stop conditions
- status
- created timestamp

### Why “system impact” is mandatory
A task must declare whether it is expected to touch:

- UI only
- workflow only
- auth
- data
- payment
- deployment
- shared infra

This is a hard risk-control field, not optional flavor text.

---

## 15. Truth Mapping Truth

Truth mapping is mandatory before broad automation.

### Minimum WCS truth mapping outputs

- repo structure summary
- framework indicators
- scripts and entry points
- route map overview
- component map overview
- obvious fragile areas
- recent known blockers if any

Truth mapping records facts.
It does not generate completion claims.

---

## 16. Failure Policy Truth

### Hard numbers for phase 1

- max planned tasks per cycle: **1**
- max WCS tasks per day: **1**
- planning timeout: **90 sec**
- QA timeout: **300 sec**
- parse retry: **1**
- QA auto-retry: **0**
- consecutive escalations before pause: **2**

### Immediate escalation conditions

- malformed JSON
- missing required packet fields
- target files missing
- task exceeds scope
- unexpected high-risk impact
- QA hard fail
- operator clarification required

### Pause rule
After 2 consecutive active task escalations/failures, pause further execution until review.

---

## 17. Scheduling Truth

Scheduling is **not** phase-1 proof.

The system must first prove:

- planning loop works
- packet contract works
- WCS worker result capture works
- WCS QA works
- escalation handling works

Only after that may scheduling be enabled.

Initial scheduling rule:
- one run
- one task
- no overlap

---

## 18. Voice Truth

Voice is explicitly later-phase work.

The voice layer does not solve the hard problem.
The hard problem is trustworthy orchestration and verification.

Only when the boring loop works should voice be added.

---

## 19. Future Worker Truth

Allowed future workers include:

- error/issues research scout
- content/topic research scout
- n8n workflow/content improver
- local machine maintenance worker
- voice interface worker

Each future worker must satisfy the standard worker rule before activation.

No new worker may be added just to hide a broken core loop.

---

## 20. Build Order Truth

### Week 1 order

#### Days 1–2
- create workspace structure
- create markdown files
- create JSON sidecars
- implement `jarvis.py` planning loop
- implement WCS truth mapping

#### Day 3
- define task packet, worker result, QA result, escalation record templates
- run a mock worker test

#### Days 4–5
- execute one semi-manual WCS task through Cursor
- record worker result

#### Days 6–7
- run Playwright QA
- prove done/fail/escalate transitions
- update run log and project status correctly

### Explicitly rejected for week 1

- building the full agent fleet
- building voice interaction
- building full LangGraph orchestration
- building a dashboard before the loop works
- adding project leads
- pretending n8n quality automation is solved

---

## 21. Expansion Trigger

The system is ready for phase-2 discussion only when:

- 5 or more WCS tasks have completed or escalated through the full loop
- state files remain understandable
- task packets stay stable
- QA catches real issues
- pause/escalation behavior works
- operator trust is increasing, not decreasing

Until then, phase 1 stays phase 1.

---

## 22. Final Statement

Jarvis is not being rebuilt to look intelligent.

Jarvis is being rebuilt to make **controlled, auditable, low-drama progress** on real projects.

That means the phase-1 system must stay small, honest, and verifiable.
```

## FILE: JARVIS_MULTI_AGENT_SYSTEM_PRD_v3
````md
# Jarvis Multi-Agent Development System
## Product Requirements Document (PRD)

**Version:** 3.0  
**Date:** March 9, 2026  
**Status:** Current rebuild baseline  
**Type:** Product definition and implementation direction

---

## 1. Product Overview

The **Jarvis Multi-Agent Development System** is a **local-first development operations system** for one operator running multiple real projects from one workstation.

Jarvis is **not** the main coder.  
Jarvis is the **foreman**.

Jarvis exists to:

- read durable project state
- select the next bounded task
- generate a strict task packet
- route work to the correct worker
- require independent verification
- record outcomes and next actions
- keep progress moving with minimal babysitting

The system is designed around one governing principle:

> **Small verified progress beats large speculative progress.**

### Initial project domains

1. **WCS website**
   - mostly built
   - needs stabilization, cleanup, and completion work
   - current code editing tool is Cursor

2. **n8n voice/content system**
   - working but uneven
   - needs quality improvements for X.com content generation
   - needs a tighter quality rubric before real automation

### Phase-1 architectural truth

Phase 1 is **not** a flashy autonomous multi-agent empire.

Phase 1 is:

- one simple Python orchestration loop
- markdown files for human-readable state
- JSON sidecars for machine-readable state
- one semi-manual WCS worker flow through Cursor
- one independent QA flow through Playwright
- one repeatable proof loop

---

## 2. Product Problem

The user already has tools and projects, but they are fragmented:

- planning is scattered
- priorities drift
- small fixes accumulate
- verification is inconsistent
- project memory is mostly informal
- current AI tooling either over-promises or requires babysitting

Typical AI-agent setups fail because they:

- blur planning, execution, and QA
- hide state inside chats
- lack durable task contracts
- make autonomous claims without evidence
- burn time and money on orchestration theater

Jarvis solves that by creating:

- visible system state
- bounded tasks
- narrow workers
- hard verification gates
- a repeatable daily operating loop

---

## 3. Product Goals

### Primary goals

1. Turn project chaos into a prioritized bounded backlog.
2. Keep durable project state across days and sessions.
3. Generate clear task packets instead of vague missions.
4. Move work through planning → execution → verification → logging.
5. Reduce manual coordination overhead.
6. Keep runtime and API costs controlled.
7. Support future modular workers without redesigning the core.

### Secondary goals

- enable later voice interaction
- support scheduled daily cycles
- preserve local-first control
- keep tooling replaceable
- avoid dependency on one fragile runtime shell

### Non-goals for Phase 1

- full autonomy across multiple repos
- automatic voice conversation
- automatic cleanup of the whole machine
- multi-lead hierarchy
- LangGraph-first orchestration
- a giant all-in-one agent framework

---

## 4. Product Principles

### 4.1 Jarvis is a coordinator, not a worker
Jarvis selects, routes, and records.
Jarvis does not pretend to be the builder, the researcher, and the QA lead at once.

### 4.2 Every task must be bounded
No worker receives a vague instruction like “improve the site.”
Every task packet must define scope, acceptance criteria, and exit conditions.

### 4.3 No worker self-certifies success
Independent verification is mandatory for anything that counts as completed work.

### 4.4 Human-readable state is required
State must remain visible and editable by the operator.

### 4.5 Machine-readable state is also required
Automation must not depend on parsing loose prose only.

### 4.6 Start with the simplest durable runtime
A boring script that survives real use is better than a “smart” framework that collapses under debugging.

---

## 5. Current Architecture Decision

### Phase-1 runtime decision
**Chosen:** simple Python orchestration script

### Phase-1 state decision
**Chosen:** markdown + JSON sidecars

### Phase-1 WCS worker truth
**Chosen:** WCS worker with Jarvis-generated task packets, executed semi-manually through Cursor in this phase

### First proof-of-work sequence
1. planning loop
2. mock worker loop
3. semi-manual WCS packet through Cursor
4. Playwright QA verification
5. logging and escalation handling

### Deferred items
- LangGraph
- project leads
- fully automated coding worker
- fully autonomous research loops
- voice layer
- machine maintenance worker

---

## 6. Phase-1 Architecture

```text
User
  ↓
Jarvis (python foreman)
  ↓
State files (.md + .json)
  ↓
Task packet
  ↓
Semi-manual WCS worker (Cursor)
  ↓
QA worker (Playwright)
  ↓
Run log / project status / escalation record
```

### Initial active components

- **Jarvis planner/orchestrator**
- **WCS task packet flow**
- **WCS coding worker executed through Cursor**
- **WCS QA worker**
- **truth-mapping scripts**
- **logging + escalation flow**

### Workers deferred but recognized

- **Research Scout**
- **n8n content worker**
- **n8n QA worker**
- **machine maintenance worker**
- **topic research worker**

---

## 7. Worker Model

Each worker must have:

- a defined purpose
- a defined input packet
- an approved scope
- a known output contract
- a verification path
- escalation rules

Every worker contract must answer:

1. What can it touch?
2. What tasks can it accept?
3. What file or process starts it?
4. What output JSON does it return?
5. What does success look like?
6. What causes immediate escalation?

---

## 8. Initial Worker Definitions

### 8.1 WCS Semi-Manual Cursor Worker

**Purpose:** Implement bounded WCS code changes.

**Reality in Phase 1:** Jarvis prepares the packet. A human opens Cursor and executes the task using the packet.

**Why this is correct now:** It is honest, cheap, and buildable this week. Fully automated coding can come later if the packet interface proves stable.

**Allowed tasks:**
- broken UI fixes
- small styling cleanup
- small completion tasks
- minor refactors
- small wiring repairs

**Not allowed:**
- broad redesigns
- multi-page rewrites
- database migrations without explicit approval
- large dependency changes
- repo-wide refactors

**Required outputs:**
- worker result JSON
- changed files list
- short implementation summary
- blocker notes if applicable

---

### 8.2 WCS QA Worker

**Purpose:** Verify that WCS changes actually work.

**Execution path:** Playwright

**Checks may include:**
- route loads
- target elements exist
- target interaction works
- screenshot or layout check where needed
- regression notes

**Required outputs:**
- QA result JSON
- pass/fail status
- evidence location
- issue notes
- retest recommendation

---

### 8.3 n8n Content Worker (recognized, not phase-1 active)

**Purpose:** Improve the n8n content-generation system.

**Current status:** Deferred until the quality rubric is machine-checkable.

**Reason for deferral:** “Better content” is too subjective unless reduced to a measurable rubric.

**Activation requirement:**
- clear output schema
- measurable scoring rubric
- known regression checks
- sample test set

---

### 8.4 Research Scout (recognized, not phase-1 active)

**Purpose:** Investigate errors, docs, and implementation options without editing production code.

**Current status:** Deferred until the planning loop and WCS loop are proven.

---

## 9. Task Packet Requirements

Every task packet must include:

- task ID
- project
- worker type
- title
- problem statement
- desired outcome
- suspected files or scope
- acceptance criteria
- QA method
- risk level
- system impact
- stop conditions
- status
- created timestamp

### Example WCS task shape

- **Task ID:** WCS-021
- **Project:** WCS
- **Worker:** wcs-cursor-worker
- **Title:** Fix mobile navbar overlap on home page
- **Problem:** menu overlays hero text at small widths
- **Goal:** navbar collapses without blocking hero
- **Scope:** navbar component and related styles only
- **Acceptance Criteria:** no overlap at mobile width; menu opens and closes correctly
- **QA Method:** Playwright locator + screenshot check
- **Risk:** Low
- **System Impact:** UI only; no auth, DB, or payment impact
- **Stop Conditions:** if fix requires route redesign or large layout rewrite

---

## 10. State Model

### Human-readable state
Markdown files remain the operator-facing source of truth.

### Machine-readable sidecars
JSON sidecars make planning, routing, logging, and QA reliable.

### Phase-1 rule
No critical automation decision may depend only on free-form markdown prose.

---

## 11. Core Files

### Required markdown files

- `MASTER_BACKLOG.md`
- `DAILY_PLAN.md`
- `RUN_LOG.md`
- `PROJECT_STATUS_WCS.md`
- `PROJECT_STATUS_N8N.md`
- `ESCALATIONS.md`
- `OPERATING_RULES.md`
- `AGENT_REGISTRY.md`

### Required JSON files

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Required task folders

- `tasks/open/`
- `tasks/in_progress/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/escalated/`

### Required template folders

- `templates/task_packets/`
- `templates/results/`
- `templates/qa/`

---

## 12. Minimal Phase-1 Scripts

### Must exist in phase 1

1. `jarvis.py`
   - loads backlog and project status
   - chooses next task
   - writes task packet
   - writes daily plan entry
   - appends run log entry

2. `truth_map_wcs.py`
   - scans WCS repo
   - records structure and obvious status signals
   - updates project status files

3. `seed_backlog_wcs.py`
   - creates initial bounded WCS backlog items

4. `record_worker_result.py`
   - ingests worker result JSON
   - updates task state

5. `run_wcs_qa.py`
   - triggers Playwright verification
   - writes QA result JSON

6. `escalate_task.py`
   - records failure or human-intervention need

### Nice to have later

- `truth_map_n8n.py`
- `daily_summary.py`
- `cost_report.py`
- `health_check.py`

---

## 13. Failure and Escalation Policy

### Phase-1 limits

- **Max planned tasks per cycle:** 1
- **Max WCS tasks per day:** 1 initially
- **Planning timeout:** 90 seconds
- **QA timeout:** 300 seconds
- **Automatic retries for transient parsing issues:** 1
- **Automatic retries for failed QA:** 0
- **Consecutive escalations before pausing the system:** 2

### Immediate escalation conditions

- malformed worker result JSON
- missing required task fields
- required target files not found
- QA hard fail
- task exceeds allowed scope
- task affects unexpected high-risk areas
- operator clarification required

### Phase-1 pause rule

If 2 consecutive active tasks escalate or fail verification, the system pauses new execution and writes a pause note to `ESCALATIONS.md` and `escalations.json`.

---

## 14. Verification Model

### Verification rule
Anything recorded as complete must have evidence.

### WCS evidence examples
- Playwright pass/fail
- screenshot file path
- route check result
- relevant notes

### n8n rule for later activation
n8n work cannot be promoted to “completed” until the rubric is machine-checkable.

---

## 15. Scheduling Strategy

Scheduling is **not** the first proof.

Phase 1 proves the loop manually.

Scheduling becomes active only after:

- planning loop is stable
- task packet contract is stable
- WCS QA flow is stable
- escalation logic is stable

When scheduling is introduced, it should start with:

- 1 daytime cycle
- 1 task max
- no overlapping runs

---

## 16. Voice Strategy

Voice is explicitly deferred.

### Why
Voice is a UX layer, not the core operating problem.

### Later design
- speech-to-text in
- Jarvis reads logs and status
- Jarvis responds in text
- text-to-speech reads summary aloud

This is phase-later work only.

---

## 17. Success Criteria

Phase 1 is successful when the following loop works cleanly:

1. backlog item exists
2. Jarvis selects it
3. Jarvis writes a valid task packet
4. human executes the packet in Cursor
5. worker result is recorded
6. Playwright QA runs
7. task is marked done or escalated
8. project status and run log update correctly

If this loop does not work, the system is not ready for more workers.

---

## 18. Future Expansion

Future workers can be added if they provide:

- a bounded purpose
- a strict input packet
- a strict output contract
- a known QA path
- escalation rules
- low-risk activation plan

Likely future workers:

- research scout for debugging
- research scout for content/topic gathering
- n8n workflow/content improver
- local machine maintenance worker
- voice interaction layer

Expansion happens only after the phase-1 loop is stable.

---

## 19. Final Product Position

This system is not an AI toy.

It is a **development operations layer** that coordinates work across real projects with visible state, bounded tasks, and independent verification.

The product does not win by sounding intelligent.

It wins by making boring, trustworthy progress.
```

## FILE: JARVIS_SYSTEM_DOCUMENTATION_v3
````md
# JARVIS Multi-Agent Development System
## Master Documentation

**Version:** v3.0  
**Date:** March 9, 2026  
**Status:** Current operating documentation for the rebuild  
**Audience:** Operator / developer / future maintainer

---

## Table of Contents

1. Purpose
2. What Jarvis Is
3. What Jarvis Is Not
4. Current Build Decision
5. Operating Philosophy
6. Phase-1 Architecture
7. Workspace Layout
8. Core Files
9. JSON Sidecars
10. Task Packet Standard
11. Truth Mapping
12. WCS Operating Flow
13. QA Operating Flow
14. n8n Status
15. Failure Handling
16. Cost Controls
17. Scheduling Rules
18. Future Modules
19. Build Order
20. Glossary

---

## 1. Purpose

This document explains how the rebuilt Jarvis system is supposed to work **right now**, not as a fantasy future version.

It exists to answer:

- what the system is
- how phase 1 really works
- what files matter
- what the first proof loop is
- what is intentionally deferred
- how to add future workers without wrecking the core

---

## 2. What Jarvis Is

Jarvis is a **small local orchestration layer**.

In phase 1, Jarvis is a **Python foreman script** that reads file-based state, chooses the next bounded task, writes a task packet, records progress, and enforces escalation rules.

Jarvis owns:

- planning
- task selection
- task packet generation
- logging
- state updates
- escalation decisions

Jarvis does **not** own:

- making big code changes itself
- verifying its own work
- broad repo roaming
- unsupervised multi-task execution
- fake “autonomous company” behavior

---

## 3. What Jarvis Is Not

Jarvis is not:

- a full coding agent in phase 1
- a LangGraph deployment in phase 1
- a voice assistant in phase 1
- a general machine-admin bot in phase 1
- a replacement for your judgment
- an excuse to skip verification

If the system cannot perform one boring loop reliably, it is not ready for any glamorous features.

---

## 4. Current Build Decision

### Hard choices already made

| Area | Current decision |
|---|---|
| Runtime | Simple Python script |
| State model | Markdown + JSON sidecars |
| WCS builder | Semi-manual Cursor workflow |
| WCS QA | Playwright |
| n8n worker | Deferred until rubric is machine-checkable |
| LangGraph | Deferred |
| Voice | Deferred |
| Scheduling | Deferred until manual loop is stable |
| Project leads | Deferred |

### Why this is correct

Because it is buildable, debuggable, cheap, and honest.

Anything more ambitious at this stage is ceremony.

---

## 5. Operating Philosophy

### The five rules

1. **One task at a time**
2. **No vague missions**
3. **No self-certified success**
4. **Visible state beats hidden context**
5. **Cheap boring progress beats expensive agent theater**

### Translation into practice

That means:

- one active task packet per cycle
- clear acceptance criteria
- JSON outputs where machines need certainty
- markdown where humans need readability
- no launching new workers just because it sounds cool

---

## 6. Phase-1 Architecture

```text
workspace-jarvis/
  ├─ brain/
  │   ├─ markdown state
  │   └─ json sidecars
  ├─ tasks/
  │   ├─ open
  │   ├─ in_progress
  │   ├─ done
  │   ├─ failed
  │   └─ escalated
  ├─ scripts/
  │   ├─ jarvis.py
  │   ├─ truth_map_wcs.py
  │   ├─ seed_backlog_wcs.py
  │   ├─ record_worker_result.py
  │   ├─ run_wcs_qa.py
  │   └─ escalate_task.py
  ├─ templates/
  ├─ reports/
  └─ qa/
```

### Runtime picture

```text
backlog + status files
        ↓
      jarvis.py
        ↓
   task packet written
        ↓
 human executes in Cursor
        ↓
 worker result captured
        ↓
 Playwright QA runs
        ↓
 done / failed / escalated
        ↓
 logs + status updated
```

This is the first real operating loop.

---

## 7. Workspace Layout

Recommended top-level layout:

```text
workspace-jarvis/
  brain/
    MASTER_BACKLOG.md
    DAILY_PLAN.md
    RUN_LOG.md
    PROJECT_STATUS_WCS.md
    PROJECT_STATUS_N8N.md
    ESCALATIONS.md
    AGENT_REGISTRY.md
    OPERATING_RULES.md
    master_backlog.json
    daily_plan.json
    run_log.json
    project_status_wcs.json
    project_status_n8n.json
    escalations.json

  tasks/
    open/
    in_progress/
    done/
    failed/
    escalated/

  templates/
    task_packet.template.json
    worker_result.template.json
    qa_result.template.json
    escalation_record.template.json

  scripts/
    jarvis.py
    truth_map_wcs.py
    seed_backlog_wcs.py
    record_worker_result.py
    run_wcs_qa.py
    escalate_task.py

  qa/
    playwright/
      tests/
      screenshots/
      reports/

  reports/
    daily/
    qa/
    truth_maps/
```

---

## 8. Core Files

### Markdown state files

#### `MASTER_BACKLOG.md`
Human-readable backlog view.
Should group WCS backlog by:

- Broken
- Ugly
- Incomplete
- Optimization

Phase 1 should only pull from:

- Broken
- Ugly

#### `DAILY_PLAN.md`
Shows the current selected task and why it was chosen.

#### `RUN_LOG.md`
Append-only human-readable log of runs, task selection, outcomes, and escalation notes.

#### `PROJECT_STATUS_WCS.md`
Repo truth snapshot, major areas, known risks, recent changes, and current confidence.

#### `PROJECT_STATUS_N8N.md`
Current known facts only. This project remains partially deferred until its quality rubric is formalized.

#### `ESCALATIONS.md`
Human-readable record of failures, pauses, operator intervention needs, and unresolved blockers.

### JSON sidecars

The JSON files mirror the operational parts of the markdown files and should be treated as the machine-facing contract.

---

## 9. JSON Sidecars

### Why sidecars exist

Markdown is good for people.  
JSON is good for scripts.

Using both avoids two bad outcomes:

- unreadable state hidden in a database too early
- brittle automation trying to scrape loose prose only

### Required sidecars

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Rule

Any field that affects routing, verification, escalation, or status transitions must exist in JSON.

---

## 10. Task Packet Standard

### Minimum packet fields

Every task packet must contain:

- `task_id`
- `project`
- `worker`
- `title`
- `problem`
- `goal`
- `scope`
- `suspected_files`
- `acceptance_criteria`
- `qa_method`
- `risk_level`
- `system_impact`
- `stop_conditions`
- `status`
- `created_at`

### Example packet shape

```json
{
  "task_id": "WCS-021",
  "project": "WCS",
  "worker": "wcs-cursor-worker",
  "title": "Fix mobile navbar overlap on home page",
  "problem": "Menu overlaps hero copy at small widths",
  "goal": "Navbar collapses cleanly without blocking hero content",
  "scope": "Navbar component and related mobile styles only",
  "suspected_files": [
    "components/navbar.tsx",
    "app/page.tsx",
    "app/globals.css"
  ],
  "acceptance_criteria": [
    "No overlap at mobile width",
    "Menu opens and closes correctly",
    "Hero content remains visible"
  ],
  "qa_method": "Playwright locator + screenshot",
  "risk_level": "low",
  "system_impact": "UI only; no auth, payment, or database changes expected",
  "stop_conditions": [
    "Requires route redesign",
    "Touches unrelated pages",
    "Needs new dependency"
  ],
  "status": "ready",
  "created_at": "2026-03-09T00:00:00"
}
```

---

## 11. Truth Mapping

### What truth mapping is

Truth mapping is the first discipline step before broad automation.

It means:

- scan the repo
- record structure
- identify likely app entry points
- capture scripts/configs
- note obvious risk areas
- update project status files with facts, not guesses

### WCS truth mapping should capture

- top-level folders
- framework indicators
- package scripts
- routing structure
- component structure
- key config files
- current test status if known
- likely fragile areas
- excluded areas if any

### Truth mapping outputs

- markdown summary in `PROJECT_STATUS_WCS.md`
- JSON summary in `project_status_wcs.json`
- optional report under `reports/truth_maps/`

### What truth mapping should not do

- invent architecture
- rewrite code
- mark tasks done
- make quality claims without evidence

---

## 12. WCS Operating Flow

### Phase-1 real flow

1. backlog is seeded
2. truth mapping is performed
3. `jarvis.py` selects the top bounded WCS task
4. Jarvis writes:
   - `DAILY_PLAN.md`
   - `daily_plan.json`
   - task packet file
5. operator opens Cursor and executes the packet
6. worker result is recorded
7. Playwright QA runs
8. task becomes:
   - done
   - failed
   - escalated
9. logs and project status update

### Why semi-manual is correct

Because you already use Cursor, already pay for it, and can get real value without pretending the interface is mature enough for unattended coding.

This is honest progress, not fake autonomy.

---

## 13. QA Operating Flow

### QA inputs

- task packet
- changed files summary
- acceptance criteria
- target route or test target

### QA outputs

- `qa_result.json`
- pass/fail
- evidence path
- issue notes
- retest recommendation

### QA rules

- builder confidence does not matter if QA fails
- failed QA does not auto-retry the code change in phase 1
- QA hard fail triggers escalation
- evidence must be written before a task can be marked complete

### WCS QA examples

- page loads
- button exists
- modal opens
- navigation works
- screenshot looks acceptable
- no overlap / visibility regression

---

## 14. n8n Status

The n8n project is important but under-defined for automation.

### Current decision

n8n remains **recognized but deferred** until the quality rubric is machine-checkable.

### Why

Because “better content” is not enough.  
The system needs measurable checks such as:

- required blocks present
- schema valid
- output length within bounds
- score against a known rubric
- banned failures absent

### Until then

n8n can still exist in the backlog and status files, but it should not be treated as a phase-1 autonomous worker path.

---

## 15. Failure Handling

### Failure types

- malformed JSON output
- missing required packet fields
- missing target files
- QA hard fail
- task exceeds scope
- unclear system impact
- operator input required

### Phase-1 numeric policy

| Policy item | Value |
|---|---|
| Planned tasks per cycle | 1 |
| WCS tasks per day | 1 |
| Planning timeout | 90 sec |
| QA timeout | 300 sec |
| Parse retry | 1 |
| QA auto-retry | 0 |
| Consecutive escalations before pause | 2 |

### Pause rule

Two consecutive escalated or failed active tasks pause further execution until reviewed.

### Escalation record should include

- task ID
- time
- reason
- evidence
- recommended next action
- pause flag

---

## 16. Cost Controls

Cost discipline must be operational, not rhetorical.

### Phase-1 cost rules

- use one LLM decision call per planning cycle where possible
- do not run multiple workers per cycle
- avoid premium model usage for low-value file shuffling
- log model usage if available
- keep phase 1 manual enough to avoid runaway tool churn

### Why this matters

If a project cannot stay understandable and cheap at low scale, it has no business pretending it will scale.

---

## 17. Scheduling Rules

Scheduling is deferred until the manual loop feels trustworthy.

### Scheduling activation requirements

- valid task packets produced consistently
- worker result flow stable
- WCS QA stable
- escalation handling proven
- no silent state corruption

### First scheduled configuration

- one cycle at a fixed time
- one task max
- no overlapping runs
- pause honored automatically

---

## 18. Future Modules

Future workers are allowed, but only if each new worker defines:

- purpose
- scope
- input packet
- output JSON
- QA path
- escalation rules
- activation conditions

### Likely future modules

- error/issues research scout
- X.com content topic researcher
- n8n content improver
- local machine maintenance worker
- voice interface layer

### Expansion rule

Do not add a new worker to compensate for a broken core.

Fix the core first.

---

## 19. Build Order

### The realistic sequence

#### Days 1–2
- create workspace structure
- create markdown files
- create JSON sidecars
- build `jarvis.py` planning loop
- build WCS truth mapping

#### Day 3
- create task packet templates
- create worker result template
- create QA result template
- test mock worker loop

#### Days 4–5
- run one semi-manual WCS task through Cursor
- capture result
- record changed files and notes

#### Days 6–7
- run Playwright QA
- test done/fail/escalate transitions
- update logs and status correctly

### Anything beyond this in week 1 is greed

No voice.  
No LangGraph.  
No extra workers.  
No scheduling hype.

---

## 20. Glossary

### Jarvis
The orchestrator / foreman script.

### Task packet
The bounded machine-readable work order.

### Truth mapping
The fact-gathering repo scan that grounds project state.

### Worker
A narrow executor with known scope and outputs.

### QA worker
The verification layer that checks work independently.

### Sidecar
A JSON file paired with a markdown file for machine-readable state.

### Escalation
A recorded failure, blocker, or operator-intervention event.

### System impact
A statement about what areas a task could affect and why that matters.
```

## FILE: JARVIS_SCRIPT_PROCESS_REFERENCE.md
````md
# JARVIS_SCRIPT_PROCESS_REFERENCE_v2.md

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
12. The worker result JSON is finalized truthfully (placeholders replaced with factual data).
13. QA is run in the WCS repo using:
    - `npm run build`
    - `npm run test:e2e:smoke`
14. The QA result JSON is finalized truthfully (placeholders replaced with factual data).
15. `stamp_result_timestamp.py` is run once for the worker result file and once for the QA result file.
16. `pre_reconcile_check.py` is run as a read-only readiness gate.
17. `reconcile_task_outcome.py --task WCS-XXX` is run.
18. Reconcile verifies:
    - valid worker result
    - valid QA result
    - expected branch == current branch
    - task branch has committed work and is ahead of `main`
    - repo/task evidence is sufficient
19. Backlog JSON and rendered Markdown are updated from reconcile output.
20. If task packet artifacts exist, reconcile also syncs task packet JSON and task packet markdown to the same terminal outcome (`done`, `blocked`, or `escalated`) so packet files do not remain misleadingly `ready`.
21. Backlog/state remains authoritative; task packet artifacts remain generated/operator-facing views that are kept aligned during reconcile.
22. `post_reconcile_validate.py` is run as a read-only validator of final state surfaces.

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

**Local machine-state handling:** `state/project_status_wcs.json` is machine-specific local state and should normally stay out of commits. To avoid Git status noise from local path/config differences, you can run:

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


## FILE: JARVIS_TASK_EXECUTION_CHECKLIST.md
````md
# JARVIS_TASK_EXECUTION_CHECKLIST_v2.md

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

Perform the bounded WCS worker change through Cursor or by direct operator edit.

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

Cursor is currently the execution surface for the WCS worker, but the operator still validates the result.

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

* commit-state verification before worker result finalization
* stronger branch/commit summaries
* commit gate helper that refuses unsafe repo state

---

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

## Phase 11 — Stamp finalized result timestamps

### Current action

Stamp the finalized worker result and QA result files with real local timestamps.

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


## FILE: JARVIS_PHASE_CHECKLIST.md
# JARVIS_REBUILD_PHASE_CHECKLIST.md

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
- **Phase 3 — true Jarvis foreman loop:** foreman built; daily plan/run log active; live cycles and optional state (escalations, etc.) still in progress
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
- [x] Decide Cursor remains the current semi-manual coding worker
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
- [ ] Make `escalations.json` real and active
- [ ] Make `ESCALATIONS.md` real and active
- [x] Make `project_status_n8n.json` real even if deferred
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
- [ ] Add research scout for debugging support
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
- [ ] Build `render_file_registry.py`
- [ ] Stop hand-maintaining `FILE_REGISTRY.md`
- [ ] Add health checks for new critical scripts/configs
- [ ] Harden all script wrappers
- [ ] Standardize output log locations
- [ ] Reduce naming drift across docs/state/scripts
- [ ] Improve evidence reporting and human review surfaces

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
- [ ] Complete escalation state files (`escalations.json` / `ESCALATIONS.md`) and any remaining state surfaces
- [ ] Run real Jarvis-controlled WCS cycles and prove consecutive-task stability
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

## FILE: JARVIS HARDENING CONTEXT ANCHOR — CURRENT PRIORITIES_3-12-26.txt
# JARVIS HARDENING CONTEXT ANCHOR — CURRENT PRIORITIES

We are **not** designing Jarvis from scratch.
We are **not** prioritizing sexy features, dashboards, more agents, or broad expansion right now.

We are in the middle of **hardening `jarvis.py`** so the system can move toward **little to zero human interaction** without turning into uncontrolled garbage.

## Current truth

The project already has meaningful working pieces:
- backlog rendering
- task packet generation
- reconcile flow
- public scout / defect normalization
- overnight health check
- real WCS tasks already completed through the system
- `jarvis.py` exists and is active

So the problem is **not** “invent more architecture.”
The problem is:

> the live loop still depends too much on operator discipline.

That means the next work is to convert fragile human checks into enforced system guardrails.

---

# What we are optimizing for

Primary goal:
- **low-human-interaction autonomy**

That means Jarvis must be able to:
1. choose work safely
2. detect when work is not safe to proceed
3. validate artifacts truthfully
4. detect bad repo/task state
5. pause and escalate cleanly
6. reconcile state without corruption

We are aiming for:
- **human exception handling**
- **not human babysitting**

---

# What "hardening jarvis.py" means right now

## Top priority items

### 1. Escalation state completion
Jarvis must formally track:
- blockers
- repeated failures
- pause conditions
- human intervention required
- escalation notes

This should use real state surfaces such as:
- `ESCALATIONS.md`
- `escalations.json`

This is a high priority because autonomy is fake if failures only live in the operator’s head.

---

### 2. Human-action-required recording
`jarvis.py` should explicitly record when it cannot safely proceed and why.

Examples:
- task packet missing
- wrong branch
- repo dirty
- repeated QA failure
- malformed worker result
- malformed QA result
- reconcile not safe
- circuit-breaker condition hit

This should be machine-visible state, not informal terminal commentary.

---

### 3. State-surface completion
Finish and harden the state files and their relationships.

Examples:
- `AGENT_REGISTRY.md`
- `OPERATING_RULES.md`
- `ESCALATIONS.md`
- `escalations.json`

Goal:
- every state surface should have a clear purpose
- no stale fake placeholders
- no ambiguity about which file is authoritative for what

---

### 4. Prove repeated live WCS cycles
We need repeated real-world proof of the boring loop:

1. Jarvis selects task
2. Jarvis writes packet
3. correct task branch is prepared
4. worker executes
5. worker result is captured
6. QA runs
7. QA result is captured
8. reconcile updates state
9. task ends as done / failed / escalated
10. loop repeats across multiple tasks

The goal is not one lucky run.
The goal is repeatable reliability.

---

### 5. Reuse vs `--force` guardrail
Jarvis currently risks confusion around reusing today’s selected task versus forcing a fresh selection.

Need:
- explicit logic
- explicit messaging
- explicit guardrails so the wrong task does not get worked accidentally

---

### 6. Branch and repo cleanliness verification
Before execution, Jarvis should verify:
- correct task branch
- repo clean before work starts
- no unresolved merge/rebase/conflict state
- branch matches packet task
- expected repo path is correct

This should be enforced, not assumed.

---

### 7. Packet/repo mismatch detection
Jarvis should detect when:
- packet context does not match repo state
- scope drift has occurred
- actual changed files do not fit the intended task

This helps stop work before it becomes unrelated repo thrashing.

---

### 8. Diff sanity / changed-file allowlist validation
Jarvis should detect:
- suspiciously broad diffs
- unrelated changed files
- accidental refactors
- edits outside expected scope

This is a major anti-stupidity safeguard.

---

### 9. Worker-result schema validation
Jarvis should reject worker result artifacts that are:
- missing required fields
- invalid status
- fake or placeholder-shaped
- incorrectly stamped
- claiming files that do not match reality
- missing executor identity or evidence

No reconcile should happen from trash artifacts.

---

### 10. QA-result schema validation
Jarvis should reject QA artifacts that are:
- placeholder-shaped
- missing checks
- fake pass/fail output
- invalid status
- not tied to actual build/test evidence

---

### 11. Pre-reconcile readiness check
Before reconcile, Jarvis should confirm:
- worker result exists
- QA result exists
- both are valid
- statuses are allowed
- evidence is real
- task is actually ready for reconcile

No more blind reconcile.

---

### 12. Post-reconcile state validation
After reconcile, Jarvis should verify:
- correct task changed
- adjacent tasks did not accidentally change
- JSON state is correct
- rendered Markdown matches JSON
- no drift or corruption was introduced

This is critical because the system uses JSON as state and Markdown as rendered human view.

---

### 13. Dedicated Python QA runner
QA should move away from semi-manual interpretation and toward a controlled entrypoint that:
- runs build/test commands
- captures stdout/stderr
- writes real QA artifacts
- returns structured pass/fail/escalate status

This should be pulled earlier if possible because it reduces operator dependency.

---

### 14. Commit gate helper
Before finalizing task work, Jarvis should verify:
- correct branch
- no unrelated file changes
- valid commit exists
- worktree state is acceptable
- no post-commit repo mess remains

---

# Implementation priority order

## Build now (current high-priority hardening focus)
1. commit gate helper
2. dual-stamp / no-draft-stamping guardrails
3. file registry automation
4. naming drift cleanup

## Build later
18. limited scheduling
19. Research Scout worker
20. n8n improver worker
21. additional workers / productization

---

# What we are NOT prioritizing right now

Do **not** derail into:
- dashboards
- sexy UI
- more agents
- worker marketplaces
- voice features
- office copilots
- sandboxes everywhere
- generalized platform expansion
- productization before the loop is trustworthy

Those may matter later.
They are not the blocker now.

---

# CURRENT STATUS VS NEXT

## What is already proven
- reconcile branch verification is live
- reconcile verifies that the task branch is ahead of `main` for done-path completion
- `jarvis.py` exists and has materially improved operator-safety output
- task-state execution eligibility validation exists in `jarvis.py`
- packet/result placeholder contract validation exists in `jarvis.py`
- repeated live WCS cycles have been proven for `WCS-016`, `WCS-017`, `WCS-018`, and `WCS-019`
- fake tasks must be baseline-relative when new task branches are created from `main`
- `jarvis.py` now records durable escalation state on hard failures into `state/escalations.json` and renders `state/ESCALATIONS.md` as the human view
- `pre_reconcile_check.py` exists and is proven as a read-only readiness gate that validates task/result/repo prerequisites before running reconcile
- `post_reconcile_validate.py` exists and is proven as a read-only post-reconcile validator that confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, review output, and result files
- `worker_change_check.py` exists and is proven as a read-only worker-boundary validator that checks changed-file scope and simple diff sanity; it validates from the working tree when there are uncommitted changes and from the HEAD commit when the working tree is clean, so the post_worker flow is consistent with the commit gate (including PASS on committed state, e.g. WCS-040)
- `commit_gate_check.py` exists and is proven as a read-only commit-state gate for a WCS task branch and HEAD, with a real PASS path inside a completed/reconciled loop (currently including `WCS-019`)

## What remains the next priority
- Dual-stamp / no-draft-stamping core guardrails are now live via `stamp_guard_check.py` as a read-only pre-stamp helper that runs before `stamp_result_timestamp.py`.
- File-registry drift/coverage checking is now live via `file_registry_check.py` (read-only helper; part of hardening surfaces, not the core task execution loop).
- Naming-drift detection across core hardening surfaces is now live via `naming_drift_check.py` as a read-only helper that reports obvious inconsistencies between core scripts/docs and the file registry without auto-fixing names.
- Registry rendering is now live via `render_file_registry.py` as a helper that renders `state/FILE_REGISTRY.md` from `state/file_registry.json` in the approved registry format.
- Critical-surface health checking is now live via `critical_surface_health_check.py` as a read-only sanity checker (existence of critical scripts/docs/registry, compile of critical helpers, and file_registry_check + naming_drift_check pass).
- Cursor handoff building is now live via `build_cursor_handoff.py` as a workflow helper that writes bounded, copy/paste-ready handoff files from task packets (does not execute tasks or mutate state). It fails with exit code 1 and does not write a handoff file when bounded file scope cannot be derived from the task packet.
- Task-cycle summary building is now live via `build_task_cycle_summary.py` as a workflow helper that reads current task packet, worker result, and QA result (when present) and writes a human-readable markdown summary under `scratch/task_cycle_summaries/` for a single WCS task cycle; it does not execute tasks, change task state, or mutate backlog/results.
- Guarded task-cycle orchestration is now live via `run_guarded_task_cycle.py` as a workflow/orchestration helper that runs the existing guarded task-cycle scripts in order and stops on the first failure; it does not replace their logic, execute worker code directly, or schedule tasks. **pre_worker** is unchanged. In **post_worker** and **full** modes, the operator can now optionally pass `--draft-worker-result` plus repeatable truthful `--worker-command <text>` values (and optional `--worker-executor <text>`); the orchestration then inserts a step named `draft_worker_result_from_evidence` immediately before `worker_result_validate.py --mode pre-stamp`, runs `draft_worker_result_from_evidence.py --write`, passes `--worker-command` through as `--command`, and passes `--worker-executor` through as `--executor` when supplied. Missing worker-result JSON is tolerated only when `--draft-worker-result` is supplied; otherwise the run still fails with the explicit missing-worker-result message. Worker commands are still explicit operator input, not auto-captured or inferred. In **post_worker** and **full** modes, the existing optional `--draft-qa-result` QA wiring remains intact and unchanged in this step: the orchestration inserts `draft_qa_result_from_evidence.py --write` before pre-stamp QA validation when QA draft args are supplied, and otherwise still requires the QA result JSON file. This remains optional drafting integration only; no automatic QA execution or log parsing was added.
- Next-task selection is now live via `select_next_ready_task.py` as a read-only workflow helper that selects the next eligible ready task from backlog/planning surfaces using the explicit progression ladder (execution_lane, test_phase, selector_rank) when present, supporting fake/reversible-first testing; it does not mutate state or launch execution.
- Daily execution prep is now live via `build_daily_execution_prep.py` as a workflow helper that prepares an operator-facing daily execution prep package by chaining selection, ensuring task packet availability by invoking `generate_task_packet.py` when needed, then handoff and summary helpers; it writes prep markdown and helper outputs only, does not execute the task itself, and does not mutate backlog/state beyond approved helper outputs (e.g. packet generation when missing).
- **draft_worker_result_from_evidence.py** now supports truthful worker command evidence via repeatable `--command <text>`: explicit operator-supplied commands populate `commands_run`, entries are normalized (trimmed, empty values dropped, obvious placeholders rejected), and `worker_complete` drafting now fails clearly unless at least one meaningful command is provided. This closes the practical validator/stamp-guard gap for `commands_run` without inventing command history. Commands are not auto-inferred from repo evidence or `evidence_source`.
- **draft_qa_result_from_evidence.py** is built and live: drafts truthful pre-stamp QA result JSON from operator-supplied evidence (CLI: build/smoke/manual status); dry-run by default, `--write` to persist; does not stamp, reconcile, or fabricate evidence; validated in pre-stamp mode (e.g. WCS-042 with qa_result_validate.py). v1 is CLI-evidence-driven and does not auto-parse build/test logs; operator still reviews before post-worker.
- A real guarded end-to-end task cycle has succeeded on **WCS-042** (Agent-first run_cursor_worker, task repo workspace, draft_worker_result_from_evidence, stamp, QA, reconcile).
- Other hardening focus areas: manual naming drift cleanup guided by `naming_drift_check.py`; optional further registry automation or script wrappers.

## Cursor worker execution wrapper (live)

The current workflow stack is strong through task selection, packet generation, daily execution prep, handoff generation, and the guarded pre/post-worker flow. `run_cursor_worker.py` is live as an **Agent-first Cursor invocation bridge** for the current WCS worker execution surface: it prefers the real **agent** CLI when available (Windows-hardened detection), then falls back to the desktop cursor launcher. Execution runs against the **task repo workspace** (`repo_path` from the task packet), not the Jarvis workspace; Agent is invoked with `--workspace <repo_path>` and `--trust`; handoff content is passed as prompt when small enough. It reports PASS / BLOCKED / FAIL honestly; output includes both Jarvis workspace and task repo workspace. It does not fabricate completion or write a fake worker_complete result. The operator still verifies completion and finalizes worker-result evidence. The system remains **operator-assisted at the completion/evidence stage**; full autonomy is not claimed.

**Worker-result drafting:** `draft_worker_result_from_evidence.py` is live and proven. It drafts a truthful `worker_result.json` from task packet and repo evidence (branch, changed files), plus explicit operator-supplied `--command <text>` entries for `commands_run`. Those command entries are trimmed, empty values are dropped, and obvious placeholders like `todo`, `tbd`, and `placeholder` are rejected. For `worker_complete`, at least one meaningful `--command` is now required or the draft fails clearly before writing. The script does not auto-infer commands from `evidence_source`, does not fabricate shell history, and does not stamp or reconcile. WCS-042 proved the negative cases (no `--command`, placeholder-only `--command`) and the positive path (dry-run, write, `worker_result_validate.py --mode pre-stamp`, and `stamp_guard_check.py` PASS).

**Guarded-flow worker-draft integration:** `run_guarded_task_cycle.py` now optionally wires worker-result drafting into **post_worker** and **full** by adding `--draft-worker-result`, repeatable `--worker-command <text>`, and optional `--worker-executor <text>`. The inserted step is `draft_worker_result_from_evidence`, and it runs immediately before `worker_result_validate.py --mode pre-stamp`. If meaningful `--worker-command` input is missing, the guarded run fails at that inserted worker-draft step and stops there. Worker commands are still explicit operator-supplied truth, not auto-captured shell history. QA draft wiring was not changed in this step.

**Safe proof boundary on completed WCS-042:** the new guarded-flow worker-draft path was proven on WCS-042 up to a safe honest boundary: `worker_change_check` PASS, `commit_gate_check` PASS, `draft_worker_result_from_evidence` PASS, and `worker_result_validate_pre_stamp` PASS. The proof then intentionally stopped before stamp/reconcile by temporarily forcing QA pre-stamp validation to fail and restoring the QA file afterward, so this step does not claim a fresh full successful `post_worker` or `full` completion rerun on already-completed WCS-042.

**QA-result drafting:** `draft_qa_result_from_evidence.py` is live and validator-proven. It drafts a truthful pre-stamp `qa_result.json` from operator-supplied evidence (CLI: build/smoke/manual status). Dry-run by default; `--write` to persist. It does not stamp, reconcile, or fabricate checks/artifacts; v1 does not auto-parse build/test logs. The operator should review the drafted result before stamp and guarded post-worker flow.

## What is explicitly not being prioritized yet
- dashboards and “sexy” UI
- additional workers or marketplaces
- voice features
- broad multi-project scheduling
- generalized productization before the current loop is trustworthy

---

# Process documentation rule

Whenever a new process change, guardrail, contract, or script behavior is **locked in and live**, the working process and hardening documentation files in this workspace **must be updated immediately** so they stay aligned with the actual system.

---

# Simple framing for the next assistant

If you are helping on this project, assume this rule:

> The next best work is anything that converts operator discipline into system-enforced guardrails inside or immediately around `jarvis.py`.

Do not propose broad redesign unless it directly helps the above hardening goals.

Do not treat the project as greenfield.

Do not push scheduling or more workers before the current loop is trustworthy.

---

# Immediate coding focus

We are currently hardening `jarvis.py`.

The assistant should help identify and implement:
- escalation recording
- human-action-required state
- branch/repo/packet guardrails
- artifact schema validation
- reconcile readiness checks
- post-reconcile validation

These are the current priorities.

## FILE: JARVIS_CODEBASE_STRUCTURE.md
# Jarvis Workspace — Codebase Structure

## Purpose

This document describes the layout and conventions of the Jarvis workspace so you can find things quickly and understand how folders and files relate. For a full list of registered files and their roles, see `state\FILE_REGISTRY.md` and `state\file_registry.json`.

**Conventions (locked):**

- **JSON** = machine-readable source of truth where it exists.
- **Markdown** = human-readable view (often rendered from JSON or written by scripts).
- **scripts** = Python (and some PowerShell wrappers) that operate on **state** and **config**.
- **One bounded WCS task at a time**; task artifacts live under `tasks\`, `results\`, `qa\`, and sometimes `logs\`.

---

## Top-Level Layout

```
jarvis-workspace/
├── config/           # Configuration (scout routes, noise rules)
├── logs/             # All runtime logs (scout, health check, escalation)
├── qa/               # QA result JSONs per task (e.g. WCS-010_qa_result.json)
├── results/          # Worker result JSONs per task (e.g. WCS-010_worker_result.json)
├── scripts/          # Python foreman and support scripts (+ PS1 wrappers, docs)
├── state/            # Source-of-truth state (backlog, plan, run log, project status, registry)
├── tasks/            # Task packets (JSON + Markdown) per WCS task
├── scratch/          # Ad-hoc working copies and rescue files (not part of official loop)
│
├── README_START_HERE.md
├── JARVIS_PHASE_CHECKLIST.md
├── JARVIS_AGENT_IDEA_BACKLOG.md
├── CODEBASE_STRUCTURE.md   # this file
└── (handoff/other root docs as needed)
```

---

## Folder Roles

### `config/`

- **Purpose:** Configuration consumed by scripts; not state.
- **Key files:**
  - `scout_noise_rules.json` — Rules for filtering known scout noise in defect normalization.
  - `wcs_scout_routes.json` — Routes and options for the WCS public scout run.

### `logs/`

- **Purpose:** Runtime output only; append-only or timestamped. Do not treat as source of truth.
- **Contents:**
  - `wcs_scout/<timestamp>/` — Per-run scout output (Playwright results, normalizer report, summaries).
  - `overnight_health_*.json` / `overnight_health_*.txt` — Overnight health check results.
  - `WCS-<id>_escalation.json` — Escalation records for a task (when used).

### `qa/`

- **Purpose:** One QA result file per task, e.g. `WCS-010_qa_result.json`. Evidence for done/fail/escalate.
- **Owner:** Playwright (or manual) run; reconciled by `reconcile_task_outcome.py`.

### `results/`

- **Purpose:** One worker result file per task, e.g. `WCS-010_worker_result.json`. What the WCS worker did.
- **Owner:** Operator / WCS worker evidence capture; timestamps can be set via `stamp_result_timestamp.py`.

### `scripts/`

- **Purpose:** All automation and runbooks. Python is canonical; `.ps1` files are wrappers or convenience.
- **Key scripts:**
  - **Foreman:** `jarvis.py` — Selects one WCS task, writes `daily_plan.json` / `DAILY_PLAN.md`, appends to run log, generates task packet, prepares branch.
  - **Backlog / packet:** `render_master_backlog.py`, `generate_task_packet.py`, `reconcile_task_outcome.py`.
  - **Scout / intake:** `run_wcs_scout.py`, `normalize_scout_to_backlog.py` (plus `.ps1` wrappers where present).
  - **Operations:** `overnight_health_check.py`, `prepare_wcs_task_branch.py`, `stamp_result_timestamp.py`.
- **Also:** `manual_loop_checklist.md`, `cursor_completion_contract.txt`, and other runbook/spec snippets.

### `state/`

- **Purpose:** Durable, source-of-truth state that drives the system. JSON is primary; Markdown is human view.
- **Key files:**
  - **Backlog:** `master_backlog.json`, `MASTER_BACKLOG.md`.
  - **Plan / run log:** `daily_plan.json`, `DAILY_PLAN.md`, `run_log.json`, `RUN_LOG.md`.
  - **Project status:** `project_status_wcs.json`, `PROJECT_STATUS_WCS.md`, `project_status_n8n.json`, `PROJECT_STATUS_N8N.md`.
  - **Registry:** `file_registry.json`, `FILE_REGISTRY.md`.
  - **Other:** `DAILY_REVIEW.md`; test/backlog variants (e.g. `master_backlog_test.json`) as needed.

### `tasks/`

- **Purpose:** One task packet per WCS task. Generated by `generate_task_packet.py` (or by Jarvis); consumed by the worker.
- **Pattern:** `WCS-<id>_task.json`, `WCS-<id>_task.md`.

### `scratch/`

- **Purpose:** Ad-hoc or rescue work (e.g. copied components, one-off specs). Not part of the official task/result/QA loop. Can be ignored for “where does the system live?” questions.

---

## Data Flow (Simplified)

1. **Backlog** (`state\master_backlog.json`) + **project status** (`state\project_status_wcs.json`) → **Jarvis** (`scripts\jarvis.py`) selects one task.
2. **Jarvis** writes **daily plan** and **run log** (`state\daily_plan.json`, `state\run_log.json`, plus `.md`), then generates **task packet** (`tasks\WCS-<id>_task.*`) and prepares branch (WCS repo).
3. **Worker** (e.g. Cursor) does the work; fills **worker result** (`results\WCS-<id>_worker_result.json`).
4. **QA** (semi-manual, via Playwright) runs:
   - `npm run build`
   - `npm run test:e2e:smoke`
   and produces **QA result** (`qa\WCS-<id>_qa_result.json`).
5. **Pre-reconcile check** (`pre_reconcile_check.py`) runs as a read-only gate to confirm task/result/repo readiness.
6. **Reconcile** (`reconcile_task_outcome.py`) updates backlog and status from worker + QA evidence, verifying branch state and commits ahead of main; escalation artifacts may go to `logs\` or state.
7. **Post-reconcile validation** (`post_reconcile_validate.py`) runs as a read-only validator to confirm the task is marked done and visible in backlog JSON, rendered backlog markdown, review surfaces, and result files.
8. **Escalation state surfaces** (`state\escalations.json`, `state\ESCALATIONS.md`) reflect durable Jarvis hard failures when they occur.
9. **Worker-boundary and result-schema helpers**:
   - `worker_change_check.py` — read-only validator for changed-file scope and simple diff sanity before commit.
   - `worker_result_validate.py` — read-only schema validator for worker result JSON in pre-stamp and post-stamp modes.
   - `qa_result_validate.py` — read-only schema validator for QA result JSON in pre-stamp and post-stamp modes.

Scout path: **Scout run** → `logs\wcs_scout\<timestamp>\` → **normalizer** (`normalize_scout_to_backlog.py`) → backlog updates (and optional `MASTER_BACKLOG.md` re-render).

---

## Where to Look Next

- **First-time setup and one manual loop:** `README_START_HERE.md`
- **Phase status and what’s done next:** `JARVIS_PHASE_CHECKLIST.md`
- **Every registered file and its role:** `state\FILE_REGISTRY.md` (and `state\file_registry.json` for tooling)
- **WCS repo path and local URL:** `README_START_HERE.md` (e.g. `C:\dev\wcsv2.0-new`, `http://localhost:3000`)


## FILE: state/file_registry.json
[
  {
    "file": "JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "High-level product requirements for Jarvis rebuild",
    "updated_by": "user",
    "notes": "Core planning doc"
  },
  {
    "file": "JARVIS_SYSTEM_DOCUMENTATION_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_SYSTEM_DOCUMENTATION_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Detailed architecture and operating documentation",
    "updated_by": "user",
    "notes": "Core planning doc"
  },
  {
    "file": "JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Current authoritative decisions and system rules",
    "updated_by": "user",
    "notes": "Most important design reference"
  },
  {
    "file": "master_backlog.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\master_backlog.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable task backlog",
    "updated_by": "user / jarvis_script",
    "notes": "Primary backlog source"
  },
  {
    "file": "MASTER_BACKLOG.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\MASTER_BACKLOG.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable backlog table",
    "updated_by": "render_master_backlog.py",
    "notes": "Rendered from master_backlog.json"
  },
  {
    "file": "DAILY_REVIEW.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\DAILY_REVIEW.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Daily execution log and summary",
    "updated_by": "user / jarvis_script",
    "notes": "Reconcile appends entries"
  },
  {
    "file": "DAILY_PLAN.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\DAILY_PLAN.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Current planned work for the day",
    "updated_by": "user",
    "notes": "Lightly used so far"
  },
  {
    "file": "PROJECT_STATUS_WCS.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\PROJECT_STATUS_WCS.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Human-readable WCS project status",
    "updated_by": "user / jarvis_script",
    "notes": "May later be rendered"
  },
  {
    "file": "PROJECT_STATUS_N8N.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\PROJECT_STATUS_N8N.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Human-readable n8n project status",
    "updated_by": "user",
    "notes": "n8n worker deferred"
  },
  {
    "file": "file_registry.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\file_registry.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable file registry",
    "updated_by": "user / jarvis_script",
    "notes": "Source for FILE_REGISTRY.md"
  },
  {
    "file": "FILE_REGISTRY.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\FILE_REGISTRY.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable file registry",
    "updated_by": "user / future renderer",
    "notes": "Registry view"
  },
  {
    "file": "render_master_backlog.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\render_master_backlog.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Renders MASTER_BACKLOG.md from backlog JSON",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "update_master_backlog.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\update_master_backlog.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for backlog renderer",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "generate_task_packet.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\generate_task_packet.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Creates task packet files and blank result files",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "generate_task_packet.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\generate_task_packet.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for task generator",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "reconcile_task_outcome.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Reconciles worker and QA results into backlog state",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "reconcile_task_outcome.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for reconciler",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "cursor_completion_contract.txt",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\cursor_completion_contract.txt",
    "category": "template",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Forces structured Cursor completion summaries",
    "updated_by": "user",
    "notes": "Used in worker prompts"
  },
  {
    "file": "overnight_health_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\overnight_health_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only overnight system health watcher",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "run_overnight_health_check.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_overnight_health_check.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Wrapper for overnight health watcher",
    "updated_by": "user",
    "notes": "Used for manual or scheduled runs"
  },
  {
    "file": "register_overnight_health_task.txt",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\register_overnight_health_task.txt",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Task Scheduler command notes",
    "updated_by": "user",
    "notes": "Scheduling helper"
  },
  {
    "file": "run_wcs_scout.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_wcs_scout.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Runs public WCS scout and stores results",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "wcs_scout_routes.json",
    "path": "C:\\dev\\jarvis-workspace\\config\\wcs_scout_routes.json",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Public routes list for WCS scout",
    "updated_by": "user",
    "notes": "/shop and /news removed for now"
  },
  {
    "file": "WCS-001_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-001_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-001_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-001_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-002_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-002_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-002_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-002_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-003_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-003_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-003_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-003_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-004_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-004_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Completed after branch cleanup"
  },
  {
    "file": "WCS-004_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-004_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Completed after branch cleanup"
  },
  {
    "file": "WCS-011_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-011_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "QA infrastructure task"
  },
  {
    "file": "WCS-011_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-011_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "QA infrastructure task"
  },
  {
    "file": "*_worker_result.json",
    "path": "C:\\dev\\jarvis-workspace\\results\\*_worker_result.json",
    "category": "worker_result",
    "source_type": "runtime_output",
    "owner": "cursor_worker",
    "purpose": "Worker completion record per task",
    "updated_by": "user / cursor_worker",
    "notes": "Reconciler input"
  },
  {
    "file": "*_qa_result.json",
    "path": "C:\\dev\\jarvis-workspace\\qa\\*_qa_result.json",
    "category": "qa_result",
    "source_type": "runtime_output",
    "owner": "playwright",
    "purpose": "QA completion record per task",
    "updated_by": "user / playwright",
    "notes": "Reconciler input"
  },
  {
    "file": "*_escalation.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\*_escalation.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Escalation record for blocked or escalated tasks",
    "updated_by": "user / jarvis_script",
    "notes": "May be blank for many tasks"
  },
  {
    "file": "overnight_health_*.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\overnight_health_*.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Machine-readable overnight health output",
    "updated_by": "overnight_health_check.py",
    "notes": "Working"
  },
  {
    "file": "overnight_health_*.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\overnight_health_*.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Human-readable overnight health summary",
    "updated_by": "overnight_health_check.py",
    "notes": "Working"
  },
  {
    "file": "public_scout_results.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_results.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Structured route scout results",
    "updated_by": "run_wcs_scout.py / public_scout.spec.ts",
    "notes": "Latest run currently PASS"
  },
  {
    "file": "public_scout_summary.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_summary.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Human-readable scout summary",
    "updated_by": "run_wcs_scout.py",
    "notes": "Latest run currently PASS"
  },
  {
    "file": "playwright_stdout.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\playwright_stdout.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Raw Playwright stdout from scout run",
    "updated_by": "run_wcs_scout.py",
    "notes": "Debug support"
  },
  {
    "file": "playwright_stderr.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\playwright_stderr.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Raw Playwright stderr from scout run",
    "updated_by": "run_wcs_scout.py",
    "notes": "Debug support"
  },
  {
    "file": "public_scout.spec.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\public_scout.spec.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Public route scout spec for WCS",
    "updated_by": "user",
    "notes": "External WCS repo Playwright spec at C:\\dev\\wcsv2.0-new\\tests\\e2e"
  },
  {
    "file": "home.spec.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\home.spec.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Smoke QA spec for home page",
    "updated_by": "user",
    "notes": "External WCS repo Playwright spec at C:\\dev\\wcsv2.0-new\\tests\\e2e"
  },
  {
    "file": "global-setup.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\helpers\\global-setup.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Shared Playwright startup and readiness logic",
    "updated_by": "user",
    "notes": "External WCS repo Playwright helper at C:\\dev\\wcsv2.0-new\\tests\\e2e\\helpers"
  },
  {
    "file": "package.json",
    "path": "C:\\dev\\wcsv2.0-new\\package.json",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Repo scripts including test:e2e:smoke",
    "updated_by": "user",
    "notes": "WCS repo-side dependency in external WCS repo at C:\\dev\\wcsv2.0-new"
  },
  {
    "file": "normalize_scout_to_backlog.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\normalize_scout_to_backlog.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Normalizes scout defects into backlog-ready tasks and updates backlog state",
    "updated_by": "user",
    "notes": "Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md"
  },
  {
    "file": "normalize_scout_to_backlog.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\normalize_scout_to_backlog.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for scout defect normalizer",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "scout_noise_rules.json",
    "path": "C:\\dev\\jarvis-workspace\\config\\scout_noise_rules.json",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Known scout noise filtering rules for backlog normalization",
    "updated_by": "user",
    "notes": "Used by normalize_scout_to_backlog.py"
  },
  {
    "file": "JARVIS_PHASE_CHECKLIST.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_PHASE_CHECKLIST.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Phase-by-phase rebuild checklist and status for Jarvis workspace",
    "updated_by": "user",
    "notes": "Current canonical overview of phases, missing state surfaces, and next priorities"
  },
  {
    "file": "JARVIS_AGENT_IDEA_BACKLOG.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_AGENT_IDEA_BACKLOG.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Idea backlog for short-term modules and longer-term agent business concepts",
    "updated_by": "user",
    "notes": "Reusable idea backlog aligned with current Jarvis architecture"
  },
  {
    "file": "manual_loop_checklist.md",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\manual_loop_checklist.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Manual proof-loop checklist for running a WCS task through backlog, worker, QA, and reconcile",
    "updated_by": "user",
    "notes": "Operator runbook; should be aligned with actual script and state behavior to avoid drift"
  },
  {
    "file": "jarvis.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\jarvis.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Phase 3 foreman; reads backlog and project status, selects one WCS task, writes daily_plan and run_log",
    "updated_by": "user",
    "notes": "Does not modify backlog or run workers; selection and plan/run-log recording only"
  },
  {
    "file": "prepare_wcs_task_branch.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\prepare_wcs_task_branch.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Prepares WCS task branch for bounded task work",
    "updated_by": "user",
    "notes": "Used in task workflow to create or switch to task branch in WCS repo"
  },
  {
    "file": "stamp_result_timestamp.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\stamp_result_timestamp.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Stamps completed_at (or similar) on worker and QA result JSON files",
    "updated_by": "user",
    "notes": "Helper to keep result timestamps consistent"
  },
  {
    "file": "daily_plan.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\daily_plan.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Current selected task and plan metadata; machine-readable",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py; pairs with DAILY_PLAN.md"
  },
  {
    "file": "run_log.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\run_log.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Append-only machine-readable run history",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py when a task is selected"
  },
  {
    "file": "RUN_LOG.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\RUN_LOG.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Append-only human-readable run log",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py when a task is selected"
  },
  {
    "file": "project_status_wcs.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\project_status_wcs.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable WCS project status",
    "updated_by": "user",
    "notes": "Mirror of PROJECT_STATUS_WCS.md; consumed by jarvis.py and scripts"
  },
  {
    "file": "project_status_n8n.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\project_status_n8n.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable n8n project status",
    "updated_by": "user",
    "notes": "Mirror of PROJECT_STATUS_N8N.md; n8n worker deferred"
  },
  {
    "file": "escalations.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\escalations.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Machine-readable escalation records for Jarvis hard failures",
    "updated_by": "jarvis.py",
    "notes": "Authoritative escalation state; rendered to ESCALATIONS.md"
  },
  {
    "file": "ESCALATIONS.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\ESCALATIONS.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable escalation log",
    "updated_by": "jarvis.py",
    "notes": "Rendered from escalations.json whenever Jarvis records an escalation"
  },
  {
    "file": "pre_reconcile_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\pre_reconcile_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only pre-reconcile readiness gate for a WCS task",
    "updated_by": "user",
    "notes": "Validates task/result/repo prerequisites before running reconcile"
  },
  {
    "file": "post_reconcile_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\post_reconcile_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only post-reconcile validator for a WCS task",
    "updated_by": "user",
    "notes": "Confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, DAILY_REVIEW.md, and result files"
  },
  {
    "file": "worker_change_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\worker_change_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only worker-boundary validator for changed-file scope and simple diff sanity",
    "updated_by": "user",
    "notes": "Validates that changed files stay within task scope and diffs are small before commit/finalization"
  },
  {
    "file": "worker_result_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\worker_result_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only worker-result schema validator for a WCS task",
    "updated_by": "user",
    "notes": "Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes"
  },
  {
    "file": "qa_result_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\qa_result_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only QA-result schema validator for a WCS task",
    "updated_by": "user",
    "notes": "Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes"
  }
]

## FILE: state/FILE_REGISTRY.md
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
| JARVIS_PHASE_CHECKLIST.md | C:\dev\jarvis-workspace\JARVIS_PHASE_CHECKLIST.md | doc | source_of_truth | user | Phase-by-phase rebuild checklist and status for Jarvis workspace | user | Current canonical overview of phases, missing state surfaces, and next priorities |
| JARVIS_AGENT_IDEA_BACKLOG.md | C:\dev\jarvis-workspace\JARVIS_AGENT_IDEA_BACKLOG.md | doc | source_of_truth | user | Idea backlog for short-term modules and longer-term agent business concepts | user | Reusable idea backlog aligned with current Jarvis architecture |
| master_backlog.json | C:\dev\jarvis-workspace\state\master_backlog.json | state | source_of_truth | user | Machine-readable task backlog | user / jarvis_script | Primary backlog source |
| MASTER_BACKLOG.md | C:\dev\jarvis-workspace\state\MASTER_BACKLOG.md | state | generated | jarvis_script | Human-readable backlog table | render_master_backlog.py | Rendered from master_backlog.json |
| DAILY_REVIEW.md | C:\dev\jarvis-workspace\state\DAILY_REVIEW.md | state | source_of_truth | user | Daily execution log and summary | user / jarvis_script | Reconcile appends entries |
| DAILY_PLAN.md | C:\dev\jarvis-workspace\state\DAILY_PLAN.md | state | source_of_truth | user | Current planned work for the day | user | Lightly used so far |
| PROJECT_STATUS_WCS.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_WCS.md | state | source_of_truth | user | Human-readable WCS project status | user / jarvis_script | May later be rendered |
| PROJECT_STATUS_N8N.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_N8N.md | state | source_of_truth | user | Human-readable n8n project status | user | n8n worker deferred |
| escalations.json | C:\dev\jarvis-workspace\state\escalations.json | state | source_of_truth | jarvis_script | Machine-readable escalation records for Jarvis hard failures | jarvis.py | Authoritative escalation state; rendered to ESCALATIONS.md |
| ESCALATIONS.md | C:\dev\jarvis-workspace\state\ESCALATIONS.md | state | generated | jarvis_script | Human-readable escalation log | jarvis.py | Rendered from escalations.json whenever Jarvis records an escalation |
| file_registry.json | C:\dev\jarvis-workspace\state\file_registry.json | state | source_of_truth | user | Machine-readable file registry | user / jarvis_script | Source for this markdown file |
| FILE_REGISTRY.md | C:\dev\jarvis-workspace\state\FILE_REGISTRY.md | state | generated | jarvis_script | Human-readable file registry | user / future renderer | Human-readable registry view; currently hand-maintained and intended to be rendered from file_registry.json later |
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
| manual_loop_checklist.md | C:\dev\jarvis-workspace\scripts\manual_loop_checklist.md | doc | source_of_truth | user | Manual proof-loop checklist for running a WCS task through backlog, worker, QA, and reconcile | user | Operator runbook; should be aligned with actual script and state behavior to avoid drift |
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
| public_scout.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\public_scout.spec.ts | repo_test | source_of_truth | playwright | Public route scout spec for WCS | user | External WCS repo Playwright spec at C:\dev\wcsv2.0-new\tests\e2e |
| home.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\home.spec.ts | repo_test | source_of_truth | playwright | Smoke QA spec for home page | user | External WCS repo Playwright spec at C:\dev\wcsv2.0-new\tests\e2e |
| global-setup.ts | C:\dev\wcsv2.0-new\tests\e2e\helpers\global-setup.ts | repo_test | source_of_truth | playwright | Shared Playwright startup and readiness logic | user | External WCS repo Playwright helper at C:\dev\wcsv2.0-new\tests\e2e\helpers |
| package.json | C:\dev\wcsv2.0-new\package.json | repo_test | source_of_truth | user | Repo scripts including test:e2e:smoke | user | WCS repo-side dependency in external WCS repo at C:\dev\wcsv2.0-new |
| normalize_scout_to_backlog.py | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.py | script | source_of_truth | jarvis_script | Normalizes scout defects into backlog-ready tasks and updates backlog state | user | Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md |
| normalize_scout_to_backlog.ps1 | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for scout defect normalizer | user | Convenience wrapper |
| scout_noise_rules.json | C:\dev\jarvis-workspace\config\scout_noise_rules.json | config | source_of_truth | user | Known scout noise filtering rules for backlog normalization | user | Used by normalize_scout_to_backlog.py |
| jarvis.py | C:\dev\jarvis-workspace\scripts\jarvis.py | script | source_of_truth | jarvis_script | Phase 3 foreman; reads backlog and project status, selects one WCS task, writes daily_plan and run_log | user | Does not modify backlog or run workers; selection and plan/run-log recording only |
| prepare_wcs_task_branch.py | C:\dev\jarvis-workspace\scripts\prepare_wcs_task_branch.py | script | source_of_truth | user | Prepares WCS task branch for bounded task work | user | Used in task workflow to create or switch to task branch in WCS repo |
| stamp_result_timestamp.py | C:\dev\jarvis-workspace\scripts\stamp_result_timestamp.py | script | source_of_truth | user | Stamps completed_at (or similar) on worker and QA result JSON files | user | Helper to keep result timestamps consistent |
| daily_plan.json | C:\dev\jarvis-workspace\state\daily_plan.json | state | source_of_truth | jarvis_script | Current selected task and plan metadata; machine-readable | jarvis.py | Written by jarvis.py; pairs with DAILY_PLAN.md |
| run_log.json | C:\dev\jarvis-workspace\state\run_log.json | state | source_of_truth | jarvis_script | Append-only machine-readable run history | jarvis.py | Written by jarvis.py when a task is selected |
| RUN_LOG.md | C:\dev\jarvis-workspace\state\RUN_LOG.md | state | source_of_truth | jarvis_script | Append-only human-readable run log | jarvis.py | Written by jarvis.py when a task is selected |
| project_status_wcs.json | C:\dev\jarvis-workspace\state\project_status_wcs.json | state | source_of_truth | user | Machine-readable WCS project status | user | Mirror of PROJECT_STATUS_WCS.md; consumed by jarvis.py and scripts |
| project_status_n8n.json | C:\dev\jarvis-workspace\state\project_status_n8n.json | state | source_of_truth | user | Machine-readable n8n project status | user | Mirror of PROJECT_STATUS_N8N.md; n8n worker deferred |
| pre_reconcile_check.py | C:\dev\jarvis-workspace\scripts\pre_reconcile_check.py | script | source_of_truth | jarvis_script | Read-only pre-reconcile readiness gate for a WCS task | user | Validates task/result/repo prerequisites before running reconcile |
| post_reconcile_validate.py | C:\dev\jarvis-workspace\scripts\post_reconcile_validate.py | script | source_of_truth | jarvis_script | Read-only post-reconcile validator for a WCS task | user | Confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, DAILY_REVIEW.md, and result files |
| worker_change_check.py | C:\dev\jarvis-workspace\scripts\worker_change_check.py | script | source_of_truth | jarvis_script | Read-only worker-boundary validator for changed-file scope and simple diff sanity | user | Validates that changed files stay within task scope and diffs are small before commit/finalization |
| worker_result_validate.py | C:\dev\jarvis-workspace\scripts\worker_result_validate.py | script | source_of_truth | jarvis_script | Read-only worker-result schema validator for a WCS task | user | Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes |
| qa_result_validate.py | C:\dev\jarvis-workspace\scripts\qa_result_validate.py | script | source_of_truth | jarvis_script | Read-only QA-result schema validator for a WCS task | user | Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes |

## FILE: state/project_status_wcs.json
{
  "project": "WCS",
  "repo_path": "C:\\dev\\wcsv2.0-new",
  "install_command": "npm install",
  "dev_command": "npm run dev",
  "build_command": "npm run build",
  "local_url": "http://localhost:3000",
  "deploy_target": "Vercel via GitHub push",
  "priority_routes": [
    "/",
    "/about",
    "/teams"
  ],
  "checks_needed": [
    "python_version",
    "node_version",
    "playwright_installed",
    "testids_present"
  ],
  "scout_defect_intake": {
    "enabled": true,
    "runner": "run_wcs_scout.py",
    "normalizer": "normalize_scout_to_backlog.py",
    "noise_rules": "scout_noise_rules.json",
    "results_path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_results.json",
    "report_path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\scout_normalizer_report.json",
    "backlog_target": "C:\\dev\\jarvis-workspace\\state\\master_backlog.json",
    "backlog_markdown": "C:\\dev\\jarvis-workspace\\state\\MASTER_BACKLOG.md"
  },
  "validation_completed": [
    "public_scout_clean_noop_path",
    "public_scout_synthetic_failure_insertion",
    "public_scout_duplicate_suppression",
    "integrated_scout_to_normalizer_run"
  ]
}

## FILE: state/master_backlog.json
[
  {
    "task_id": "WCS-001",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "done",
    "title": "Fix testimonial typo in PlayerTestimonials quote",
    "notes": "src/components/PlayerTestimonials.tsx"
  },
  {
    "task_id": "WCS-002",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Fix stats section showing 0 for all metrics",
    "notes": "src/components/StatsSection.tsx"
  },
  {
    "task_id": "WCS-003",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Add timeout/fallback handling for long loading states",
    "notes": "TodaysEvents.tsx, LogoMarquee.tsx"
  },
  {
    "task_id": "WCS-004",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "done",
    "title": "Improve empty Around the WCS state",
    "notes": "src/components/TeamUpdates.tsx"
  },
  {
    "task_id": "WCS-005",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Make footer email signup form functional",
    "notes": "src/components/Footer.tsx"
  },
  {
    "task_id": "WCS-006",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fix hero headline accessibility spacing/aria label",
    "notes": "src/components/Hero.tsx"
  },
  {
    "task_id": "WCS-007",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Hide test site banner in production",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-008",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Clarify navbar Coaches link label for logged-out users",
    "notes": "src/components/Navbar.tsx"
  },
  {
    "task_id": "WCS-009",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "done",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "notes": "src/components/LogoMarquee.tsx"
  },
  {
    "task_id": "WCS-010",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "done",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "notes": "src/components/TodaysEvents.tsx"
  },
  {
    "task_id": "WCS-011",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Stabilize local Playwright smoke QA for home page",
    "notes": "tests/e2e, playwright config, global setup for http://localhost:3000"
  },
  {
    "task_id": "WCS-013",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Hide links to unfinished /shop page",
    "notes": "Public navigation or CTA paths should not expose /shop until the page is built out"
  },
  {
    "task_id": "WCS-014",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Hide links to unfinished /news page",
    "notes": "Public links should not expose /news until the page is built out"
  },
  {
    "task_id": "WCS-015",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "ready",
    "title": "Investigate /schedules Supabase realtime auth console error",
    "notes": "Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials"
  },
  {
    "task_id": "WCS-016",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner background from black to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-017",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner background from white back to black",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-018",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner text color from white to black",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-019",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "ready",
    "title": "Flip TestSiteBanner text color from black back to white",
    "notes": "src/components/TestSiteBanner.tsx"
  }
]


## FILE: state/MASTER_BACKLOG.md
# MASTER_BACKLOG

| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |
|---|---|---|---|---|---|---|---|
| WCS-001 | WCS | ugly | P2 | low | done | Fix testimonial typo in PlayerTestimonials quote | src/components/PlayerTestimonials.tsx |
| WCS-002 | WCS | broken | P1 | medium | done | Fix stats section showing 0 for all metrics | src/components/StatsSection.tsx |
| WCS-003 | WCS | broken | P1 | medium | done | Add timeout/fallback handling for long loading states | TodaysEvents.tsx, LogoMarquee.tsx |
| WCS-004 | WCS | ugly | P2 | low | done | Improve empty Around the WCS state | src/components/TeamUpdates.tsx |
| WCS-005 | WCS | broken | P1 | medium | ready | Make footer email signup form functional | src/components/Footer.tsx |
| WCS-006 | WCS | ugly | P3 | low | ready | Fix hero headline accessibility spacing/aria label | src/components/Hero.tsx |
| WCS-007 | WCS | ugly | P3 | low | ready | Hide test site banner in production | src/components/TestSiteBanner.tsx |
| WCS-008 | WCS | ugly | P3 | low | ready | Clarify navbar Coaches link label for logged-out users | src/components/Navbar.tsx |
| WCS-009 | WCS | broken | P2 | medium | ready | Improve LogoMarquee response.ok handling and fallback | src/components/LogoMarquee.tsx |
| WCS-010 | WCS | broken | P2 | medium | done | Show fallback message instead of hiding TodaysEvents on error | src/components/TodaysEvents.tsx |
| WCS-011 | WCS | broken | P1 | low | done | Stabilize local Playwright smoke QA for home page | tests/e2e, playwright config, global setup for http://localhost:3000 |
| WCS-013 | WCS | broken | P2 | low | ready | Hide links to unfinished /shop page | Public navigation or CTA paths should not expose /shop until the page is built out |
| WCS-014 | WCS | broken | P2 | low | ready | Hide links to unfinished /news page | Public links should not expose /news until the page is built out |
| WCS-015 | WCS | broken | P2 | medium | ready | Investigate /schedules Supabase realtime auth console error | Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials |
| WCS-016 | WCS | broken | P2 | medium | ready | Investigate public /teams scout HTTP 500 failure | Scout route: /teams; label: Teams; family: http_status; issues: HTTP status 500 on initial load. \|\| Console errors detected: 1; console: TypeError: Cannot read properties of undefined (reading ''map''); screenshot: C:\dev\jarvis-workspace\logs\wcs_scout\synthetic\public-teams.png; source: C:\dev\jarvis-workspace\logs\wcs_scout\synthetic_scout_fail.json |


## FILE: state/daily_plan.json
{
  "generated_at": "2026-03-12T15:04:13-05:00",
  "selected_task": {
    "task_id": "WCS-019",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "ready",
    "title": "Flip TestSiteBanner text color from black back to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  "selection_reason": {
    "rule": "priority_risk_task_id",
    "details": "Selected highest-priority eligible ready WCS task using deterministic ordering (priority, then risk, then numeric task id)."
  }
}


## FILE: state/DAILY_PLAN.md
# DAILY PLAN

**Generated at:** 2026-03-12T15:04:13-05:00

## Selected Task

- **Task ID:** WCS-019
- **Project:** WCS
- **Bucket:** ugly
- **Priority:** P1
- **Risk:** low
- **Status:** ready
- **Title:** Flip TestSiteBanner text color from black back to white
- **Notes:** src/components/TestSiteBanner.tsx

## Selection Reason

- **Rule:** priority_risk_task_id
- **Details:** Selected highest-priority eligible ready WCS task using deterministic ordering (priority, then risk, then numeric task id).


## FILE: state/run_log.json
[
  {
    "timestamp": "2026-03-11T12:19:02-05:00",
    "event": "task_selected",
    "task_id": "WCS-005",
    "project": "WCS",
    "title": "Make footer email signup form functional",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T13:46:40-05:00",
    "event": "task_selected",
    "task_id": "WCS-009",
    "project": "WCS",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T13:46:40-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-009",
    "project": "WCS",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-009_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-009_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-009_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-009_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-009_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_selected",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-010_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-010_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-010_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-010_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-010_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-010",
    "artifacts": [
      "jarvis-task-wcs-010"
    ]
  },
  {
    "timestamp": "2026-03-11T21:24:48-05:00",
    "event": "task_selected",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T21:24:48-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-016_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-016_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-016_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-016_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-016_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T21:24:49-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-016",
    "artifacts": [
      "jarvis-task-wcs-016"
    ]
  },
  {
    "timestamp": "2026-03-12T10:37:44-05:00",
    "event": "task_selected",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T10:37:44-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-017_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-017_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-017_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-017_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-017_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T10:37:45-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-017",
    "artifacts": [
      "jarvis-task-wcs-017",
      "C:\\dev\\wcsv2.0-new"
    ]
  },
  {
    "timestamp": "2026-03-12T11:16:29-05:00",
    "event": "task_selected",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T12:28:50-05:00",
    "event": "task_selected",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T12:28:50-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis generated task packet and contract-valid placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-018_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-018_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-018_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-018_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-018_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T12:28:51-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-018",
    "artifacts": [
      "jarvis-task-wcs-018",
      "C:\\dev\\wcsv2.0-new"
    ]
  },
  {
    "timestamp": "2026-03-12T13:04:45-05:00",
    "event": "task_selected",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "event": "task_selected",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis generated task packet and contract-valid placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-019_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-019_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-019_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-019_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-019_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T15:04:13-05:00",
    "event": "task_selected",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T15:04:14-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-019",
    "artifacts": [
      "jarvis-task-wcs-019",
      "C:\\dev\\wcsv2.0-new"
    ]
  }
]


## FILE: state/RUN_LOG.md
# RUN LOG

## 2026-03-11T12:19:02-05:00 — task_selected

- **Task ID:** WCS-005
- **Project:** WCS
- **Title:** Make footer email signup form functional
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T13:46:40-05:00 — task_selected

- **Task ID:** WCS-009
- **Project:** WCS
- **Title:** Improve LogoMarquee response.ok handling and fallback
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T13:46:40-05:00 — task_packet_generated

- **Task ID:** WCS-009
- **Project:** WCS
- **Title:** Improve LogoMarquee response.ok handling and fallback
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-009_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-009_task.md
  - C:\dev\jarvis-workspace\results\WCS-009_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-009_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-009_escalation.json

## 2026-03-11T14:49:02-05:00 — task_selected

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T14:49:02-05:00 — task_packet_generated

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-010_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-010_task.md
  - C:\dev\jarvis-workspace\results\WCS-010_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-010_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-010_escalation.json

## 2026-03-11T14:49:02-05:00 — task_branch_prepared

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-010
- **Artifacts:**
  - jarvis-task-wcs-010

## 2026-03-11T21:24:48-05:00 — task_selected

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T21:24:48-05:00 — task_packet_generated

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-016_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-016_task.md
  - C:\dev\jarvis-workspace\results\WCS-016_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-016_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-016_escalation.json

## 2026-03-11T21:24:49-05:00 — task_branch_prepared

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-016
- **Artifacts:**
  - jarvis-task-wcs-016

## 2026-03-12T10:37:44-05:00 — task_selected

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T10:37:44-05:00 — task_packet_generated

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-017_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-017_task.md
  - C:\dev\jarvis-workspace\results\WCS-017_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-017_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-017_escalation.json

## 2026-03-12T10:37:45-05:00 — task_branch_prepared

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-017
- **Artifacts:**
  - jarvis-task-wcs-017
  - C:\dev\wcsv2.0-new

## 2026-03-12T11:16:29-05:00 — task_selected

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T12:28:50-05:00 — task_selected

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T12:28:50-05:00 — task_packet_generated

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis generated task packet and contract-valid placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-018_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-018_task.md
  - C:\dev\jarvis-workspace\results\WCS-018_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-018_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-018_escalation.json

## 2026-03-12T12:28:51-05:00 — task_branch_prepared

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-018
- **Artifacts:**
  - jarvis-task-wcs-018
  - C:\dev\wcsv2.0-new

## 2026-03-12T13:04:45-05:00 — task_selected

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T14:57:08-05:00 — task_selected

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T14:57:08-05:00 — task_packet_generated

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis generated task packet and contract-valid placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-019_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-019_task.md
  - C:\dev\jarvis-workspace\results\WCS-019_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-019_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-019_escalation.json

## 2026-03-12T15:04:13-05:00 — task_selected

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T15:04:14-05:00 — task_branch_prepared

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-019
- **Artifacts:**
  - jarvis-task-wcs-019
  - C:\dev\wcsv2.0-new


## FILE: state/DAILY_REVIEW.md
# DAILY\_REVIEW

Date: 2026-03-09

## Summary

* WCS-001 completed.
* \- Updated Michael J. testimonial text in src/components/PlayerTestimonials.tsx
* \- npm run build passed
* \- Manual browser QA passed on localhost:3000
* \- Existing Playwright suite timed out during global setup and needs stabilization as a separate task
* WCS-011 completed.
* \- Stabilized Playwright global setup by waiting for local server readiness before browser navigation
* \- Added a dedicated home page smoke test
* \- Added a test:e2e:smoke script to package.json
* \- Playwright smoke QA passed locally with 1 passing test

## Wins

* Workspace initialized.

## Failures / blockers

* &nbsp;

## Next step

* Next step
* Execute WCS-002: fix stats section showing 0 for all metrics, and verify with build + smoke QA.

### WCS-002 — done
- Title: Fix stats section showing 0 for all metrics
- Worker: Added a 400ms fallback in StatsSection StatCard so the count-up animation always starts, preventing the metrics from staying at 0.
- QA: QA passed. Build completed successfully, Playwright home-page smoke test passed, and manual browser verification confirmed the stats animate from 0 to their target values instead of remaining stuck at 0.
- Files changed: src/components/StatsSection.tsx
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npm run test:e2e:smoke
- Reconciled at: 2026-03-09T18:46:09-05:00

### WCS-003 — done
- Title: Add timeout/fallback handling for long loading states
- Worker: Added AbortController-based timeout handling to TodaysEvents and LogoMarquee so long-running fetches fail instead of hanging indefinitely, allowing the existing error and fallback behavior to run.
- QA: QA passed. Build completed successfully, Playwright home-page smoke test passed, and manual browser verification confirmed long-loading requests no longer hang indefinitely. TodaysEvents exits loading state correctly and LogoMarquee uses fallback behavior on timeout/error.
- Files changed: src/components/TodaysEvents.tsx, src/components/LogoMarquee.tsx
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npm run test:e2e:smoke
- Reconciled at: 2026-03-09T19:16:49-05:00

### WCS-011 — done
- Title: Stabilize local Playwright smoke QA for home page
- Worker: Stabilized Playwright smoke QA by updating global setup to poll for server readiness for up to 90 seconds before verifying page load, adding a dedicated home page smoke test, and adding a test:e2e:smoke script.
- QA: QA passed. Build completed successfully, Playwright global setup successfully waited for the local server, and the dedicated home page smoke test passed.
- Files changed: tests/e2e/helpers/global-setup.ts, tests/e2e/home.spec.ts, package.json
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npm run test:e2e:smoke
- Reconciled at: 2026-03-09T20:22:30-05:00

### WCS-004 — done
- Title: Improve empty Around the WCS state
- Worker: Improved the empty 'Around the WCS' state in TeamUpdates by replacing the generic message with friendlier copy and increasing padding so the card looks intentional instead of broken.
- QA: Partial QA only. Build passed, but automated smoke QA was unavailable in this branch and manual browser verification did not reproduce the empty-state condition for 'Around the WCS', so the acceptance criteria could not be confirmed.
- Files changed: src/components/TeamUpdates.tsx
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npx playwright test tests/e2e/home.spec.ts
- Reconciled at: 2026-03-09T20:35:32-05:00

### WCS-005 — done
- Title: Make footer email signup form functional
- Worker: Wired the footer email signup form to open a prefilled mailto to info@wcsbasketball.com using the entered address, and ensured the app still builds and the home smoke Playwright test passes.
- QA: Verified that the footer email signup form now opens a prefilled mailto to info@wcsbasketball.com using the entered address, and that build and home smoke QA still pass.
- Files changed: src/components/Footer.tsx
- Commands run: npm run build, npm run test:e2e:smoke
- Reconciled at: 2026-03-11T13:35:42-05:00

### WCS-009 — done
- Title: Improve LogoMarquee response.ok handling and fallback
- Worker: Improved LogoMarquee API error handling by logging non-OK responses from the /api/teams endpoint while preserving the existing fallback behavior.
- QA: Confirmed that LogoMarquee now logs a devError when /api/teams returns a non-OK response while preserving the existing success path and fallback behavior, and that build and home smoke QA still pass.
- Files changed: src/components/LogoMarquee.tsx
- Commands run: npm run build, npm run test:e2e:smoke
- Reconciled at: 2026-03-11T14:19:09-05:00

### WCS-010 — done
- Title: Show fallback message instead of hiding TodaysEvents on error
- Worker: Updated TodaysEvents to show a clear fallback message when an error occurs instead of rendering nothing, while keeping the normal loading and no-events behaviors unchanged.
- QA: Verified that TodaysEvents now shows a visible fallback message when an error occurs instead of disappearing, while the normal loading and no-events behaviors remain unchanged and existing build and smoke QA still pass.
- Files changed: src/components/TodaysEvents.tsx
- Commands run: npm run build, npm run test:e2e:smoke
- Reconciled at: 2026-03-11T15:09:54-05:00

### WCS-016 — done
- Title: Flip TestSiteBanner background from black to white
- Worker: Updated src/components/TestSiteBanner.tsx to change the banner background from amber to white for the bounded WCS-016 fake hardening task.
- QA: Build passed and Playwright home smoke QA passed after updating TestSiteBanner background to white on the WCS-016 task branch.
- Files changed: src/components/TestSiteBanner.tsx
- Commands run: git branch --show-current, git status, git add .\src\components\TestSiteBanner.tsx, git commit -m "WCS-016 fake hardening test: flip TestSiteBanner background to white"
- Repo path: C:\dev\wcsv2.0-new
- Verified branch: jarvis-task-wcs-016
- Commits ahead of main: 1
- HEAD commit: 190060c
- Branch verified at: 2026-03-12T08:11:07-05:00
- Reconciled at: 2026-03-12T08:11:07-05:00

### WCS-017 — done
- Title: Flip TestSiteBanner background from white back to black
- Worker: Updated src/components/TestSiteBanner.tsx to change the banner background from amber to black for the bounded WCS-017 fake hardening task.
- QA: Build passed and Playwright home smoke QA passed after updating TestSiteBanner background to black on the WCS-017 task branch.
- Files changed: src/components/TestSiteBanner.tsx
- Commands run: git branch --show-current, git status, git add .\src\components\TestSiteBanner.tsx, git commit -m "WCS-017 fake hardening test: flip TestSiteBanner background to black"
- Repo path: C:\dev\wcsv2.0-new
- Verified branch: jarvis-task-wcs-017
- Commits ahead of main: 1
- HEAD commit: 197dce7
- Branch verified at: 2026-03-12T11:54:49-05:00
- Reconciled at: 2026-03-12T11:54:49-05:00

### WCS-018 — done
- Title: Flip TestSiteBanner text color from white to black
- Worker: Updated src/components/TestSiteBanner.tsx to change the banner text color to black for the bounded WCS-018 fake hardening task.
- QA: Build passed and Playwright home smoke QA passed after updating TestSiteBanner text color to black on the WCS-018 task branch.
- Files changed: src/components/TestSiteBanner.tsx
- Commands run: git branch --show-current, git status, git add .\src\components\TestSiteBanner.tsx, git commit -m "WCS-018 fake hardening test: flip TestSiteBanner text color to black"
- Repo path: C:\dev\wcsv2.0-new
- Verified branch: jarvis-task-wcs-018
- Commits ahead of main: 1
- HEAD commit: cd40f04
- Branch verified at: 2026-03-12T14:21:14-05:00
- Reconciled at: 2026-03-12T14:21:14-05:00


## FILE: state/escalations.json
[
  {
    "timestamp": "2026-03-12T13:04:45-05:00",
    "task_id": "WCS-018",
    "project": "WCS",
    "phase": "jarvis_packet_validation",
    "severity": "error",
    "status": "open",
    "human_action_required": true,
    "reason_code": "packet_contract_mismatch",
    "summary": "Jarvis detected invalid or mismatched packet/result placeholder contracts.",
    "details": [
      "C:\\dev\\jarvis-workspace\\results\\WCS-018_worker_result.json: expected placeholder status 'draft' before execution. Found: worker_complete"
    ],
    "recommended_next_action": "Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet)."
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "task_id": "WCS-019",
    "project": "WCS",
    "phase": "jarvis_branch_preparation",
    "severity": "error",
    "status": "open",
    "human_action_required": true,
    "reason_code": "branch_prepare_failed",
    "summary": "Jarvis branch preparer reported a non-zero exit code.",
    "details": [
      "Return code: 1",
      "STDERR: ERROR: Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.\nCurrent branch: jarvis-task-wcs-018\nTarget branch: jarvis-task-wcs-019\nDirty files:\n M src/components/TestSiteBanner.tsx"
    ],
    "recommended_next_action": "Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py."
  }
]


## FILE: state/ESCALATIONS.md
# ESCALATIONS

## 2026-03-12T13:04:45-05:00 - packet_contract_mismatch

- **Task ID:** WCS-018
- **Project:** WCS
- **Phase:** jarvis_packet_validation
- **Severity:** error
- **Status:** open
- **Human action required:** yes
- **Summary:** Jarvis detected invalid or mismatched packet/result placeholder contracts.

- **Details:**
  - C:\dev\jarvis-workspace\results\WCS-018_worker_result.json: expected placeholder status 'draft' before execution. Found: worker_complete

- **Recommended next action:** Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet).

## 2026-03-12T14:57:08-05:00 - branch_prepare_failed

- **Task ID:** WCS-019
- **Project:** WCS
- **Phase:** jarvis_branch_preparation
- **Severity:** error
- **Status:** open
- **Human action required:** yes
- **Summary:** Jarvis branch preparer reported a non-zero exit code.

- **Details:**
  - Return code: 1
  - STDERR: ERROR: Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.
Current branch: jarvis-task-wcs-018
Target branch: jarvis-task-wcs-019
Dirty files:
 M src/components/TestSiteBanner.tsx

- **Recommended next action:** Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py.


## FILE: scripts/jarvis.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class JarvisError(Exception):
    pass


PRIORITY_ORDER = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
ELIGIBLE_BUCKETS = {"broken", "ugly"}
ALLOWED_PROJECT = "WCS"
REQUIRED_TASK_FIELDS = {"task_id", "project", "bucket", "priority", "risk", "status", "title"}
PLACEHOLDER_STATUS = "draft"


ESCALATIONS_JSON_NAME = "escalations.json"
ESCALATIONS_MD_NAME = "ESCALATIONS.md"


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today_local_date() -> str:
    return datetime.now().astimezone().date().isoformat()


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path, expected_type: type | None = None) -> Any:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise JarvisError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise JarvisError(f"Invalid JSON in {path}: {exc}") from exc

    if expected_type is not None and not isinstance(data, expected_type):
        raise JarvisError(
            f"Expected {expected_type.__name__} in {path}, got {type(data).__name__}"
        )
    return data


def read_optional_json(path: Path, default: Any, expected_type: type | None = None) -> Any:
    if not path.exists():
        return default
    return read_json(path, expected_type=expected_type)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_escalations(escalations_path: Path) -> list[dict[str, Any]]:
    """Load existing escalations, initializing an empty list if the file does not exist."""
    if not escalations_path.exists():
        return []
    data = read_json(escalations_path, expected_type=list)
    # Defensive: ensure list of dict-like items
    cleaned: list[dict[str, Any]] = []
    for item in data:
        if isinstance(item, dict):
            cleaned.append(item)
    return cleaned


def render_escalations_md(records: list[dict[str, Any]]) -> str:
    lines = ["# ESCALATIONS", ""]
    if not records:
        lines.append("_No escalations recorded._")
        return "\n".join(lines)

    for record in records:
        timestamp = normalize_text(record.get("timestamp"))
        reason_code = normalize_text(record.get("reason_code"))
        human_action_required = "yes" if bool(record.get("human_action_required")) else "no"

        lines.extend(
            [
                f"## {timestamp} - {reason_code}",
                "",
                f"- **Task ID:** {normalize_text(record.get('task_id'))}",
                f"- **Project:** {normalize_text(record.get('project'))}",
                f"- **Phase:** {normalize_text(record.get('phase'))}",
                f"- **Severity:** {normalize_text(record.get('severity'))}",
                f"- **Status:** {normalize_text(record.get('status'))}",
                f"- **Human action required:** {human_action_required}",
                f"- **Summary:** {normalize_text(record.get('summary'))}",
                "",
                "- **Details:**",
            ]
        )

        details = record.get("details")
        if isinstance(details, list) and details:
            for detail in details:
                lines.append(f"  - {normalize_text(detail)}")
        else:
            lines.append("  - (none)")

        lines.extend(
            [
                "",
                f"- **Recommended next action:** {normalize_text(record.get('recommended_next_action'))}",
                "",
            ]
        )

    return "\n".join(lines).rstrip()


def append_escalation(
    *,
    state_dir: Path,
    task_id: str,
    phase: str,
    reason_code: str,
    summary: str,
    details: list[str],
    recommended_next_action: str,
) -> None:
    """Append a durable escalation record and render the markdown view."""
    escalations_path = state_dir / ESCALATIONS_JSON_NAME
    escalations_md_path = state_dir / ESCALATIONS_MD_NAME

    records = load_escalations(escalations_path)

    record = {
        "timestamp": now_local_iso(),
        "task_id": normalize_text(task_id).upper(),
        "project": ALLOWED_PROJECT,
        "phase": phase,
        "severity": "error",
        "status": "open",
        "human_action_required": True,
        "reason_code": reason_code,
        "summary": summary,
        "details": details,
        "recommended_next_action": recommended_next_action,
    }
    records.append(record)
    write_json(escalations_path, records)
    write_text(escalations_md_path, render_escalations_md(records))

    print("")
    print("JARVIS: escalation recorded")
    print(f"- JSON: {escalations_path}")
    print(f"- Markdown: {escalations_md_path}")


def parse_task_number(task_id: str) -> int:
    task_id = normalize_text(task_id).upper()
    if not task_id.startswith("WCS-"):
        raise JarvisError(f"Expected task id like WCS-016. Got: {task_id}")
    number_part = task_id.split("-", 1)[1]
    if not number_part.isdigit():
        raise JarvisError(f"Expected numeric WCS task id suffix. Got: {task_id}")
    return int(number_part)


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def priority_rank(task: dict[str, Any]) -> int:
    return PRIORITY_ORDER.get(normalize_text(task.get("priority")).upper(), 999)


def risk_rank(task: dict[str, Any]) -> int:
    return RISK_ORDER.get(normalize_text(task.get("risk")).lower(), 999)


def validate_task_shape(task: dict[str, Any], *, context: str) -> None:
    missing = [field for field in sorted(REQUIRED_TASK_FIELDS) if not normalize_text(task.get(field))]
    if missing:
        raise JarvisError(f"{context}: task is missing required fields: {', '.join(missing)}")

    task_id = normalize_text(task.get("task_id")).upper()
    parse_task_number(task_id)

    project = normalize_text(task.get("project")).upper()
    if project != ALLOWED_PROJECT:
        raise JarvisError(f"{context}: task project must be {ALLOWED_PROJECT}. Found: {project}")

    bucket = normalize_text(task.get("bucket")).lower()
    if bucket not in ELIGIBLE_BUCKETS:
        raise JarvisError(
            f"{context}: task bucket must be one of {sorted(ELIGIBLE_BUCKETS)}. Found: {bucket}"
        )

    status = normalize_text(task.get("status")).lower()
    if status != "ready":
        raise JarvisError(f"{context}: task status must be ready for execution. Found: {status}")

    priority = normalize_text(task.get("priority")).upper()
    if priority not in PRIORITY_ORDER:
        raise JarvisError(f"{context}: invalid priority: {priority}")

    risk = normalize_text(task.get("risk")).lower()
    if risk not in RISK_ORDER:
        raise JarvisError(f"{context}: invalid risk: {risk}")


def validate_backlog_task_uniqueness(backlog: list[dict[str, Any]], task_id: str) -> None:
    normalized = normalize_text(task_id).upper()
    matches = [
        task for task in backlog
        if isinstance(task, dict) and normalize_text(task.get("task_id")).upper() == normalized
    ]
    if len(matches) != 1:
        raise JarvisError(
            f"Backlog must contain exactly one entry for {normalized}. Found: {len(matches)}"
        )


def is_ready_wcs_task(task: dict[str, Any]) -> bool:
    if normalize_text(task.get("project")).upper() != ALLOWED_PROJECT:
        return False
    if normalize_text(task.get("status")).lower() != "ready":
        return False
    if normalize_text(task.get("bucket")).lower() not in ELIGIBLE_BUCKETS:
        return False
    task_id = normalize_text(task.get("task_id")).upper()
    return task_id.startswith("WCS-")


def select_task(backlog: list[dict[str, Any]]) -> dict[str, Any]:
    eligible = [task for task in backlog if isinstance(task, dict) and is_ready_wcs_task(task)]
    if not eligible:
        raise JarvisError("No eligible ready WCS task found in master_backlog.json.")

    try:
        eligible.sort(
            key=lambda task: (
                priority_rank(task),
                risk_rank(task),
                parse_task_number(normalize_text(task.get("task_id"))),
            )
        )
    except JarvisError:
        raise
    except Exception as exc:
        raise JarvisError(f"Failed to sort eligible tasks: {exc}") from exc

    return eligible[0]


def get_backlog_task_by_id(backlog: list[dict[str, Any]], task_id: str) -> dict[str, Any] | None:
    normalized = normalize_text(task_id).upper()
    for task in backlog:
        if not isinstance(task, dict):
            continue
        if normalize_text(task.get("task_id")).upper() == normalized:
            return task
    return None


def task_selected_today(
    daily_plan: dict[str, Any],
    run_log: list[dict[str, Any]],
    current_date: str,
) -> dict[str, Any] | None:
    selected_task = daily_plan.get("selected_task")
    generated_at = normalize_text(daily_plan.get("generated_at"))

    if isinstance(selected_task, dict) and generated_at.startswith(current_date):
        return selected_task

    for entry in reversed(run_log):
        if not isinstance(entry, dict):
            continue
        if normalize_text(entry.get("event")) != "task_selected":
            continue
        timestamp = normalize_text(entry.get("timestamp"))
        if not timestamp.startswith(current_date):
            continue
        task_id = normalize_text(entry.get("task_id"))
        if task_id:
            return {"task_id": task_id}
    return None


def build_daily_plan(selected_task: dict[str, Any], timestamp: str) -> dict[str, Any]:
    return {
        "generated_at": timestamp,
        "selected_task": selected_task,
        "selection_reason": {
            "rule": "priority_risk_task_id",
            "details": (
                "Selected highest-priority eligible ready WCS task using deterministic "
                "ordering (priority, then risk, then numeric task id)."
            ),
        },
    }


def render_daily_plan_md(plan: dict[str, Any]) -> str:
    selected_task = plan.get("selected_task", {})
    selection_reason = plan.get("selection_reason", {})
    lines = [
        "# DAILY PLAN",
        "",
        f"**Generated at:** {normalize_text(plan.get('generated_at'))}",
        "",
        "## Selected Task",
        "",
        f"- **Task ID:** {normalize_text(selected_task.get('task_id'))}",
        f"- **Project:** {normalize_text(selected_task.get('project'))}",
        f"- **Bucket:** {normalize_text(selected_task.get('bucket'))}",
        f"- **Priority:** {normalize_text(selected_task.get('priority'))}",
        f"- **Risk:** {normalize_text(selected_task.get('risk'))}",
        f"- **Status:** {normalize_text(selected_task.get('status'))}",
        f"- **Title:** {normalize_text(selected_task.get('title'))}",
        f"- **Notes:** {normalize_text(selected_task.get('notes'))}",
        "",
        "## Selection Reason",
        "",
        f"- **Rule:** {normalize_text(selection_reason.get('rule'))}",
        f"- **Details:** {normalize_text(selection_reason.get('details'))}",
    ]
    return "\n".join(lines)


def render_run_log_md(run_log: list[dict[str, Any]]) -> str:
    lines = ["# RUN LOG", ""]
    if not run_log:
        lines.append("_No run log entries yet._")
        return "\n".join(lines)

    for entry in run_log:
        lines.extend(
            [
                f"## {normalize_text(entry.get('timestamp'))} — {normalize_text(entry.get('event'))}",
                "",
                f"- **Task ID:** {normalize_text(entry.get('task_id'))}",
                f"- **Project:** {normalize_text(entry.get('project'))}",
                f"- **Title:** {normalize_text(entry.get('title'))}",
                f"- **Summary:** {normalize_text(entry.get('summary'))}",
            ]
        )
        artifacts = entry.get("artifacts")
        if isinstance(artifacts, list) and artifacts:
            lines.append("- **Artifacts:**")
            for artifact in artifacts:
                lines.append(f"  - {normalize_text(artifact)}")
        lines.append("")
    return "\n".join(lines).rstrip()


def build_run_log_entry(
    *,
    event: str,
    selected_task: dict[str, Any],
    timestamp: str,
    summary: str,
    artifacts: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "timestamp": timestamp,
        "event": event,
        "task_id": normalize_text(selected_task.get("task_id")).upper(),
        "project": normalize_text(selected_task.get("project")).upper(),
        "title": normalize_text(selected_task.get("title")),
        "summary": summary,
        "artifacts": artifacts or [],
    }


def append_run_log_entry(
    run_log_json_path: Path,
    run_log_md_path: Path,
    run_log: list[dict[str, Any]],
    entry: dict[str, Any],
) -> None:
    run_log.append(entry)
    write_json(run_log_json_path, run_log)
    write_text(run_log_md_path, render_run_log_md(run_log))


def task_artifact_paths(workspace: Path, task_id: str) -> dict[str, Path]:
    normalized_task_id = normalize_text(task_id).upper()
    return {
        "task_json": workspace / "tasks" / f"{normalized_task_id}_task.json",
        "task_md": workspace / "tasks" / f"{normalized_task_id}_task.md",
        "worker_result": workspace / "results" / f"{normalized_task_id}_worker_result.json",
        "qa_result": workspace / "qa" / f"{normalized_task_id}_qa_result.json",
        "escalation": workspace / "logs" / f"{normalized_task_id}_escalation.json",
    }


def analyze_artifacts(artifact_map: dict[str, Path]) -> tuple[list[Path], list[Path]]:
    existing = []
    missing = []
    for path in artifact_map.values():
        if path.exists():
            existing.append(path)
        else:
            missing.append(path)
    return existing, missing


def run_packet_generator(workspace: Path, task_id: str, *, force_packet: bool) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "generate_task_packet.py"
    if not helper_path.exists():
        raise JarvisError(f"Packet generator not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]
    if force_packet:
        cmd.append("--force")

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def run_branch_preparer(workspace: Path, task_id: str) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "prepare_wcs_task_branch.py"
    if not helper_path.exists():
        raise JarvisError(f"Branch preparer not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def parse_branch_prep_output(stdout: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip().upper()] = value.strip()
    return parsed


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def verify_repo_branch_state(repo_path: Path) -> dict[str, str]:
    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise JarvisError(
            current_branch_result.stderr.strip() or f"Failed to inspect repo branch at {repo_path}"
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise JarvisError(
            status_result.stderr.strip() or f"Failed to inspect repo status at {repo_path}"
        )

    current_branch = current_branch_result.stdout.strip()
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    return {
        "current_branch": current_branch,
        "dirty": "true" if dirty_lines else "false",
        "dirty_count": str(len(dirty_lines)),
    }


def validate_task_json_contract(path: Path, expected_task: dict[str, Any]) -> None:
    data = read_json(path, expected_type=dict)
    expected_id = normalize_text(expected_task.get("task_id")).upper()

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != expected_id:
        raise JarvisError(f"{path}: task_id mismatch. Expected {expected_id}, found {actual_id}")

    required = ["task_id", "title"]
    missing = [field for field in required if not normalize_text(data.get(field))]
    if missing:
        raise JarvisError(f"{path}: missing required task packet fields: {', '.join(missing)}")


def validate_result_placeholder_contract(path: Path, expected_task_id: str, kind: str) -> None:
    data = read_json(path, expected_type=dict)
    actual_id = normalize_text(data.get("task_id")).upper()
    expected_id = normalize_text(expected_task_id).upper()

    if actual_id != expected_id:
        raise JarvisError(f"{path}: {kind} task_id mismatch. Expected {expected_id}, found {actual_id}")

    status = normalize_text(data.get("status")).lower()
    if status != PLACEHOLDER_STATUS:
        raise JarvisError(
            f"{path}: expected placeholder status '{PLACEHOLDER_STATUS}' before execution. Found: {status}"
        )

    completed_at = data.get("completed_at")
    if normalize_text(completed_at):
        raise JarvisError(f"{path}: placeholder completed_at must be blank before execution")

    if kind == "worker_result":
        for field in ["executor", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing worker placeholder field: {field}")
        for list_field in ["files_changed", "commands_run", "issues_encountered"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: worker placeholder field must be a list: {list_field}")

    if kind == "qa_result":
        for field in ["qa_tool", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing QA placeholder field: {field}")
        for list_field in ["checks_run", "checks_passed", "checks_failed", "artifacts"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: QA placeholder field must be a list: {list_field}")


def validate_existing_artifacts(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()

    if not artifact_map["task_md"].exists():
        raise JarvisError(f"Existing packet set is invalid: missing markdown packet: {artifact_map['task_md']}")
    if not artifact_map["escalation"].exists():
        raise JarvisError(
            f"Existing packet set is invalid: missing escalation file: {artifact_map['escalation']}"
        )

    validate_task_json_contract(artifact_map["task_json"], selected_task)
    validate_result_placeholder_contract(artifact_map["worker_result"], task_id, "worker_result")
    validate_result_placeholder_contract(artifact_map["qa_result"], task_id, "qa_result")


def validate_generated_placeholders(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    for path in artifact_map.values():
        if not path.exists():
            raise JarvisError(f"Expected generated artifact not found after packet generation: {path}")

    validate_existing_artifacts(artifact_map, selected_task)


def print_mode_banner(mode: str) -> None:
    print("=" * 72)
    print(f"JARVIS MODE: {mode}")
    print("=" * 72)


def print_packet_placeholder_warning(task_id: str, artifact_map: dict[str, Path], skipped_existing: bool) -> None:
    print("")
    print("JARVIS: artifact safety warning")
    print(
        "These task packet result files are placeholders until the worker result and QA result are filled truthfully."
    )
    print("They are NOT execution proof and do NOT mean the task is reconcile-ready.")
    print(f"- Worker placeholder: {artifact_map['worker_result']}")
    print(f"- QA placeholder:     {artifact_map['qa_result']}")
    print(f"- Escalation file:   {artifact_map['escalation']}")
    if skipped_existing:
        print("")
        print("JARVIS: packet generation was skipped because all artifacts already exist.")
        print("That does NOT mean the task is complete.")
        print("Existing packet/result artifacts were contract-validated before continuing.")
        print("Inspect existing worker/QA result contents before relying on them.")


def print_result_contracts() -> None:
    print("")
    print("JARVIS: result contracts")
    print("- Worker result status must be one of: worker_complete | blocked | escalated")
    print("- QA result status must be one of: qa_pass | qa_fail | escalated")
    print("- Keep completed_at blank in worker/QA result files until stamp_result_timestamp.py runs")


def print_contract_validation_summary(
    selected_task: dict[str, Any],
    packet_validated: bool,
    task_validated: bool,
) -> None:
    print("")
    print("JARVIS: contract validation")
    print(f"- Selected task execution-eligible: {'yes' if task_validated else 'no'}")
    print(f"- Packet/result placeholder contract valid: {'yes' if packet_validated else 'no'}")
    print(f"- Selected task: {normalize_text(selected_task.get('task_id')).upper()}")


def print_next_steps(
    selected_task: dict[str, Any],
    workspace: Path,
    repo_path: Path,
    artifact_map: dict[str, Path],
    branch_name: str,
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()
    print("")
    print("JARVIS: foreman phase complete")
    print("TASK IS NOT COMPLETE YET")
    print("Do NOT run reconcile until code is committed, worker result is final, QA result is final, and both are stamped.")
    print("")
    print("Next steps:")
    print(f"1. Open repo: {repo_path}")
    print("2. Verify git state:")
    print("   - git branch --show-current")
    print("   - git status")
    print(f"3. Confirm branch is: {branch_name}")
    print("4. Review task packet:")
    print(f"   - {artifact_map['task_json']}")
    print(f"   - {artifact_map['task_md']}")
    print("5. Perform the bounded implementation only")
    print("6. Inspect the diff before commit")
    print(f"   - git diff -- {normalize_text(selected_task.get('notes')) or '<target_file>'}")
    print("7. Commit on the correct task branch")
    print(f"8. Finalize worker result JSON: {artifact_map['worker_result']}")
    print("9. Run QA (current live path):")
    print("   - npm run build")
    print("   - npm run test:e2e:smoke")
    print(f"10. Finalize QA result JSON: {artifact_map['qa_result']}")
    print("11. Stamp timestamps:")
    print(f"   - python .\\stamp_result_timestamp.py ..\\results\\{task_id}_worker_result.json")
    print(f"   - python .\\stamp_result_timestamp.py ..\\qa\\{task_id}_qa_result.json")
    print("12. Reconcile only when ready:")
    print(f"   - python .\\reconcile_task_outcome.py --task {task_id}")
    print("")
    print("Working process/documentation files should be updated whenever a new process rule or hardening change is locked in.")
    print(f"Workspace: {workspace}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Jarvis foreman v6: select or reuse one WCS task, validate task/artifact contracts, generate packet artifacts, prepare the correct repo branch, and print operator-safe handoff guidance."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow a new selection even if a WCS task was already selected today.",
    )
    parser.add_argument(
        "--force-packet",
        action="store_true",
        help="Force overwrite of existing task packet/result/qa/escalation files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = script_path.parent.parent
    state_dir = workspace / "state"

    backlog_path = state_dir / "master_backlog.json"
    project_status_path = state_dir / "project_status_wcs.json"
    daily_plan_json_path = state_dir / "daily_plan.json"
    daily_plan_md_path = state_dir / "DAILY_PLAN.md"
    run_log_json_path = state_dir / "run_log.json"
    run_log_md_path = state_dir / "RUN_LOG.md"

    try:
        backlog = read_json(backlog_path, expected_type=list)
        project_status_wcs = read_json(project_status_path, expected_type=dict)
        daily_plan = read_optional_json(daily_plan_json_path, default={}, expected_type=dict)
        run_log = read_optional_json(run_log_json_path, default=[], expected_type=list)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id="",
            phase="jarvis_state_load",
            reason_code="invalid_json_state",
            summary="Jarvis failed to load required JSON state during startup.",
            details=[str(exc)],
            recommended_next_action="Inspect the referenced JSON file, repair or restore it, then rerun jarvis.py.",
        )
        print("JARVIS: hard failure while loading required JSON state.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    current_date = today_local_date()
    current_timestamp = now_local_iso()

    used_existing_selection = False
    mode_banner = "NEW_SELECTION_NO_EXISTING_TODAY_TASK"

    try:
        if not args.force:
            existing_today = task_selected_today(daily_plan, run_log, current_date)
            if existing_today:
                existing_task_id = normalize_text(existing_today.get("task_id"))
                backlog_match = get_backlog_task_by_id(backlog, existing_task_id)
                if not backlog_match:
                    raise JarvisError(
                        f"Daily plan references task {existing_task_id}, but that task was not found in master_backlog.json."
                    )
                selected_task = backlog_match
                used_existing_selection = True
                mode_banner = "REUSING_ALREADY_SELECTED_TASK"
            else:
                selected_task = select_task(backlog)
        else:
            selected_task = select_task(backlog)
            mode_banner = "FORCED_FRESH_SELECTION"

        task_id = normalize_text(selected_task.get("task_id")).upper()
        validate_backlog_task_uniqueness(backlog, task_id)
        validate_task_shape(selected_task, context=f"Selected task {task_id}")
        task_validated = True
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=locals().get("task_id", ""),
            phase="jarvis_selection",
            reason_code="invalid_selected_task",
            summary="Jarvis failed to select a valid execution-eligible WCS task.",
            details=[str(exc)],
            recommended_next_action="Inspect the backlog entry and project status for this task, correct invalid fields or duplicates, then rerun jarvis.py.",
        )
        print("JARVIS: task selection/validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    if not used_existing_selection:
        plan = build_daily_plan(selected_task, current_timestamp)
        selection_entry = build_run_log_entry(
            event="task_selected",
            selected_task=selected_task,
            timestamp=current_timestamp,
            summary="Jarvis selected task for current daily plan.",
        )

        write_json(daily_plan_json_path, plan)
        write_text(daily_plan_md_path, render_daily_plan_md(plan))
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, selection_entry)
    else:
        plan = daily_plan

    artifact_map = task_artifact_paths(workspace, task_id)
    existing_artifacts, missing_artifacts = analyze_artifacts(artifact_map)

    packet_generated = False
    packet_skipped_existing = False
    packet_contract_validated = False

    if existing_artifacts and missing_artifacts and not args.force_packet:
        message = (
            "Partial packet artifact state detected. Some packet files already exist, but not all of them. "
            "Inspect the task artifacts and rerun with --force-packet only if overwrite is intentional.\n"
            + "\n".join(f"- existing: {path}" for path in existing_artifacts)
            + "\n"
            + "\n".join(f"- missing: {path}" for path in missing_artifacts)
        )
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="partial_packet_artifacts",
            summary="Jarvis detected partial packet artifact state for the selected task.",
            details=[message],
            recommended_next_action="Inspect existing/missing packet artifacts, decide whether to clean up or rerun with --force-packet, then rerun jarvis.py.",
        )
        print("JARVIS: partial packet artifact state detected.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    try:
        if existing_artifacts and not missing_artifacts and not args.force_packet:
            validate_existing_artifacts(artifact_map, selected_task)
            packet_contract_validated = True
            packet_skipped_existing = True
        else:
            returncode, packet_stdout, packet_stderr = run_packet_generator(
                workspace,
                task_id,
                force_packet=args.force_packet,
            )

            if returncode != 0:
                append_escalation(
                    state_dir=state_dir,
                    task_id=task_id,
                    phase="jarvis_packet_validation",
                    reason_code="packet_contract_mismatch",
                    summary="Jarvis packet generator reported a non-zero exit code.",
                    details=[
                        f"Return code: {returncode}",
                        f"STDERR: {packet_stderr.strip() or '(no stderr output)'}",
                    ],
                    recommended_next_action="Inspect generate_task_packet.py output, fix the underlying issue, then rerun jarvis.py (optionally with --force-packet).",
                )
                print("JARVIS: packet generation failed.", file=sys.stderr)
                print("An escalation record was written for operator follow-up.", file=sys.stderr)
                raise SystemExit(returncode)

            validate_generated_placeholders(artifact_map, selected_task)
            packet_contract_validated = True
            packet_generated = True
            packet_event = build_run_log_entry(
                event="task_packet_generated",
                selected_task=selected_task,
                timestamp=now_local_iso(),
                summary="Jarvis generated task packet and contract-valid placeholder execution artifacts.",
                artifacts=[str(path) for path in artifact_map.values()],
            )
            append_run_log_entry(run_log_json_path, run_log_md_path, run_log, packet_event)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="packet_contract_mismatch",
            summary="Jarvis detected invalid or mismatched packet/result placeholder contracts.",
            details=[str(exc)],
            recommended_next_action="Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet).",
        )
        print("JARVIS: packet/result placeholder contract validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_returncode, branch_stdout, branch_stderr = run_branch_preparer(workspace, task_id)

    if branch_returncode != 0:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_preparation",
            reason_code="branch_prepare_failed",
            summary="Jarvis branch preparer reported a non-zero exit code.",
            details=[
                f"Return code: {branch_returncode}",
                f"STDERR: {branch_stderr.strip() or '(no stderr output)'}",
            ],
            recommended_next_action="Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py.",
        )
        print("JARVIS: branch preparation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(branch_returncode)

    branch_info = parse_branch_prep_output(branch_stdout)
    target_branch = branch_info.get("TARGET_BRANCH", task_branch_name(task_id))
    repo_path = Path(
        branch_info.get("REPO_PATH") or normalize_text(project_status_wcs.get("repo_path"))
    ).resolve()

    try:
        verified_repo_state = verify_repo_branch_state(repo_path)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="repo_inspection_failed",
            summary="Jarvis failed to inspect the WCS repo branch/status after preparation.",
            details=[str(exc)],
            recommended_next_action="Inspect the WCS repo manually (branch and status), resolve issues, then rerun jarvis.py.",
        )
        print("JARVIS: repo branch/status inspection failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_mode = branch_info.get("MODE", "")
    if branch_mode in {"switched_to_existing_target", "created_new_target_from_main"}:
        branch_event = build_run_log_entry(
            event="task_branch_prepared",
            selected_task=selected_task,
            timestamp=now_local_iso(),
            summary=f"Jarvis prepared repo branch for task execution: {target_branch}",
            artifacts=[target_branch, str(repo_path)],
        )
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, branch_event)

    print_mode_banner(mode_banner)

    if used_existing_selection:
        print("JARVIS: using existing task selected today")
    else:
        print("JARVIS: task selected")
        print(f"Workspace: {workspace}")
        print(f"Priority: {normalize_text(selected_task.get('priority'))}")
        print(f"Risk: {normalize_text(selected_task.get('risk'))}")
        print(f"Bucket: {normalize_text(selected_task.get('bucket'))}")
        print(f"daily_plan.json: {daily_plan_json_path}")
        print(f"DAILY_PLAN.md: {daily_plan_md_path}")
        print(f"run_log.json: {run_log_json_path}")
        print(f"RUN_LOG.md: {run_log_md_path}")

    print(f"Task ID: {task_id}")
    print(f"Title: {normalize_text(selected_task.get('title'))}")

    print("")
    if packet_skipped_existing:
        print("JARVIS: packet generation skipped")
        print("Reason: all packet artifacts already exist for this task. Use --force-packet to overwrite.")
        for path in artifact_map.values():
            print(f"- {path}")
    elif packet_generated:
        print("JARVIS: packet generation complete")
        for path in artifact_map.values():
            print(f"WROTE: {path}")
        print("")
        print("Task packet generation complete.")
        print(f"Task packet markdown: {artifact_map['task_md']}")
        print(f"Task packet JSON:     {artifact_map['task_json']}")

    print("")
    print("JARVIS: branch preparation result")
    for line in branch_stdout.strip().splitlines():
        print(line)

    print("")
    print("JARVIS: final branch verification")
    print(f"VERIFIED_REPO_PATH: {repo_path}")
    print(f"VERIFIED_CURRENT_BRANCH: {verified_repo_state['current_branch']}")
    print(f"VERIFIED_EXPECTED_BRANCH: {target_branch}")
    print(f"VERIFIED_DIRTY: {verified_repo_state['dirty']}")
    print(f"VERIFIED_DIRTY_COUNT: {verified_repo_state['dirty_count']}")

    if verified_repo_state["current_branch"] != target_branch:
        details = [
            "Post-branch-prep verification failed. Repo is not on the expected task branch.",
            f"Expected: {target_branch}",
            f"Actual:   {verified_repo_state['current_branch']}",
        ]
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="branch_verification_failed",
            summary="Jarvis detected a branch mismatch after branch preparation.",
            details=details,
            recommended_next_action="Switch the WCS repo to the expected task branch or repair the branch state, then rerun jarvis.py.",
        )
        print("JARVIS: post-branch-prep branch verification failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    print_contract_validation_summary(selected_task, packet_contract_validated, task_validated)
    print_packet_placeholder_warning(task_id, artifact_map, packet_skipped_existing)
    print_result_contracts()
    print_next_steps(selected_task, workspace, repo_path, artifact_map, target_branch)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except JarvisError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        # Record a generic escalation when a JarvisError bubbles out that was not already
        # handled by a more specific escalation path.
        script_path = Path(__file__).resolve()
        state_dir = script_path.parent.parent / "state"
        try:
            append_escalation(
                state_dir=state_dir,
                task_id="",
                phase="jarvis_preflight",
                reason_code="invalid_json_state",
                summary="Jarvis encountered an unhandled JarvisError.",
                details=[str(exc)],
                recommended_next_action="Inspect the error message and recent changes, repair the underlying issue, then rerun jarvis.py.",
            )
        except Exception:
            # If escalation writing itself fails, avoid masking the original error.
            pass
        print("JARVIS: an escalation record may have been written for this failure.", file=sys.stderr)
        raise SystemExit(1)

## FILE: scripts/generate_task_packet.py
from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

VALID_STATUSES = {
    "draft",
    "ready",
    "dispatched",
    "in_progress",
    "worker_complete",
    "qa_pass",
    "qa_fail",
    "blocked",
    "escalated",
    "done",
    "deferred",
}

DEFAULT_PROJECT_CONFIG = {
    "WCS": {
        "repo_path": r"C:\dev\wcsv2.0-new",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Run npm run build",
            "Start local app with npm run dev",
            "Run Playwright smoke QA if available",
            "Verify the targeted change locally in the browser",
        ],
        "default_stop_conditions": [
            "Required file cannot be found",
            "Build fails for unrelated reasons",
            "Task scope expands beyond the targeted fix",
        ],
    },
    "N8N": {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Validate workflow or prompt output against the task rubric",
            "Confirm no malformed JSON or broken node configuration",
        ],
        "default_stop_conditions": [
            "Required workflow file cannot be found",
            "Task scope expands beyond the targeted fix",
            "Quality cannot be verified with the current rubric",
        ],
    },
}

TASK_MD_TEMPLATE = """# TASK PACKET

## Header
- Task ID: {task_id}
- Project: {project}
- Title: {title}
- Bucket: {bucket}
- Priority: {priority}
- Risk: {risk}
- Status: {status}

## Repo
- Repo Path: `{repo_path}`
- Branch Name: `{branch_name}`

## Problem Summary
{problem_summary}

## Goal
{goal}

## Suspected Files
{suspected_files_md}

## Acceptance Criteria
{acceptance_criteria_md}

## QA Plan
{qa_plan_md}

## System Impact
{system_impact}

## Stop Conditions
{stop_conditions_md}

## Notes
{notes}
"""


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class PacketGenerationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PacketGenerationError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PacketGenerationError(f"Invalid JSON in {path}: {exc}") from exc



def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")



def parse_notes_to_files(notes: str) -> list[str]:
    if not notes:
        return []
    cleaned = notes.replace("`", "").strip()
    parts = [part.strip() for part in re.split(r",|;", cleaned) if part.strip()]
    return parts



def humanize_title_to_problem(title: str) -> str:
    title = title.strip()
    if not title:
        return "Describe the current issue clearly before execution."
    return f"{title}."



def goal_from_title(title: str) -> str:
    if not title.strip():
        return "Complete the scoped task and verify the result."
    return f"Resolve: {title}, with the smallest safe change that satisfies QA."



def acceptance_from_backlog(item: dict[str, Any], suspected_files: list[str]) -> list[str]:
    project = item.get("project", "")
    title = item.get("title", "")
    criteria = [f"The scoped issue is resolved: {title}"] if title else ["The scoped issue is resolved"]
    if project == "WCS":
        criteria.extend([
            "App builds successfully with npm run build",
            "Local app can be opened for verification",
            "Targeted change is visible or behaves correctly on the relevant page/flow",
        ])
    elif project == "N8N":
        criteria.extend([
            "Workflow or prompt output passes the defined quality/rubric check",
            "No malformed JSON or broken node configuration is introduced",
        ])
    if suspected_files:
        criteria.append("Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated")
    return criteria



def system_impact_from_risk(project: str, risk: str, suspected_files: list[str]) -> str:
    base = {
        "low": "Low risk.",
        "medium": "Medium risk.",
        "high": "High risk.",
    }.get(risk, "Risk level not specified.")
    if suspected_files:
        scope = f" Primary expected scope: {', '.join(suspected_files)}."
    else:
        scope = " Scope should stay tightly bounded to the targeted issue."
    if project == "WCS":
        return base + " This should avoid unrelated production-facing behavior changes unless strictly necessary." + scope
    if project == "N8N":
        return base + " This should avoid unrelated workflow, credential, or publishing changes unless strictly necessary." + scope
    return base + scope



def bulletize(items: list[str], fallback: str) -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)



def build_packet_json(item: dict[str, Any], project_cfg: dict[str, Any], dispatch: bool) -> dict[str, Any]:
    task_id = item["task_id"]
    project = item["project"]
    notes = str(item.get("notes", "") or "")
    suspected_files = parse_notes_to_files(notes)
    ts = now_local()
    status = "dispatched" if dispatch else str(item.get("status", "ready") or "ready")
    if status not in VALID_STATUSES:
        raise PacketGenerationError(f"Task {task_id} has unsupported status: {status}")

    packet = {
        "task_id": task_id,
        "project": project,
        "title": str(item.get("title", "") or ""),
        "bucket": str(item.get("bucket", "") or ""),
        "priority": str(item.get("priority", "") or ""),
        "risk": str(item.get("risk", "") or ""),
        "status": status,
        "repo_path": project_cfg.get("repo_path", ""),
        "branch_name": f"{project_cfg.get('branch_prefix', 'jarvis-task-')}{task_id.lower()}",
        "problem_summary": humanize_title_to_problem(str(item.get("title", "") or "")),
        "goal": goal_from_title(str(item.get("title", "") or "")),
        "suspected_files": suspected_files,
        "acceptance_criteria": acceptance_from_backlog(item, suspected_files),
        "qa_plan": deepcopy(project_cfg.get("default_qa_plan", [])),
        "system_impact": system_impact_from_risk(project, str(item.get("risk", "") or ""), suspected_files),
        "stop_conditions": deepcopy(project_cfg.get("default_stop_conditions", [])),
        "notes": notes,
        "created_at": ts,
        "updated_at": ts,
    }
    return packet



def build_packet_markdown(packet: dict[str, Any]) -> str:
    suspected_files_md = bulletize(packet.get("suspected_files", []), "Confirm the target files before execution")
    acceptance_md = bulletize(packet.get("acceptance_criteria", []), "Add acceptance criteria before execution")
    qa_plan_md = bulletize(packet.get("qa_plan", []), "Add a QA plan before execution")
    stop_md = bulletize(packet.get("stop_conditions", []), "Add stop conditions before execution")
    notes = packet.get("notes") or "No additional notes."

    return TASK_MD_TEMPLATE.format(
        task_id=packet.get("task_id", ""),
        project=packet.get("project", ""),
        title=packet.get("title", ""),
        bucket=packet.get("bucket", ""),
        priority=packet.get("priority", ""),
        risk=packet.get("risk", ""),
        status=packet.get("status", ""),
        repo_path=packet.get("repo_path", ""),
        branch_name=packet.get("branch_name", ""),
        problem_summary=packet.get("problem_summary", ""),
        goal=packet.get("goal", ""),
        suspected_files_md=suspected_files_md,
        acceptance_criteria_md=acceptance_md,
        qa_plan_md=qa_plan_md,
        system_impact=packet.get("system_impact", ""),
        stop_conditions_md=stop_md,
        notes=notes,
    )



def create_blank_result(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "executor": "",
        "summary": "",
        "files_changed": [],
        "commands_run": [],
        "issues_encountered": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_qa(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "qa_tool": "",
        "summary": "",
        "checks_run": [],
        "checks_passed": [],
        "checks_failed": [],
        "artifacts": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_escalation(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "reason": "",
        "details": "",
        "recommended_next_action": "",
        "created_at": "",
    }



def maybe_write(path: Path, content: str | dict[str, Any], *, force: bool) -> tuple[bool, str]:
    if path.exists() and not force:
        return False, f"SKIPPED (exists): {path}"
    if isinstance(content, str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    else:
        save_json(path, content)
    return True, f"WROTE: {path}"



def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, new_status: str) -> None:
    for item in backlog_items:
        if item.get("task_id") == task_id:
            item["status"] = new_status
            return
    raise PacketGenerationError(f"Task {task_id} not found while updating backlog status")



def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        notes = str(item.get("notes", "") or "")
        lines.append(
            f"| {item.get('task_id','')} | {item.get('project','')} | {item.get('bucket','')} | {item.get('priority','')} | {item.get('risk','')} | {item.get('status','')} | {item.get('title','')} | {notes} |"
        )
    lines.append("")
    return "\n".join(lines)



def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Jarvis task packet files from master_backlog.json")
    parser.add_argument("--task", help="Task ID to generate, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite packet/result/qa/escalation files if they already exist")
    parser.add_argument("--dispatch", action="store_true", help="Mark the backlog item as dispatched when generating files")
    parser.add_argument("--list-ready", action="store_true", help="List ready tasks and exit")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    tasks_dir = workspace / "tasks"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise PacketGenerationError(f"Expected a JSON array in {backlog_json_path}")

    if args.list_ready:
        ready = [item for item in backlog if str(item.get("status", "")).lower() == "ready"]
        if not ready:
            print("No ready tasks found.")
            return 0
        print("Ready tasks:")
        for item in ready:
            print(f"- {item.get('task_id')}: {item.get('title')}")
        return 0

    if not args.task:
        parser.error("--task is required unless --list-ready is used")

    task_id = args.task.strip().upper()
    item = next((row for row in backlog if str(row.get("task_id", "")).upper() == task_id), None)
    if not item:
        raise PacketGenerationError(f"Task {task_id} not found in {backlog_json_path}")

    project = str(item.get("project", "") or "")
    project_cfg = DEFAULT_PROJECT_CONFIG.get(project, {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": ["Run the project-appropriate QA checks"],
        "default_stop_conditions": ["Task scope expands beyond the targeted fix"],
    })

    packet = build_packet_json(item, project_cfg, dispatch=args.dispatch)
    packet_md = build_packet_markdown(packet)

    task_json_path = tasks_dir / f"{task_id}_task.json"
    task_md_path = tasks_dir / f"{task_id}_task.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    outputs = [
        maybe_write(task_json_path, packet, force=args.force),
        maybe_write(task_md_path, packet_md, force=args.force),
        maybe_write(worker_result_path, create_blank_result(task_id), force=args.force),
        maybe_write(qa_result_path, create_blank_qa(task_id), force=args.force),
        maybe_write(escalation_path, create_blank_escalation(task_id), force=args.force),
    ]

    if args.dispatch:
        update_backlog_status(backlog, task_id, "dispatched")
        save_json(backlog_json_path, backlog)
        backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")
        print(f"UPDATED backlog status to dispatched for {task_id}")
        print(f"RENDERED: {backlog_md_path}")

    for _, message in outputs:
        print(message)

    print("\nTask packet generation complete.")
    print(f"Task packet markdown: {task_md_path}")
    print(f"Task packet JSON:     {task_json_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PacketGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)


## FILE: scripts/prepare_wcs_task_branch.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class BranchPrepError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BranchPrepError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BranchPrepError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def normalize_task_id(task_id: str) -> str:
    task_id = task_id.strip().upper()
    if not task_id.startswith("WCS-"):
        raise BranchPrepError(f"Expected task id like WCS-009. Got: {task_id}")
    return task_id


def target_branch_name(task_id: str) -> str:
    return f"jarvis-task-{task_id.lower()}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare the correct WCS task branch before execution."
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-009")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root. Defaults to script grandparent directory.",
    )
    parser.add_argument(
        "--repo",
        help="Override WCS repo path. If omitted, use state/project_status_wcs.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"

    task_id = normalize_task_id(args.task)
    target_branch = target_branch_name(task_id)

    if args.repo:
        repo_path = Path(args.repo).resolve()
    else:
        project_status = read_json(state_dir / "project_status_wcs.json")
        repo_path = Path(project_status["repo_path"]).resolve()

    if not repo_path.exists():
        raise BranchPrepError(f"WCS repo path does not exist: {repo_path}")

    git_dir = repo_path / ".git"
    if not git_dir.exists():
        raise BranchPrepError(f"Path is not a git repo: {repo_path}")

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise BranchPrepError(current_branch_result.stderr.strip() or "Failed to detect current branch.")

    current_branch = current_branch_result.stdout.strip()

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise BranchPrepError(status_result.stderr.strip() or "Failed to inspect repo status.")

    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    is_dirty = bool(dirty_lines)

    if current_branch == target_branch:
        mode = "already_on_target_dirty" if is_dirty else "already_on_target_clean"
        print(f"MODE: {mode}")
        print(f"CURRENT_BRANCH: {current_branch}")
        print(f"TARGET_BRANCH: {target_branch}")
        print(f"DIRTY: {'true' if is_dirty else 'false'}")
        if dirty_lines:
            print("DIRTY_FILES:")
            for line in dirty_lines:
                print(line)
        return 0

    if is_dirty:
        raise BranchPrepError(
            "Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.\n"
            f"Current branch: {current_branch}\n"
            f"Target branch: {target_branch}\n"
            "Dirty files:\n" + "\n".join(dirty_lines)
        )

    branch_exists_result = run_git(repo_path, ["branch", "--list", target_branch])
    if branch_exists_result.returncode != 0:
        raise BranchPrepError(branch_exists_result.stderr.strip() or "Failed to inspect branch list.")

    target_exists = bool(branch_exists_result.stdout.strip())

    if target_exists:
        switch_result = run_git(repo_path, ["switch", target_branch])
        if switch_result.returncode != 0:
            raise BranchPrepError(switch_result.stderr.strip() or f"Failed to switch to {target_branch}.")
        mode = "switched_to_existing_target"
    else:
        main_exists_result = run_git(repo_path, ["branch", "--list", "main"])
        if main_exists_result.returncode != 0:
            raise BranchPrepError(main_exists_result.stderr.strip() or "Failed to inspect main branch.")
        if not main_exists_result.stdout.strip():
            raise BranchPrepError("Cannot create target branch because local 'main' branch was not found.")

        create_result = run_git(repo_path, ["switch", "-c", target_branch, "main"])
        if create_result.returncode != 0:
            raise BranchPrepError(create_result.stderr.strip() or f"Failed to create {target_branch} from main.")
        mode = "created_new_target_from_main"

    print(f"MODE: {mode}")
    print(f"CURRENT_BRANCH: {current_branch}")
    print(f"TARGET_BRANCH: {target_branch}")
    print("DIRTY: false")
    print(f"REPO_PATH: {repo_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BranchPrepError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

## FILE: scripts/render_master_backlog.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_COLUMNS = [
    ("task_id", "Task ID"),
    ("project", "Project"),
    ("bucket", "Bucket"),
    ("priority", "Priority"),
    ("risk", "Risk"),
    ("status", "Status"),
    ("title", "Title"),
    ("notes", "Notes"),
]


def escape_md(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ").strip()


def load_backlog(json_path: Path) -> list[dict[str, Any]]:
    if not json_path.exists():
        raise FileNotFoundError(f"Backlog JSON not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Backlog JSON must contain a list of task objects.")

    cleaned: list[dict[str, Any]] = []
    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Task #{i} is not a JSON object.")
        cleaned.append(item)
    return cleaned


def render_markdown(tasks: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# MASTER_BACKLOG")
    lines.append("")
    header = "| " + " | ".join(label for _, label in DEFAULT_COLUMNS) + " |"
    divider = "|" + "|".join(["---"] * len(DEFAULT_COLUMNS)) + "|"
    lines.append(header)
    lines.append(divider)

    for task in tasks:
        row = []
        for key, _label in DEFAULT_COLUMNS:
            row.append(escape_md(task.get(key, "")))
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render MASTER_BACKLOG.md from master_backlog.json"
    )
    parser.add_argument(
        "--json",
        dest="json_path",
        default=None,
        help="Path to master_backlog.json",
    )
    parser.add_argument(
        "--md",
        dest="md_path",
        default=None,
        help="Path to output MASTER_BACKLOG.md",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    state_dir = script_dir.parent / "state"

    json_path = Path(args.json_path).expanduser() if args.json_path else state_dir / "master_backlog.json"
    md_path = Path(args.md_path).expanduser() if args.md_path else state_dir / "MASTER_BACKLOG.md"

    tasks = load_backlog(json_path)
    markdown = render_markdown(tasks)

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown, encoding="utf-8")

    print(f"Rendered {len(tasks)} tasks")
    print(f"JSON source: {json_path}")
    print(f"Markdown output: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


## FILE: scripts/reconcile_task_outcome.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

FINAL_STATUSES = {
    "done",
    "blocked",
    "escalated",
    "worker_complete",
    "qa_fail",
}


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class ReconcileError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ReconcileError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReconcileError(f"Invalid JSON in {path}: {exc}") from exc


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def escape_md(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def normalize_text(value: Any) -> str:
    return str(value or "").strip()


def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(item.get("task_id", "")),
                    escape_md(item.get("project", "")),
                    escape_md(item.get("bucket", "")),
                    escape_md(item.get("priority", "")),
                    escape_md(item.get("risk", "")),
                    escape_md(item.get("status", "")),
                    escape_md(item.get("title", "")),
                    escape_md(item.get("notes", "")),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def normalize_status(value: str) -> str:
    return str(value or "").strip().lower()


def decide_final_status(worker: dict[str, Any], qa: dict[str, Any], escalation: dict[str, Any]) -> str:
    worker_status = normalize_status(worker.get("status", ""))
    qa_status = normalize_status(qa.get("status", ""))
    escalation_status = normalize_status(escalation.get("status", ""))

    if escalation_status == "escalated":
        return "escalated"
    if worker_status == "escalated":
        return "escalated"
    if worker_status == "blocked":
        return "blocked"

    if worker_status != "worker_complete":
        raise ReconcileError(
            f"Worker result must have status 'worker_complete', 'blocked', or 'escalated'. Found: {worker_status or '<blank>'}"
        )

    if qa_status == "qa_pass":
        return "done"
    if qa_status == "qa_fail":
        return "blocked"
    if qa_status == "escalated":
        return "escalated"

    raise ReconcileError(
        f"QA result must have status 'qa_pass', 'qa_fail', or 'escalated'. Found: {qa_status or '<blank>'}"
    )


def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, final_status: str) -> dict[str, Any]:
    for item in backlog_items:
        if str(item.get("task_id", "")).upper() == task_id.upper():
            item["status"] = final_status
            return item
    raise ReconcileError(f"Task {task_id} not found in backlog")


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def load_repo_path_for_project(workspace: Path, project: str) -> Path:
    project_upper = normalize_text(project).upper()
    if project_upper == "WCS":
        status_path = workspace / "state" / "project_status_wcs.json"
    else:
        raise ReconcileError(f"Repo verification is not defined for project: {project_upper or '<blank>'}")

    status = load_json(status_path)
    if not isinstance(status, dict):
        raise ReconcileError(f"Expected JSON object in {status_path}")

    raw_repo_path = normalize_text(status.get("repo_path"))
    if not raw_repo_path:
        raise ReconcileError(f"Missing repo_path in {status_path}")

    repo_path = Path(raw_repo_path)
    if not repo_path.exists():
        raise ReconcileError(f"Configured repo path does not exist: {repo_path}")
    if not (repo_path / ".git").exists():
        raise ReconcileError(f"Configured repo path is not a git repository: {repo_path}")
    return repo_path


def detect_baseline_branch(repo_path: Path) -> str | None:
    for candidate in ("main", "master"):
        result = run_git(repo_path, ["branch", "--list", candidate])
        if result.returncode != 0:
            raise ReconcileError(result.stderr.strip() or f"Failed to inspect git branches in {repo_path}")
        if result.stdout.strip():
            return candidate
    return None


def verify_done_repo_state(workspace: Path, task: dict[str, Any]) -> dict[str, Any]:
    task_id = normalize_text(task.get("task_id")).upper()
    project = normalize_text(task.get("project")).upper()
    repo_path = load_repo_path_for_project(workspace, project)
    expected_branch = task_branch_name(task_id)

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise ReconcileError(current_branch_result.stderr.strip() or "Failed to detect current git branch.")
    current_branch = current_branch_result.stdout.strip()

    if current_branch != expected_branch:
        raise ReconcileError(
            "Refusing to mark task done because repo is on the wrong branch. "
            f"Current branch: {current_branch or '<blank>'}. Expected: {expected_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise ReconcileError(status_result.stderr.strip() or "Failed to inspect git status.")
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    if dirty_lines:
        raise ReconcileError(
            "Refusing to mark task done because repo has uncommitted changes.\n"
            + "\n".join(dirty_lines)
        )

    baseline_branch = detect_baseline_branch(repo_path)
    commits_ahead = None
    if baseline_branch:
        ahead_result = run_git(repo_path, ["rev-list", "--count", f"{baseline_branch}..HEAD"])
        if ahead_result.returncode != 0:
            raise ReconcileError(
                ahead_result.stderr.strip()
                or f"Failed to compare {expected_branch} against {baseline_branch}."
            )
        try:
            commits_ahead = int(ahead_result.stdout.strip() or "0")
        except ValueError as exc:
            raise ReconcileError(
                f"Unexpected rev-list output while comparing {expected_branch} against {baseline_branch}: {ahead_result.stdout!r}"
            ) from exc

        if commits_ahead < 1:
            raise ReconcileError(
                "Refusing to mark task done because the task branch has no commits ahead of "
                f"{baseline_branch}. Expected at least one committed task change on {expected_branch}."
            )

    head_commit_result = run_git(repo_path, ["rev-parse", "--short", "HEAD"])
    if head_commit_result.returncode != 0:
        raise ReconcileError(head_commit_result.stderr.strip() or "Failed to read HEAD commit.")

    return {
        "repo_path": str(repo_path),
        "expected_branch": expected_branch,
        "current_branch": current_branch,
        "baseline_branch": baseline_branch or "",
        "commits_ahead_of_baseline": commits_ahead,
        "head_commit": head_commit_result.stdout.strip(),
        "verified_at": now_local(),
    }


def build_daily_review_entry(
    task: dict[str, Any],
    worker: dict[str, Any],
    qa: dict[str, Any],
    final_status: str,
    repo_verification: dict[str, Any] | None = None,
) -> str:
    task_id = task.get("task_id", "")
    title = task.get("title", "")
    worker_summary = (worker.get("summary") or "").strip()
    qa_summary = (qa.get("summary") or "").strip()
    files_changed = worker.get("files_changed") or []
    commands_run = worker.get("commands_run") or []

    lines = [
        f"### {task_id} — {final_status}",
        f"- Title: {title}",
    ]
    if worker_summary:
        lines.append(f"- Worker: {worker_summary}")
    if qa_summary:
        lines.append(f"- QA: {qa_summary}")
    if files_changed:
        lines.append(f"- Files changed: {', '.join(map(str, files_changed))}")
    if commands_run:
        lines.append(f"- Commands run: {', '.join(map(str, commands_run))}")
    if repo_verification:
        lines.append(f"- Repo path: {repo_verification.get('repo_path', '')}")
        lines.append(f"- Verified branch: {repo_verification.get('current_branch', '')}")
        baseline_branch = normalize_text(repo_verification.get("baseline_branch"))
        if baseline_branch:
            lines.append(
                f"- Commits ahead of {baseline_branch}: {repo_verification.get('commits_ahead_of_baseline', '')}"
            )
        lines.append(f"- HEAD commit: {repo_verification.get('head_commit', '')}")
        lines.append(f"- Branch verified at: {repo_verification.get('verified_at', '')}")
    lines.append(f"- Reconciled at: {now_local()}")
    lines.append("")
    return "\n".join(lines)


def append_daily_review(
    review_path: Path,
    task: dict[str, Any],
    worker: dict[str, Any],
    qa: dict[str, Any],
    final_status: str,
    repo_verification: dict[str, Any] | None = None,
) -> None:
    entry = build_daily_review_entry(task, worker, qa, final_status, repo_verification=repo_verification)
    if review_path.exists():
        existing = review_path.read_text(encoding="utf-8")
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        existing = f"# DAILY_REVIEW\n\nDate: {today}\n\nSummary\n\nWins\n\nFailures / blockers\n\nNext step\n\n"

    task_id = str(task.get("task_id", ""))
    if f"### {task_id} —" in existing:
        return

    content = existing.rstrip() + "\n\n" + entry
    review_path.write_text(content, encoding="utf-8")


CURSOR_COMPLETION_CONTRACT = """When you finish the task, return your summary in this exact structure:

1. What changed
- Files changed:
- Short description of each change:

2. Commands run
- List each command exactly as run

3. Result
- Build result:
- Test result:
- QA result:

4. Issues encountered
- None
or
- List each issue clearly

5. Stop conditions
- State whether any stop condition was hit

6. Recommended worker_result.json fields
{
  \"status\": \"worker_complete\",
  \"summary\": \"...\",
  \"files_changed\": [\"...\"],
  \"commands_run\": [\"...\"],
  \"issues_encountered\": [],
  \"notes\": \"...\"
}

Do not add extra sections. Do not give broad advice unless asked."""


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconcile task outcome from worker and QA JSON files")
    parser.add_argument("--task", required=False, help="Task ID to reconcile, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--skip-review", action="store_true", help="Do not append an entry to DAILY_REVIEW.md")
    parser.add_argument("--print-cursor-contract", action="store_true", help="Print the recommended Cursor completion contract and exit")
    args = parser.parse_args()

    if args.print_cursor_contract:
        print(CURSOR_COMPLETION_CONTRACT)
        return 0

    if not args.task:
        parser.error("--task is required unless --print-cursor-contract is used")

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"

    task_id = args.task.strip().upper()
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"
    daily_review_path = state_dir / "DAILY_REVIEW.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise ReconcileError(f"Expected a JSON array in {backlog_json_path}")

    task = next((item for item in backlog if str(item.get("task_id", "")).upper() == task_id), None)
    if not task:
        raise ReconcileError(f"Task {task_id} not found in backlog")

    worker = load_json(worker_result_path)
    qa = load_json(qa_result_path)
    escalation = load_json(escalation_path) if escalation_path.exists() else {"status": "draft"}

    if str(worker.get("task_id", "")).upper() != task_id:
        raise ReconcileError(f"Worker result task_id mismatch in {worker_result_path}")
    if str(qa.get("task_id", "")).upper() != task_id:
        raise ReconcileError(f"QA result task_id mismatch in {qa_result_path}")

    final_status = decide_final_status(worker, qa, escalation)
    repo_verification = verify_done_repo_state(workspace, task) if final_status == "done" else None

    updated_task = update_backlog_status(backlog, task_id, final_status)
    save_json(backlog_json_path, backlog)
    backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")

    if not args.skip_review:
        append_daily_review(daily_review_path, updated_task, worker, qa, final_status, repo_verification=repo_verification)

    print(f"FINAL STATUS: {final_status}")
    if repo_verification:
        print("BRANCH VERIFIED: yes")
        print(f"REPO PATH: {repo_verification['repo_path']}")
        print(f"EXPECTED BRANCH: {repo_verification['expected_branch']}")
        print(f"CURRENT BRANCH: {repo_verification['current_branch']}")
        if repo_verification.get("baseline_branch"):
            print(
                f"COMMITS AHEAD OF {repo_verification['baseline_branch'].upper()}: "
                f"{repo_verification['commits_ahead_of_baseline']}"
            )
        print(f"HEAD COMMIT: {repo_verification['head_commit']}")
    print(f"UPDATED: {backlog_json_path}")
    print(f"RENDERED: {backlog_md_path}")
    if not args.skip_review:
        print(f"UPDATED: {daily_review_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReconcileError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)


## FILE: scripts/stamp_result_timestamp.py
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class StampError(Exception):
    pass


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise StampError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise StampError(f"Invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stamp a result JSON file with the current local ISO timestamp in completed_at."
    )
    parser.add_argument("file", help="Path to the JSON result file to stamp")
    parser.add_argument(
        "--field",
        default="completed_at",
        help="Field name to stamp. Defaults to completed_at.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing non-empty timestamp.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.file).resolve()

    data = read_json(path)
    if not isinstance(data, dict):
        raise StampError(f"Expected a JSON object in {path}, got {type(data).__name__}")

    field_name = args.field
    existing_value = data.get(field_name)

    if existing_value and not args.force:
        print(f"SKIPPED: {path}")
        print(f"Reason: {field_name} already has a value: {existing_value}")
        print("Use --force if you intentionally want to overwrite it.")
        return 0

    stamped_value = now_local_iso()
    data[field_name] = stamped_value
    write_json(path, data)

    print(f"STAMPED: {path}")
    print(f"{field_name}: {stamped_value}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except StampError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

## FILE: scripts/pre_reconcile_check.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Tuple


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class CheckError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise CheckError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CheckError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only pre-reconcile readiness check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016.",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id: str) -> str:
    task_id_norm = normalize_text(task_id).upper()
    if not task_id_norm.startswith("WCS-"):
        raise CheckError(f"Invalid task id (expected WCS-XXX): {task_id_norm}")
    suffix = task_id_norm.split("-", 1)[1]
    if not suffix.isdigit():
        raise CheckError(f"Invalid task id suffix (expected numeric): {task_id_norm}")
    return task_id_norm


def check_artifacts(workspace: Path, task_id: str, failures: list[str]) -> Tuple[Path, Path, Path]:
    task_json = workspace / "tasks" / f"{task_id}_task.json"
    worker_result = workspace / "results" / f"{task_id}_worker_result.json"
    qa_result = workspace / "qa" / f"{task_id}_qa_result.json"

    if not task_json.exists():
        failures.append(f"Missing task packet JSON: {task_json}")
    if not worker_result.exists():
        failures.append(f"Missing worker result JSON: {worker_result}")
    if not qa_result.exists():
        failures.append(f"Missing QA result JSON: {qa_result}")

    return task_json, worker_result, qa_result


def check_worker_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def resolve_repo_path(workspace: Path, failures: list[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except CheckError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    repo_raw = normalize_text(data.get("repo_path"))
    if not repo_raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(repo_raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def check_repo_state(repo_path: Path, task_id: str, failures: list[str]) -> tuple[str | None, str | None, int | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"Failed to read current branch in repo {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        failures.append(
            f"Failed to inspect repo status in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
        if dirty_lines:
            failures.append(
                f"Repo working tree is not clean in {repo_path}. {len(dirty_lines)} changed path(s) detected."
            )

    base_branch = None
    for candidate in ["main", "master"]:
        rev_parse = run_git(repo_path, ["rev-parse", "--verify", candidate])
        if rev_parse.returncode == 0:
            base_branch = candidate
            break

    if base_branch is None:
        failures.append(f"Neither 'main' nor 'master' branch exists in repo {repo_path}.")
        return expected_branch, current_branch, None

    ahead_result = run_git(repo_path, ["rev-list", "--count", f"{base_branch}..{current_branch or 'HEAD'}"])
    if ahead_result.returncode != 0:
        failures.append(
            f"Failed to compute commits ahead of {base_branch} in {repo_path}: "
            f"{ahead_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, current_branch, None

    ahead_str = normalize_text(ahead_result.stdout)
    try:
        ahead_count = int(ahead_str or "0")
    except ValueError:
        failures.append(
            f"Unexpected rev-list output for {base_branch}..{current_branch or 'HEAD'} in {repo_path}: {ahead_str}"
        )
        return expected_branch, current_branch, None

    if ahead_count < 1:
        failures.append(
            f"Task branch must be ahead of {base_branch} by at least 1 commit. Found: {ahead_count}."
        )

    return expected_branch, current_branch, ahead_count


def main() -> int:
    args = parse_args()

    if not args.task:
        print("PRE-RECONCILE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except CheckError as exc:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json, worker_result, qa_result = check_artifacts(workspace, task_id, failures)

    if worker_result.exists():
        check_worker_result(worker_result, task_id, failures)

    if qa_result.exists():
        check_qa_result(qa_result, task_id, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = None
    current_branch = None
    ahead_count: int | None = None

    if repo_path is not None:
        expected_branch, current_branch, ahead_count = check_repo_state(
            repo_path, task_id, failures
        )

    if failures:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("PRE-RECONCILE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch is not None and current_branch is not None:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        if ahead_count is not None:
            print(f"Commits ahead of main/master: {ahead_count}")
    print("Passed checks:")
    print("- task, worker result, and QA result artifacts present")
    print("- worker result contract and completed_at valid")
    print("- QA result contract and completed_at valid")
    print("- repo path, branch, and clean working tree valid")
    print("- task branch ahead of main/master by at least 1 commit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/post_reconcile_validate.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class ValidationError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ValidationError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only post-reconcile validation for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id_raw: str) -> str:
    task_id = normalize_text(task_id_raw).upper()
    if not task_id.startswith("WCS-"):
        raise ValidationError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise ValidationError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_state_files_exist(workspace: Path, failures: list[str]) -> dict[str, Path]:
    state_dir = workspace / "state"
    paths = {
        "backlog_json": state_dir / "master_backlog.json",
        "backlog_md": state_dir / "MASTER_BACKLOG.md",
        "daily_review_md": state_dir / "DAILY_REVIEW.md",
    }
    for key, path in paths.items():
        if not path.exists():
            failures.append(f"Missing state file: {path}")
    return paths


def check_backlog_json(backlog_json_path: Path, task_id: str, failures: list[str]) -> dict[str, Any] | None:
    try:
        data = read_json(backlog_json_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, list):
        failures.append(f"master_backlog.json root must be a list: {backlog_json_path}")
        return None

    matches: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if normalize_text(item.get("task_id")).upper() == task_id:
            matches.append(item)

    if len(matches) == 0:
        failures.append(f"No backlog entry found for task {task_id} in master_backlog.json.")
        return None
    if len(matches) > 1:
        failures.append(f"Expected exactly one backlog entry for {task_id}, found {len(matches)}.")
        return None

    record = matches[0]
    project = normalize_text(record.get("project")).upper()
    status = normalize_text(record.get("status")).lower()

    if project != "WCS":
        failures.append(
            f"Backlog entry for {task_id} has wrong project. Expected WCS, found {project or '(blank)'}."
        )
    if status != "done":
        failures.append(
            f"Backlog entry for {task_id} must have status 'done'. Found {status or '(blank)'}."
        )

    return record


def check_backlog_markdown(
    backlog_md_path: Path,
    task_id: str,
    title: str | None,
    failures: list[str],
) -> None:
    try:
        text = backlog_md_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing backlog markdown file: {backlog_md_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read backlog markdown {backlog_md_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in MASTER_BACKLOG.md.")

    if title:
        if title not in text:
            failures.append(f"Task title not found in MASTER_BACKLOG.md: {title}")

    # Simple done indicator: look for a line containing both the task id and 'done' (case-insensitive).
    done_line_found = False
    for line in text.splitlines():
        if task_id in line and "done" in line.lower():
            done_line_found = True
            break
    if not done_line_found:
        failures.append(
            f"MASTER_BACKLOG.md does not show a simple 'done' indicator on the same line as {task_id}."
        )


def check_daily_review(daily_review_path: Path, task_id: str, failures: list[str]) -> None:
    try:
        text = daily_review_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing DAILY_REVIEW.md: {daily_review_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read DAILY_REVIEW.md {daily_review_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in DAILY_REVIEW.md.")


def check_worker_result(worker_path: Path, task_id: str, failures: list[str]) -> None:
    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")
        return

    try:
        data = read_json(worker_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(qa_path: Path, task_id: str, failures: list[str]) -> None:
    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")
        return

    try:
        data = read_json(qa_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("POST-RECONCILE VALIDATION: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except ValidationError as exc:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    paths = check_state_files_exist(workspace, failures)

    backlog_record: dict[str, Any] | None = None
    title: str | None = None

    backlog_json_path = paths["backlog_json"]
    backlog_md_path = paths["backlog_md"]
    daily_review_path = paths["daily_review_md"]

    if backlog_json_path.exists():
        backlog_record = check_backlog_json(backlog_json_path, task_id, failures)
        if backlog_record is not None:
            title = normalize_text(backlog_record.get("title"))

    if backlog_md_path.exists():
        check_backlog_markdown(backlog_md_path, task_id, title, failures)

    if daily_review_path.exists():
        check_daily_review(daily_review_path, task_id, failures)

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    check_worker_result(worker_path, task_id, failures)
    check_qa_result(qa_path, task_id, failures)

    if failures:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    status = ""
    if backlog_record is not None:
        status = normalize_text(backlog_record.get("status"))

    print("POST-RECONCILE VALIDATION: PASS")
    print(f"Task: {task_id}")
    if title:
        print(f"Title: {title}")
    if status:
        print(f"Backlog status: {status}")
    print("Passed checks:")
    print("- backlog JSON contains one WCS backlog entry for this task with status done")
    print("- MASTER_BACKLOG.md shows the task id, title, and a done indicator")
    print("- DAILY_REVIEW.md includes the task id")
    print("- worker result exists with matching task_id, allowed status, and non-blank completed_at")
    print("- QA result exists with matching task_id, allowed status, and non-blank completed_at")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/worker_change_check.py
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


class WorkerChangeError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise WorkerChangeError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerChangeError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker change boundary check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerChangeError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerChangeError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path, failures: List[str]) -> Set[str]:
    try:
        data = read_json(task_json_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return set()

    if not isinstance(data, dict):
        failures.append(f"Task packet must be a JSON object: {task_json_path}")
        return set()

    expected: Set[str] = set()

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    if not expected:
        failures.append(
            f"Unable to determine expected file scope from task packet: {task_json_path}"
        )

    return expected


def resolve_repo_path(workspace: Path, failures: List[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    raw = normalize_text(data.get("repo_path"))
    if not raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def gather_changed_files(repo_path: Path, failures: List[str]) -> Set[str]:
    changed: Set[str] = set()

    status_result = run_git(repo_path, ["status", "--short"])
    if status_result.returncode != 0:
        failures.append(
            f"git status --short failed in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in status_result.stdout.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(maxsplit=1)
            if len(parts) == 2:
                changed.add(parts[1].replace("\\", "/"))

    diff_result = run_git(repo_path, ["diff", "--name-only"])
    if diff_result.returncode != 0:
        failures.append(
            f"git diff --name-only failed in {repo_path}: "
            f"{diff_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in diff_result.stdout.splitlines():
            path = normalize_text(line)
            if path:
                changed.add(path.replace("\\", "/"))

    return changed


def check_branch(repo_path: Path, task_id: str, failures: List[str]) -> Tuple[str, str | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"git branch --show-current failed in {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    return expected_branch, current_branch


def check_diff_sanity(repo_path: Path, changed_files: Set[str], failures: List[str]) -> None:
    if len(changed_files) > 3:
        failures.append(
            f"Too many changed files for a bounded task. Expected at most 3, found {len(changed_files)}."
        )

    for path in sorted(changed_files):
        diff_result = run_git(repo_path, ["diff", "--unified=0", "--", path])
        if diff_result.returncode != 0:
            failures.append(
                f"git diff --unified=0 failed for {path} in {repo_path}: "
                f"{diff_result.stderr.strip() or '(no stderr output)'}"
            )
            continue

        total_changes = 0
        for line in diff_result.stdout.splitlines():
            if not line:
                continue
            if line.startswith("@@"):
                continue
            if line.startswith("+++ ") or line.startswith("--- "):
                continue
            if line[0] in {"+", "-"}:
                total_changes += 1

        if total_changes > 40:
            failures.append(
                f"File {path} has too many changed lines for a bounded task. "
                f"Found {total_changes}, limit is 40."
            )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER CHANGE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerChangeError as exc:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json_path = workspace / "tasks" / f"{task_id}_task.json"
    expected_files = determine_expected_files(task_json_path, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = ""
    current_branch: str | None = None

    changed_files: Set[str] = set()
    if repo_path is not None:
        expected_branch, current_branch = check_branch(repo_path, task_id, failures)
        changed_files = gather_changed_files(repo_path, failures)

        if not changed_files:
            failures.append("No changed files detected in the WCS repo for this task.")

        if expected_files:
            for path in sorted(changed_files):
                if path not in expected_files:
                    failures.append(
                        f"Changed file {path} is outside the expected task scope: {sorted(expected_files)}."
                    )

        if changed_files:
            check_diff_sanity(repo_path, changed_files, failures)

    if failures:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("WORKER CHANGE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch and current_branch:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
    if expected_files:
        print(f"Expected file scope: {', '.join(sorted(expected_files))}")
    print(f"Actual changed files: {', '.join(sorted(changed_files))}")
    print("Passed checks:")
    print("- repo path and current branch resolved correctly")
    print("- changed files exist and are within expected task scope")
    print("- number of changed files is within the allowed limit")
    print("- per-file diff size is within the allowed limit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/worker_result_validate.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List, Set


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}


class WorkerResultError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise WorkerResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path) -> Set[str]:
    expected: Set[str] = set()
    try:
        data = read_json(task_json_path)
    except WorkerResultError:
        return expected

    if not isinstance(data, dict):
        return expected

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    return expected


def check_worker_result(
    worker_path: Path,
    task_id: str,
    mode: str,
    expected_files: Set[str],
    failures: List[str],
) -> None:
    try:
        data = read_json(worker_path)
    except WorkerResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    # Required fields
    required_fields = [
        "task_id",
        "status",
        "executor",
        "summary",
        "files_changed",
        "commands_run",
        "issues_encountered",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"Worker result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    executor = normalize_text(data.get("executor"))
    if not executor:
        failures.append("Worker result executor must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("Worker result summary must be present and non-blank.")

    files_changed = data.get("files_changed")
    if not isinstance(files_changed, list):
        failures.append("Worker result files_changed must be a list.")
        files_changed_list: List[str] = []
    else:
        files_changed_list = [normalize_text(x) for x in files_changed]

    commands_run = data.get("commands_run")
    if not isinstance(commands_run, list):
        failures.append("Worker result commands_run must be a list.")

    issues_encountered = data.get("issues_encountered")
    if not isinstance(issues_encountered, list):
        failures.append("Worker result issues_encountered must be a list.")

    # notes field must exist (already checked) but may be blank or non-blank; no extra content rule

    if status == "worker_complete":
        if not files_changed_list:
            failures.append(
                "Worker result files_changed must contain at least one entry when status is worker_complete."
            )

    for entry in files_changed_list:
        if not entry:
            failures.append("Worker result files_changed contains a blank entry.")

    # Simple task-scope consistency if expected scope is known
    if expected_files:
        for entry in files_changed_list:
            normalized_entry = entry.replace("\\", "/")
            if normalized_entry and normalized_entry not in expected_files:
                failures.append(
                    f"Worker result files_changed entry {normalized_entry} is outside expected task scope: {sorted(expected_files)}."
                )

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, worker result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, worker result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerResultError as exc:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    task_json_path = workspace / "tasks" / f"{task_id}_task.json"

    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")

    expected_files = determine_expected_files(task_json_path)

    if worker_path.exists():
        check_worker_result(worker_path, task_id, args.mode, expected_files, failures)

    if failures:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    # Best-effort display of key fields on pass
    data = read_json(worker_path)
    executor = normalize_text(data.get("executor"))
    status = normalize_text(data.get("status"))
    files_changed = data.get("files_changed") or []
    files_changed_display = [normalize_text(x) for x in files_changed if normalize_text(x)]

    print("WORKER RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"Executor: {executor}")
    print(f"Status: {status}")
    print(f"Files changed: {', '.join(files_changed_display) if files_changed_display else '(none)'}")
    print("Passed checks:")
    print("- worker result JSON exists and parses")
    print("- required worker result fields are present")
    print("- executor and summary are non-blank")
    print("- list fields (files_changed, commands_run, issues_encountered) have the correct types")
    print("- files_changed is non-empty for worker_complete (if applicable)")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")
    if expected_files:
        print("- files_changed entries are within expected task scope")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/qa_result_validate.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List


ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class QaResultError(Exception):
    pass


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise QaResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise QaResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only QA result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise QaResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise QaResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_qa_result(
    qa_path: Path,
    task_id: str,
    mode: str,
    failures: List[str],
) -> None:
    try:
        data = read_json(qa_path)
    except QaResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    required_fields = [
        "task_id",
        "status",
        "qa_tool",
        "summary",
        "checks_run",
        "checks_passed",
        "checks_failed",
        "artifacts",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"QA result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    qa_tool = normalize_text(data.get("qa_tool"))
    if not qa_tool:
        failures.append("QA result qa_tool must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("QA result summary must be present and non-blank.")

    checks_run = data.get("checks_run")
    checks_passed = data.get("checks_passed")
    checks_failed = data.get("checks_failed")
    artifacts = data.get("artifacts")

    if not isinstance(checks_run, list):
        failures.append("QA result checks_run must be a list.")
        checks_run_list: List[str] = []
    else:
        checks_run_list = [normalize_text(x) for x in checks_run]

    if not isinstance(checks_passed, list):
        failures.append("QA result checks_passed must be a list.")
        checks_passed_list: List[str] = []
    else:
        checks_passed_list = [normalize_text(x) for x in checks_passed]

    if not isinstance(checks_failed, list):
        failures.append("QA result checks_failed must be a list.")
        checks_failed_list: List[str] = []
    else:
        checks_failed_list = [normalize_text(x) for x in checks_failed]

    if not isinstance(artifacts, list):
        failures.append("QA result artifacts must be a list.")
        artifacts_list: List[str] = []
    else:
        artifacts_list = [normalize_text(x) for x in artifacts]

    # notes must exist (checked above) but can be blank or non-blank; no extra content rule

    if status in {"qa_pass", "qa_fail"} and not checks_run_list:
        failures.append(
            "QA result checks_run must contain at least one entry when status is qa_pass or qa_fail."
        )

    for arr_name, arr in [
        ("checks_run", checks_run_list),
        ("checks_passed", checks_passed_list),
        ("checks_failed", checks_failed_list),
        ("artifacts", artifacts_list),
    ]:
        for entry in arr:
            if not isinstance(entry, str):
                failures.append(f"QA result {arr_name} contains a non-string entry.")
            elif not entry:
                failures.append(f"QA result {arr_name} contains a blank entry.")

    # Simple internal consistency
    if status == "qa_pass":
        if checks_failed_list:
            failures.append("QA result checks_failed must be empty when status is qa_pass.")
        if not checks_passed_list:
            failures.append("QA result checks_passed must contain at least one entry when status is qa_pass.")
    elif status == "qa_fail":
        if not checks_failed_list:
            failures.append("QA result checks_failed must contain at least one entry when status is qa_fail.")
    # status == escalated: no extra requirements for checks_passed / checks_failed beyond type and content shape

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, QA result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, QA result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("QA RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except QaResultError as exc:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")

    if qa_path.exists():
        check_qa_result(qa_path, task_id, args.mode, failures)

    if failures:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    data = read_json(qa_path)
    qa_tool = normalize_text(data.get("qa_tool"))
    status = normalize_text(data.get("status"))
    checks_run = data.get("checks_run") or []
    checks_run_display = [normalize_text(x) for x in checks_run if normalize_text(x)]

    print("QA RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"QA tool: {qa_tool}")
    print(f"Status: {status}")
    print(f"Checks run: {', '.join(checks_run_display) if checks_run_display else '(none)'}")
    print("Passed checks:")
    print("- QA result JSON exists and parses")
    print("- required QA result fields are present")
    print("- qa_tool and summary are non-blank")
    print("- list fields (checks_run, checks_passed, checks_failed, artifacts) have the correct types")
    print("- checks_run is non-empty for qa_pass/qa_fail (if applicable)")
    print("- internal consistency between status, checks_passed, and checks_failed")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
````

### JARVIS_PHASE_CHECKLIST.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_PHASE_CHECKLIST.md`
- Status: active
- Short purpose: Phase-by-phase rebuild checklist and status for Jarvis workspace
- Note: Current live phase checklist.

````md
# JARVIS_REBUILD_PHASE_CHECKLIST.md

## Live Doc Status
- Last reviewed: 2026-03-14
- Last updated: 2026-03-14 (doc pass: packet lifecycle/status cleanup + future-option parking)
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Status: aligned to current live hardening state (escalation surfaces live; commit gate helper live and proven; file registry drift/coverage checker live; QA result drafting helper live and validator-proven; packet lifecycle/status cleanup now keeps reconciled task packet artifacts aligned)

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
- [ ] Add research scout for debugging support
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
- [ ] Harden all script wrappers
- [ ] Standardize output log locations
- [ ] Reduce naming drift across docs/state/scripts
- [ ] Improve evidence reporting and human review surfaces

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
- [x] Wire optional QA-result drafting into guarded post_worker/full via `run_guarded_task_cycle.py --draft-qa-result` and QA evidence passthrough; draft step runs before `qa_result_validate.py --mode pre-stamp`; without `--draft-qa-result`, QA result JSON still required — **live**
- [x] Wire optional worker-result drafting into guarded post_worker/full via `run_guarded_task_cycle.py --draft-worker-result` plus truthful repeatable `--worker-command <text>` (and optional `--worker-executor` passthrough); inserted worker-draft step runs immediately before `worker_result_validate.py --mode pre-stamp`, pre_worker remains unchanged, and WCS-042 proved the safe boundary through worker draft PASS + worker pre-stamp validation PASS before intentionally stopping ahead of stamp/reconcile — **live**
- [x] Build `select_next_ready_task.py` as a read-only workflow helper that selects the next eligible ready task from backlog/planning surfaces using progression ladder (execution_lane, test_phase, selector_rank) when present, without mutating state — **live**
- [x] Build `build_daily_execution_prep.py` as a workflow helper that prepares operator-facing daily execution prep by ensuring packet availability (invoking `generate_task_packet.py` when needed), then chaining handoff and summary helpers, without executing tasks or mutating state beyond approved helper outputs — **live**
- [x] **Next major milestone:** Build Cursor invocation bridge (`run_cursor_worker.py`) — prefers real Agent CLI (`agent`) when available (Windows-hardened detection: which/where/PowerShell), falls back to desktop cursor launcher; attempts execution of generated handoff; reports PASS/BLOCKED/FAIL honestly; does not prove completion or write worker_complete; operator still verifies completion and finalizes worker-result evidence; system remains operator-assisted at the worker completion/evidence stage — **live**
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
````

### JARVIS_SCRIPT_PROCESS_REFERENCE.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_SCRIPT_PROCESS_REFERENCE.md`
- Status: active
- Short purpose: Live reference for Jarvis WCS task execution process and hardening helpers
- Note: Current live script/process reference.

````md
````md
# JARVIS_SCRIPT_PROCESS_REFERENCE_v2.md

## Live Doc Status
- Last reviewed: 2026-03-14
- Last updated: 2026-03-14 (doc pass: packet lifecycle/status cleanup live)
- Status: aligned to current live hardening state (hardened loop with validation gates, commit gate, stamping, file-registry checker, and packet lifecycle/status cleanup during reconcile; proven across WCS-016–WCS-019, full guarded cycle WCS-042, and fresh integrated-loop proof WCS-043)
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Proof: Real guarded end-to-end task cycles succeeded on WCS-042 and WCS-043. On WCS-043, reconcile safely proved that task packet JSON and task packet markdown now sync to the terminal outcome instead of remaining misleadingly `ready`.

## Current local state / follow-up
- No special local follow-up is required for the packet lifecycle/status cleanup beyond normal review and commit discipline.

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

`run_cursor_worker.py` is live as a **Cursor invocation bridge**: it prefers the **real Cursor Agent CLI** (`agent`) when available; if not, it falls back to the **desktop cursor launcher**. Execution runs against the **task repo workspace** (from the task packet), not the Jarvis workspace; Agent uses `--trust` for non-interactive use. It reports PASS / BLOCKED / FAIL honestly. It does not by itself prove task completion or write a truthful worker_complete result. The operator still verifies completion and finalizes worker-result evidence. The system remains **operator-assisted at the worker completion/evidence stage**; full autonomy is not achieved.

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
- optional `--workspace` (default: Jarvis workspace root), optional `--handoff` (default: `scratch/cursor_handoffs/<task>_cursor_handoff.md`)
- validates: task id, Jarvis workspace, handoff file exists, task packet exists; **reads and validates `repo_path` from task packet** (required; must exist and be a directory; FAIL if missing or invalid)
- **Agent CLI detection (Windows-hardened):** tries `shutil.which("agent")`, then `agent.cmd`, `agent.exe`, `agent.bat`; on Windows only, if none found, runs `where agent` / `where agent.cmd` and uses first existing path, then tries PowerShell `Get-Command agent`. If Agent CLI still cannot be found in the process environment, falls back to cursor and reports which path was used.
- **Execution target:** Agent and desktop launcher both use the **task repo workspace** (`repo_path` from packet): Agent is run with `--workspace <repo_path>`, `--trust` (non-interactive trust for that repo), and subprocess cwd = `repo_path`; desktop launcher subprocess cwd = `repo_path`. Handoff file remains in Jarvis workspace; execution context is the task repo.
- **Execution priority:** (1) if `agent` CLI is detected, runs `agent --print --workspace <repo_path> --trust "<prompt>"` with cwd = repo_path (prompt is handoff file content when ≤6000 chars, else path-based instruction); (2) else if `cursor` launcher is on PATH, runs `cursor <handoff_path>` with cwd = repo_path; (3) if neither found, exits BLOCKED (exit 2). When agent returns non-zero and stderr mentions authentication, a hint suggests running `agent login`.
- does not fabricate worker completion; does not write a worker result unless execution is truthfully successful (scripted execution does not provide completion evidence; operator must finalize the worker result)
- exit codes: 0 PASS (agent or cursor process started and exited 0), 2 BLOCKED (neither agent nor cursor found, or process failed/timeout), 1 FAIL (malformed input, missing handoff/packet, missing or invalid repo_path, or validation failure)

### Output

- On PASS: `RUN CURSOR WORKER: PASS`, task id, **Jarvis workspace**, **Task repo workspace**, handoff path, whether **Real Agent CLI** or **Desktop launcher fallback** was used, that worker result was not written (no completion evidence), summary
- On BLOCKED: `RUN CURSOR WORKER: BLOCKED`, reason, **Jarvis workspace**, **Task repo workspace**, worker result not written
- On FAIL: `RUN CURSOR WORKER: FAIL`, reason (e.g. handoff file does not exist; task packet has no repo_path; repo path does not exist or is not a directory)

### Why it exists

This script is the Cursor invocation bridge for the current WCS worker execution surface: it runs Agent (or cursor launcher) against the task repo workspace from the packet, with non-interactive trust for that repo when using Agent. It does not prove task completion or write a truthful worker_complete result; the operator still verifies completion and finalizes worker-result evidence. The system remains operator-assisted at the worker completion/evidence stage.

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
````

### JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md`
- Status: legacy
- Short purpose: Current authoritative decisions and system rules
- Note: Legacy design-era baseline still kept as a current reference; live truth is primarily in the live handoff/process docs.

````md
# JARVIS Multi-Agent Development System
## System Source of Truth

**Version:** v3.0  
**Date:** March 9, 2026  
**Last updated:** 2026-03-14  
**Last reviewed:** 2026-03-14  
**Status:** Authoritative decisions; design-era baseline. For **current live process and script list** (validators, stamping, reconcile gates), see **JARVIS_LIVE_HANDOFF_BUNDLE.md** and **JARVIS_SCRIPT_PROCESS_REFERENCE.md**.  
**Use:** Final reference for architecture, constraints, and phase-1 rules

---

## 1. Purpose of This Document

This file records the hard decisions that govern the Jarvis rebuild.

It exists so the project does not drift every time a new idea sounds exciting.

If another note, prompt, or conversation conflicts with this file, this file wins until it is intentionally revised.

---

## 2. Core Identity

Jarvis is a **local-first development foreman** for one operator.

Jarvis is not the main builder.
Jarvis is the coordinator that turns project state into bounded work.

The system is meant to help move real projects forward through:

- planning
- packet generation
- worker routing
- verification
- logging
- escalation

The system succeeds by creating **trustworthy progress**, not by sounding autonomous.

---

## 3. Governing Rule

> **Small verified progress beats large speculative progress.**

Everything below follows from that rule.

---

## 4. Architecture Verdict

### 4.1 Phase-1 runtime
**Chosen:** simple Python orchestration script

### 4.2 Phase-1 state model
**Chosen:** markdown + JSON sidecars

### 4.3 Phase-1 coding execution truth
**Chosen:** semi-manual Cursor worker for WCS

### 4.4 Phase-1 verification truth
**Chosen:** Playwright for WCS

### 4.5 Phase-1 activation scope
**Chosen:** WCS planning and proof loop first

### 4.6 Deferred elements
- LangGraph
- project leads
- fully automated coding worker
- n8n autonomous worker
- voice interface
- machine maintenance worker
- dashboard-first work

---

## 5. Phase-1 Mission

The mission of phase 1 is **not** to build the full Jarvis dream.

The mission is to prove one boring loop:

1. state exists
2. Jarvis reads it
3. Jarvis chooses one bounded WCS task
4. Jarvis writes a valid packet
5. task is executed in Cursor
6. result is recorded
7. Playwright QA runs
8. task becomes done or escalated
9. status and logs update correctly

If that loop is not trustworthy, nothing else should be added.

---

## 6. Current Project Priority

### Priority 1
**WCS stabilization and cleanup**

Reason:
- visible value
- bounded UI issues
- clear acceptance criteria
- Playwright is a strong QA path

### Priority 2
**n8n quality improvement design**

Reason:
- important project
- current workflow exists
- quality criteria still too subjective for real automation

### Priority 3
**Future workers**

Only after phase-1 loop stability.

---

## 7. WCS Truth

### 7.1 WCS is the first active build domain
This is the first project where the system must prove it can generate and move real tasks.

### 7.2 WCS task sourcing
Initial WCS backlog categories:

1. Broken
2. Ugly
3. Incomplete
4. Optimization

### 7.3 WCS phase-1 pull rule
Jarvis only pulls from:

- Broken
- Ugly

### 7.4 WCS task size rule
No phase-1 WCS task should require:

- broad redesign
- multi-route change
- database migration
- dependency upgrade
- auth flow rewrite

If it does, the task is too big or wrongly framed.

---

## 8. n8n Truth

### 8.1 n8n is real but deferred
The n8n project matters, but it is not phase-1 execution priority.

### 8.2 Why it is deferred
The system does not yet have a machine-checkable rubric for “better output.”

### 8.3 Activation requirement
Before n8n becomes an active worker path, the build must define:

- output schema
- scoreable quality rubric
- required blocks
- regression tests
- fail conditions

Until then, n8n planning can exist, but n8n automation cannot be trusted.

---

## 9. Worker Truth

### 9.1 Worker rule
Every worker must have:

- purpose
- scope
- input packet
- output contract
- QA path
- escalation rules

### 9.2 No undefined workers
If a worker cannot state those five things clearly, it is not a worker yet. It is just an idea.

### 9.3 No self-grading
No worker may certify final success for its own work.

---

## 10. WCS Worker Truth

### 10.1 Current reality
The WCS worker is **semi-manual**.

### 10.2 What that means
- Jarvis writes the packet
- the operator executes the packet in Cursor
- the result is captured back into the system
- QA verifies independently

### 10.3 Why this is correct
It matches current habits, current tooling, and current reliability.

Pretending phase 1 is fully autonomous coding would be fake autonomy.

---

## 11. State Truth

### 11.1 Markdown remains mandatory
The operator must be able to inspect and edit state directly.

### 11.2 JSON remains mandatory
Scripts must not depend on scraping prose only.

### 11.3 No premature database
SQLite is not phase-1 state.

If markdown + JSON sidecars become genuinely painful in real use, database adoption can be reconsidered later.

### 11.4 Source-of-truth stance
In phase 1, markdown and JSON sidecars are the official state pair.

---

## 12. File Truth

### Mandatory markdown files

- `MASTER_BACKLOG.md`
- `DAILY_PLAN.md`
- `RUN_LOG.md`
- `PROJECT_STATUS_WCS.md`
- `PROJECT_STATUS_N8N.md`
- `ESCALATIONS.md`
- `AGENT_REGISTRY.md`
- `OPERATING_RULES.md`

### Mandatory JSON files

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Mandatory template files

- `task_packet.template.json`
- `worker_result.template.json`
- `qa_result.template.json`
- `escalation_record.template.json`

---

## 13. Script Truth

### Scripts that must exist in phase 1

1. `jarvis.py`
2. `truth_map_wcs.py`
3. `seed_backlog_wcs.py`
4. `record_worker_result.py`
5. `run_wcs_qa.py`
6. `escalate_task.py`

### What does not need to exist yet

- LangGraph graph definitions
- lead-manager scripts
- voice loop scripts
- machine cleanup scripts
- scheduler-first infrastructure
- dashboard-first infrastructure

---

## 14. Task Packet Truth

Every executable task packet must include:

- task ID
- project
- worker
- title
- problem
- goal
- scope
- suspected files
- acceptance criteria
- QA method
- risk level
- system impact
- stop conditions
- status
- created timestamp

### Why “system impact” is mandatory
A task must declare whether it is expected to touch:

- UI only
- workflow only
- auth
- data
- payment
- deployment
- shared infra

This is a hard risk-control field, not optional flavor text.

---

## 15. Truth Mapping Truth

Truth mapping is mandatory before broad automation.

### Minimum WCS truth mapping outputs

- repo structure summary
- framework indicators
- scripts and entry points
- route map overview
- component map overview
- obvious fragile areas
- recent known blockers if any

Truth mapping records facts.
It does not generate completion claims.

---

## 16. Failure Policy Truth

### Hard numbers for phase 1

- max planned tasks per cycle: **1**
- max WCS tasks per day: **1**
- planning timeout: **90 sec**
- QA timeout: **300 sec**
- parse retry: **1**
- QA auto-retry: **0**
- consecutive escalations before pause: **2**

### Immediate escalation conditions

- malformed JSON
- missing required packet fields
- target files missing
- task exceeds scope
- unexpected high-risk impact
- QA hard fail
- operator clarification required

### Pause rule
After 2 consecutive active task escalations/failures, pause further execution until review.

---

## 17. Scheduling Truth

Scheduling is **not** phase-1 proof.

The system must first prove:

- planning loop works
- packet contract works
- WCS worker result capture works
- WCS QA works
- escalation handling works

Only after that may scheduling be enabled.

Initial scheduling rule:
- one run
- one task
- no overlap

---

## 18. Voice Truth

Voice is explicitly later-phase work.

The voice layer does not solve the hard problem.
The hard problem is trustworthy orchestration and verification.

Only when the boring loop works should voice be added.

---

## 18A. Deferred Future Interface And Audit Options

### 18A.1 LiveKit
LiveKit is the leading future candidate for a Jarvis voice transport / realtime voice interface layer.

If used later, LiveKit is not Jarvis's brain and does not replace Jarvis core planning, orchestration, state, or execution flow.

Preferred layering if voice is activated later:
- speech-to-text
- intent/router layer
- Jarvis command adapter
- Jarvis core
- text-to-speech

Early voice support should stay read-only / low-risk:
- what's next
- summarize status
- read escalations
- read today's plan

Voice remains deferred in the current phase.

### 18A.2 LibreCrawl
LibreCrawl is a future optional crawl-audit companion, not a replacement for Playwright.

If used later, it should stay a bounded supporting audit layer for:
- broken links
- crawl coverage
- metadata issues
- content/asset discovery
- broad regression scanning

LibreCrawl evidence should feed QA/review, not decide task completion by itself. It should not be allowed to create noisy low-value alert spam.

Playwright remains the primary QA path in the current phase.

---

## 19. Future Worker Truth

Allowed future workers include:

- error/issues research scout
- content/topic research scout
- n8n workflow/content improver
- local machine maintenance worker
- voice interface worker

Each future worker must satisfy the standard worker rule before activation.

No new worker may be added just to hide a broken core loop.

---

## 20. Build Order Truth

### Week 1 order

#### Days 1–2
- create workspace structure
- create markdown files
- create JSON sidecars
- implement `jarvis.py` planning loop
- implement WCS truth mapping

#### Day 3
- define task packet, worker result, QA result, escalation record templates
- run a mock worker test

#### Days 4–5
- execute one semi-manual WCS task through Cursor
- record worker result

#### Days 6–7
- run Playwright QA
- prove done/fail/escalate transitions
- update run log and project status correctly

### Explicitly rejected for week 1

- building the full agent fleet
- building voice interaction
- building full LangGraph orchestration
- building a dashboard before the loop works
- adding project leads
- pretending n8n quality automation is solved

---

## 21. Expansion Trigger

The system is ready for phase-2 discussion only when:

- 5 or more WCS tasks have completed or escalated through the full loop
- state files remain understandable
- task packets stay stable
- QA catches real issues
- pause/escalation behavior works
- operator trust is increasing, not decreasing

Until then, phase 1 stays phase 1.

---

## 22. Final Statement

Jarvis is not being rebuilt to look intelligent.

Jarvis is being rebuilt to make **controlled, auditable, low-drama progress** on real projects.

That means the phase-1 system must stay small, honest, and verifiable.
````

### JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md`
- Status: legacy
- Short purpose: High-level product requirements for Jarvis rebuild
- Note: Legacy design-era PRD baseline still kept for planning context; not the primary live operating truth.

````md
# Jarvis Multi-Agent Development System
## Product Requirements Document (PRD)

**Version:** 3.0  
**Date:** March 9, 2026  
**Last updated:** 2026-03-14  
**Last reviewed:** 2026-03-14  
**Status:** Rebuild baseline; design-era. For **current live execution loop and scripts**, see **JARVIS_LIVE_HANDOFF_BUNDLE.md** and **JARVIS_SCRIPT_PROCESS_REFERENCE.md**.  
**Type:** Product definition and implementation direction

---

## 1. Product Overview

The **Jarvis Multi-Agent Development System** is a **local-first development operations system** for one operator running multiple real projects from one workstation.

Jarvis is **not** the main coder.  
Jarvis is the **foreman**.

Jarvis exists to:

- read durable project state
- select the next bounded task
- generate a strict task packet
- route work to the correct worker
- require independent verification
- record outcomes and next actions
- keep progress moving with minimal babysitting

The system is designed around one governing principle:

> **Small verified progress beats large speculative progress.**

### Initial project domains

1. **WCS website**
   - mostly built
   - needs stabilization, cleanup, and completion work
   - current code editing tool is Cursor

2. **n8n voice/content system**
   - working but uneven
   - needs quality improvements for X.com content generation
   - needs a tighter quality rubric before real automation

### Phase-1 architectural truth

Phase 1 is **not** a flashy autonomous multi-agent empire.

Phase 1 is:

- one simple Python orchestration loop
- markdown files for human-readable state
- JSON sidecars for machine-readable state
- one semi-manual WCS worker flow through Cursor
- one independent QA flow through Playwright
- one repeatable proof loop

---

## 2. Product Problem

The user already has tools and projects, but they are fragmented:

- planning is scattered
- priorities drift
- small fixes accumulate
- verification is inconsistent
- project memory is mostly informal
- current AI tooling either over-promises or requires babysitting

Typical AI-agent setups fail because they:

- blur planning, execution, and QA
- hide state inside chats
- lack durable task contracts
- make autonomous claims without evidence
- burn time and money on orchestration theater

Jarvis solves that by creating:

- visible system state
- bounded tasks
- narrow workers
- hard verification gates
- a repeatable daily operating loop

---

## 3. Product Goals

### Primary goals

1. Turn project chaos into a prioritized bounded backlog.
2. Keep durable project state across days and sessions.
3. Generate clear task packets instead of vague missions.
4. Move work through planning → execution → verification → logging.
5. Reduce manual coordination overhead.
6. Keep runtime and API costs controlled.
7. Support future modular workers without redesigning the core.

### Secondary goals

- enable later voice interaction
- support scheduled daily cycles
- preserve local-first control
- keep tooling replaceable
- avoid dependency on one fragile runtime shell

### Non-goals for Phase 1

- full autonomy across multiple repos
- automatic voice conversation
- automatic cleanup of the whole machine
- multi-lead hierarchy
- LangGraph-first orchestration
- a giant all-in-one agent framework

---

## 4. Product Principles

### 4.1 Jarvis is a coordinator, not a worker
Jarvis selects, routes, and records.
Jarvis does not pretend to be the builder, the researcher, and the QA lead at once.

### 4.2 Every task must be bounded
No worker receives a vague instruction like “improve the site.”
Every task packet must define scope, acceptance criteria, and exit conditions.

### 4.3 No worker self-certifies success
Independent verification is mandatory for anything that counts as completed work.

### 4.4 Human-readable state is required
State must remain visible and editable by the operator.

### 4.5 Machine-readable state is also required
Automation must not depend on parsing loose prose only.

### 4.6 Start with the simplest durable runtime
A boring script that survives real use is better than a “smart” framework that collapses under debugging.

---

## 5. Current Architecture Decision

### Phase-1 runtime decision
**Chosen:** simple Python orchestration script

### Phase-1 state decision
**Chosen:** markdown + JSON sidecars

### Phase-1 WCS worker truth
**Chosen:** semi-manual Cursor worker with Jarvis-generated task packets

### First proof-of-work sequence
1. planning loop
2. mock worker loop
3. semi-manual WCS packet through Cursor
4. Playwright QA verification
5. logging and escalation handling

### Deferred items
- LangGraph
- project leads
- fully automated coding worker
- fully autonomous research loops
- voice layer
- machine maintenance worker

---

## 6. Phase-1 Architecture

```text
User
  ↓
Jarvis (python foreman)
  ↓
State files (.md + .json)
  ↓
Task packet
  ↓
Semi-manual WCS worker (Cursor)
  ↓
QA worker (Playwright)
  ↓
Run log / project status / escalation record
```

### Initial active components

- **Jarvis planner/orchestrator**
- **WCS task packet flow**
- **WCS semi-manual Cursor worker**
- **WCS QA worker**
- **truth-mapping scripts**
- **logging + escalation flow**

### Workers deferred but recognized

- **Research Scout**
- **n8n content worker**
- **n8n QA worker**
- **machine maintenance worker**
- **topic research worker**

---

## 7. Worker Model

Each worker must have:

- a defined purpose
- a defined input packet
- an approved scope
- a known output contract
- a verification path
- escalation rules

Every worker contract must answer:

1. What can it touch?
2. What tasks can it accept?
3. What file or process starts it?
4. What output JSON does it return?
5. What does success look like?
6. What causes immediate escalation?

---

## 8. Initial Worker Definitions

### 8.1 WCS Semi-Manual Cursor Worker

**Purpose:** Implement bounded WCS code changes.

**Reality in Phase 1:** Jarvis prepares the packet. A human opens Cursor and executes the task using the packet.

**Why this is correct now:** It is honest, cheap, and buildable this week. Fully automated coding can come later if the packet interface proves stable.

**Allowed tasks:**
- broken UI fixes
- small styling cleanup
- small completion tasks
- minor refactors
- small wiring repairs

**Not allowed:**
- broad redesigns
- multi-page rewrites
- database migrations without explicit approval
- large dependency changes
- repo-wide refactors

**Required outputs:**
- worker result JSON
- changed files list
- short implementation summary
- blocker notes if applicable

---

### 8.2 WCS QA Worker

**Purpose:** Verify that WCS changes actually work.

**Execution path:** Playwright

**Checks may include:**
- route loads
- target elements exist
- target interaction works
- screenshot or layout check where needed
- regression notes

**Required outputs:**
- QA result JSON
- pass/fail status
- evidence location
- issue notes
- retest recommendation

---

### 8.3 n8n Content Worker (recognized, not phase-1 active)

**Purpose:** Improve the n8n content-generation system.

**Current status:** Deferred until the quality rubric is machine-checkable.

**Reason for deferral:** “Better content” is too subjective unless reduced to a measurable rubric.

**Activation requirement:**
- clear output schema
- measurable scoring rubric
- known regression checks
- sample test set

---

### 8.4 Research Scout (recognized, not phase-1 active)

**Purpose:** Investigate errors, docs, and implementation options without editing production code.

**Current status:** Deferred until the planning loop and WCS loop are proven.

---

## 9. Task Packet Requirements

Every task packet must include:

- task ID
- project
- worker type
- title
- problem statement
- desired outcome
- suspected files or scope
- acceptance criteria
- QA method
- risk level
- system impact
- stop conditions
- status
- created timestamp

### Example WCS task shape

- **Task ID:** WCS-021
- **Project:** WCS
- **Worker:** wcs-cursor-worker
- **Title:** Fix mobile navbar overlap on home page
- **Problem:** menu overlays hero text at small widths
- **Goal:** navbar collapses without blocking hero
- **Scope:** navbar component and related styles only
- **Acceptance Criteria:** no overlap at mobile width; menu opens and closes correctly
- **QA Method:** Playwright locator + screenshot check
- **Risk:** Low
- **System Impact:** UI only; no auth, DB, or payment impact
- **Stop Conditions:** if fix requires route redesign or large layout rewrite

---

## 10. State Model

### Human-readable state
Markdown files remain the operator-facing source of truth.

### Machine-readable sidecars
JSON sidecars make planning, routing, logging, and QA reliable.

### Phase-1 rule
No critical automation decision may depend only on free-form markdown prose.

---

## 11. Core Files

### Required markdown files

- `MASTER_BACKLOG.md`
- `DAILY_PLAN.md`
- `RUN_LOG.md`
- `PROJECT_STATUS_WCS.md`
- `PROJECT_STATUS_N8N.md`
- `ESCALATIONS.md`
- `OPERATING_RULES.md`
- `AGENT_REGISTRY.md`

### Required JSON files

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Required task folders

- `tasks/open/`
- `tasks/in_progress/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/escalated/`

### Required template folders

- `templates/task_packets/`
- `templates/results/`
- `templates/qa/`

---

## 12. Minimal Phase-1 Scripts

### Must exist in phase 1

1. `jarvis.py`
   - loads backlog and project status
   - chooses next task
   - writes task packet
   - writes daily plan entry
   - appends run log entry

2. `truth_map_wcs.py`
   - scans WCS repo
   - records structure and obvious status signals
   - updates project status files

3. `seed_backlog_wcs.py`
   - creates initial bounded WCS backlog items

4. `record_worker_result.py`
   - ingests worker result JSON
   - updates task state

5. `run_wcs_qa.py`
   - triggers Playwright verification
   - writes QA result JSON

6. `escalate_task.py`
   - records failure or human-intervention need

### Nice to have later

- `truth_map_n8n.py`
- `daily_summary.py`
- `cost_report.py`
- `health_check.py`

---

## 13. Failure and Escalation Policy

### Phase-1 limits

- **Max planned tasks per cycle:** 1
- **Max WCS tasks per day:** 1 initially
- **Planning timeout:** 90 seconds
- **QA timeout:** 300 seconds
- **Automatic retries for transient parsing issues:** 1
- **Automatic retries for failed QA:** 0
- **Consecutive escalations before pausing the system:** 2

### Immediate escalation conditions

- malformed worker result JSON
- missing required task fields
- required target files not found
- QA hard fail
- task exceeds allowed scope
- task affects unexpected high-risk areas
- operator clarification required

### Phase-1 pause rule

If 2 consecutive active tasks escalate or fail verification, the system pauses new execution and writes a pause note to `ESCALATIONS.md` and `escalations.json`.

---

## 14. Verification Model

### Verification rule
Anything recorded as complete must have evidence.

### WCS evidence examples
- Playwright pass/fail
- screenshot file path
- route check result
- relevant notes

### n8n rule for later activation
n8n work cannot be promoted to “completed” until the rubric is machine-checkable.

---

## 15. Scheduling Strategy

Scheduling is **not** the first proof.

Phase 1 proves the loop manually.

Scheduling becomes active only after:

- planning loop is stable
- task packet contract is stable
- WCS QA flow is stable
- escalation logic is stable

When scheduling is introduced, it should start with:

- 1 daytime cycle
- 1 task max
- no overlapping runs

---

## 16. Voice Strategy

Voice is explicitly deferred.

### Why
Voice is a UX layer, not the core operating problem.

### Later design
- speech-to-text in
- Jarvis reads logs and status
- Jarvis responds in text
- text-to-speech reads summary aloud

This is phase-later work only.

---

## 17. Success Criteria

Phase 1 is successful when the following loop works cleanly:

1. backlog item exists
2. Jarvis selects it
3. Jarvis writes a valid task packet
4. human executes the packet in Cursor
5. worker result is recorded
6. Playwright QA runs
7. task is marked done or escalated
8. project status and run log update correctly

If this loop does not work, the system is not ready for more workers.

---

## 18. Future Expansion

Future workers can be added if they provide:

- a bounded purpose
- a strict input packet
- a strict output contract
- a known QA path
- escalation rules
- low-risk activation plan

Likely future workers:

- research scout for debugging
- research scout for content/topic gathering
- n8n workflow/content improver
- local machine maintenance worker
- voice interaction layer

Deferred future options to keep parked cleanly:
- **LiveKit** is the leading future candidate for a voice transport / realtime voice interface layer, not Jarvis's brain and not a replacement for Jarvis core planning, orchestration, state, or execution flow. Voice remains deferred for the current phase.
- **LibreCrawl** is a future optional crawl-audit companion for bounded supporting evidence such as broken links, crawl coverage, metadata issues, content/asset discovery, and broad regression scanning. It does not replace Playwright and must not decide task completion by itself.

Expansion happens only after the phase-1 loop is stable.

---

## 19. Final Product Position

This system is not an AI toy.

It is a **development operations layer** that coordinates work across real projects with visible state, bounded tasks, and independent verification.

The product does not win by sounding intelligent.

It wins by making boring, trustworthy progress.
````

### JARVIS_SYSTEM_DOCUMENTATION_v3.md

- Exact path: `C:\dev\jarvis-workspace\JARVIS_SYSTEM_DOCUMENTATION_v3.md`
- Status: legacy
- Short purpose: Detailed architecture and operating documentation
- Note: Legacy design-era master documentation baseline still kept for planning context; not the primary live operating truth.

````md
# JARVIS Multi-Agent Development System
## Master Documentation

**Version:** v3.0  
**Date:** March 9, 2026  
**Last updated:** 2026-03-14  
**Last reviewed:** 2026-03-14  
**Status:** Operating documentation for the rebuild; design-era baseline. For **current live hardened loop** (validation gates, stamping, reconcile, post-reconcile validation), see **JARVIS_LIVE_HANDOFF_BUNDLE.md** and **JARVIS_SCRIPT_PROCESS_REFERENCE.md**.  
**Audience:** Operator / developer / future maintainer

---

## Table of Contents

1. Purpose
2. What Jarvis Is
3. What Jarvis Is Not
4. Current Build Decision
5. Operating Philosophy
6. Phase-1 Architecture
7. Workspace Layout
8. Core Files
9. JSON Sidecars
10. Task Packet Standard
11. Truth Mapping
12. WCS Operating Flow
13. QA Operating Flow
14. n8n Status
15. Failure Handling
16. Cost Controls
17. Scheduling Rules
18. Future Modules
19. Build Order
20. Glossary

---

## 1. Purpose

This document explains how the rebuilt Jarvis system is supposed to work **right now**, not as a fantasy future version.

It exists to answer:

- what the system is
- how phase 1 really works
- what files matter
- what the first proof loop is
- what is intentionally deferred
- how to add future workers without wrecking the core

---

## 2. What Jarvis Is

Jarvis is a **small local orchestration layer**.

In phase 1, Jarvis is a **Python foreman script** that reads file-based state, chooses the next bounded task, writes a task packet, records progress, and enforces escalation rules.

Jarvis owns:

- planning
- task selection
- task packet generation
- logging
- state updates
- escalation decisions

Jarvis does **not** own:

- making big code changes itself
- verifying its own work
- broad repo roaming
- unsupervised multi-task execution
- fake “autonomous company” behavior

---

## 3. What Jarvis Is Not

Jarvis is not:

- a full coding agent in phase 1
- a LangGraph deployment in phase 1
- a voice assistant in phase 1
- a general machine-admin bot in phase 1
- a replacement for your judgment
- an excuse to skip verification

If the system cannot perform one boring loop reliably, it is not ready for any glamorous features.

---

## 4. Current Build Decision

### Hard choices already made

| Area | Current decision |
|---|---|
| Runtime | Simple Python script |
| State model | Markdown + JSON sidecars |
| WCS builder | Semi-manual Cursor workflow |
| WCS QA | Playwright |
| n8n worker | Deferred until rubric is machine-checkable |
| LangGraph | Deferred |
| Voice | Deferred |
| Scheduling | Deferred until manual loop is stable |
| Project leads | Deferred |

### Why this is correct

Because it is buildable, debuggable, cheap, and honest.

Anything more ambitious at this stage is ceremony.

---

## 5. Operating Philosophy

### The five rules

1. **One task at a time**
2. **No vague missions**
3. **No self-certified success**
4. **Visible state beats hidden context**
5. **Cheap boring progress beats expensive agent theater**

### Translation into practice

That means:

- one active task packet per cycle
- clear acceptance criteria
- JSON outputs where machines need certainty
- markdown where humans need readability
- no launching new workers just because it sounds cool

---

## 6. Phase-1 Architecture

```text
workspace-jarvis/
  ├─ brain/
  │   ├─ markdown state
  │   └─ json sidecars
  ├─ tasks/
  │   ├─ open
  │   ├─ in_progress
  │   ├─ done
  │   ├─ failed
  │   └─ escalated
  ├─ scripts/
  │   ├─ jarvis.py
  │   ├─ truth_map_wcs.py
  │   ├─ seed_backlog_wcs.py
  │   ├─ record_worker_result.py
  │   ├─ run_wcs_qa.py
  │   └─ escalate_task.py
  ├─ templates/
  ├─ reports/
  └─ qa/
```

### Runtime picture

```text
backlog + status files
        ↓
      jarvis.py
        ↓
   task packet written
        ↓
 human executes in Cursor
        ↓
 worker result captured
        ↓
 Playwright QA runs
        ↓
 done / failed / escalated
        ↓
 logs + status updated
```

This is the first real operating loop.

---

## 7. Workspace Layout

Recommended top-level layout:

```text
workspace-jarvis/
  brain/
    MASTER_BACKLOG.md
    DAILY_PLAN.md
    RUN_LOG.md
    PROJECT_STATUS_WCS.md
    PROJECT_STATUS_N8N.md
    ESCALATIONS.md
    AGENT_REGISTRY.md
    OPERATING_RULES.md
    master_backlog.json
    daily_plan.json
    run_log.json
    project_status_wcs.json
    project_status_n8n.json
    escalations.json

  tasks/
    open/
    in_progress/
    done/
    failed/
    escalated/

  templates/
    task_packet.template.json
    worker_result.template.json
    qa_result.template.json
    escalation_record.template.json

  scripts/
    jarvis.py
    truth_map_wcs.py
    seed_backlog_wcs.py
    record_worker_result.py
    run_wcs_qa.py
    escalate_task.py

  qa/
    playwright/
      tests/
      screenshots/
      reports/

  reports/
    daily/
    qa/
    truth_maps/
```

---

## 8. Core Files

### Markdown state files

#### `MASTER_BACKLOG.md`
Human-readable backlog view.
Should group WCS backlog by:

- Broken
- Ugly
- Incomplete
- Optimization

Phase 1 should only pull from:

- Broken
- Ugly

#### `DAILY_PLAN.md`
Shows the current selected task and why it was chosen.

#### `RUN_LOG.md`
Append-only human-readable log of runs, task selection, outcomes, and escalation notes.

#### `PROJECT_STATUS_WCS.md`
Repo truth snapshot, major areas, known risks, recent changes, and current confidence.

#### `PROJECT_STATUS_N8N.md`
Current known facts only. This project remains partially deferred until its quality rubric is formalized.

#### `ESCALATIONS.md`
Human-readable record of failures, pauses, operator intervention needs, and unresolved blockers.

### JSON sidecars

The JSON files mirror the operational parts of the markdown files and should be treated as the machine-facing contract.

---

## 9. JSON Sidecars

### Why sidecars exist

Markdown is good for people.  
JSON is good for scripts.

Using both avoids two bad outcomes:

- unreadable state hidden in a database too early
- brittle automation trying to scrape loose prose only

### Required sidecars

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Rule

Any field that affects routing, verification, escalation, or status transitions must exist in JSON.

---

## 10. Task Packet Standard

### Minimum packet fields

Every task packet must contain:

- `task_id`
- `project`
- `worker`
- `title`
- `problem`
- `goal`
- `scope`
- `suspected_files`
- `acceptance_criteria`
- `qa_method`
- `risk_level`
- `system_impact`
- `stop_conditions`
- `status`
- `created_at`

### Example packet shape

```json
{
  "task_id": "WCS-021",
  "project": "WCS",
  "worker": "wcs-cursor-worker",
  "title": "Fix mobile navbar overlap on home page",
  "problem": "Menu overlaps hero copy at small widths",
  "goal": "Navbar collapses cleanly without blocking hero content",
  "scope": "Navbar component and related mobile styles only",
  "suspected_files": [
    "components/navbar.tsx",
    "app/page.tsx",
    "app/globals.css"
  ],
  "acceptance_criteria": [
    "No overlap at mobile width",
    "Menu opens and closes correctly",
    "Hero content remains visible"
  ],
  "qa_method": "Playwright locator + screenshot",
  "risk_level": "low",
  "system_impact": "UI only; no auth, payment, or database changes expected",
  "stop_conditions": [
    "Requires route redesign",
    "Touches unrelated pages",
    "Needs new dependency"
  ],
  "status": "ready",
  "created_at": "2026-03-09T00:00:00"
}
```

---

## 11. Truth Mapping

### What truth mapping is

Truth mapping is the first discipline step before broad automation.

It means:

- scan the repo
- record structure
- identify likely app entry points
- capture scripts/configs
- note obvious risk areas
- update project status files with facts, not guesses

### WCS truth mapping should capture

- top-level folders
- framework indicators
- package scripts
- routing structure
- component structure
- key config files
- current test status if known
- likely fragile areas
- excluded areas if any

### Truth mapping outputs

- markdown summary in `PROJECT_STATUS_WCS.md`
- JSON summary in `project_status_wcs.json`
- optional report under `reports/truth_maps/`

### What truth mapping should not do

- invent architecture
- rewrite code
- mark tasks done
- make quality claims without evidence

---

## 12. WCS Operating Flow

### Phase-1 real flow

1. backlog is seeded
2. truth mapping is performed
3. `jarvis.py` selects the top bounded WCS task
4. Jarvis writes:
   - `DAILY_PLAN.md`
   - `daily_plan.json`
   - task packet file
5. operator opens Cursor and executes the packet
6. worker result is recorded
7. Playwright QA runs
8. task becomes:
   - done
   - failed
   - escalated
9. logs and project status update

### Why semi-manual is correct

Because you already use Cursor, already pay for it, and can get real value without pretending the interface is mature enough for unattended coding.

This is honest progress, not fake autonomy.

---

## 13. QA Operating Flow

### QA inputs

- task packet
- changed files summary
- acceptance criteria
- target route or test target

### QA outputs

- `qa_result.json`
- pass/fail
- evidence path
- issue notes
- retest recommendation

### QA rules

- builder confidence does not matter if QA fails
- failed QA does not auto-retry the code change in phase 1
- QA hard fail triggers escalation
- evidence must be written before a task can be marked complete

### WCS QA examples

- page loads
- button exists
- modal opens
- navigation works
- screenshot looks acceptable
- no overlap / visibility regression

---

## 14. n8n Status

The n8n project is important but under-defined for automation.

### Current decision

n8n remains **recognized but deferred** until the quality rubric is machine-checkable.

### Why

Because “better content” is not enough.  
The system needs measurable checks such as:

- required blocks present
- schema valid
- output length within bounds
- score against a known rubric
- banned failures absent

### Until then

n8n can still exist in the backlog and status files, but it should not be treated as a phase-1 autonomous worker path.

---

## 15. Failure Handling

### Failure types

- malformed JSON output
- missing required packet fields
- missing target files
- QA hard fail
- task exceeds scope
- unclear system impact
- operator input required

### Phase-1 numeric policy

| Policy item | Value |
|---|---|
| Planned tasks per cycle | 1 |
| WCS tasks per day | 1 |
| Planning timeout | 90 sec |
| QA timeout | 300 sec |
| Parse retry | 1 |
| QA auto-retry | 0 |
| Consecutive escalations before pause | 2 |

### Pause rule

Two consecutive escalated or failed active tasks pause further execution until reviewed.

### Escalation record should include

- task ID
- time
- reason
- evidence
- recommended next action
- pause flag

---

## 16. Cost Controls

Cost discipline must be operational, not rhetorical.

### Phase-1 cost rules

- use one LLM decision call per planning cycle where possible
- do not run multiple workers per cycle
- avoid premium model usage for low-value file shuffling
- log model usage if available
- keep phase 1 manual enough to avoid runaway tool churn

### Why this matters

If a project cannot stay understandable and cheap at low scale, it has no business pretending it will scale.

---

## 17. Scheduling Rules

Scheduling is deferred until the manual loop feels trustworthy.

### Scheduling activation requirements

- valid task packets produced consistently
- worker result flow stable
- WCS QA stable
- escalation handling proven
- no silent state corruption

### First scheduled configuration

- one cycle at a fixed time
- one task max
- no overlapping runs
- pause honored automatically

---

## 18. Future Modules

Future workers are allowed, but only if each new worker defines:

- purpose
- scope
- input packet
- output JSON
- QA path
- escalation rules
- activation conditions

### Likely future modules

- error/issues research scout
- X.com content topic researcher
- n8n content improver
- local machine maintenance worker
- voice interface layer

### Deferred interface and audit options

**LiveKit:** leading future candidate for a voice transport / realtime voice interface layer. If used later, it sits around Jarvis, not in place of Jarvis: speech-to-text -> intent/router -> Jarvis command adapter -> Jarvis core -> text-to-speech. Voice remains deferred in the current phase, and any early support should start with read-only / low-risk commands such as "what's next", "summarize status", "read escalations", and "read today's plan".

**LibreCrawl:** future optional crawl-audit companion for broad supporting checks such as broken links, crawl coverage, metadata issues, content/asset discovery, and broader regression scanning. It does not replace Playwright, and it must feed QA/review evidence rather than decide task completion by itself. No noisy low-value alert spam.

### Expansion rule

Do not add a new worker to compensate for a broken core.

Fix the core first.

---

## 19. Build Order

### The realistic sequence

#### Days 1–2
- create workspace structure
- create markdown files
- create JSON sidecars
- build `jarvis.py` planning loop
- build WCS truth mapping

#### Day 3
- create task packet templates
- create worker result template
- create QA result template
- test mock worker loop

#### Days 4–5
- run one semi-manual WCS task through Cursor
- capture result
- record changed files and notes

#### Days 6–7
- run Playwright QA
- test done/fail/escalate transitions
- update logs and status correctly

### Anything beyond this in week 1 is greed

No voice.  
No LangGraph.  
No extra workers.  
No scheduling hype.

---

## 20. Glossary

### Jarvis
The orchestrator / foreman script.

### Task packet
The bounded machine-readable work order.

### Truth mapping
The fact-gathering repo scan that grounds project state.

### Worker
A narrow executor with known scope and outputs.

### QA worker
The verification layer that checks work independently.

### Sidecar
A JSON file paired with a markdown file for machine-readable state.

### Escalation
A recorded failure, blocker, or operator-intervention event.

### System impact
A statement about what areas a task could affect and why that matters.
````

## 7. Current File/Artifact Discovery Notes

- Real task packets are currently stored under `tasks/` using the naming pattern `WCS-XXX_task.json` and `WCS-XXX_task.md`.
- Worker result artifacts are currently stored under `results/` using the naming pattern `WCS-XXX_worker_result.json`.
- QA result artifacts are currently stored under `qa/` using the naming pattern `WCS-XXX_qa_result.json`.
- Cursor handoff files are currently stored under `scratch/cursor_handoffs/` using the naming pattern `WCS-XXX_cursor_handoff.md`.
- Task cycle summary files are currently stored under `scratch/task_cycle_summaries/` using the naming pattern `WCS-XXX_task_cycle_summary.md`.
- Current live examples in this bundle use the latest `WCS-043` artifacts because they are the most recent complete reconciled proof set in the workspace.
- Important drift visible from current files: `state/file_registry.json` still points some v3 planning docs at `C:\dev\jarvis-workspace\docs\...` paths while the live files currently exist at the workspace root; Pathfinder planning should trust the actual existing files included in this bundle over those stale path strings.
- Important drift visible from current implementation vs older docs: some v3 planning docs are intentionally design-era baselines, while `JARVIS_LIVE_HANDOFF_BUNDLE.md`, `JARVIS_SCRIPT_PROCESS_REFERENCE.md`, and the live scripts reflect the actual current loop.
- Another notable live truth: reconcile now syncs existing task packet artifacts to terminal status, so task packet examples may show a terminal status such as `done` instead of staying frozen at generation-time `ready`.
- No dedicated current `AGENT_REGISTRY.md` file exists in the workspace even though some planning-era docs still refer to it as a desired state surface.

## 8. Pathfinder Prep Relevance Notes

- Most relevant files for designing Pathfinder packet/result contracts: `scripts/generate_task_packet.py`, `scripts/draft_worker_result_from_evidence.py`, `scripts/draft_qa_result_from_evidence.py`, `scripts/worker_result_validate.py`, `scripts/qa_result_validate.py`, `scripts/reconcile_task_outcome.py`, the JSON templates in `templates/`, and the real `WCS-043` task/worker/QA artifacts.
- Most relevant files for designing Pathfinder QA rules: `scripts/draft_qa_result_from_evidence.py`, `scripts/qa_result_validate.py`, `scripts/qa_failure_triage.py`, `scripts/stamp_guard_check.py`, `scripts/pre_reconcile_check.py`, and the real `WCS-043` QA artifact plus cycle summary.
- Files that suggest naming/structure conventions Pathfinder should follow: `state/file_registry.json`, `state/FILE_REGISTRY.md`, `scripts/build_cursor_handoff.py`, `scripts/build_task_cycle_summary.py`, the `templates/` directory, and the current `WCS-043` artifact naming pattern across `tasks/`, `results/`, `qa/`, and `scratch/`.
- Obvious gaps Pathfinder prep docs will need to account for: some contracts are implied by validators and examples rather than a single canonical schema file; there is no current `AGENT_REGISTRY.md`; some planning-era docs still lag behind live implementation details; and file-registry path entries for several v3 docs currently drift from their real on-disk locations.
