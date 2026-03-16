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
    parser.add_argument(
        "--require-auditable-delta",
        action="store_true",
        help=(
            "After a successful launch attempt, require an immediate auditable "
            "working-tree delta on the expected branch and fail if changed files "
            "are missing or outside task scope."
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


def parse_worktree_changed_files(status_output: str) -> List[str]:
    changed: List[str] = []
    seen: set[str] = set()

    for raw_line in status_output.splitlines():
        if not raw_line.strip() or len(raw_line) < 4:
            continue

        path_text = raw_line[3:].strip()
        candidates = [path_text]
        if " -> " in path_text:
            old_path, new_path = path_text.split(" -> ", 1)
            candidates = [old_path, new_path]

        for candidate in candidates:
            normalized = candidate.strip().strip('"')
            if normalized and normalized not in seen:
                seen.add(normalized)
                changed.append(normalized)

    return changed


def path_in_scope(path: str, expected_scope: List[str]) -> bool:
    normalized = path.replace("\\", "/")
    for scope_item in expected_scope:
        scoped = scope_item.replace("\\", "/").rstrip("/")
        if normalized == scoped or normalized.startswith(f"{scoped}/"):
            return True
    return False


def audit_post_launch(
    repo_path: Path,
    expected_branch: str,
    packet: dict[str, Any],
) -> Tuple[Optional[str], List[str], List[str], List[str]]:
    failures: List[str] = []

    branch_code, branch_output = run_git(repo_path, ["branch", "--show-current"])
    branch_after = branch_output.strip() if branch_code == 0 and branch_output.strip() else None
    if branch_after is None:
        failures.append("Unable to determine current branch after launch.")
    elif branch_after != expected_branch:
        failures.append(
            f"Branch drift detected after launch. Expected {expected_branch}, got {branch_after}."
        )

    status_code, status_output = run_git(repo_path, ["status", "--porcelain", "--untracked-files=all"])
    changed_files = parse_worktree_changed_files(status_output) if status_code == 0 else []
    if status_code != 0:
        failures.append("Unable to inspect working tree after launch.")
    elif not changed_files:
        failures.append("No auditable working-tree delta detected after launch.")

    expected_scope = derive_expected_scope(packet)
    if not expected_scope:
        failures.append("Unable to derive expected file scope from task packet for strict audit.")
    elif changed_files:
        out_of_scope = [path for path in changed_files if not path_in_scope(path, expected_scope)]
        if out_of_scope:
            failures.append("Changed files fell outside task scope: " + ", ".join(out_of_scope))

    return branch_after, changed_files, expected_scope, failures


def print_changed_files(changed_files: List[str]) -> None:
    print("Changed files detected:")
    if changed_files:
        for path in changed_files:
            print(f"- {path}")
    else:
        print("- (none)")


def print_strict_audit_result(
    *,
    branch_after: Optional[str],
    changed_files: List[str],
    expected_scope: List[str],
    failures: List[str],
) -> None:
    print(f"Branch after launch: {branch_after if branch_after else '(unable to resolve)'}")
    print(
        "Expected file scope: "
        + (", ".join(expected_scope) if expected_scope else "(unable to derive)")
    )
    print_changed_files(changed_files)
    in_scope = not any("outside task scope" in failure for failure in failures)
    print(f"In scope: {'yes' if in_scope else 'no'}")
    if failures:
        print("Audit failures:")
        for failure in failures:
            print(f"- {failure}")


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
            packet=packet,
            require_auditable_delta=args.require_auditable_delta,
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
            packet=packet,
            require_auditable_delta=args.require_auditable_delta,
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
    packet: dict[str, Any],
    require_auditable_delta: bool,
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
    if require_auditable_delta:
        branch_after, changed_files, expected_scope, failures = audit_post_launch(
            repo_path=repo_path,
            expected_branch=expected_branch,
            packet=packet,
        )
        if failures:
            print("RUN CURSOR WORKER: FAIL")
            print(f"Task: {task_id}")
            print(f"Jarvis workspace: {workspace}")
            print(f"Task repo workspace: {repo_path}")
            print(f"Handoff path: {handoff_path}")
            print("Cursor execution: Real Agent CLI attempted (exited 0).")
            print("Reason: Strict post-launch audit failed.")
            print_strict_audit_result(
                branch_after=branch_after,
                changed_files=changed_files,
                expected_scope=expected_scope,
                failures=failures,
            )
            print("Worker result: not written (launch was attempted, but immediate repo state is not trustworthy enough to treat as an auditable operator surface).")
            return 1
    print("RUN CURSOR WORKER: PASS")
    print(f"Task: {task_id}")
    print(f"Jarvis workspace: {workspace}")
    print(f"Task repo workspace: {repo_path}")
    print(f"Handoff path: {handoff_path}")
    print("Cursor execution: Real Agent CLI attempted (exited 0).")
    if require_auditable_delta:
        branch_after, changed_files, expected_scope, failures = audit_post_launch(
            repo_path=repo_path,
            expected_branch=expected_branch,
            packet=packet,
        )
        print("Post-launch audit: PASS")
        print_strict_audit_result(
            branch_after=branch_after,
            changed_files=changed_files,
            expected_scope=expected_scope,
            failures=failures,
        )
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
    packet: dict[str, Any],
    require_auditable_delta: bool,
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
    if require_auditable_delta:
        branch_after, changed_files, expected_scope, failures = audit_post_launch(
            repo_path=repo_path,
            expected_branch=expected_branch,
            packet=packet,
        )
        if failures:
            print("RUN CURSOR WORKER: FAIL")
            print(f"Task: {task_id}")
            print(f"Jarvis workspace: {workspace}")
            print(f"Task repo workspace: {repo_path}")
            print(f"Handoff path: {handoff_path}")
            print("Cursor execution: Desktop launcher fallback attempted (exited 0).")
            print("Reason: Strict post-launch audit failed.")
            print_strict_audit_result(
                branch_after=branch_after,
                changed_files=changed_files,
                expected_scope=expected_scope,
                failures=failures,
            )
            print("Worker result: not written (launch was attempted, but immediate repo state is not trustworthy enough to treat as an auditable operator surface).")
            return 1
    print("RUN CURSOR WORKER: PASS")
    print(f"Task: {task_id}")
    print(f"Jarvis workspace: {workspace}")
    print(f"Task repo workspace: {repo_path}")
    print(f"Handoff path: {handoff_path}")
    print("Cursor execution: Desktop launcher fallback attempted (exited 0).")
    if require_auditable_delta:
        branch_after, changed_files, expected_scope, failures = audit_post_launch(
            repo_path=repo_path,
            expected_branch=expected_branch,
            packet=packet,
        )
        print("Post-launch audit: PASS")
        print_strict_audit_result(
            branch_after=branch_after,
            changed_files=changed_files,
            expected_scope=expected_scope,
            failures=failures,
        )
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
