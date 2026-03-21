#!/usr/bin/env python3
"""
Phase A: Unattended bounded collector.

Ingests operator URL list + optional bounded discovery queries.
Merges, dedups, classifies. Processes supported items only.
Skips/logs restricted and unsupported. Continues after failures.
Writes run summary + appends to cumulative ledger.

Supported: GitHub + article/webpage only.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse

_SCRIPT_DIR = Path(__file__).resolve().parent
_MODULE_ROOT = _SCRIPT_DIR.parent
_OUTPUTS = _MODULE_ROOT / "outputs"
_LEDGER = _OUTPUTS / "phase_a_collection_ledger.jsonl"

_VIDEO_HOSTS = frozenset({"youtube.com", "www.youtube.com", "youtu.be", "vimeo.com", "www.vimeo.com"})
_RESTRICTED_SIGNALS = ("HTTP 403", "403", "restricted", "paywall", "unavailable")


def _classify_url(url: str) -> str:
    """Classify: github | article | unsupported_video | unsupported_other."""
    url = (url or "").strip()
    if not url:
        return "unsupported_other"
    try:
        parsed = urlparse(url)
    except Exception:
        return "unsupported_other"
    host = (parsed.netloc or "").lower().replace("www.", "", 1)
    for h in _VIDEO_HOSTS:
        if h in host or host.endswith("." + h):
            return "unsupported_video"
    sys.path.insert(0, str(_SCRIPT_DIR))
    try:
        from acquisition.source_classifier import classify_from_url, is_supported
        st = classify_from_url(url)
        return st if is_supported(st) else "unsupported_other"
    except ValueError:
        return "unsupported_other"


def _load_urls_file(path: Path) -> list[dict]:
    """Load URLs from file. Returns [{url, input_origin: urls_file}]."""
    text = path.read_text(encoding="utf-8", errors="replace")
    seen: set[str] = set()
    items: list[dict] = []
    for line in text.splitlines():
        u = line.strip()
        if u and not u.startswith("#") and u not in seen:
            seen.add(u)
            items.append({"url": u, "input_origin": "urls_file"})
    return items


def _load_queries_file(path: Path) -> list[dict]:
    """Load queries. Returns [{query, source_class, max}]. Default max 5."""
    data = json.loads(path.read_text(encoding="utf-8"))
    queries = data.get("queries") or []
    max_total = data.get("max_total_discovery", 20)
    result: list[dict] = []
    for q in queries[:10]:
        if isinstance(q, dict):
            result.append({
                "query": (q.get("query") or "").strip(),
                "source_class": q.get("source_class", "github"),
                "max": min(int(q.get("max", 5)), 10),
            })
        elif isinstance(q, str):
            result.append({"query": q.strip(), "source_class": "github", "max": 5})
    return result, max_total


def _run_discovery(query: str, source_class: str, max_cand: int, outputs: Path) -> list[dict]:
    """Run discovery for one query. Returns [{url, input_origin: discovery}]."""
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out_path = outputs / f"phase_a_discovery_{source_class}_{run_id}.json"
    if source_class == "github":
        r = subprocess.run(
            [sys.executable, "run_discovery.py", "-q", query, "--max", str(max_cand), "--out", str(out_path)],
            cwd=str(_SCRIPT_DIR),
            capture_output=True,
            text=True,
            timeout=30,
        )
    else:
        r = subprocess.run(
            [sys.executable, "run_discovery_article.py", "-q", query, "--max", str(max_cand), "--out", str(out_path)],
            cwd=str(_SCRIPT_DIR),
            capture_output=True,
            text=True,
            timeout=30,
        )
    if r.returncode != 0 or not out_path.exists():
        return []
    try:
        data = json.loads(out_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    items: list[dict] = []
    for c in data.get("candidates") or []:
        u = (c.get("source_url") or "").strip()
        if u:
            items.append({"url": u, "input_origin": "discovery"})
    return items


def _is_restricted(detail: str) -> bool:
    """True if acquisition failure looks like restricted/paywalled."""
    d = (detail or "").lower()
    return any(s.lower() in d for s in _RESTRICTED_SIGNALS)


def _run_acquisition(url: str, packet_path: Path) -> tuple[bool, bool, str]:
    """(success, was_restricted, detail)."""
    r = subprocess.run(
        [sys.executable, "run_acquisition.py", "--url", url, "--out", str(packet_path)],
        cwd=str(_SCRIPT_DIR),
        capture_output=True,
        text=True,
        timeout=60,
    )
    detail = (r.stderr or r.stdout or "unknown").strip()[:300]
    if r.returncode == 0 and packet_path.exists():
        return True, False, "ok"
    restricted = _is_restricted(detail)
    return False, restricted, detail


def _run_extraction(packet_path: Path) -> tuple[bool, str]:
    """(success, detail)."""
    r = subprocess.run(
        [sys.executable, "run_extractor_api.py", "--packet", str(packet_path)],
        cwd=str(_SCRIPT_DIR),
        capture_output=True,
        text=True,
        timeout=120,
    )
    report_path = packet_path.parent / (
        f"extraction_report_{packet_path.stem.replace('source_packet_', '')}_api.json"
    )
    if r.returncode == 0 and report_path.exists():
        return True, str(report_path)
    return False, (r.stderr or r.stdout or "unknown").strip()[:200]


def _assess_usefulness(report_path: Path) -> str:
    try:
        data = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return "weak"
    summary = (data.get("summary") or "").strip()
    methods = data.get("methods_tools_patterns") or []
    claims = data.get("key_claims") or []
    if len(summary) >= 100 and (len(methods) >= 2 or len(claims) >= 2):
        return "useful"
    if summary or methods or claims:
        return "borderline"
    return "weak"


def main() -> int:
    parser = argparse.ArgumentParser(description="Phase A: Unattended bounded collector.")
    parser.add_argument("--urls-file", type=Path, required=True, help="Operator URL list (one per line)")
    parser.add_argument("--queries-file", type=Path, default=None, help="Optional discovery queries JSON")
    args = parser.parse_args()

    outputs = _OUTPUTS.resolve()
    outputs.mkdir(parents=True, exist_ok=True)

    if not args.urls_file.exists():
        print(f"Error: URLs file not found: {args.urls_file}", file=sys.stderr)
        return 1

    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    now_iso = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # 1. Load list URLs
    list_items = _load_urls_file(args.urls_file.resolve())
    all_items: list[dict] = [(it, "urls_file") for it in list_items]

    # 2. Optional discovery
    discovery_queries_used: list[dict] = []
    if args.queries_file and args.queries_file.exists():
        queries, max_total = _load_queries_file(args.queries_file.resolve())
        total_discovered = 0
        for q in queries:
            if not q.get("query"):
                continue
            if total_discovered >= max_total:
                break
            max_cand = min(q.get("max", 5), max_total - total_discovered)
            discovered = _run_discovery(q["query"], q["source_class"], max_cand, outputs)
            discovery_queries_used.append({"query": q["query"], "source_class": q["source_class"], "found": len(discovered)})
            for it in discovered:
                all_items.append((it, "discovery"))
            total_discovered += len(discovered)

    # 3. Merge + dedup
    seen: set[str] = set()
    merged: list[tuple[dict, str]] = []
    for it, origin in all_items:
        u = it.get("url", "").strip()
        if u and u not in seen:
            seen.add(u)
            merged.append(({**it, "input_origin": it.get("input_origin", origin)}, origin))

    # 4. Classify
    by_class: dict[str, list[dict]] = {"github": [], "article": [], "unsupported_video": [], "unsupported_other": []}
    for it, _ in merged:
        c = _classify_url(it["url"])
        by_class.setdefault(c, []).append(it)

    supported = by_class["github"] + by_class["article"]
    skipped_unsupported = (by_class.get("unsupported_video") or []) + (by_class.get("unsupported_other") or [])

    run_summary: dict = {
        "run_id": run_id,
        "started_at": now_iso,
        "urls_file": str(args.urls_file.resolve()),
        "queries_file": str(args.queries_file.resolve()) if args.queries_file else None,
        "discovery_queries_used": discovery_queries_used,
        "raw_from_list": len(list_items),
        "after_merge_dedup": len(merged),
        "github": len(by_class.get("github", [])),
        "article": len(by_class.get("article", [])),
        "unsupported_video": len(by_class.get("unsupported_video", [])),
        "unsupported_other": len(by_class.get("unsupported_other", [])),
        "processed": 0,
        "success": 0,
        "partial": 0,
        "fail": 0,
        "skipped_restricted": 0,
        "skipped_unsupported": len(skipped_unsupported),
        "results": [],
        "recurring_failures": [],
    }

    # 5. Process supported items
    for i, it in enumerate(supported):
        url = it["url"]
        sc = _classify_url(url)
        packet_path = outputs / f"phase_a_packet_{run_id}_{i}.json"
        rec = {
            "run_id": run_id,
            "timestamp": now_iso,
            "source_url": url,
            "source_class": sc,
            "input_origin": it.get("input_origin", "urls_file"),
            "outcome": "fail",
            "failure_reason": None,
            "usefulness": "weak",
            "packet_path": None,
            "extraction_path": None,
        }

        ok, restricted, detail = _run_acquisition(url, packet_path)
        if not ok:
            if restricted:
                rec["outcome"] = "skipped"
                rec["failure_reason"] = "restricted/paywall"
                run_summary["skipped_restricted"] += 1
                print(f"[SKIP restricted] {url[:55]}...")
            else:
                rec["outcome"] = "fail"
                rec["failure_reason"] = detail
                run_summary["fail"] += 1
                run_summary["processed"] += 1
                print(f"[FAIL acq] {url[:55]}...")
            run_summary["results"].append(rec)
            _append_ledger(rec)
            continue

        rec["packet_path"] = str(packet_path)
        ok2, detail2 = _run_extraction(packet_path)
        run_summary["processed"] += 1
        if not ok2:
            rec["outcome"] = "partial"
            rec["failure_reason"] = detail2
            run_summary["partial"] += 1
            print(f"[PARTIAL ext] {url[:55]}...")
        else:
            usefulness = _assess_usefulness(Path(detail2))
            rec["outcome"] = "success"
            rec["usefulness"] = usefulness
            rec["extraction_path"] = detail2
            run_summary["success"] += 1
            print(f"[OK] {url[:55]}... {usefulness}")

        run_summary["results"].append(rec)
        _append_ledger(rec)

    # Recurring failure summary
    fail_reasons: dict[str, int] = {}
    for r in run_summary["results"]:
        reason = r.get("failure_reason") or ""
        if reason and r.get("outcome") in ("fail", "partial"):
            key = reason[:80] if len(reason) > 80 else reason
            fail_reasons[key] = fail_reasons.get(key, 0) + 1
    run_summary["recurring_failures"] = [{"reason": k, "count": v} for k, v in sorted(fail_reasons.items(), key=lambda x: -x[1])[:5]]

    # 6. Write run summary
    summary_json = outputs / f"phase_a_run_summary_{run_id}.json"
    summary_md = outputs / f"phase_a_run_summary_{run_id}.md"
    with open(summary_json, "w", encoding="utf-8") as f:
        json.dump(run_summary, f, indent=2, ensure_ascii=False)
    _write_summary_md(run_summary, summary_md)
    print(f"\nSummary: {summary_json}")
    print(f"Ledger: {_LEDGER}")
    return 0


def _append_ledger(rec: dict) -> None:
    _LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with open(_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _write_summary_md(summary: dict, path: Path) -> None:
    lines = [
        f"# Phase A Run Summary — {summary['run_id']}",
        "",
        f"**Started:** {summary['started_at']}",
        f"**URLs file:** {summary['urls_file']}",
        f"**Queries file:** {summary.get('queries_file') or 'none'}",
        "",
        "## Counts",
        f"- After merge/dedup: {summary['after_merge_dedup']}",
        f"- GitHub: {summary['github']} | Article: {summary['article']}",
        f"- Unsupported video: {summary['unsupported_video']} | Other: {summary['unsupported_other']}",
        f"- Processed: {summary['processed']}",
        f"- Success: {summary['success']} | Partial: {summary['partial']} | Fail: {summary['fail']}",
        f"- Skipped restricted: {summary['skipped_restricted']} | Skipped unsupported: {summary['skipped_unsupported']}",
        "",
        "## Recurring failures",
    ]
    for rf in summary.get("recurring_failures") or []:
        lines.append(f"- {rf['count']}x: {rf['reason'][:100]}...")
    if not summary.get("recurring_failures"):
        lines.append("- None")
    lines.extend(["", "## Per-item results", ""])
    for r in summary.get("results") or []:
        lines.append(f"- [{r['outcome']}] {r['source_url'][:70]}... | {r.get('usefulness', '—')}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
