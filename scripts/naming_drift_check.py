from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class CoreItem:
    name: str
    kind: str  # "script", "doc", or "state"


CORE_ITEMS: List[CoreItem] = [
    CoreItem("jarvis.py", "script"),
    CoreItem("prepare_wcs_task_branch.py", "script"),
    CoreItem("worker_change_check.py", "script"),
    CoreItem("commit_gate_check.py", "script"),
    CoreItem("worker_result_validate.py", "script"),
    CoreItem("qa_result_validate.py", "script"),
    CoreItem("qa_failure_triage.py", "script"),
    CoreItem("stamp_guard_check.py", "script"),
    CoreItem("stamp_result_timestamp.py", "script"),
    CoreItem("pre_reconcile_check.py", "script"),
    CoreItem("reconcile_task_outcome.py", "script"),
    CoreItem("post_reconcile_validate.py", "script"),
    CoreItem("file_registry_check.py", "script"),
    CoreItem("JARVIS_SCRIPT_PROCESS_REFERENCE.md", "doc"),
    CoreItem("JARVIS_TASK_EXECUTION_CHECKLIST.md", "doc"),
    CoreItem("JARVIS_PHASE_CHECKLIST.md", "doc"),
    CoreItem("JARVIS_LIVE_HANDOFF_BUNDLE.md", "doc"),
    CoreItem("file_registry.json", "state"),
    CoreItem("FILE_REGISTRY.md", "state"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only naming drift detector for core Jarvis hardening surfaces. "
            "Checks for obvious inconsistencies between core script/doc names in "
            "live docs and the file registry."
        )
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def expected_path(workspace: Path, item: CoreItem) -> Path:
    if item.kind == "script":
        return (workspace / "scripts" / item.name).resolve()
    if item.kind == "state":
        return (workspace / "state" / item.name).resolve()
    # docs live at workspace root
    return (workspace / item.name).resolve()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_registry_json(path: Path) -> List[Dict[str, object]]:
    import json

    text = read_text(path)
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("file_registry.json root must be a list.")
    return [entry for entry in data if isinstance(entry, dict)]


def build_registry_index(
    entries: List[Dict[str, object]],
) -> Dict[str, List[Dict[str, object]]]:
    by_file: Dict[str, List[Dict[str, object]]] = {}
    for entry in entries:
        name = str(entry.get("file", "")).strip()
        if not name:
            continue
        by_file.setdefault(name, []).append(entry)
    return by_file


def parse_markdown_registry(path: Path) -> List[Tuple[str, str]]:
    text = read_text(path)
    rows: List[Tuple[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        parts = [col.strip() for col in line.split("|")]
        if len(parts) < 4:
            continue
        file_name = parts[1]
        file_path = parts[2]
        if file_name and file_path and file_name != "File" and file_path != "Path":
            rows.append((file_name, file_path))
    return rows


def detect_doc_near_misses(
    docs: Dict[str, str],
    items: List[CoreItem],
    findings: List[str],
) -> None:
    """Detect lines that mention a core script stem without the canonical name."""

    for item in items:
        # Limit near-miss detection to scripts; docs/state often appear without extension
        # in narrative text, which is not considered naming drift for this helper.
        if item.kind != "script":
            continue
        stem = item.name.rsplit(".", 1)[0]
        canonical = item.name
        for doc_name, text in docs.items():
            if stem not in text:
                continue
            if canonical in text:
                continue
            findings.append(
                f"Possible naming drift in {doc_name!r}: references stem {stem!r} "
                f"without canonical name {canonical!r}."
            )


def main() -> int:
    args = parse_args()

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    findings: List[str] = []

    if not workspace.exists():
        print("NAMING DRIFT CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Findings:")
        print("- Workspace path does not exist.")
        return 1

    # Resolve key paths
    docs_to_read = [
        "JARVIS_SCRIPT_PROCESS_REFERENCE.md",
        "JARVIS_TASK_EXECUTION_CHECKLIST.md",
        "JARVIS_PHASE_CHECKLIST.md",
        "JARVIS_LIVE_HANDOFF_BUNDLE.md",
    ]

    doc_texts: Dict[str, str] = {}
    for name in docs_to_read:
        path = workspace / name
        try:
            doc_texts[name] = read_text(path)
        except FileNotFoundError:
            findings.append(f"Missing core live doc: {path}")
        except OSError as exc:
            findings.append(f"Unable to read core live doc {path}: {exc}")

    json_path = workspace / "state" / "file_registry.json"
    md_path = workspace / "state" / "FILE_REGISTRY.md"

    registry_entries: List[Dict[str, object]] = []
    registry_by_file: Dict[str, List[Dict[str, object]]] = {}
    md_rows: List[Tuple[str, str]] = []

    try:
        registry_entries = load_registry_json(json_path)
        registry_by_file = build_registry_index(registry_entries)
    except FileNotFoundError:
        findings.append(f"Missing registry JSON file: {json_path}")
    except Exception as exc:
        findings.append(f"Unable to parse registry JSON file {json_path}: {exc}")

    try:
        md_rows = parse_markdown_registry(md_path)
    except FileNotFoundError:
        findings.append(f"Missing registry markdown file: {md_path}")
    except OSError as exc:
        findings.append(f"Unable to read registry markdown file {md_path}: {exc}")

    md_index = {(file_name, file_path) for file_name, file_path in md_rows}

    # 1) Registry naming consistency for core items.
    for item in CORE_ITEMS:
        expected = str(expected_path(workspace, item))
        rows = registry_by_file.get(item.name, [])
        if not rows:
            findings.append(
                f"Registry JSON missing entry for core item {item.name!r} "
                f"(expected path {expected!r})."
            )
        else:
            # Check whether any row matches the expected path.
            if all(str(row.get("path", "")).strip() != expected for row in rows):
                findings.append(
                    f"Registry JSON path drift for {item.name!r}: "
                    f"expected {expected!r}, saw {[row.get('path') for row in rows]!r}."
                )

        if md_index and (item.name, expected) not in md_index:
            findings.append(
                f"Registry markdown drift for {item.name!r}: "
                f"no row with expected path {expected!r}."
            )

    # 2) Obvious near-miss references in docs for core stems.
    if doc_texts:
        detect_doc_near_misses(doc_texts, CORE_ITEMS, findings)

    if findings:
        print("NAMING DRIFT CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Findings:")
        for msg in findings:
            print(f"- {msg}")
        return 1

    print("NAMING DRIFT CHECK: PASS")
    print(f"Workspace: {workspace}")
    print("Summary:")
    print("- Core live docs and registry surfaces were readable.")
    print("- Core script/doc/state names matched between registry JSON, FILE_REGISTRY.md, and expected paths.")
    print("- No obvious naming drift or near-miss references were detected for current core items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

