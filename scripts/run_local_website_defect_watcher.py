"""
B1 v1 — Local Website Defect Watcher

Read-only watcher that visits configured routes, checks load/selectors/console,
gathers evidence, and produces proposed defect packets for operator review.

Usage:
  python scripts/run_local_website_defect_watcher.py --config <path>

Requires: pip install playwright && playwright install chromium

Contract: B1_WCS_DEFECT_WATCHER_V1_SPEC.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
DEDUPE_PATH = WORKSPACE / "state" / "local_website_defect_watcher_dedupe.json"

REQUIRED_CONFIG = [
    "watcher_id", "watcher_version", "target_site", "allowed_routes",
    "critical_routes", "critical_selectors", "run_mode", "max_routes",
    "capture_screenshot", "capture_console", "dedupe_window_hours", "output_dir",
]


def _fail(msg: str) -> None:
    print("B1_WATCHER: FAIL", file=sys.stderr)
    print(msg, file=sys.stderr)
    sys.exit(1)


def _load_json(path: Path) -> dict | list | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _route_slug(route: str) -> str:
    if route == "/" or route == "":
        return "root"
    return route.strip("/").replace("/", "_")


def _normalize_summary(s: str, max_len: int = 80) -> str:
    n = re.sub(r"\s+", " ", (s or "").lower().strip())
    return n[:max_len] if len(n) > max_len else n


def _duplicate_key(route: str, defect_type: str, summary: str) -> str:
    norm = _normalize_summary(summary)
    return f"{route}:{defect_type}:{norm}"


def _load_dedupe() -> dict[str, str]:
    data = _load_json(DEDUPE_PATH)
    if isinstance(data, dict):
        return data
    return {}


def _save_dedupe(data: dict[str, str]) -> None:
    DEDUPE_PATH.parent.mkdir(parents=True, exist_ok=True)
    DEDUPE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _is_duplicate(key: str, dedupe: dict[str, str], window_hours: int) -> bool:
    last = dedupe.get(key)
    if not last:
        return False
    try:
        dt = datetime.fromisoformat(last.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=window_hours)
        return dt > cutoff
    except ValueError:
        return False


def _validate_config(cfg: dict) -> None:
    for k in REQUIRED_CONFIG:
        if k not in cfg:
            _fail(f"Config missing required field: {k}")
    if not isinstance(cfg.get("allowed_routes"), list) or not cfg["allowed_routes"]:
        _fail("Config allowed_routes must be non-empty array")
    if not isinstance(cfg.get("critical_selectors"), dict):
        _fail("Config critical_selectors must be object")
    base = (cfg.get("target_site") or "").strip()
    if not base.startswith("https://"):
        _fail("Config target_site must be HTTPS")


def _check_route(
    page,
    base_url: str,
    route: str,
    critical_routes: list[str],
    critical_selectors: dict,
    capture_screenshot: bool,
    capture_console: bool,
    run_dir: Path,
    workspace_rel: str,
) -> tuple[dict, list[dict], list[dict], list[dict]]:
    """Returns (checked_route, screenshots, console_errors, raw_findings)."""
    url = base_url.rstrip("/") + (route if route.startswith("/") else "/" + route)
    checked_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    screenshots: list[dict] = []
    console_errors: list[dict] = []
    raw_findings: list[dict] = []

    load_status = "pass"
    nav_status = "pass"
    critical_selector_status = "pass"
    screenshot_path: str | None = None

    try:
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_load_state("networkidle", timeout=15000)
    except Exception as e:
        load_status = "timeout" if "timeout" in str(e).lower() else "fail"
        raw_findings.append({
            "defect_type": "load_failure",
            "severity": "critical" if route == "/" or route in critical_routes else "high",
            "summary": f"Route {route} failed to load: {str(e)[:100]}",
            "affected_route": route,
            "critical": route in critical_routes,
        })
        return (
            {
                "route": route,
                "checked_at": checked_at,
                "load_status": load_status,
                "nav_status": "skipped",
                "critical_selector_status": "skipped",
                "screenshot_path": None,
            },
            screenshots,
            console_errors,
            raw_findings,
        )

    # Nav: for v1, direct navigation = nav pass; broken nav = when route unreachable (already caught by load)
    nav_status = "pass"

    # Critical selectors
    selectors = critical_selectors.get(route, critical_selectors.get("/", []))
    missing: list[str] = []
    empty_selectors: list[str] = []
    for sel in selectors:
        try:
            loc = page.locator(sel)
            if loc.count() == 0:
                missing.append(sel)
            else:
                text = loc.first.inner_text()
                if (text or "").strip() == "" and sel not in ["nav", "main"]:
                    empty_selectors.append(sel)
        except Exception:
            missing.append(sel)

    if missing:
        critical_selector_status = "fail"
        raw_findings.append({
            "defect_type": "missing_critical_section",
            "severity": "high" if route in critical_routes else "medium",
            "summary": f"Route {route} missing critical selector(s): {', '.join(missing[:3])}",
            "affected_route": route,
            "critical": route in critical_routes,
            "selector_missing": missing[0] if missing else None,
        })
    elif empty_selectors:
        critical_selector_status = "fail"
        raw_findings.append({
            "defect_type": "empty_content",
            "severity": "medium" if route in critical_routes else "low",
            "summary": f"Route {route} has empty content for selector(s): {', '.join(empty_selectors[:2])}",
            "affected_route": route,
            "critical": route in critical_routes,
        })

    # Console errors
    if capture_console:
        try:
            logs = page.context.logs if hasattr(page.context, "logs") else []
            for entry in page.context.logs if hasattr(page, "context") else []:
                pass
            # Playwright: page.on("console") - we need to collect during navigation
            # For sync API, we use page.evaluate to get console.errors from window
            # Simpler: listen before goto. Playwright sync_api exposes page.on("console")
            pass
        except Exception:
            pass
        # Console capture: Playwright Python sync_api - console events are async
        # We'll add a simple listener. For v1 minimal: we can skip console if complex
        # and add a placeholder. Or use CDP. Let me check - sync_playwright has page.on("console")
        # Actually we need to attach listener before goto. So we do it in the caller.
        pass

    # Screenshot
    if capture_screenshot:
        slug = _route_slug(route)
        screens_dir = run_dir / "screenshots"
        screens_dir.mkdir(parents=True, exist_ok=True)
        fp = screens_dir / f"{slug}.png"
        try:
            page.screenshot(path=str(fp))
            rel = f"{workspace_rel}/screenshots/{slug}.png"
            screenshot_path = rel
            screenshots.append({
                "path": rel,
                "route": route,
                "captured_at": checked_at,
                "purpose": "evidence" if raw_findings else "route_check",
            })
        except Exception:
            pass

    return (
        {
            "route": route,
            "checked_at": checked_at,
            "load_status": load_status,
            "nav_status": nav_status,
            "critical_selector_status": critical_selector_status,
            "screenshot_path": screenshot_path,
        },
        screenshots,
        console_errors,
        raw_findings,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="B1 Local Website Defect Watcher v1")
    parser.add_argument("--config", required=True, help="Path to watcher config JSON")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_file():
        _fail(f"Config file not found: {config_path}")

    cfg = _load_json(config_path)
    if not isinstance(cfg, dict):
        _fail("Config must be a JSON object")
    _validate_config(cfg)

    watcher_id = (cfg.get("watcher_id") or "").strip()
    target_site = (cfg.get("target_site") or "").strip().rstrip("/")
    allowed_routes = cfg.get("allowed_routes") or []
    critical_routes = cfg.get("critical_routes") or []
    critical_selectors = cfg.get("critical_selectors") or {}
    max_routes = int(cfg.get("max_routes") or 4)
    capture_screenshot = bool(cfg.get("capture_screenshot"))
    capture_console = bool(cfg.get("capture_console"))
    dedupe_window_hours = int(cfg.get("dedupe_window_hours") or 24)
    output_dir = Path(cfg.get("output_dir") or "scratch/local_website_defect_watcher")

    routes = [r for r in allowed_routes if isinstance(r, str)][:max_routes]
    if not routes:
        _fail("No allowed routes to check")

    run_id = f"B1-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    run_dir = WORKSPACE / output_dir / watcher_id / run_id
    workspace_rel = str(output_dir / watcher_id / run_id).replace("\\", "/")
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "screenshots").mkdir(parents=True, exist_ok=True)
    (run_dir / "proposed_defect_packets").mkdir(parents=True, exist_ok=True)

    dedupe = _load_dedupe()
    started_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        _fail("Playwright not installed. Run: pip install playwright && playwright install chromium")

    all_checked: list[dict] = []
    all_screenshots: list[dict] = []
    all_console_errors: list[dict] = []
    all_raw_findings: list[dict] = []
    console_buffer: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            def on_console(msg):
                text = (msg.text or "").strip()
                if not text:
                    return
                level = msg.type or "log"
                if level in ("error", "warning"):
                    console_buffer.append({
                        "route": "",
                        "level": level,
                        "message": text[:500],
                        "captured_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                    })
            page.on("console", on_console)

            for route in routes:
                console_buffer.clear()
                checked, screens, errs, findings = _check_route(
                    page,
                    target_site,
                    route,
                    critical_routes,
                    critical_selectors,
                    capture_screenshot,
                    capture_console,
                    run_dir,
                    workspace_rel,
                )
                for m in console_buffer:
                    m["route"] = route
                all_console_errors.extend(console_buffer)
                all_checked.append(checked)
                all_screenshots.extend(screens)
                all_console_errors.extend(errs)
                for f in findings:
                    f["_route"] = route
                    all_raw_findings.append(f)
        finally:
            browser.close()

    # Filter third-party noise from console
    noise_keywords = [
        "analytics", "advertisement", "gtag", "facebook", "google-analytics",
        "third-party", "websocket", "supabase", "realtime",
    ]
    def _is_noise(msg: str) -> bool:
        lower = msg.lower()
        return any(k in lower for k in noise_keywords)
    filtered_console = [c for c in all_console_errors if not _is_noise(c.get("message", ""))]
    if capture_console and filtered_console:
        for f in all_raw_findings:
            if f.get("defect_type") == "missing_critical_section" and not f.get("evidence"):
                pass
        # Add console_error findings for critical routes
        for ce in filtered_console:
            r = ce.get("route", "")
            if ce.get("level") == "error" and r in critical_routes:
                all_raw_findings.append({
                    "defect_type": "console_error",
                    "severity": "medium",
                    "summary": f"Console error on {r}: {ce.get('message', '')[:80]}",
                    "affected_route": r,
                    "critical": True,
                })

    # Dedupe and build findings with evidence
    findings: list[dict] = []
    finding_counter = 0
    evidence_manifest: list[dict] = []

    for raw in all_raw_findings:
        route = raw.get("affected_route", raw.get("_route", ""))
        defect_type = raw.get("defect_type", "unknown")
        summary = raw.get("summary", "")
        key = _duplicate_key(route, defect_type, summary)
        if _is_duplicate(key, dedupe, dedupe_window_hours):
            continue
        dedupe[key] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        finding_counter += 1
        finding_id = f"B1-FND-{datetime.now().strftime('%Y%m%d')}-{finding_counter:03d}"

        evidence: list[dict] = []
        slug = _route_slug(route)
        screenshot_rel = f"{workspace_rel}/screenshots/{slug}.png"
        for chk in all_checked:
            if chk.get("route") == route and chk.get("screenshot_path"):
                evidence.append({
                    "evidence_type": "screenshot",
                    "path": chk["screenshot_path"],
                    "note": f"{route} page at time of check",
                })
                evidence_manifest.append({
                    "evidence_type": "screenshot",
                    "path": chk["screenshot_path"],
                    "note": f"{route} page at time of check",
                    "finding_id": finding_id,
                })
                break
        if raw.get("selector_missing"):
            evidence.append({
                "evidence_type": "selector_missing",
                "path": raw["selector_missing"],
                "note": "Critical selector absent from DOM",
            })
            evidence_manifest.append({
                "evidence_type": "selector_missing",
                "path": raw["selector_missing"],
                "note": "Critical selector absent from DOM",
                "finding_id": finding_id,
            })
        route_console = [c for c in filtered_console if c.get("route") == route]
        if route_console:
            evidence.append({
                "evidence_type": "console_error",
                "path": f"{workspace_rel}/console_errors.json",
                "note": route_console[0].get("message", "")[:80],
            })
            evidence_manifest.append({
                "evidence_type": "console_error",
                "path": f"{workspace_rel}/console_errors.json",
                "note": route_console[0].get("message", "")[:80],
                "finding_id": finding_id,
            })

        rec_followup = "Verify page renders; check for empty-state, data fetch failure, or build issue"
        findings.append({
            "finding_id": finding_id,
            "defect_type": defect_type,
            "severity": raw.get("severity", "medium"),
            "summary": summary,
            "affected_route": route,
            "critical": raw.get("critical", False),
            "evidence": evidence,
            "duplicate_key": key,
            "recommended_followup": rec_followup,
            "requires_operator_review": True,
        })

        # Write proposed packet
        packet = {
            "packet_id": finding_id,
            "source": watcher_id,
            "target_site": target_site + "/",
            "defect_type": defect_type,
            "severity": raw.get("severity", "medium"),
            "summary": summary,
            "affected_route": route,
            "reproduction_hint": f"Load {target_site}{route}; {raw.get('selector_missing', 'check page')}",
            "evidence": evidence,
            "duplicate_key": key,
            "recommended_followup": rec_followup,
            "operator_status": "pending_review",
        }
        (run_dir / "proposed_defect_packets" / f"{finding_id}.json").write_text(
            json.dumps(packet, indent=2), encoding="utf-8"
        )

    _save_dedupe(dedupe)

    completed_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    status = "completed" if not any(c.get("load_status") == "fail" for c in all_checked) else "partial"
    if all(c.get("load_status") in ("fail", "timeout") for c in all_checked):
        status = "failed"

    recommended_action = "review" if findings else "dismiss"
    run_result = {
        "run_id": run_id,
        "watcher_id": watcher_id,
        "watcher_version": cfg.get("watcher_version", "1.0"),
        "target_site": target_site + "/",
        "started_at": started_at,
        "completed_at": completed_at,
        "status": status,
        "findings": findings,
        "checked_routes": all_checked,
        "screenshots": all_screenshots,
        "console_errors": filtered_console,
        "proposed_packet_count": len(findings),
        "recommended_action": recommended_action,
        "requires_operator_review": bool(findings),
    }

    (run_dir / "run_result.json").write_text(json.dumps(run_result, indent=2), encoding="utf-8")
    (run_dir / "console_errors.json").write_text(json.dumps(filtered_console, indent=2), encoding="utf-8")
    (run_dir / "evidence_manifest.json").write_text(json.dumps(evidence_manifest, indent=2), encoding="utf-8")

    print("B1_WATCHER: PASS")
    print(f"  run_id: {run_id}")
    print(f"  output: {run_dir}")
    print(f"  routes_checked: {len(all_checked)}")
    print(f"  findings: {len(findings)}")
    print(f"  screenshots: {len(all_screenshots)}")
    print(f"  console_errors: {len(filtered_console)}")
    print(f"  proposed_packets: {len(findings)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
