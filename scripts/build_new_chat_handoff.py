"""
One-off script to build JARVIS_NEW_CHAT_HANDOFF_BUNDLE_2026-03-14.md.
Reads all 14 source files and writes one markdown file with context anchor,
current truth, TOC, and full verbatim embedded files.
"""
from pathlib import Path
import sys

WORKSPACE = Path(__file__).resolve().parent.parent
OUT_PATH = WORKSPACE / "JARVIS_NEW_CHAT_HANDOFF_BUNDLE_2026-03-14.md"

FILES = [
    ("scripts/run_cursor_worker.py", "Agent-first Cursor invocation bridge; proven on WCS-042."),
    ("scripts/run_guarded_task_cycle.py", "Orchestrates guarded task-cycle helpers; stops on first failure."),
    ("scripts/draft_worker_result_from_evidence.py", "Drafts truthful worker result from repo evidence; live and proven."),
    ("scripts/worker_result_validate.py", "Read-only worker-result schema validator."),
    ("scripts/qa_result_validate.py", "Read-only QA-result schema validator."),
    ("tasks/WCS-042_task.json", "Example WCS-042 task packet (successful cycle)."),
    ("results/WCS-042_worker_result.json", "Example WCS-042 worker result (drafted then stamped)."),
    ("qa/WCS-042_qa_result.json", "Example WCS-042 QA result (manual QA then stamped)."),
    ("JARVIS_SCRIPT_PROCESS_REFERENCE.md", "Live reference for WCS task execution process and hardening."),
    ("JARVIS_LIVE_HANDOFF_BUNDLE.md", "Live handoff bundle: system truth, hardening state, helper surfaces."),
    ("JARVIS_PHASE_CHECKLIST.md", "Phase-by-phase rebuild checklist and next priorities."),
    ("cursor_prompt_templates.md", "Reusable Cursor prompt templates for Jarvis tasks."),
    ("state/file_registry.json", "Machine-readable file registry (source for FILE_REGISTRY.md)."),
    ("state/FILE_REGISTRY.md", "Human-readable file registry rendered from JSON."),
]


def max_backticks(content: str) -> int:
    """Longest run of backticks in content."""
    n = 0
    run = 0
    for c in content:
        if c == "`":
            run += 1
        else:
            n = max(n, run)
            run = 0
    return max(n, run)


def fence_for(content: str, ext: str) -> str:
    """Use a fence longer than any backtick run in content so embedded code blocks don't close it. Minimum 3 for valid fenced block."""
    k = max_backticks(content)
    return "`" * max(3, k + 1)


def read_file(rel_path: str) -> str:
    p = WORKSPACE / rel_path
    return p.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    lines = []

    # --- Title and intro
    lines.append("# JARVIS New Chat Handoff Bundle — 2026-03-14")
    lines.append("")
    lines.append("Single markdown handoff for a new ChatGPT (or Cursor) window. Attach this file only to continue the Jarvis rebuild without restarting from theory.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Table of contents
    lines.append("## Table of contents")
    lines.append("")
    lines.append("1. [Context anchor](#context-anchor)")
    lines.append("2. [Current truth](#current-truth)")
    for i, (rel, _) in enumerate(FILES, start=3):
        anchor = rel.replace("/", "-").replace(" ", "-").replace(".", "-")
        lines.append(f"{i}. [{rel}](#embedded-{anchor})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Context anchor
    lines.append("## Context anchor")
    lines.append("")
    lines.append("- **Project roots:** Local-first Jarvis rebuild in `jarvis-workspace`; WCS website is the first active proof domain; state is markdown + JSON; Cursor is the semi-manual worker; Playwright is QA.")
    lines.append("- **What Jarvis is:** A local Python foreman/orchestrator that reads state, selects one bounded WCS task, writes task packets, prepares the task branch, and records outcomes. Jarvis does not perform the code change or QA; it coordinates the loop.")
    lines.append("- **What is already proven:** Agent-first `run_cursor_worker.py` (task repo workspace, Agent CLI or cursor launcher); successful guarded WCS-042 cycle (worker implementation → draft_worker_result_from_evidence → stamp → QA → reconcile); `draft_worker_result_from_evidence.py` is live and proven.")
    lines.append("- **Next build target:** `draft_qa_result_from_evidence.py` — draft truthful QA result JSON from evidence (same honesty/stamp rules as draft_worker_result).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Current truth
    lines.append("## Current truth")
    lines.append("")
    lines.append("- **Agent-first `run_cursor_worker.py`:** Prefers Cursor Agent CLI (`agent`), falls back to desktop cursor launcher; runs handoff against **task repo workspace** from packet; uses `--workspace` and `--trust`; does not fabricate worker completion.")
    lines.append("- **Successful guarded WCS-042 cycle:** Full loop: run_cursor_worker → implementation → draft_worker_result_from_evidence → stamp_guard_check → stamp both results → pre_reconcile_check → reconcile → post_reconcile_validate.")
    lines.append("- **`draft_worker_result_from_evidence.py`:** Already live and proven; drafts worker result from task packet + repo evidence (branch, changed files); does not stamp or reconcile; operator reviews before post-worker.")
    lines.append("- **Current remaining manual gap:** QA result JSON is still filled and stamped manually after running build + Playwright smoke; no script yet drafts QA result from evidence.")
    lines.append("- **Next target:** `draft_qa_result_from_evidence.py` — draft truthful QA result from build/test evidence; same discipline as draft_worker_result (no stamp, no fabricate; operator reviews).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Embedded files
    missing = []
    for rel_path, why in FILES:
        full_path = WORKSPACE / rel_path
        anchor = rel_path.replace("/", "-").replace(" ", "-").replace(".", "-")
        lines.append(f"## Embedded: {rel_path}")
        lines.append("")
        lines.append(f"**Path:** `{rel_path}`")
        lines.append("")
        lines.append(f"**Why it matters:** {why}")
        lines.append("")
        if not full_path.exists():
            missing.append((rel_path, "file not found"))
            lines.append("*(File not found; could not embed.)*")
            lines.append("")
            continue
        try:
            content = read_file(rel_path)
        except Exception as e:
            missing.append((rel_path, str(e)))
            lines.append(f"*(Could not read: {e})*")
            lines.append("")
            continue
        ext = full_path.suffix.lstrip(".")
        if ext == "py":
            lang = "python"
        elif ext == "json":
            lang = "json"
        else:
            lang = ext or "text"
        fence = fence_for(content, ext)
        lines.append(fence + lang)
        lines.append(content.rstrip())
        lines.append(fence)
        lines.append("")
        lines.append("---")
        lines.append("")

    out_text = "\n".join(lines)
    OUT_PATH.write_text(out_text, encoding="utf-8", newline="\n")
    print("Wrote:", OUT_PATH)
    print("Included files:", len(FILES) - len(missing), "/", len(FILES))
    if missing:
        for path, reason in missing:
            print("  Could not embed:", path, "—", reason)
    return 0


if __name__ == "__main__":
    sys.exit(main())
