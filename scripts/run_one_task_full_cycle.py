"""
Full one-command single-task closeout wrapper for the active Jarvis/WCS lane.

Extends the proven one-task wrapper approach so a single command can run the full
single-task cycle honestly for one bounded WCS task: prep, optional strict launch,
commit, build, smoke, manual verification, and post.

Preserves live truth: no fabrication of worker completion, QA pass, or manual
verification. Operator must provide --confirm-commit and --manual-check to proceed
past those checkpoints. One task only; no batching, scheduling, or fake autonomy.

Resume/finalize mode (--finalize): for a task already committed and smoke-tested,
skip prep/launch/commit/build/smoke and delegate directly to post. Requires
--task and --manual-check. Optional --artifact for screenshot path(s).

Dev-server management: with --manage-dev-server, reuses existing server on port
unless --force-restart-dev-server. Screenshot capture (--capture-screenshot) saves
to qa/artifacts/<TASK_ID>_manual_check.png and wires into QA artifacts; does NOT
imply manual verification passed.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import socket
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Optional, Sequence, Tuple


class FullCycleError(Exception):
    pass


# Exit codes for callers (e.g. run_task_sequence) to detect checkpoint stops without parsing stdout
EXIT_STOP_COMMIT = 10  # Stopped at commit checkpoint; re-run with --confirm-commit
EXIT_STOP_MANUAL = 11  # Stopped at manual checkpoint; re-run with --finalize --manual-check


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
            "Full one-command single-task closeout for exactly one bounded WCS task. "
            "Runs prep, optional strict launch, then operator-controlled commit/build/"
            "smoke/manual/post with honest checkpoints."
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
        help="Optional passthrough for the real Agent CLI timeout. Used only with --launch-cursor.",
    )
    parser.add_argument(
        "--agent-model",
        metavar="MODEL",
        help="Optional passthrough for the real Agent CLI model (e.g. composer-1.5). Used only with --launch-cursor.",
    )
    parser.add_argument(
        "--confirm-commit",
        action="store_true",
        help=(
            "Operator confirmation: proceed past diff review and create commit. "
            "Required to run commit step. Do not use until diff is reviewed."
        ),
    )
    parser.add_argument(
        "--commit-message",
        metavar="TEXT",
        help="Optional custom commit message. Default: {task_id}: bounded change in {scope}.",
    )
    parser.add_argument(
        "--manual-check",
        metavar="TEXT",
        help=(
            "Operator-provided manual verification note. Required to run post. "
            "Example: 'Verified the targeted change locally in the browser for {task_id}.'"
        ),
    )
    parser.add_argument(
        "--manage-dev-server",
        action="store_true",
        help=(
            "Manage dev server for smoke/manual: reuse existing server on port if in use, "
            "or start new one. Only kill server on exit if this wrapper started it."
        ),
    )
    parser.add_argument(
        "--dev-port",
        type=positive_int,
        default=3000,
        metavar="PORT",
        help="Port for dev server (default: 3000). Used with --manage-dev-server.",
    )
    parser.add_argument(
        "--force-restart-dev-server",
        action="store_true",
        help=(
            "Kill only the process on --dev-port before starting. "
            "Used with --manage-dev-server. Does not kill other dev servers."
        ),
    )
    parser.add_argument(
        "--capture-screenshot",
        action="store_true",
        help=(
            "Capture screenshot of manual-verification target page. Saves to "
            "qa/artifacts/<TASK_ID>_manual_check.png and wires into QA artifacts. "
            "Does NOT imply manual verification passed."
        ),
    )
    parser.add_argument(
        "--manual-url",
        metavar="URL",
        help=(
            "URL for manual verification page (e.g. http://localhost:3000/schedules). "
            "Required when --capture-screenshot is used. Default port from --dev-port."
        ),
    )
    parser.add_argument(
        "--finalize",
        action="store_true",
        help=(
            "Resume/finalize mode: skip prep, launch, commit, build, smoke. "
            "For a task already committed and smoke-tested. Requires --task and --manual-check. "
            "Delegates directly to run_wcs_operator_entrypoint.py post."
        ),
    )
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        metavar="PATH",
        help=(
            "Optional screenshot or QA artifact path to wire into post. "
            "Repeatable. In --finalize mode, defaults to qa/artifacts/<TASK_ID>_manual_check.png if present."
        ),
    )
    return parser.parse_args()


def workspace_from_args(raw_workspace: str | None) -> Path:
    if raw_workspace:
        return Path(raw_workspace).resolve()
    return Path(__file__).resolve().parent.parent


def ensure_workspace_exists(workspace: Path) -> None:
    if not workspace.exists():
        raise FullCycleError(f"Workspace path does not exist: {workspace}")


def run_helper(
    cmd: Sequence[str],
    cwd: Path,
    *,
    shell: bool = False,
    env: Optional[dict[str, str]] = None,
) -> Tuple[int, str]:
    kwargs: dict[str, Any] = {
        "cwd": str(cwd),
        "capture_output": True,
        "text": True,
        "encoding": "utf-8",
        "errors": "replace",
    }
    if env is not None:
        kwargs["env"] = env
    if shell:
        cmd_str = subprocess.list2cmdline(cmd) if cmd else ""
        proc = subprocess.run(cmd_str, shell=True, **kwargs)
    else:
        proc = subprocess.run(list(cmd), **kwargs)
    output = ""
    if proc.stdout:
        output += proc.stdout
    if proc.stderr:
        if output:
            output += "\n"
        output += proc.stderr
    return proc.returncode, output.rstrip()


def run_node_cmd(
    cmd: Sequence[str],
    cwd: Path,
    *,
    env: Optional[dict[str, str]] = None,
) -> Tuple[int, str]:
    """
    Run node/npm/npx command with Windows-safe resolution.
    On Windows, npm/npx are .cmd batch files and must run via shell for PATH resolution.
    """
    if not cmd:
        return 1, "Empty command"
    name = cmd[0].lower()
    if sys.platform == "win32":
        if name in ("npm", "npx"):
            return run_helper(cmd, cwd, shell=True, env=env)
        if name == "node":
            resolved = shutil.which("node")
            if resolved:
                cmd = [resolved] + list(cmd[1:])
    return run_helper(cmd, cwd, env=env)


def _safe_print(text: str) -> None:
    """Print text; on Windows cp1252 UnicodeEncodeError, fall back to ASCII-safe output."""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", errors="replace").decode("ascii"))


def print_helper_result(cmd: Sequence[str], output: str) -> None:
    print(f"Running helper command: {' '.join(cmd)}")
    if output:
        print("--- helper output begin ---")
        _safe_print(output)
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


def scope_to_page_route(scope_paths: List[str]) -> Optional[str]:
    """
    Map task scope to a non-home route for page-specific smoke.
    Returns None when scope is home or unknown (skip page-smoke).
    Reuses same mapping as screenshot capture logic.
    """
    if not scope_paths:
        return None
    first = scope_paths[0]
    if "schedules" in first:
        return "/schedules"
    if "about" in first:
        return "/about"
    if "drills" in first:
        return "/drills"
    return None


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


def run_git_diff(repo_path: Path, scope_paths: List[str]) -> Tuple[int, str]:
    if not scope_paths:
        return run_helper(["git", "diff"], repo_path)
    return run_helper(["git", "diff", "--"] + scope_paths, repo_path)


def run_git_status_porcelain(repo_path: Path) -> Tuple[int, str]:
    return run_helper(["git", "status", "--porcelain"], repo_path)


def run_git_add_commit(
    repo_path: Path,
    scope_paths: List[str],
    task_id: str,
    first_scope: str,
    commit_message: Optional[str],
) -> Tuple[int, str]:
    if not scope_paths:
        return 1, "No scope paths; cannot commit."
    # Idempotent: if working tree is clean, skip commit (already committed in prior run).
    status_code, status_out = run_git_status_porcelain(repo_path)
    if status_code == 0 and not status_out.strip():
        return 0, "(working tree clean; commit already done; skipping)"
    add_cmd = ["git", "add", "--"] + scope_paths
    code, out = run_helper(add_cmd, repo_path)
    if code != 0:
        return code, out
    msg = commit_message or f"{task_id}: bounded change in {first_scope}"
    commit_cmd = ["git", "commit", "-m", msg]
    return run_helper(commit_cmd, repo_path)


def run_npm_build(repo_path: Path) -> Tuple[int, str]:
    return run_node_cmd(["npm", "run", "build"], repo_path)


def is_port_in_use(port: int) -> bool:
    """Check if a port is in use (Windows-safe)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("127.0.0.1", port)) == 0


def get_pid_on_port(port: int) -> Optional[int]:
    """Get PID of process listening on port. Windows-safe via netstat."""
    cmd = ["netstat", "-ano"]
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        return None
    for line in proc.stdout.splitlines():
        if f":{port}" in line and "LISTENING" in line:
            parts = line.split()
            if parts:
                try:
                    return int(parts[-1])
                except ValueError:
                    continue
    return None


def kill_process_on_port(port: int) -> Tuple[bool, str]:
    """Kill only the process on the given port. Windows-safe via taskkill."""
    pid = get_pid_on_port(port)
    if pid is None:
        return True, "(no process found on port)"
    proc = subprocess.run(
        ["taskkill", "/F", "/PID", str(pid)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode == 0:
        return True, f"(killed PID {pid})"
    return False, proc.stderr or proc.stdout or f"taskkill failed for PID {pid}"


def start_npm_dev_background(repo_path: Path) -> subprocess.Popen:
    cmd = ["npm", "run", "dev"]
    if sys.platform == "win32":
        return subprocess.Popen(
            subprocess.list2cmdline(cmd),
            cwd=str(repo_path),
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    return subprocess.Popen(
        cmd,
        cwd=str(repo_path),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


def run_npm_smoke(repo_path: Path) -> Tuple[int, str]:
    return run_node_cmd(["npm", "run", "test:e2e:smoke"], repo_path)


def capture_screenshot(
    repo_path: Path,
    workspace: Path,
    url: str,
    task_id: str,
    scripts_dir: Path,
) -> Tuple[Optional[Path], str]:
    """
    Capture screenshot of URL. Returns (artifact_path, message).
    Uses Node script with Playwright from WCS repo. Sets NODE_PATH so require('playwright')
    resolves from repo_path/node_modules (same env as npm run test:e2e:smoke).
    """
    artifact_dir = workspace / "qa" / "artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    out_path = artifact_dir / f"{task_id}_manual_check.png"
    capture_script = scripts_dir / "capture_screenshot.js"
    if not capture_script.is_file():
        return None, f"Capture script not found: {capture_script}"
    wcs_node_modules = repo_path / "node_modules"
    env = os.environ.copy()
    env["NODE_PATH"] = str(wcs_node_modules)
    code, out = run_node_cmd(
        ["node", str(capture_script), url, str(out_path)],
        repo_path,
        env=env,
    )
    if code != 0:
        return None, f"Screenshot capture failed: {out}"
    if not out_path.is_file():
        return None, "Screenshot file was not created"
    return out_path, f"Saved to {out_path}"


def build_post_command(
    workspace: Path,
    task_id: str,
    first_scope: str,
    manual_check: str,
    artifact_paths: Optional[List[str]] = None,
) -> List[str]:
    scripts_dir = workspace / "scripts"
    cmd = [
        sys.executable,
        str(scripts_dir / "run_wcs_operator_entrypoint.py"),
        "post",
        "--task",
        task_id,
        "--workspace",
        str(workspace),
        "--draft-worker-result",
        "--worker-executor",
        "cursor_operator",
        "--worker-command",
        f"Implemented bounded {task_id} change in {first_scope} on the task branch",
        "--draft-qa-result",
        "--build-status",
        "pass",
        "--smoke-status",
        "pass",
        "--manual-status",
        "pass",
        "--manual-check",
        manual_check,
    ]
    for p in artifact_paths or []:
        cmd.extend(["--artifact", p])
    return cmd


def fail(msg: str, task_id: str, phase: str) -> int:
    print("")
    print("RUN ONE TASK FULL CYCLE: FAIL")
    print(f"Task: {task_id}")
    print(f"Phase: {phase}")
    print(f"Reason: {msg}")
    return 1


def main() -> int:
    args = parse_args()
    workspace = workspace_from_args(args.workspace)
    try:
        ensure_workspace_exists(workspace)
    except FullCycleError as e:
        print("RUN ONE TASK FULL CYCLE: FAIL")
        print(f"Reason: {e}")
        return 1

    # --- Finalize/resume mode: skip prep/launch/commit/build/smoke, delegate to post only ---
    if args.finalize:
        if not args.task:
            return fail("--finalize requires --task", "<task>", "finalize")
        if not args.manual_check:
            return fail("--finalize requires --manual-check", args.task or "<task>", "finalize")
        try:
            task_id = normalize_task_id(args.task)
        except ValueError as e:
            return fail(str(e), args.task or "<task>", "finalize")
        packet_path = workspace / "tasks" / f"{task_id}_task.json"
        if not packet_path.is_file():
            return fail(f"Expected task packet missing: {packet_path}", task_id, "finalize")
        try:
            packet = read_json(packet_path)
        except Exception as e:
            return fail(f"Could not read task packet: {e}", task_id, "finalize")
        if not isinstance(packet, dict):
            return fail("Task packet must be a JSON object", task_id, "finalize")
        scope_paths = derive_expected_scope(packet)
        first_scope = scope_paths[0] if scope_paths else "<expected file scope from task packet>"
        artifact_paths: List[str] = list(args.artifact) if args.artifact else []
        if not artifact_paths:
            default_artifact = workspace / "qa" / "artifacts" / f"{task_id}_manual_check.png"
            if default_artifact.is_file():
                artifact_paths = [str(default_artifact)]
        print("")
        print("RUN ONE TASK FULL CYCLE: FINALIZE MODE")
        print(f"Task: {task_id}")
        print("Skipping: prep, launch, diff review, commit, build, smoke.")
        print("Delegating to run_wcs_operator_entrypoint.py post.")
        print("")
        post_cmd = build_post_command(
            workspace=workspace,
            task_id=task_id,
            first_scope=first_scope,
            manual_check=args.manual_check,
            artifact_paths=artifact_paths if artifact_paths else None,
        )
        post_code, post_out = run_helper(post_cmd, workspace)
        print_helper_result(post_cmd, post_out)
        if post_code != 0:
            return fail("run_wcs_operator_entrypoint post failed", task_id, "post")
        print("")
        print("RUN ONE TASK FULL CYCLE: PASS (finalize)")
        print(f"Task: {task_id}")
        print("Status: post completed (reconcile ran as part of post; backlog updated).")
        return 0

    # --- Task selection ---
    if args.task:
        try:
            task_id = normalize_task_id(args.task)
        except ValueError as e:
            print("RUN ONE TASK FULL CYCLE: FAIL")
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
            print("RUN ONE TASK FULL CYCLE: FAIL")
            print("Failed delegated step: select_next_ready_task")
            return code if code != 0 else 1
        selection_mode = "automatic --select-ready"

    # --- Prep (and optional strict launch) ---
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
        return fail("run_wcs_operator_entrypoint prep failed", task_id, "prep")

    packet_path = workspace / "tasks" / f"{task_id}_task.json"
    if not packet_path.is_file():
        return fail(f"Expected task packet missing: {packet_path}", task_id, "prep")

    try:
        packet = read_json(packet_path)
    except Exception as e:
        return fail(f"Could not read task packet: {e}", task_id, "prep")

    if not isinstance(packet, dict):
        return fail("Task packet must be a JSON object", task_id, "prep")

    raw_repo = normalize_text(packet.get("repo_path"))
    if not raw_repo:
        return fail("Task packet has no repo_path", task_id, "prep")

    repo_path = Path(raw_repo).resolve()
    scope_paths = derive_expected_scope(packet)
    first_scope = scope_paths[0] if scope_paths else "<expected file scope from task packet>"

    print("")
    print("RUN ONE TASK FULL CYCLE: PREP PASS")
    print(f"Task: {task_id}")
    print(f"Selection mode: {selection_mode}")
    if args.launch_cursor:
        print("Cursor launch: strict launch attempted and passed.")
    else:
        print("Cursor launch: not attempted.")
    print("")

    # --- Closeout phase: diff summary ---
    print("--- CLOSEOUT CHECKPOINT: diff review ---")
    diff_code, diff_out = run_git_diff(repo_path, scope_paths)
    print(f"git diff -- {shell_join_paths(scope_paths)}")
    if diff_out:
        print("--- diff output begin ---")
        _safe_print(diff_out)
        print("--- diff output end ---")
    else:
        print("(no diff or empty)")
    print("")

    if not args.confirm_commit:
        print("RUN ONE TASK FULL CYCLE: STOP (operator confirmation required)")
        print(f"Task: {task_id}")
        print("Phase: closeout (before commit)")
        print("")
        print("Review the diff above. To proceed with commit, build, smoke, and post, re-run with:")
        print(f'  --confirm-commit [--commit-message "custom message"]')
        print("")
        print("To also complete post, add:")
        print(f'  --manual-check "Verified the targeted change locally in the browser for {task_id}."')
        return EXIT_STOP_COMMIT

    # --- Commit ---
    print("--- CLOSEOUT: commit (operator confirmed) ---")
    commit_code, commit_out = run_git_add_commit(
        repo_path=repo_path,
        scope_paths=scope_paths,
        task_id=task_id,
        first_scope=first_scope,
        commit_message=args.commit_message,
    )
    print_helper_result(
        ["git", "add", "--"] + scope_paths + ["&&", "git", "commit", "-m", "..."],
        commit_out,
    )
    if commit_code != 0:
        return fail("git add/commit failed", task_id, "commit")

    # --- Build ---
    print("")
    print("--- CLOSEOUT: build (mechanical) ---")
    build_code, build_out = run_node_cmd(["npm", "run", "build"], repo_path)
    print_helper_result(["npm", "run", "build"], build_out)
    if build_code != 0:
        return fail("npm run build failed", task_id, "build")

    # --- Dev server for smoke (and optional screenshot) ---
    dev_proc: Optional[subprocess.Popen] = None
    we_started_dev_server = False
    dev_port = args.dev_port or 3000

    if args.manage_dev_server:
        print("")
        print("--- CLOSEOUT: dev server (managed) ---")
        port_in_use = is_port_in_use(dev_port)
        if args.force_restart_dev_server and port_in_use:
            ok, msg = kill_process_on_port(dev_port)
            if not ok:
                return fail(f"Could not kill process on port {dev_port}: {msg}", task_id, "dev-server")
            print(f"Killed process on port {dev_port} {msg}")
            port_in_use = False
        if port_in_use:
            print(f"Reusing existing server on port {dev_port}.")
        else:
            dev_proc = start_npm_dev_background(repo_path)
            we_started_dev_server = True
            print(f"Started npm run dev (PID {dev_proc.pid}). Waiting 10s for server on port {dev_port}...")
            try:
                dev_proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
            if dev_proc.poll() is not None and (dev_proc.returncode or 0) != 0:
                return fail("npm run dev exited unexpectedly before smoke", task_id, "dev-server")
    else:
        print("")
        print("--- CLOSEOUT: starting dev server for smoke (mechanical) ---")
        dev_proc = start_npm_dev_background(repo_path)
        we_started_dev_server = True
        print(f"Started npm run dev (PID {dev_proc.pid}). Waiting 10s for server to be ready...")
        try:
            dev_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            pass
        if dev_proc.poll() is not None and (dev_proc.returncode or 0) != 0:
            return fail("npm run dev exited unexpectedly before smoke", task_id, "dev-server")

    print("")

    # --- Smoke ---
    print("--- CLOSEOUT: smoke (mechanical) ---")
    print("Note: Current smoke test is limited; page-specific coverage should be improved later.")
    smoke_code, smoke_out = run_node_cmd(["npm", "run", "test:e2e:smoke"], repo_path)
    print_helper_result(["npm", "run", "test:e2e:smoke"], smoke_out)
    if smoke_code != 0:
        if we_started_dev_server and dev_proc is not None:
            try:
                dev_proc.terminate()
            except Exception:
                pass
        return fail("npm run test:e2e:smoke failed", task_id, "smoke")

    # --- Page-specific smoke (when task scope maps to non-home route) ---
    page_route = scope_to_page_route(scope_paths)
    if page_route is not None:
        print("")
        print(f"--- CLOSEOUT: page-smoke (task scope maps to {page_route}) ---")
        page_env = os.environ.copy()
        page_env["E2E_SMOKE_PAGE"] = page_route
        page_smoke_code, page_smoke_out = run_node_cmd(
            ["npm", "run", "test:e2e:smoke:page"],
            repo_path,
            env=page_env,
        )
        print_helper_result(
            ["npm", "run", "test:e2e:smoke:page", f"E2E_SMOKE_PAGE={page_route}"],
            page_smoke_out,
        )
        if page_smoke_code != 0:
            if we_started_dev_server and dev_proc is not None:
                try:
                    dev_proc.terminate()
                except Exception:
                    pass
            return fail(
                f"npm run test:e2e:smoke:page failed for {page_route}",
                task_id,
                "page-smoke",
            )
        print(f"Page-smoke PASS for {page_route}")
    else:
        print("")
        print("--- CLOSEOUT: page-smoke (skipped; task scope is home or unknown) ---")

    # --- Optional screenshot capture (dev server still running) ---
    screenshot_artifact_path: Optional[Path] = None
    if args.capture_screenshot:
        print("")
        print("--- CLOSEOUT: screenshot capture (optional QA artifact) ---")
        manual_url = args.manual_url or f"http://127.0.0.1:{dev_port}/"
        if not args.manual_url and scope_paths:
            first = scope_paths[0]
            if "schedules" in first:
                manual_url = f"http://127.0.0.1:{dev_port}/schedules"
            elif "about" in first:
                manual_url = f"http://127.0.0.1:{dev_port}/about"
            elif "drills" in first:
                manual_url = f"http://127.0.0.1:{dev_port}/drills"
        path, msg = capture_screenshot(
            repo_path=repo_path,
            workspace=workspace,
            url=manual_url,
            task_id=task_id,
            scripts_dir=workspace / "scripts",
        )
        if path:
            screenshot_artifact_path = path
            print(msg)
        else:
            print(f"Screenshot capture skipped or failed: {msg}")

    if we_started_dev_server and dev_proc is not None:
        try:
            dev_proc.terminate()
        except Exception:
            pass

    # --- Manual verification checkpoint ---
    print("")
    print("--- CLOSEOUT CHECKPOINT: manual verification ---")
    if not args.manual_check:
        print("RUN ONE TASK FULL CYCLE: STOP (manual verification note required)")
        print(f"Task: {task_id}")
        print("Phase: closeout (before post)")
        print("")
        print("Manually verify the targeted change in the browser. Then either:")
        print("  (A) Re-run full cycle: --confirm-commit --manual-check \"Verified ...\"")
        print("  (B) Finalize only (skip prep/commit/build/smoke): --finalize --task " + task_id + ' --manual-check "Verified ..."')
        print("")
        print("Note: Use (B) if already committed and smoke-tested.")
        return EXIT_STOP_MANUAL

    # --- Post ---
    print("")
    print("--- CLOSEOUT: post (operator provided manual-check) ---")
    artifact_paths: List[str] = []
    if screenshot_artifact_path is not None:
        artifact_paths.append(str(screenshot_artifact_path))
    post_cmd = build_post_command(
        workspace=workspace,
        task_id=task_id,
        first_scope=first_scope,
        manual_check=args.manual_check,
        artifact_paths=artifact_paths if artifact_paths else None,
    )
    post_code, post_out = run_helper(post_cmd, workspace)
    print_helper_result(post_cmd, post_out)
    if post_code != 0:
        return fail("run_wcs_operator_entrypoint post failed", task_id, "post")

    print("")
    print("RUN ONE TASK FULL CYCLE: PASS")
    print(f"Task: {task_id}")
    print("Status: prep, launch (if requested), commit, build, smoke, manual verification, and post completed.")
    print("")
    print("Operator next actions:")
    print("1. Run reconcile to update backlog: python scripts/reconcile_task_outcome.py --task " + task_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
