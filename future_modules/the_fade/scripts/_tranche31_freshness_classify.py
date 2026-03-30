"""One-off Tranche 31 evidence: classify FR slot freshness from JSONL + snapshots. Not production."""
from __future__ import annotations

import json
import pathlib
import re
from datetime import datetime, timedelta, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "lane_b_real_observation"
LOG = ROOT / "tranche21_fr_slot_runs.jsonl"
WIN_START = "2026-03-27T16:00:00Z"
WIN_END = "2026-03-29T16:00:00Z"
# Fresh if observation is within this duration after publication instant (UTC midnight on publication_date).
FRESH_MAX = timedelta(hours=48)


def parse_obs(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return datetime.fromisoformat(s)


def pub_instant(pub_date: str) -> datetime:
    """Federal Register date-only field -> UTC midnight start of that calendar day."""
    return datetime.strptime(pub_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def extract_publication_date_results0(preview: str) -> str | None:
    """First publication_date after results:[{ — matches results[0] for per_page=1 (preview may list more)."""
    idx = preview.find('"results":[{')
    if idx < 0:
        return None
    m = re.search(r'"publication_date"\s*:\s*"([^"]+)"', preview[idx:])
    return m.group(1) if m else None


def main() -> None:
    rows: list[dict] = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        if o.get("task_id") == "t30_valid_002":
            continue
        if o.get("window_start_utc") != WIN_START or o.get("window_end_utc") != WIN_END:
            continue
        task_id = o["task_id"]
        ap = o.get("artifact_path") or ""
        name = pathlib.Path(ap).name
        snap_path = ROOT / name
        if not snap_path.exists():
            rows.append(
                {
                    "task_id": task_id,
                    "classification": "cannot_classify",
                    "reason": "snapshot_missing",
                }
            )
            continue
        data = json.loads(snap_path.read_text(encoding="utf-8"))
        preview = data.get("response_preview_utf8") or ""
        pub_d = extract_publication_date_results0(preview)
        t_obs = parse_obs(o["actual_started_at_utc"])
        if not pub_d:
            rows.append(
                {
                    "task_id": task_id,
                    "classification": "cannot_classify",
                    "reason": "publication_date_not_found_in_preview",
                }
            )
            continue
        try:
            t_pub = pub_instant(pub_d)
        except ValueError:
            rows.append(
                {
                    "task_id": task_id,
                    "classification": "cannot_classify",
                    "reason": "publication_date_unparseable",
                    "raw": pub_d,
                }
            )
            continue
        delta = t_obs - t_pub
        if delta < timedelta(0):
            rows.append(
                {
                    "task_id": task_id,
                    "classification": "cannot_classify",
                    "reason": "negative_delta_obs_before_pub",
                    "publication_date": pub_d,
                    "delta_hours": delta.total_seconds() / 3600,
                }
            )
            continue
        if delta <= FRESH_MAX:
            cls = "fresh"
        else:
            cls = "stale"
        rows.append(
            {
                "task_id": task_id,
                "classification": cls,
                "publication_date": pub_d,
                "t_obs_utc": o["actual_started_at_utc"],
                "delta_hours": round(delta.total_seconds() / 3600, 4),
            }
        )

    fresh = sum(1 for r in rows if r["classification"] == "fresh")
    stale = sum(1 for r in rows if r["classification"] == "stale")
    unk = sum(1 for r in rows if r["classification"] == "cannot_classify")
    print(json.dumps({"total": len(rows), "fresh": fresh, "stale": stale, "cannot_classify": unk}, indent=2))
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
