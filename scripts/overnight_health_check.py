import json
import shutil
import socket
import subprocess
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(r"C:\dev\jarvis-workspace")
STATE_DIR = WORKSPACE / "state"
LOGS_DIR = WORKSPACE / "logs"
WCS_REPO = Path(r"C:\dev\wcsv2.0-new")

MASTER_BACKLOG_JSON = STATE_DIR / "master_backlog.json"
PACKAGE_JSON = WCS_REPO / "package.json"
HOME_SPEC = WCS_REPO / "tests" / "e2e" / "home.spec.ts"
GLOBAL_SETUP = WCS_REPO / "tests" / "e2e" / "helpers" / "global-setup.ts"


def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            shell=False
        )
        return {
            "ok": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": (result.stdout or "").strip(),
            "stderr": (result.stderr or "").strip(),
        }
    except FileNotFoundError as e:
        return {
            "ok": False,
            "returncode": -1,
            "stdout": "",
            "stderr": str(e),
        }
    except Exception as e:
        return {
            "ok": False,
            "returncode": -1,
            "stdout": "",
            "stderr": str(e),
        }


def detect_npm():
    npm_cmd = run_cmd(["npm.cmd", "--version"])
    if npm_cmd["ok"]:
        return npm_cmd
    return run_cmd(["npm", "--version"])


def check_port(host="127.0.0.1", port=3000, timeout=1.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        return s.connect_ex((host, port)) == 0
    finally:
        s.close()


def safe_read_text(path: Path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def load_backlog_counts(path: Path):
    counts = {
        "total": 0,
        "done": 0,
        "ready": 0,
        "dispatched": 0,
        "blocked": 0,
        "escalated": 0,
        "other": 0,
    }
    if not path.exists():
        return counts

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            return counts

        counts["total"] = len(data)
        for item in data:
            status = str(item.get("status", "")).strip().lower()
            if status in counts:
                counts[status] += 1
            else:
                counts["other"] += 1
        return counts
    except Exception:
        return counts


def git_info(repo: Path):
    if not repo.exists():
        return {
            "repo_exists": False,
            "branch": "",
            "status_clean": False,
            "dirty_files": [],
        }

    branch = run_cmd(["git", "branch", "--show-current"], cwd=repo)
    status = run_cmd(["git", "status", "--porcelain"], cwd=repo)

    dirty_files = []
    if status["stdout"]:
        dirty_files = status["stdout"].splitlines()

    return {
        "repo_exists": True,
        "branch": branch["stdout"] if branch["ok"] else "",
        "status_clean": len(dirty_files) == 0,
        "dirty_files": dirty_files,
    }


def docker_info():
    docker_version = run_cmd(["docker", "--version"])
    if not docker_version["ok"]:
        return {
            "docker_available": False,
            "containers": [],
        }

    ps = run_cmd(["docker", "ps", "--format", "{{.Names}}|{{.Image}}|{{.Status}}"])
    containers = ps["stdout"].splitlines() if ps["ok"] and ps["stdout"] else []

    return {
        "docker_available": True,
        "containers": containers,
    }


def main():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    json_path = LOGS_DIR / f"overnight_health_{timestamp}.json"
    txt_path = LOGS_DIR / f"overnight_health_{timestamp}.txt"

    disk = shutil.disk_usage(str(WORKSPACE.anchor if WORKSPACE.anchor else "C:\\"))

    python_v = run_cmd([sys.executable, "--version"])
    node_v = run_cmd(["node", "--version"])
    npm_v = detect_npm()

    git = git_info(WCS_REPO)
    backlog = load_backlog_counts(MASTER_BACKLOG_JSON)
    docker = docker_info()

    package_text = safe_read_text(PACKAGE_JSON)
    global_setup_text = safe_read_text(GLOBAL_SETUP)

    smoke_script_exists = '"test:e2e:smoke"' in package_text
    home_spec_exists = HOME_SPEC.exists()
    wait_for_server_ready_exists = "waitForServerReady" in global_setup_text
    port_3000_open = check_port()

    warnings = []

    if not WCS_REPO.exists():
        warnings.append("WCS repo path is missing.")
    if not git["status_clean"]:
        warnings.append("WCS repo has uncommitted changes.")
    if not smoke_script_exists:
        warnings.append("Smoke test script is missing from package.json.")
    if not home_spec_exists:
        warnings.append("tests/e2e/home.spec.ts is missing.")
    if not wait_for_server_ready_exists:
        warnings.append("waitForServerReady helper is missing from global-setup.ts.")
    if backlog["dispatched"] > 0:
        warnings.append(f"There are {backlog['dispatched']} dispatched task(s) still open.")
    if backlog["blocked"] > 0:
        warnings.append(f"There are {backlog['blocked']} blocked task(s).")
    if disk.free < 20 * 1024 * 1024 * 1024:
        warnings.append("Disk free space is below 20 GB.")
    if not node_v["ok"]:
        warnings.append("Node is not available.")
    if not npm_v["ok"]:
        warnings.append("npm is not available.")

    overall_status = "PASS" if len(warnings) == 0 else "WARN"

    report = {
        "timestamp": timestamp,
        "overall_status": overall_status,
        "workspace": str(WORKSPACE),
        "wcs_repo": str(WCS_REPO),
        "disk": {
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "free_gb": round(disk.free / (1024 ** 3), 2),
        },
        "tools": {
            "python": python_v["stdout"] or python_v["stderr"],
            "node": node_v["stdout"] or node_v["stderr"],
            "npm": npm_v["stdout"] or npm_v["stderr"],
        },
        "wcs_repo_health": {
            "repo_exists": git["repo_exists"],
            "branch": git["branch"],
            "status_clean": git["status_clean"],
            "dirty_files": git["dirty_files"],
            "port_3000_open": port_3000_open,
            "smoke_script_exists": smoke_script_exists,
            "home_spec_exists": home_spec_exists,
            "waitForServerReady_exists": wait_for_server_ready_exists,
        },
        "backlog_counts": backlog,
        "docker": docker,
        "warnings": warnings,
    }

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = []
    lines.append("=== OVERNIGHT HEALTH CHECK ===")
    lines.append(f"Timestamp: {timestamp}")
    lines.append(f"Overall status: {overall_status}")
    lines.append("")
    lines.append("--- Disk ---")
    lines.append(f"Free GB: {report['disk']['free_gb']}")
    lines.append("")
    lines.append("--- Tools ---")
    lines.append(f"Python: {report['tools']['python']}")
    lines.append(f"Node:   {report['tools']['node']}")
    lines.append(f"npm:    {report['tools']['npm']}")
    lines.append("")
    lines.append("--- WCS Repo ---")
    lines.append(f"Repo exists: {git['repo_exists']}")
    lines.append(f"Branch: {git['branch']}")
    lines.append(f"Clean: {git['status_clean']}")
    lines.append(f"Port 3000 open: {port_3000_open}")
    lines.append(f"Smoke script exists: {smoke_script_exists}")
    lines.append(f"Home spec exists: {home_spec_exists}")
    lines.append(f"waitForServerReady exists: {wait_for_server_ready_exists}")
    if git["dirty_files"]:
        lines.append("Dirty files:")
        for f in git["dirty_files"]:
            lines.append(f"  - {f}")
    lines.append("")
    lines.append("--- Backlog ---")
    for k, v in backlog.items():
        lines.append(f"{k}: {v}")
    lines.append("")
    lines.append("--- Docker ---")
    lines.append(f"Docker available: {docker['docker_available']}")
    if docker["containers"]:
        for c in docker["containers"]:
            lines.append(f"  - {c}")
    lines.append("")
    lines.append("--- Warnings ---")
    if warnings:
        for w in warnings:
            lines.append(f"- {w}")
    else:
        lines.append("None")

    txt_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"OVERALL: {overall_status}")
    print(f"JSON log: {json_path}")
    print(f"TXT log:  {txt_path}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"- {w}")


if __name__ == "__main__":
    main()