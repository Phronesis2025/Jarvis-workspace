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
