#!/usr/bin/env python3
"""
Lane B minimal real observation slice (THE FADE only).

Implements `docs/LANE_B_MINIMAL_REAL_EVIDENCE_PATH_SPEC.md`:
  observe — fetch/read one real HTTPS URL or local file → scout_failure | normalized_signal_event
  conflict — lane B artifact + one THE FADE-local context_only_contra JSON → conflict_packet

No research_swarm/, no scanner, no dashboard. Lane B only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

LANE_B = "lane_b_official_disclosure"
CONTEXT_ROLE = "lane_e_research_swarm_context"
MODULE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = MODULE_ROOT / "outputs" / "lane_b_real_observation"
FUSION_POLICY = MODULE_ROOT / "config" / "fusion_policy.json"


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_dt(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return datetime.fromisoformat(s)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_fusion_weights() -> Tuple[float, float]:
    data = _load_json(FUSION_POLICY)
    hints = data.get("lane_weight_hints", {})
    wb = float(hints.get(LANE_B, 1.0))
    we = float(hints.get(CONTEXT_ROLE, 0.2))
    return wb, we


def cmd_observe(args: argparse.Namespace) -> int:
    task_id = args.task_id
    ticker = args.ticker
    out_dir = Path(args.out_dir) if args.out_dir else DEFAULT_OUT
    stale_after_h = float(args.stale_after_hours)
    source_name = args.source_name or "lane_b_operator_source"

    created_at = _now_iso()
    ingested_at = created_at

    if args.url and args.file:
        print("Use either --url or --file, not both.", file=sys.stderr)
        return 2
    if not args.url and not args.file:
        print("Provide --url or --file.", file=sys.stderr)
        return 2

    raw_bytes: bytes
    evidence_url = ""
    evidence_path = ""
    http_status: Optional[int] = None
    latency_ms: Optional[float] = None

    if args.file:
        fp = Path(args.file).resolve()
        evidence_path = str(fp)
        try:
            raw_bytes = fp.read_bytes()
        except OSError as e:
            fail = _scout_failure(
                task_id=task_id,
                ticker=ticker,
                created_at=created_at,
                error_type="SOURCE_UNAVAILABLE",
                error_summary=f"file_read_failed: {e}",
                raw_context_path=evidence_path,
            )
            _write_json(out_dir / f"{task_id}_scout_failure.json", fail)
            print(json.dumps(fail, indent=2))
            return 0
        event_time = datetime.fromtimestamp(fp.stat().st_mtime, tz=timezone.utc).replace(microsecond=0)
        event_time_s = event_time.isoformat().replace("+00:00", "Z")
    else:
        url = args.url.strip()
        evidence_url = url
        t0 = time.perf_counter()
        try:
            ctx = ssl.create_default_context()
            req = urllib.request.Request(url, method="GET", headers={"User-Agent": "THE_FADE_lane_b_real_observation/1.0"})
            with urllib.request.urlopen(req, timeout=args.timeout, context=ctx) as resp:
                raw_bytes = resp.read()
                http_status = resp.getcode()
                lm = resp.headers.get("Last-Modified")
        except urllib.error.HTTPError as e:
            latency_ms = (time.perf_counter() - t0) * 1000
            fail = _scout_failure(
                task_id=task_id,
                ticker=ticker,
                created_at=created_at,
                error_type="SOURCE_UNAVAILABLE",
                error_summary=f"http_error status={e.code} url={url} latency_ms={latency_ms:.1f}",
                raw_context_path=evidence_url,
            )
            _write_json(out_dir / f"{task_id}_scout_failure.json", fail)
            print(json.dumps(fail, indent=2))
            return 0
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            latency_ms = (time.perf_counter() - t0) * 1000
            fail = _scout_failure(
                task_id=task_id,
                ticker=ticker,
                created_at=created_at,
                error_type="SOURCE_UNAVAILABLE",
                error_summary=f"fetch_failed: {e!s} url={url} latency_ms={latency_ms:.1f}",
                raw_context_path=evidence_url,
            )
            _write_json(out_dir / f"{task_id}_scout_failure.json", fail)
            print(json.dumps(fail, indent=2))
            return 0
        latency_ms = (time.perf_counter() - t0) * 1000
        if http_status and http_status >= 400:
            fail = _scout_failure(
                task_id=task_id,
                ticker=ticker,
                created_at=created_at,
                error_type="SOURCE_UNAVAILABLE",
                error_summary=f"http_status={http_status} url={url} latency_ms={latency_ms:.1f}",
                raw_context_path=evidence_url,
            )
            _write_json(out_dir / f"{task_id}_scout_failure.json", fail)
            print(json.dumps(fail, indent=2))
            return 0
        if not raw_bytes:
            fail = _scout_failure(
                task_id=task_id,
                ticker=ticker,
                created_at=created_at,
                error_type="SOURCE_UNAVAILABLE",
                error_summary=f"empty_body url={url} latency_ms={latency_ms:.1f}",
                raw_context_path=evidence_url,
            )
            _write_json(out_dir / f"{task_id}_scout_failure.json", fail)
            print(json.dumps(fail, indent=2))
            return 0
        event_time_s = created_at
        if lm:
            try:
                from email.utils import parsedate_to_datetime

                dt = parsedate_to_datetime(lm)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                event_time_s = dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
            except Exception:
                pass

    body_hash = _sha256_bytes(raw_bytes)
    try:
        raw_text = raw_bytes.decode("utf-8", errors="replace")
    except Exception:
        raw_text = ""
    if len(raw_text) > 8000:
        raw_text = raw_text[:8000] + "\n…(truncated)"

    ing_dt = _parse_dt(ingested_at)
    ev_dt = _parse_dt(event_time_s)
    freshness_hours = max(0.0, (ing_dt - ev_dt).total_seconds() / 3600.0)

    lag_class = "fresh"
    notes = f"lane_b_real_observation observe; sha256={body_hash}"
    if args.file:
        notes += f"; file_mtime_used_for_event_time"
    else:
        notes += f"; http_status={http_status} latency_ms={latency_ms:.1f}"
    if freshness_hours > stale_after_h:
        lag_class = "stale"

    evt = {
        "event_id": f"evt_{task_id}_{body_hash[:12]}",
        "task_id": task_id,
        "ticker": ticker,
        "asset_type": "other",
        "source_lane": LANE_B,
        "source_name": source_name,
        "direction_hint": "neutral",
        "event_time": event_time_s,
        "ingested_at": ingested_at,
        "freshness_hours": round(freshness_hours, 4),
        "raw_text": raw_text,
        "parsed_summary": (raw_text[:500] if raw_text else f"binary_or_empty len={len(raw_bytes)}"),
        "evidence_url": evidence_url,
        "evidence_path": evidence_path,
        "trust_tier": "operator_capture",
        "lag_class": lag_class,
        "parser_confidence": 0.35,
        "notes": notes,
    }
    _write_json(out_dir / f"{task_id}_normalized_signal_event.json", evt)
    print(json.dumps(evt, indent=2))
    return 0


def _scout_failure(
    *,
    task_id: str,
    ticker: str,
    created_at: str,
    error_type: str,
    error_summary: str,
    raw_context_path: str,
) -> Dict[str, Any]:
    return {
        "failure_id": f"fail_{task_id}_{_sha256_bytes(error_summary.encode())[:12]}",
        "stage": "lane_b_real_observation",
        "task_id": task_id,
        "ticker": ticker,
        "error_type": error_type,
        "error_summary": error_summary,
        "raw_context_path": raw_context_path,
        "created_at": created_at,
        "escalation_required": False,
        "resolved": False,
    }


def cmd_conflict(args: argparse.Namespace) -> int:
    task_id = args.task_id
    ticker = args.ticker
    out_dir = Path(args.out_dir) if args.out_dir else DEFAULT_OUT
    lane_path = Path(args.lane_b_artifact).resolve()
    contra_path = Path(args.contra).resolve()

    if not lane_path.is_file():
        print(f"Missing lane B artifact: {lane_path}", file=sys.stderr)
        return 2
    if not contra_path.is_file():
        print(f"Missing contra file: {contra_path}", file=sys.stderr)
        return 2

    lane = _load_json(lane_path)
    contra = _load_json(contra_path)

    if lane.get("source_lane") != LANE_B:
        print("Lane B artifact must have source_lane lane_b_official_disclosure.", file=sys.stderr)
        return 2
    role = contra.get("semantic_role") or contra.get("role")
    if role != CONTEXT_ROLE:
        print(f"Contra file must declare semantic_role {CONTEXT_ROLE!r}.", file=sys.stderr)
        return 2

    ld = lane.get("direction_hint")
    cd = contra.get("direction_hint")
    wb, we = _read_fusion_weights()

    mismatch = ld is not None and cd is not None and ld != cd
    primary = "lane_b_official_disclosure"
    summary = (
        f"fusion_policy lane_weight_hints: {LANE_B}={wb}, {CONTEXT_ROLE}={we}; "
        f"precedence: primary={primary}; context cannot override lane B. "
        f"direction_hint lane_b={ld!r} context_role={cd!r} mismatch={mismatch}."
    )
    reasons = [
        "lane_b_vs_context_role_under_fusion_policy",
        f"direction_hint_mismatch={mismatch}",
    ]

    pkt = {
        "conflict_packet_id": f"cf_{task_id}_{_sha256_bytes(summary.encode())[:12]}",
        "task_id": task_id,
        "ticker": ticker,
        "created_at": _now_iso(),
        "summary": summary,
        "conflict_reasons": reasons,
        "evidence_paths": [str(lane_path), str(contra_path)],
        "notes": "THE FADE local slice; no research_swarm/ read.",
    }
    _write_json(out_dir / f"{task_id}_conflict_packet.json", pkt)
    print(json.dumps(pkt, indent=2))
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Lane B real observation slice (THE FADE only)")
    sub = p.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("observe", help="Read real URL or file → scout_failure or normalized_signal_event")
    o.add_argument("--task-id", required=True)
    o.add_argument("--ticker", default="UNK")
    o.add_argument("--url", default="")
    o.add_argument("--file", default="")
    o.add_argument("--source-name", default="")
    o.add_argument("--stale-after-hours", type=float, default=48.0)
    o.add_argument("--timeout", type=int, default=30)
    o.add_argument("--out-dir", default="")

    c = sub.add_parser("conflict", help="Lane B artifact + local context_only_contra → conflict_packet")
    c.add_argument("--task-id", required=True)
    c.add_argument("--ticker", default="UNK")
    c.add_argument("--lane-b-artifact", required=True)
    c.add_argument("--contra", required=True)
    c.add_argument("--out-dir", default="")

    args = p.parse_args(argv)
    if args.cmd == "observe":
        return cmd_observe(args)
    return cmd_conflict(args)


if __name__ == "__main__":
    raise SystemExit(main())
