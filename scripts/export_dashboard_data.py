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
  python scripts/export_dashboard_data.py --dry-run   # verify without Supabase writes
"""

from __future__ import annotations

import argparse
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


def _route_from_suspected_files(suspected: list) -> str | None:
    """Derive route from task suspected_files (e.g. src/app/schedules/page.tsx -> /schedules)."""
    if not isinstance(suspected, list):
        return None
    for f in suspected:
        if not isinstance(f, str):
            continue
        f = f.strip().replace("\\", "/")
        if "/schedules/page" in f or "schedules/page" in f:
            return "/schedules"
        if "/drills/page" in f or "drills/page" in f:
            return "/drills"
        if "/about/page" in f or "about/page" in f:
            return "/about"
        if f.endswith("/page.tsx") and "/app/" in f and "schedules" not in f and "drills" not in f and "about" not in f:
            return "/"
    return None


def _derive_operator_checkpoints(tid: str) -> dict:
    """Derive trust checkpoints from qa_result, worker_result, task packet. Uses only real evidence."""
    out: dict = {
        "build": {"status": "unknown"},
        "smoke": {"status": "unknown"},
        "page_smoke": {"status": "unknown", "route": None},
        "manual_check": {"status": "unknown"},
        "screenshot": {"status": "unknown"},
    }

    qa_path = WORKSPACE / "qa" / f"{tid}_qa_result.json"
    qa = _load_json(qa_path) if qa_path.is_file() else None
    if not isinstance(qa, dict):
        return out

    checks_passed = qa.get("checks_passed") or []
    checks_failed = qa.get("checks_failed") or []
    checks_run = qa.get("checks_run") or []
    artifacts = qa.get("artifacts") or []
    if not isinstance(checks_passed, list):
        checks_passed = []
    if not isinstance(checks_failed, list):
        checks_failed = []
    if not isinstance(checks_run, list):
        checks_run = []
    if not isinstance(artifacts, list):
        artifacts = []

    def _has(coll: list, *substrs: str) -> bool:
        for c in coll:
            s = (c or "").lower() if isinstance(c, str) else ""
            for sub in substrs:
                if sub in s:
                    return True
        return False

    # Build
    if _has(checks_passed, "npm run build", "ran npm run build", "build passed"):
        out["build"]["status"] = "pass"
    elif _has(checks_failed, "npm run build", "build"):
        out["build"]["status"] = "fail"
    else:
        out["build"]["status"] = "unknown"

    # Smoke
    if _has(checks_passed, "test:e2e:smoke", "playwright smoke", "smoke test"):
        out["smoke"]["status"] = "pass"
    elif _has(checks_failed, "test:e2e:smoke", "smoke"):
        out["smoke"]["status"] = "fail"
    else:
        out["smoke"]["status"] = "unknown"

    # Page-smoke + route (only when check explicitly mentions page smoke, not manual verification)
    page_route: str | None = None
    page_smoke_evidence = False
    if _has(checks_passed, "schedules page smoke", "page smoke", "drills page smoke", "home page smoke"):
        out["page_smoke"]["status"] = "pass"
        page_smoke_evidence = True
        if _has(checks_passed, "schedules page smoke", "schedules page"):
            page_route = "/schedules"
        elif _has(checks_passed, "drills page smoke", "drills page"):
            page_route = "/drills"
        elif _has(checks_passed, "home page smoke"):
            page_route = "/"
    elif _has(checks_failed, "page smoke"):
        out["page_smoke"]["status"] = "fail"
        page_smoke_evidence = True
    if not page_route:
        pkt_path = WORKSPACE / "tasks" / f"{tid}_task.json"
        pkt = _load_json(pkt_path) if pkt_path.is_file() else None
        if isinstance(pkt, dict):
            sus = pkt.get("suspected_files") or []
            page_route = _route_from_suspected_files(sus)
    if not page_smoke_evidence:
        out["page_smoke"]["status"] = "skipped"
    out["page_smoke"]["route"] = page_route

    # Manual check
    manual_checks = [c for c in checks_passed + checks_run if c and isinstance(c, str)
                     and "npm run build" not in c.lower() and "test:e2e:smoke" not in c.lower()
                     and ("manual" in c.lower() or "verified" in c.lower() or "browser" in c.lower())]
    if manual_checks:
        out["manual_check"]["status"] = "present"
    elif qa.get("status") == "qa_pass" and (checks_passed or checks_run):
        out["manual_check"]["status"] = "missing"
    else:
        out["manual_check"]["status"] = "unknown"

    # Screenshot
    if artifacts and any(
        (a or "").lower().find("screenshot") >= 0 or (a or "").lower().endswith(".png")
        for a in artifacts if isinstance(a, str)
    ):
        out["screenshot"]["status"] = "captured"
    elif artifacts:
        out["screenshot"]["status"] = "missing"
    else:
        out["screenshot"]["status"] = "unknown"

    return out


def _derive_stop_reason(tid: str) -> str | None:
    """Derive stop/failure reason from worker_result, qa_result, escalations. Returns None if none found."""
    reasons: list[str] = []

    wres_path = WORKSPACE / "results" / f"{tid}_worker_result.json"
    wres = _load_json(wres_path) if wres_path.is_file() else None
    if isinstance(wres, dict):
        issues = wres.get("issues_encountered") or []
        if isinstance(issues, list) and issues:
            for i in issues:
                if isinstance(i, str) and i.strip():
                    reasons.append(i.strip())

    qa_path = WORKSPACE / "qa" / f"{tid}_qa_result.json"
    qa = _load_json(qa_path) if qa_path.is_file() else None
    if isinstance(qa, dict) and (qa.get("status") or "").lower() != "qa_pass":
        failed = qa.get("checks_failed") or []
        if isinstance(failed, list) and failed:
            for f in failed:
                if isinstance(f, str) and f.strip():
                    reasons.append(f.strip())
        summary = (qa.get("summary") or "").strip()
        if summary and summary not in reasons:
            reasons.append(summary)

    esc_path = WORKSPACE / "state" / "escalations.json"
    esc_data = _load_json(esc_path)
    if isinstance(esc_data, list):
        for e in esc_data:
            if isinstance(e, dict) and e.get("task_id") == tid:
                s = (e.get("summary") or "").strip()
                if s:
                    reasons.append(s)
                break

    return "; ".join(reasons) if reasons else None


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
        stop_reason = _derive_stop_reason(tid)
        checkpoints = _derive_operator_checkpoints(tid)
        outcome = status or "complete"
        runs.append({
            "run_id": f"{tid}-cycle",
            "module": "wcs",
            "script_name": "run_one_task_cycle.py",
            "task_ids": [tid],
            "started_at": dt.isoformat(),
            "ended_at": completed,
            "outcome": outcome,
            "stop_reason": stop_reason,
            "llm_used": False,
            "operator_checkpoints": checkpoints,
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
                "operator_checkpoints": None,
            })

    runs.sort(key=lambda r: r["started_at"], reverse=True)
    return runs[:100]


def _gather_module_status() -> list[dict]:
    """Static v1 mapping. Add jarvis_core for Overview module cards."""
    return [
        {
            "module_id": "jarvis_core",
            "name": "Jarvis Core",
            "status": "active",
            "phase": "Phase 3",
            "milestone_summary": "Foreman loop live; daily plan and run log active.",
        },
        {
            "module_id": "wcs",
            "name": "WCS Code Module",
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


def _run_dry_run() -> int:
    """Gather data, print summary, no Supabase writes. Returns 0 if export-safe, 1 if blocked."""
    url = _env("SUPABASE_URL", "NEXT_PUBLIC_SUPABASE_URL")
    key = _env("SUPABASE_SERVICE_KEY", "SUPABASE_SERVICE_ROLE_KEY")
    env_ok = bool(url and key)

    backlog_path = WORKSPACE / "state" / "master_backlog.json"
    if not backlog_path.is_file():
        print("EXPORT_DASHBOARD: DRY-RUN FAIL", file=sys.stderr)
        print(f"Source file not found: {backlog_path}", file=sys.stderr)
        return 1

    tasks = _gather_task_state()
    runs = _gather_runs()
    modules = _gather_module_status()
    pathfinder = _gather_pathfinder_cases()

    backlog_data = _load_json(backlog_path)
    if backlog_data is None:
        print("EXPORT_DASHBOARD: DRY-RUN FAIL", file=sys.stderr)
        print(f"Source file malformed or unreadable: {backlog_path}", file=sys.stderr)
        return 1
    if not isinstance(backlog_data, list):
        print("EXPORT_DASHBOARD: DRY-RUN FAIL", file=sys.stderr)
        print(f"Source file must be a JSON array: {backlog_path}", file=sys.stderr)
        return 1

    print("EXPORT_DASHBOARD: DRY-RUN")
    print(f"  task rows gathered: {len(tasks)}")
    print(f"  run rows gathered: {len(runs)}")
    print(f"  module status rows gathered: {len(modules)}")
    print(f"  pathfinder cases gathered: {len(pathfinder)}")
    print(f"  env SUPABASE_URL: {'present' if url else 'absent'}")
    print(f"  env SUPABASE_SERVICE_KEY: {'present' if key else 'absent'}")
    print(f"  export safe to attempt live: {'yes' if env_ok else 'no'}")
    return 0 if env_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Export Jarvis data to Supabase dashboard")
    parser.add_argument("--dry-run", action="store_true", help="Verify without Supabase writes")
    args = parser.parse_args()

    if args.dry_run:
        return _run_dry_run()

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

        # Record export freshness for Overview "Last dashboard update"
        client.table("dashboard_export_log").upsert(
            [{
                "id": "latest",
                "exported_at": datetime.now().isoformat(),
                "task_count": len(tasks),
                "run_count": len(runs),
                "module_count": len(modules),
                "pathfinder_count": len(pathfinder),
            }],
            on_conflict="id",
        ).execute()
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
