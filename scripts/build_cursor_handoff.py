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

    content = f"""# Implementation task: {task_id}

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

    impl_instruction = packet.get("implementation_instruction")
    concrete_action = impl_instruction if impl_instruction else title
    content += """
---

## Cursor implementation prompt

**Concrete action:** """ + concrete_action + """

Implement this task in a bounded way. You must make at least one code edit in the scoped file(s); do not complete without modifying the file unless a stop condition applies.

**Task:** """ + task_id + """

**Source of truth:**
- This task brief and the repo code
- Current repo state and existing code patterns in the WCS repo

**Rules:**
- Do only the assigned task; do not broaden scope.
- Do not refactor unrelated files.
- Preserve current architecture unless the task explicitly requires otherwise.
- Edit ONLY the file(s) listed in Expected file scope above. Do NOT create any new files.
- Do NOT create docs/, HANDOFF_*.md, or any documentation or summary file in the repo. Any file outside the scope will fail the audit.
- Do not claim QA was run unless it was actually run; do not fabricate status or evidence.

**Required output (in your response only; do not create files):**
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
