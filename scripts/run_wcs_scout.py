import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# --- Configuration ---
WORKSPACE = Path(r"C:\dev\jarvis-workspace")
REPO = Path(r"C:\dev\wcsv2.0-new")
CONFIG = WORKSPACE / "config" / "wcs_scout_routes.json"
LOG_ROOT = WORKSPACE / "logs" / "wcs_scout"
NORMALIZER_SCRIPT = WORKSPACE / "scripts" / "normalize_scout_to_backlog.py"


def run_cmd(cmd, cwd=None, env=None):
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False
    )
    return result.returncode, result.stdout, result.stderr


def detect_npx():
    for candidate in ["npx.cmd", "npx"]:
        try:
            result = subprocess.run(
                [candidate, "--version"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                shell=False
            )
            if result.returncode == 0:
                return candidate
        except FileNotFoundError:
            continue
    raise FileNotFoundError("Could not find npx or npx.cmd on PATH.")


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def summarize_results(results):
    failures = [r for r in results if r.get("status") != "pass"]
    overall = "PASS" if not failures else "WARN"

    lines = []
    lines.append("=== WCS PUBLIC SCOUT SUMMARY ===")
    lines.append(f"Overall: {overall}")
    lines.append(f"Total routes checked: {len(results)}")
    lines.append(f"Failures: {len(failures)}")
    lines.append("")

    for item in results:
        route = item.get("route", "")
        status = item.get("status", "unknown")
        lines.append(f"[{status.upper()}] {route}")

        for issue in item.get("issues", []):
            lines.append(f" - {issue}")
        for req in item.get("failed_requests", []):
            lines.append(f" - failed request: {req}")
        for err in item.get("console_errors", []):
            lines.append(f" - console: {err}")

    return overall, "\n".join(lines), failures


def main():
    if not CONFIG.exists():
        raise FileNotFoundError(f"Missing config file: {CONFIG}")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = LOG_ROOT / timestamp
    out_dir.mkdir(parents=True, exist_ok=True)

    results_json = out_dir / "public_scout_results.json"
    summary_txt = out_dir / "public_scout_summary.txt"
    stdout_txt = out_dir / "playwright_stdout.txt"
    stderr_txt = out_dir / "playwright_stderr.txt"
    normalizer_report_json = out_dir / "scout_normalizer_report.json"
    normalizer_stdout_txt = out_dir / "normalizer_stdout.txt"
    normalizer_stderr_txt = out_dir / "normalizer_stderr.txt"

    env = os.environ.copy()
    env["WCS_SCOUT_ROUTES_FILE"] = str(CONFIG)
    env["WCS_SCOUT_OUTPUT_FILE"] = str(results_json)
    env["WCS_SCOUT_SCREENSHOT_DIR"] = str(out_dir / "screenshots")

    npx_bin = detect_npx()
    cmd = [
        npx_bin,
        "playwright",
        "test",
        "tests/e2e/public_scout.spec.ts",
        "--reporter=line"
    ]

    print(f"Running scout in {REPO}...")
    returncode, stdout, stderr = run_cmd(cmd, cwd=REPO, env=env)

    write_text(stdout_txt, stdout or "")
    write_text(stderr_txt, stderr or "")

    if results_json.exists():
        results = json.loads(results_json.read_text(encoding="utf-8"))
    else:
        results = [{
            "route": "(scout runner)",
            "status": "fail",
            "issues": ["Scout did not produce public_scout_results.json"],
            "console_errors": [],
            "failed_requests": [],
            "screenshot": ""
        }]

    overall, summary, failures = summarize_results(results)
    write_text(summary_txt, summary)

    normalizer_returncode = None
    normalizer_stdout = ""
    normalizer_stderr = ""

    if NORMALIZER_SCRIPT.exists() and results_json.exists():
        normalizer_cmd = [
            sys.executable,
            str(NORMALIZER_SCRIPT),
            "--workspace",
            str(WORKSPACE),
            "--results",
            str(results_json),
            "--output",
            str(normalizer_report_json),
        ]
        normalizer_returncode, normalizer_stdout, normalizer_stderr = run_cmd(
            normalizer_cmd,
            cwd=WORKSPACE
        )
        write_text(normalizer_stdout_txt, normalizer_stdout or "")
        write_text(normalizer_stderr_txt, normalizer_stderr or "")
    else:
        normalizer_stderr = f"Normalizer script missing or scout results missing: {NORMALIZER_SCRIPT}"
        write_text(normalizer_stderr_txt, normalizer_stderr)

    print(f"WCS SCOUT OVERALL: {overall}")
    print(f"Summary: {summary_txt}")
    print(f"JSON: {results_json}")
    print(f"Stdout: {stdout_txt}")
    print(f"Stderr: {stderr_txt}")
    print(f"Normalizer report: {normalizer_report_json}")
    print(f"Normalizer stdout: {normalizer_stdout_txt}")
    print(f"Normalizer stderr: {normalizer_stderr_txt}")

    if returncode != 0:
        print("\nPlaywright exited with a non-zero code.")
        print(f"Return code: {returncode}")

    if normalizer_returncode not in (None, 0):
        print("\nNormalizer exited with a non-zero code.")
        print(f"Return code: {normalizer_returncode}")

    if failures:
        print("\nDetected scout failures:")
        for item in failures:
            route = item.get("route", "")
            issues = item.get("issues", [])
            if issues:
                for issue in issues:
                    print(f"- {route}: {issue}")
            else:
                print(f"- {route}: failure recorded")


if __name__ == "__main__":
    main()