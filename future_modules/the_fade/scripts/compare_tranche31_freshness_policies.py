"""Tranche 33: compare explicit freshness-policy interpretations on the 22-row FR window. Not production. No network."""
from __future__ import annotations

import json
import pathlib
import re
from datetime import datetime, timedelta, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "lane_b_real_observation"
LOG = ROOT / "tranche21_fr_slot_runs.jsonl"
OUT_JSON = ROOT / "tranche33_freshness_policy_comparison.json"
OUT_MD = ROOT / "tranche33_freshness_policy_comparison.md"
WIN_START = "2026-03-27T16:00:00Z"
WIN_END = "2026-03-29T16:00:00Z"
EXCLUDE_TASK = "t30_valid_002"
FRESH_MAX = timedelta(hours=48)


def parse_obs(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return datetime.fromisoformat(s)


def pub_instant_start(pub_date: str) -> datetime:
    return datetime.strptime(pub_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def pub_instant_end(pub_date: str) -> datetime:
    d = datetime.strptime(pub_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return d + timedelta(days=1) - timedelta(microseconds=1)


def extract_publication_date_results0(preview: str) -> str | None:
    idx = preview.find('"results":[{')
    if idx < 0:
        return None
    m = re.search(r'"publication_date"\s*:\s*"([^"]+)"', preview[idx:])
    return m.group(1) if m else None


def policy_strict_midnight_utc(
    t_obs: datetime, pub_d: str | None, t_pub: datetime | None
) -> tuple[str, str | None]:
    """Tranche 31 rule: T_pub = publication_date @ 00:00 UTC; Δ = T_obs - T_pub."""
    if not pub_d or t_pub is None:
        return "cannot_classify", "publication_date_missing"
    delta = t_obs - t_pub
    if delta < timedelta(0):
        return "cannot_classify", "negative_delta_obs_before_pub_midnight"
    if delta <= FRESH_MAX:
        return "fresh", None
    return "stale", None


def policy_publication_day_fresh(
    t_obs: datetime, pub_d: str | None, t_pub: datetime | None
) -> tuple[str, str | None]:
    """If UTC calendar date of observation <= publication_date -> fresh; else apply 48h after T_pub (midnight)."""
    if not pub_d or t_pub is None:
        return "cannot_classify", "publication_date_missing"
    d_obs = t_obs.date()
    d_pub = datetime.strptime(pub_d, "%Y-%m-%d").date()
    if d_obs <= d_pub:
        return "fresh", None
    delta = t_obs - t_pub
    if delta > FRESH_MAX:
        return "stale", None
    return "fresh", None


def policy_advance_listing_bucket(
    t_obs: datetime, pub_d: str | None, t_pub: datetime | None
) -> tuple[str, str | None]:
    """Negative Δ vs pub midnight -> explicit advance_listing bucket; else strict fresh/stale."""
    if not pub_d or t_pub is None:
        return "cannot_classify", "publication_date_missing"
    delta = t_obs - t_pub
    if delta < timedelta(0):
        return "advance_listing", None
    if delta <= FRESH_MAX:
        return "fresh", None
    return "stale", None


def policy_publication_end_of_day_utc(
    t_obs: datetime, pub_d: str | None, t_pub: datetime | None
) -> tuple[str, str | None]:
    """T_pub_end = last instant of publication calendar day (UTC). If t_obs <= T_pub_end -> fresh; else Δ from T_pub_end."""
    if not pub_d or t_pub is None:
        return "cannot_classify", "publication_date_missing"
    t_end = pub_instant_end(pub_d)
    if t_obs <= t_end:
        return "fresh", None
    delta = t_obs - t_end
    if delta <= FRESH_MAX:
        return "fresh", None
    return "stale", None


POLICIES: list[tuple[str, str, object]] = [
    (
        "strict_midnight_utc",
        "Same as Tranche 31: T_pub = publication_date at 00:00:00 UTC; fresh if 0<=Δ<=48h; stale if Δ>48h; cannot_classify if Δ<0.",
        policy_strict_midnight_utc,
    ),
    (
        "publication_day_fresh",
        "If UTC date(obs) <= publication_date -> fresh; if date(obs) > publication_date, compare Δ = T_obs - T_pub(midnight) and stale only if Δ>48h.",
        policy_publication_day_fresh,
    ),
    (
        "advance_listing_bucket",
        "If Δ<0 vs publication_date@00:00 UTC -> label advance_listing (explicit bucket); else same 48h fresh/stale as strict.",
        policy_advance_listing_bucket,
    ),
    (
        "publication_end_of_day_utc",
        "T_pub_end = 23:59:59.999999 UTC on publication_date; if T_obs <= T_pub_end -> fresh; else Δ from T_pub_end, stale if Δ>48h.",
        policy_publication_end_of_day_utc,
    ),
]


def aggregate(labels: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for lb in labels:
        out[lb] = out.get(lb, 0) + 1
    return dict(sorted(out.items(), key=lambda x: x[0]))


def load_rows() -> list[dict]:
    rows: list[dict] = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        if o.get("task_id") == EXCLUDE_TASK:
            continue
        if o.get("window_start_utc") != WIN_START or o.get("window_end_utc") != WIN_END:
            continue
        task_id = o["task_id"]
        ap = o.get("artifact_path") or ""
        name = pathlib.Path(ap).name
        snap_path = ROOT / name
        preview = ""
        err: str | None = None
        pub_d: str | None = None
        if not snap_path.exists():
            err = "snapshot_missing"
        else:
            data = json.loads(snap_path.read_text(encoding="utf-8"))
            preview = data.get("response_preview_utf8") or ""
            pub_d = extract_publication_date_results0(preview)
            if not pub_d:
                err = "publication_date_not_found_in_preview"
        t_obs = parse_obs(o["actual_started_at_utc"])
        t_pub = pub_instant_start(pub_d) if pub_d else None
        rows.append(
            {
                "task_id": task_id,
                "actual_started_at_utc": o["actual_started_at_utc"],
                "publication_date_results0": pub_d,
                "ingest_error": err,
                "t_obs": t_obs.isoformat(),
                "_t_obs": t_obs,
                "_t_pub": t_pub,
            }
        )
    rows.sort(key=lambda r: r["task_id"])
    return rows


def main() -> None:
    base_rows = load_rows()
    per_policy: dict[str, list[dict]] = {}
    for pid, desc, fn in POLICIES:
        out_rows = []
        for r in base_rows:
            if r.get("ingest_error"):
                label = "cannot_classify"
                detail = r["ingest_error"]
            else:
                label, detail = fn(r["_t_obs"], r["publication_date_results0"], r["_t_pub"])
            out_rows.append(
                {
                    "task_id": r["task_id"],
                    "actual_started_at_utc": r["actual_started_at_utc"],
                    "publication_date_results0": r["publication_date_results0"],
                    "label": label,
                    "detail": detail,
                }
            )
        per_policy[pid] = out_rows

    aggregates = {pid: aggregate([x["label"] for x in per_policy[pid]]) for pid, _, _ in POLICIES}

    ambiguous_strict = [
        x["task_id"]
        for x in per_policy["strict_midnight_utc"]
        if x["label"] == "cannot_classify" and x.get("detail") == "negative_delta_obs_before_pub_midnight"
    ]

    artifact = {
        "_meta": {
            "prompt": "Tranche 33 — freshness policy comparator (Phase 2 evidence only)",
            "not_approval": True,
            "does_not_close_gate": True,
            "phase_3_blocked": True,
            "population": "22 full-window FR JSONL lines",
            "excluded": EXCLUDE_TASK,
            "window_start_utc": WIN_START,
            "window_end_utc": WIN_END,
            "no_network": True,
        },
        "policies": {pid: {"description": desc} for pid, desc, _ in POLICIES},
        "ambiguous_under_strict_midnight_utc": ambiguous_strict,
        "aggregate_counts_by_policy": aggregates,
        "per_row": {
            r["task_id"]: {
                pid: {"label": per_policy[pid][i]["label"], "detail": per_policy[pid][i].get("detail")}
                for pid, _, _ in POLICIES
            }
            for i, r in enumerate(per_policy["strict_midnight_utc"])
        },
    }

    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    lines = [
        "# Tranche 33 — Freshness policy comparison (Lane B FR full window)",
        "",
        "**Not approval.** This file is a **policy comparator** on stored evidence only. It does **not** select a winning policy, does **not** close the MVP gate, and does **not** unlock Phase 3.",
        "",
        "## Population",
        "",
        f"- **22** JSONL lines matching full window (`{WIN_START}` … `{WIN_END}`).",
        f"- **`{EXCLUDE_TASK}`** excluded.",
        "- **No network** — script reads JSONL + snapshots only.",
        "",
        "## Policies",
        "",
    ]
    for pid, desc, _ in POLICIES:
        lines.append(f"- **`{pid}`:** {desc}")
    lines.extend(
        [
            "",
            "## Aggregate counts by policy",
            "",
            "| Policy | Counts |",
            "|--------|--------|",
        ]
    )
    for pid, _, _ in POLICIES:
        ag = aggregates[pid]
        lines.append(f"| `{pid}` | `{json.dumps(ag)}` |")
    lines.extend(
        [
            "",
            "## Ambiguous under `strict_midnight_utc` (Δ<0 vs pub midnight)",
            "",
        ]
    )
    for tid in ambiguous_strict:
        lines.append(f"- `{tid}`")
    lines.extend(["", "## Per-row matrix", "", "| task_id | " + " | ".join(pid for pid, _, _ in POLICIES) + " |", "|---|" + "|".join(["---"] * len(POLICIES)) + "|"])
    for i, r in enumerate(per_policy["strict_midnight_utc"]):
        tid = r["task_id"]
        cells = [per_policy[pid][i]["label"] for pid, _, _ in POLICIES]
        lines.append(f"| `{tid}` | " + " | ".join(cells) + " |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    print(json.dumps(aggregates, indent=2))


if __name__ == "__main__":
    main()
