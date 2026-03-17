"""
Thin operator-facing wrapper for a single bounded WCS task cycle.

This reduces operator glue for one task only by delegating to existing live
helpers. It does not create commits, run QA automatically, or fabricate task
completion.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Optional, Sequence, Tuple


class OneTaskCycleError(Exception):
    pass


def normalize_task_id(raw: str) -> str:
    task_id = raw.strip().upper()
    if not re.match(r"^WCS-\d+$", task_id):
        raise ValueError(f"Task id must match WCS-NNN. Got: {raw!r}")
    return task_id


def positive_int(raw: str) -> int:
    value = int(raw)
    if value < 1:
        raise argparse.ArgumentTypeError("Value must be a positive integer.")
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the current live prep path for exactly one bounded WCS task, "
            "then print operator next actions. Delegates to existing helpers."
        )
    )
    task_group = parser.add_mutually_exclusive_group(required=True)
    task_group.add_argument("--task", help="Task id, e.g. WCS-041")
    task_group.add_argument(
        "--select-ready",
        action="store_true",
        help="Select exactly one eligible ready WCS task via select_next_ready_task.py.",
    )
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--launch-cursor",
        action="store_true",
        help=(
            "After successful prep, delegate to strict Cursor launch via "
            "run_wcs_operator_entrypoint.py prep --launch-cursor."
        ),
    )
    parser.add_argument(
        "--agent-timeout-seconds",
        type=positive_int,
        metavar="SECONDS",
        help=(
            "Optional passthrough for the real Agent CLI timeout. "
            "Used only with --launch-cursor."
        ),
    )
    parser.add_argument(
        "--agent-model",
        metavar="MODEL",
        help=(
            "Optional passthrough for the real Agent CLI model (e.g. composer-1.5). "
            "Used only with --launch-cursor."
        ),
    )
    return parser.parse_args()


def workspace_from_args(raw_workspace: str | None) -> Path:
    if raw_workspace:
        return Path(raw_workspace).resolve()
    return Path(__file__).resolve().parent.parent


def ensure_workspace_exists(workspace: Path) -> None:
    if not workspace.exists():
        raise OneTaskCycleError(f"Workspace path does not exist: {workspace}")


def run_helper(cmd: Sequence[str], cwd: Path) -> Tuple[int, str]:
    proc = subprocess.run(
        list(cmd),
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = ""
    if proc.stdout:
        output += proc.stdout
    if proc.stderr:
        if output:
            output += "\n"
        output += proc.stderr
    return proc.returncode, output.rstrip()


def print_helper_result(cmd: Sequence[str], output: str) -> None:
    print(f"Running helper command: {' '.join(cmd)}")
    if output:
        print("--- helper output begin ---")
        print(output)
        print("--- helper output end ---")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def derive_expected_scope(packet: dict[str, Any]) -> List[str]:
    suspected = packet.get("suspected_files")
    if isinstance(suspected, list) and suspected:
        return [normalize_text(item) for item in suspected if normalize_text(item)]

    target_files = packet.get("target_files")
    if isinstance(target_files, list) and target_files:
        return [normalize_text(item) for item in target_files if normalize_text(item)]

    for key in ("target_file", "file_path", "file"):
        value = normalize_text(packet.get(key))
        if value:
            return [value]

    notes = normalize_text(packet.get("notes"))
    if notes and (
        "/" in notes
        or notes.endswith(".tsx")
        or notes.endswith(".ts")
        or notes.endswith(".jsx")
        or notes.endswith(".js")
    ):
        return [notes]

    return []


def shell_join_paths(paths: List[str]) -> str:
    if not paths:
        return '"(expected file scope unavailable from task packet)"'
    return " ".join(f'"{path}"' for path in paths)


def select_task_via_helper(workspace: Path) -> Tuple[Optional[str], int, str]:
    scripts_dir = workspace / "scripts"
    cmd = [
        sys.executable,
        str(scripts_dir / "select_next_ready_task.py"),
        "--workspace",
        str(workspace),
        "--project",
        "WCS",
    ]
    code, output = run_helper(cmd, workspace)
    task_id = None
    if code == 0:
        for line in output.splitlines():
            stripped = line.strip()
            if stripped.startswith("Selected task id:"):
                task_id = stripped.split(":", 1)[1].strip().upper()
                break
    return task_id, code, output


def build_prep_command(
    workspace: Path,
    task_id: str,
    launch_cursor: bool,
    agent_timeout_seconds: Optional[int],
    agent_model: Optional[str] = None,
) -> List[str]:
    scripts_dir = workspace / "scripts"
    cmd = [
        sys.executable,
        str(scripts_dir / "run_wcs_operator_entrypoint.py"),
        "prep",
        "--task",
        task_id,
        "--workspace",
        str(workspace),
    ]
    if launch_cursor:
        cmd.append("--launch-cursor")
        if agent_timeout_seconds is not None:
            cmd.extend(["--agent-timeout-seconds", str(agent_timeout_seconds)])
        if agent_model:
            cmd.extend(["--agent-model", agent_model])
    return cmd


def print_next_actions(
    *,
    workspace: Path,
    task_id: str,
    repo_path: Path,
    scope_paths: List[str],
    launch_cursor: bool,
) -> None:
    quoted_paths = shell_join_paths(scope_paths)
    first_scope = scope_paths[0] if scope_paths else "<expected file scope from task packet>"

    print("")
    print("RUN ONE TASK CYCLE: PASS")
    print(f"Task: {task_id}")
    print("Status: prep path completed for exactly one task.")
    if launch_cursor:
        print("Cursor launch: strict launch attempted and passed.")
    else:
        print("Cursor launch: not attempted.")
    print("Task completion: NOT COMPLETE YET")
    print("Reason: operator still verifies diff, creates commit, runs QA, and finalizes post-worker truth.")
    print("")
    print("Operator next actions:")
    print("1. Review the bounded diff.")
    print(f'   Set-Location "{repo_path}"')
    print("   git status --short --branch")
    print(f"   git diff -- {quoted_paths}")
    print("")
    print("2. Stage and commit only the intended task change after review.")
    print(f'   Set-Location "{repo_path}"')
    print(f"   git add -- {quoted_paths}")
    print(f'   git commit -m "{task_id}: concise factual message"')
    print("")
    print("3. Run QA in the WCS repo.")
    print(f'   Set-Location "{repo_path}"')
    print("   npm run build")
    print("   npm run test:e2e:smoke")
    print("")
    print("4. Manually verify the targeted change locally.")
    print(f"   Verify the bounded change in: {first_scope}")
    print("")
    print("5. Finalize the guarded post-worker path with truthful evidence.")
    print(f'   Set-Location "{workspace}"')
    print(
        f'   python "scripts/run_wcs_operator_entrypoint.py" post --task {task_id} --workspace "{workspace}" '
        '--draft-worker-result --worker-executor "cursor_operator" '
        f'--worker-command "Implemented bounded {task_id} change in {first_scope} on the task branch" '
        '--draft-qa-result --build-status pass --smoke-status pass --manual-status pass '
        f'--manual-check "Verified the targeted change locally in the browser for {task_id}."'
    )


def main() -> int:
    args = parse_args()
    workspace = workspace_from_args(args.workspace)
    try:
        ensure_workspace_exists(workspace)
    except OneTaskCycleError as e:
        print("RUN ONE TASK CYCLE: FAIL")
        print(f"Reason: {e}")
        return 1

    if args.task:
        try:
            task_id = normalize_task_id(args.task)
        except ValueError as e:
            print("RUN ONE TASK CYCLE: FAIL")
            print(f"Reason: {e}")
            return 1
        selection_mode = "explicit --task"
    else:
        task_id, code, output = select_task_via_helper(workspace)
        print_helper_result(
            [
                sys.executable,
                str(workspace / "scripts" / "select_next_ready_task.py"),
                "--workspace",
                str(workspace),
                "--project",
                "WCS",
            ],
            output,
        )
        if code != 0 or not task_id:
            print("RUN ONE TASK CYCLE: FAIL")
            print("Failed delegated step: select_next_ready_task")
            return code if code != 0 else 1
        selection_mode = "automatic --select-ready"

    prep_cmd = build_prep_command(
        workspace=workspace,
        task_id=task_id,
        launch_cursor=args.launch_cursor,
        agent_timeout_seconds=args.agent_timeout_seconds,
        agent_model=args.agent_model,
    )
    code, output = run_helper(prep_cmd, workspace)
    print_helper_result(prep_cmd, output)
    if code != 0:
        print("RUN ONE TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Selection mode: {selection_mode}")
        print("Failed delegated step: run_wcs_operator_entrypoint prep")
        return code

    packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not packet_path.is_file():
        print("RUN ONE TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Selection mode: {selection_mode}")
        print(f"Reason: Expected task packet after prep, but it is missing: {packet_path}")
        return 1

    try:
        packet = read_json(packet_path)
    except Exception as e:  # noqa: BLE001
        print("RUN ONE TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Selection mode: {selection_mode}")
        print(f"Reason: Could not read generated task packet: {e}")
        return 1

    if not isinstance(packet, dict):
        print("RUN ONE TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Selection mode: {selection_mode}")
        print("Reason: Generated task packet must be a JSON object.")
        return 1

    raw_repo = normalize_text(packet.get("repo_path"))
    if not raw_repo:
        print("RUN ONE TASK CYCLE: FAIL")
        print(f"Task: {task_id}")
        print(f"Selection mode: {selection_mode}")
        print("Reason: Task packet has no repo_path.")
        return 1
    repo_path = Path(raw_repo).resolve()
    scope_paths = derive_expected_scope(packet)

    print(f"Selection mode: {selection_mode}")
    print_next_actions(
        workspace=workspace,
        task_id=task_id,
        repo_path=repo_path,
        scope_paths=scope_paths,
        launch_cursor=args.launch_cursor,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
