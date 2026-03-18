"""
Jarvis → Supabase dashboard export script.

Reads local source-of-truth files and upserts into Supabase dashboard tables.
One-way export only. Never mutates Jarvis truth files.

Required env vars:
  SUPABASE_URL          — Supabase project URL (or NEXT_PUBLIC_SUPABASE_URL)
  SUPABASE_SERVICE_KEY  — Service role key for writes (bypasses RLS)

Requires: pip install supabase

Usage:
  python scripts/export_dashboard_data.py
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent


def _env(key: str, alt: str | None = None) -> str:
    v = os.environ.get(key) or (os.environ.get(alt) if alt else None)
    return (v or "").strip()


def _load_json(path: Path) -> list | dict | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _fail(msg: str) -> None:
    print("EXPORT_DASHBOARD: FAIL", file=sys.stderr)
    print(msg, file=sys.stderr)
    sys.exit(1)


def _gather_task_state() -> list[dict]:
    """From master_backlog.json + task packets for last_result/updated_at."""
    backlog_path = WORKSPACE / "state" / "master_backlog.json"
    data = _load_json(backlog_path)
    if not isinstance(data, list):
        return []

    escalated_ids = set()
    esc_path = WORKSPACE / "state" / "escalations.json"
    esc_data = _load_json(esc_path)
    if isinstance(esc_data, list):
        for e in esc_data:
            if isinstance(e, dict) and e.get("status") == "open":
                tid = e.get("task_id")
                if tid:
                    escalated_ids.add(tid)

    task_by_id: dict[str, dict] = {}
    for row in data:
        if not isinstance(row, dict):
            continue
        tid = (row.get("task_id") or "").strip()
        if not tid:
            continue
        status = (row.get("status") or "ready").strip().lower()
        if tid in escalated_ids and status != "done":
            status = "escalated"
        if status not in ("ready", "running", "awaiting_operator", "blocked", "escalated", "done"):
            status = "ready" if status != "done" else "done"

        task_by_id[tid] = {
            "task_id": tid,
            "title": (row.get("title") or "—")[:500],
            "project": (row.get("project") or "WCS").strip(),
            "module": "wcs",
            "risk": (row.get("risk") or "").strip() or None,
            "scope_hint": (row.get("notes") or "").strip()[:200] or None,
            "status": status,
            "last_result": None,
            "updated_at": datetime.now().isoformat(),
        }

    for task_path in (WORKSPACE / "tasks").glob("*_task.json"):
        tdata = _load_json(task_path)
        if not isinstance(tdata, dict):
            continue
        tid = (tdata.get("task_id") or "").strip()
        if not tid or tid not in task_by_id:
            continue
        updated = (tdata.get("updated_at") or "").strip()
        if updated:
            task_by_id[tid]["updated_at"] = updated

        wres_path = WORKSPACE / "results" / f"{tid}_worker_result.json"
        wres = _load_json(wres_path)
        if isinstance(wres, dict):
            task_by_id[tid]["last_result"] = (wres.get("status") or "").strip() or None

    return list(task_by_id.values())


def _gather_runs() -> list[dict]:
    """From worker results (WCS cycles) + Pathfinder results."""
    runs: list[dict] = []

    for res_path in (WORKSPACE / "results").glob("*_worker_result.json"):
        data = _load_json(res_path)
        if not isinstance(data, dict):
            continue
        tid = (data.get("task_id") or "").strip()
        if not tid or not tid.startswith("WCS-"):
            continue
        completed = (data.get("completed_at") or "").strip()
        status = (data.get("status") or "").strip()
        if not completed:
            continue
        try:
            dt = datetime.fromisoformat(completed.replace("Z", "+00:00"))
        except ValueError:
            continue
        runs.append({
            "run_id": f"{tid}-cycle",
            "module": "wcs",
            "script_name": "run_one_task_cycle.py",
            "task_ids": [tid],
            "started_at": dt.isoformat(),
            "ended_at": completed,
            "outcome": status or "complete",
            "stop_reason": None,
            "llm_used": False,
        })

    for base in [WORKSPACE / "scratch" / "pathfinder", WORKSPACE / "scratch" / "pathfinder_ab"]:
        if not base.exists():
            continue
        for jpath in base.glob("*.json"):
            data = _load_json(jpath)
            if not isinstance(data, dict):
                continue
            run_id = (data.get("run_id") or data.get("task_id") or "").strip()
            if not run_id:
                continue
            completed = (data.get("completed_at") or "").strip()
            if not completed:
                continue
            try:
                dt = datetime.fromisoformat(completed.replace("Z", "+00:00"))
            except ValueError:
                continue
            llm = "LLM synthesis used" in (data.get("commands_run") or [])
            runs.append({
                "run_id": run_id,
                "module": "pathfinder",
                "script_name": "run_pathfinder.py",
                "task_ids": None,
                "started_at": dt.isoformat(),
                "ended_at": completed,
                "outcome": (data.get("status") or "worker_complete").strip(),
                "stop_reason": None,
                "llm_used": llm,
            })

    runs.sort(key=lambda r: r["started_at"], reverse=True)
    return runs[:100]


def _gather_module_status() -> list[dict]:
    """Static v1 mapping."""
    return [
        {
            "module_id": "wcs",
            "name": "WCS",
            "status": "active",
            "phase": "Phase 3",
            "milestone_summary": "Foreman loop live; task cycles proven.",
        },
        {
            "module_id": "pathfinder",
            "name": "Pathfinder",
            "status": "active",
            "phase": "v1",
            "milestone_summary": "Read-only discovery worker proven.",
        },
    ]


def _gather_pathfinder_cases() -> list[dict]:
    """From Pathfinder result JSON files."""
    cases: list[dict] = []
    seen_run_ids: set[str] = set()

    for base in [WORKSPACE / "scratch" / "pathfinder", WORKSPACE / "scratch" / "pathfinder_ab"]:
        if not base.exists():
            continue
        for jpath in base.glob("*.json"):
            data = _load_json(jpath)
            if not isinstance(data, dict):
                continue
            run_id = (data.get("run_id") or data.get("task_id") or "").strip()
            if not run_id or run_id in seen_run_ids:
                continue
            seen_run_ids.add(run_id)

            synthesis = data.get("synthesis") or {}
            if isinstance(synthesis, dict):
                conf = (synthesis.get("confidence") or "").strip() or None
                likely = (synthesis.get("likely_next_action") or "").strip() or None
            else:
                conf = likely = None

            draft = data.get("draft_backlog_candidate")
            title = None
            if isinstance(draft, dict):
                title = (draft.get("title") or "").strip() or None
            omitted = (data.get("draft_backlog_omitted_reason") or "").strip() or None
            src = (data.get("synthesis_source") or "").strip()
            if src not in ("llm", "rule_based"):
                src = None

            completed = (data.get("completed_at") or "").strip()

            cases.append({
                "run_id": run_id,
                "intake_summary": (data.get("summary") or "").strip()[:500] or None,
                "route": None,
                "synthesis_source": src,
                "confidence": conf,
                "likely_next_action": likely,
                "backlog_candidate_title": title,
                "omitted_reason": omitted,
                "created_at": completed or datetime.now().isoformat(),
            })

    cases.sort(key=lambda c: c["created_at"], reverse=True)
    return cases[:100]


def main() -> int:
    url = _env("SUPABASE_URL", "NEXT_PUBLIC_SUPABASE_URL")
    key = _env("SUPABASE_SERVICE_KEY", "SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        _fail(
            "Missing env vars. Required: SUPABASE_URL (or NEXT_PUBLIC_SUPABASE_URL), "
            "SUPABASE_SERVICE_KEY (or SUPABASE_SERVICE_ROLE_KEY)."
        )

    try:
        from supabase import create_client
    except ImportError:
        _fail("Install supabase: pip install supabase")

    client = create_client(url, key)

    backlog_path = WORKSPACE / "state" / "master_backlog.json"
    if not backlog_path.is_file():
        _fail(f"Source file not found: {backlog_path}")

    tasks = _gather_task_state()
    runs = _gather_runs()
    modules = _gather_module_status()
    pathfinder = _gather_pathfinder_cases()

    try:
        if tasks:
            client.table("dashboard_task_state").upsert(
                tasks,
                on_conflict="task_id",
            ).execute()
        if runs:
            run_ids = [r["run_id"] for r in runs]
            if run_ids:
                in_val = "(" + ",".join(f'"{r}"' for r in run_ids) + ")"
                client.table("dashboard_runs").delete().filter("run_id", "in", in_val).execute()
            client.table("dashboard_runs").insert(runs).execute()
        if modules:
            client.table("dashboard_module_status").upsert(
                modules,
                on_conflict="module_id",
            ).execute()
        if pathfinder:
            pf_run_ids = [c["run_id"] for c in pathfinder]
            if pf_run_ids:
                in_val = "(" + ",".join(f'"{r}"' for r in pf_run_ids) + ")"
                client.table("dashboard_pathfinder_cases").delete().filter("run_id", "in", in_val).execute()
            client.table("dashboard_pathfinder_cases").insert(pathfinder).execute()
    except Exception as e:
        _fail(f"Supabase write failed: {e}")

    print("EXPORT_DASHBOARD: PASS")
    print(f"  dashboard_task_state: {len(tasks)}")
    print(f"  dashboard_runs: {len(runs)}")
    print(f"  dashboard_module_status: {len(modules)}")
    print(f"  dashboard_pathfinder_cases: {len(pathfinder)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
