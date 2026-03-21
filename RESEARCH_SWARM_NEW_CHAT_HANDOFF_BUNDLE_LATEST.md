# Research Swarm — New Chat Handoff Bundle

**Date:** 2026-03-21  
**Purpose:** Transfer context to next conversation. Attach this file to a new chat so it can continue from current state without re-discovering the project.

**Workspace root:** `C:\dev\jarvis-workspace`  
**Module path:** `future_modules/research_swarm/`  
**Current status:** Phase A collector; dashboard review page at `/research-swarm` (R55).

---

## 1. Current Live Truth

**What Research Swarm supports:**
- GitHub + generic article/webpage discovery and acquisition
- **Phase A collector:** Unattended bounded collection on operator URL list + optional discovery
- Extractor API v1 (bounded assistive drafting, QUALIFIED PASS)
- Single-run: `run_pipeline.py` — discovery → acquisition → extraction
- Batch: `run_batch.py` — up to 10 runs
- Broader corpus eval: `run_broader_corpus_eval.py` — real URL list

**What is proven:**
- Phase A collector smoke-proven (skip/log restricted, unsupported; ledger + run summary)
- Two-source-class lane (GitHub + article) hardened
- Real broader-corpus eval on operator list (R53)
- Dashboard Research Swarm page at `/research-swarm` (R55) — reads `phase_a_run_summary_*.json` + `phase_a_collection_ledger.jsonl`

**What is automated:**
- Phase A: URL list + optional discovery → collect → ledger (bounded, unattended)
- Discovery, acquisition, extraction (single-run and batch)
- Hourly scheduling path via ops scripts (no-overlap lock)

**What is still manual:**
- Evaluator, archivist
- Human review after collection

**Collection review:** Files (summary JSON/MD, ledger) + dashboard page `/research-swarm`.

**What is not integrated:**
- Jarvis export, orchestration
- Video/X/Twitter/Reddit sources (skip/log)

**Current bottleneck:** Extraction schema (LLM enum drift) and restricted/paywalled skips. Full-list run on Example URLs.txt (R55) produced 48 success, 6 partial, 2 fail, 1 restricted skip, 31 unsupported skip.

---

## 2. Exact Process/Checklist Position

**Done:**
- Phase A collector (run_phase_a_collector.py)
- Bounded discovery query file support
- Skip/log restricted + unsupported
- Ops scripts (run once, register hourly)
- Broader corpus eval (real list)
- Extractor API v1, discovery, acquisition, single-run, batch
- Dashboard Research Swarm page (R55)

**Current:**
- Phase A unattended bounded collector
- Scheduling goal: hourly, no overlap
- Purpose: durable collection data for later review/learning

**Deferred:**
- Evaluator/archivist automation
- Video/X/Twitter/Reddit
- Jarvis export/orchestration

**Active position:** Phase A collector; collection-review surface is files + dashboard page; bottleneck from full-list run: extraction schema and restricted skips.

---

## 3. Operator Rules for the Next Chat

- **Cursor response format:** Model → Prompt/code → What to expect → Then wait
- **Number every prompt:** Use `PROMPT NUMBER: #N` at top and bottom
- **Require tags:** Put `<prompt #N - RN>` at top of responses
- **Keep prompts tight:** Low-overreach, constrained scope
- **Do not stop and ask what to do next** unless: error, blocker, or checklist section just completed
- **Process-map format:** When asked where we are: exact current spot, phase ladder, done/not done, checklist fit, honest status
- **Discovery/search:** Prioritize most recent relevant sources when metadata supports it

---

## 4. Critical File Map

### Side-quest state artifacts
| File | Why |
|------|-----|
| `SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md` | Current direction, weakness profile |
| `SIDE_QUEST_PROCESS_CHECKLIST_RESEARCH_SWARM.md` | Done/active/deferred |
| `SIDE_QUEST_HANDOFF_BUNDLE_RESEARCH_SWARM_LATEST.md` | Summary, file list |

### Current scripts
| File | Why |
|------|-----|
| `future_modules/research_swarm/scripts/run_phase_a_collector.py` | Phase A collector; URL list + optional discovery |
| `future_modules/research_swarm/ops/run_phase_a_collector_once.ps1` | Run once (no-overlap) |
| `future_modules/research_swarm/ops/register_phase_a_hourly_task.ps1` | Register hourly task |
| `future_modules/research_swarm/scripts/run_pipeline.py` | Single-run orchestration |
| `future_modules/research_swarm/scripts/run_batch.py` | Batch runner (up to 10) |
| `future_modules/research_swarm/scripts/run_discovery.py` | GitHub discovery |
| `future_modules/research_swarm/scripts/run_discovery_article.py` | Article discovery |
| `future_modules/research_swarm/scripts/run_acquisition.py` | Packet acquisition |
| `future_modules/research_swarm/scripts/run_extractor_api.py` | Extraction API CLI |

### Key helpers (selection/queue/packet)
| File | Why |
|------|-----|
| `scripts/discovery/triage_helper.py` | Priority assignment; order preserved from discovery |
| `scripts/discovery/candidate_filter.py` | Filters junk; does not filter awesome-lists |
| `scripts/discovery/queue_writer.py` | Writes discovery queue JSON |
| `scripts/acquisition/source_classifier.py` | github vs article from URL |

### Schemas
| File | Why |
|------|-----|
| `schemas/source_intake.schema.json` | Packet contract |
| `schemas/extraction_report.schema.json` | Extraction output contract |

### Key examples and outputs
| File | Why |
|------|-----|
| `docs/Example URLs.txt` | Operator real URL list |
| `examples/phase_a_discovery_queries.json` | Bounded discovery input |
| `examples/phase_a_smoke_urls.txt` | Smoke-test URL subset |
| `outputs/phase_a_collection_ledger.jsonl` | Cumulative collection ledger |
| `outputs/phase_a_run_summary_*.json` | Per-run summary |
| `examples/batch_runs_10_collection.json` | Batch input |
| `outputs/extractor_api_stage_decision.md` | QUALIFIED PASS basis |

---

## 5. Pasted File Contents

### Side-quest state files

**SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md** (abbreviated — full file at workspace root)

```markdown
# Research Swarm — Side Quest Context Anchor

**Last updated:** 2026-03-21  
**Purpose:** New-chat handoff anchor for Research Swarm continuation work.

---

## What This Side Quest Is

- **Research Swarm** — planned Jarvis input-learning engine
- Transforms raw research sources (GitHub, article/webpage) into structured knowledge for evaluation and archiving
- Manual flow: source packet → extract → evaluate → archive
- **Extractor API v1** — scaffold hardened, QUALIFIED PASS (bounded assistive drafting)
- **Discovery / Intake** — implemented for GitHub + generic article/webpage
- **Content Acquisition** — implemented for GitHub + generic article/webpage
- **Single-run automation wrapper** — implemented, hardened, proven for both source classes
- **Bounded batch runner** — up to 10 runs, preserves per-run artifacts, writes batch summary
- **Real 10-run collection batch** — executed successfully; stored artifacts now exist for later use
- Collection shows meaningful quality variation (strong, medium, thin runs)
- Human review still mandatory
- Evaluator and archivist remain manual

---

## What This Side Quest Is Not

- Not an active Jarvis runtime module
- Not integrated with Jarvis Dashboard, export, or orchestration
- Not evaluator or archivist API automation
- Not unattended or scheduled
- Not video/X/Twitter/Reddit source support yet
- Not broad production trust

---

## Current Maturity / Status

| Label | Status |
|-------|--------|
| **Extractor API v1** | QUALIFIED PASS — bounded assistive drafting |
| **Discovery** | Implemented — GitHub + article/webpage |
| **Acquisition** | Implemented — GitHub + article/webpage |
| **Single-run automation** | Implemented, hardened, proven for both source classes |
| **Batch runner** | Implemented, proven — up to 10 runs |
| **10-run stored collection** | Proven — discovery, packets, extractions, summaries, batch summary, collection review |
| **Integrated with Jarvis** | No |
| **Human review** | Mandatory |
| **Evaluator / Archivist** | Manual |

---

## Known Weakness Profile

- **Selection quality:** Clearest bottleneck — first-candidate picks sometimes weak (curated lists, journey overviews vs implementation)
- **Article freshness:** Weaker metadata than GitHub freshness (DDG-based)
- **Selection rule:** Simple first-candidate; no operator override
- **Mixed-result batch:** Implemented; this 10-run proof was all-success
- **Video/X/Twitter:** Not yet implemented
- **Not unattended:** Operator-triggered only; human review mandatory

---

## What the Next Chat Should Do First

1. Read `SIDE_QUEST_HANDOFF_BUNDLE_RESEARCH_SWARM_LATEST.md` (workspace root)
2. Inspect `future_modules/research_swarm/outputs/pipeline_batch_collection_review_20260321-061000.md`
3. Inspect `future_modules/research_swarm/outputs/pipeline_batch_summary_20260321-060906.md`
4. Decide next bounded move:
   - **Option A:** Selector-quality tightening pass (e.g., filter awesome-lists, prefer implementation repos)
   - **Option B:** Video/transcript build planning (accept current selector quality consciously)
```

**SIDE_QUEST_PROCESS_CHECKLIST / HANDOFF_BUNDLE:** See workspace root. Key: done=10-run batch; active=selector-quality or video planning; deferred=evaluator, archivist, video, X, Jarvis.

---

### Core scripts (full contents)

#### run_pipeline.py

```python
#!/usr/bin/env python3
"""
Bounded pipeline: discovery -> acquisition -> extraction.
Operator-triggered. Runs discovery, selects first candidate, acquires, extracts.
Supports: github, article. Unsupported source classes fail clearly.
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_MODULE_ROOT = _SCRIPT_DIR.parent
_OUTPUTS = _MODULE_ROOT / "outputs"

SUPPORTED_SOURCE_CLASSES = frozenset({"github", "article"})
SELECTION_RULE = "First candidate in discovery queue (index 0). Queue pre-ranked by discovery (GitHub: freshness-first; Article: DDG order)."

def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)

def _run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

def main() -> int:
    parser = argparse.ArgumentParser(description="Bounded pipeline: discovery -> acquisition -> extraction.")
    parser.add_argument("--query", "-q", required=True)
    parser.add_argument("--source-class", choices=["github", "article"], default="github")
    parser.add_argument("--max", type=int, default=5)
    args = parser.parse_args()
    query = args.query.strip()
    source_class = args.source_class
    if source_class not in SUPPORTED_SOURCE_CLASSES:
        print(f"Error: Source class '{source_class}' not supported.", file=sys.stderr)
        return 1
    run_id = _run_id()
    outputs = _OUTPUTS.resolve()
    outputs.mkdir(parents=True, exist_ok=True)
    if source_class == "github":
        discovery_path = outputs / f"discovery_queue_{run_id}.json"
    else:
        discovery_path = outputs / f"discovery_queue_article_{run_id}.json"
    packet_path = outputs / f"source_packet_{run_id}.json"
    extraction_path = outputs / f"extraction_report_{run_id}_api.json"
    summary_path = outputs / f"pipeline_run_summary_{run_id}.md"
    summary = {"query": query, "source_class": source_class, "run_id": run_id, "selection_rule": SELECTION_RULE,
               "discovery_path": None, "packet_path": None, "extraction_path": None, "selected_url": None,
               "selected_priority": None, "result": None, "failure_step": None, "failure_detail": None}
    # Step 1: Discovery
    cmd = [sys.executable, "run_discovery.py" if source_class == "github" else "run_discovery_article.py",
           "-q", query, "--max", str(args.max), "--out", str(discovery_path)]
    r = _run(cmd, _SCRIPT_DIR)
    if r.returncode != 0:
        summary["failure_step"], summary["failure_detail"] = "discovery", (r.stderr or r.stdout or "Unknown").strip()
        _write_summary(summary_path, summary)
        print(f"Result: FAILED | Step: discovery | Summary: {summary_path}", file=sys.stderr)
        return 1
    if not discovery_path.exists():
        summary["failure_step"], summary["failure_detail"] = "discovery", f"Artifact not found: {discovery_path}"
        _write_summary(summary_path, summary)
        print(f"Result: FAILED | Step: discovery | Summary: {summary_path}", file=sys.stderr)
        return 1
    summary["discovery_path"] = str(discovery_path.resolve())
    # Load queue, select first candidate
    queue = json.load(open(discovery_path, encoding="utf-8"))
    candidates = queue.get("candidates") or []
    if not candidates:
        summary["failure_step"], summary["failure_detail"] = "discovery", "No candidates in queue"
        _write_summary(summary_path, summary)
        print(f"Result: FAILED | Step: discovery | Summary: {summary_path}", file=sys.stderr)
        return 1
    selected = candidates[0]  # <-- SELECTION: first candidate only
    selected_url = selected.get("source_url", "").strip()
    selected_priority = selected.get("priority", "unknown")
    summary["selected_url"], summary["selected_priority"] = selected_url, selected_priority
    # Step 2: Acquisition
    r = _run([sys.executable, "run_acquisition.py", "--url", selected_url, "--out", str(packet_path)], _SCRIPT_DIR)
    if r.returncode != 0 or not packet_path.exists():
        summary["failure_step"], summary["failure_detail"] = "acquisition", (r.stderr or "Packet not found").strip()
        _write_summary(summary_path, summary)
        print(f"Result: FAILED | Step: acquisition | Summary: {summary_path}", file=sys.stderr)
        return 1
    summary["packet_path"] = str(packet_path.resolve())
    # Step 3: Extraction
    r = _run([sys.executable, "run_extractor_api.py", "--packet", str(packet_path)], _SCRIPT_DIR)
    if r.returncode != 0 or not extraction_path.exists():
        summary["failure_step"], summary["failure_detail"] = "extraction", (r.stderr or "Extraction not found").strip()
        _write_summary(summary_path, summary)
        print(f"Result: FAILED | Step: extraction | Summary: {summary_path}", file=sys.stderr)
        return 1
    summary["extraction_path"] = str(extraction_path.resolve())
    summary["result"] = "SUCCESS"
    _write_summary(summary_path, summary)
    print("Pipeline complete")
    print(f"Result: SUCCESS | Run ID: {run_id} | Source: {source_class}")
    print(f"Summary: {summary_path}")
    return 0

def _write_summary(path: Path, summary: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Pipeline Run Summary", "", f"**Run ID:** {summary['run_id']}", f"**Query:** {summary['query']}",
             f"**Source class:** {summary['source_class']}", "", "## Selected candidate",
             f"- URL: {summary.get('selected_url') or 'N/A'}", f"- Priority: {summary.get('selected_priority') or 'N/A'}",
             "", "## Artifacts", f"- Discovery: {summary.get('discovery_path') or 'N/A'}",
             f"- Packet: {summary.get('packet_path') or 'N/A'}", f"- Extraction: {summary.get('extraction_path') or 'N/A'}",
             "", "## Result", f"- **{summary.get('result') or 'FAILED'}**"]
    if summary.get("failure_step"):
        lines.extend(["", "## Failure", f"- Step: {summary['failure_step']}", f"- Detail: {summary.get('failure_detail') or 'Unknown'}"])
    path.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    sys.exit(main())
```

#### run_batch.py

```python
#!/usr/bin/env python3
"""
Bounded batch runner: runs the single-run pipeline multiple times.
Accepts JSON with "runs" array. Max 10 entries. source_class: github | article.
"""

import argparse, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_MODULE_ROOT = _SCRIPT_DIR.parent
_OUTPUTS = _MODULE_ROOT / "outputs"
SUPPORTED_SOURCE_CLASSES = frozenset({"github", "article"})
MAX_BATCH_ENTRIES = 10

def _run_pipeline(query: str, source_class: str, max_results: int = 5):
    r = subprocess.run([sys.executable, "run_pipeline.py", "-q", query, "--source-class", source_class, "--max", str(max_results)],
                      cwd=str(_SCRIPT_DIR), capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def _parse_result_and_summary(stdout: str, stderr: str):
    combined = (stdout + "\n" + stderr).strip()
    result, run_id, summary_path = None, None, None
    for line in combined.splitlines():
        if line.startswith("Result:"):
            result = "SUCCESS" if "SUCCESS" in line else "FAILED"
            m = re.search(r"Run ID:\s*(\S+)", line)
            if m: run_id = m.group(1)
        if line.startswith("Summary:"):
            summary_path = line.replace("Summary:", "").strip() or None
    return result, run_id, summary_path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path, required=True)
    args = parser.parse_args()
    data = json.load(open(args.input.resolve(), encoding="utf-8"))
    runs = data.get("runs")
    if not isinstance(runs, list) or len(runs) == 0:
        print("Error: Batch input must have non-empty 'runs' array.", file=sys.stderr)
        return 1
    if len(runs) > MAX_BATCH_ENTRIES:
        print(f"Error: Batch has {len(runs)} entries; max is {MAX_BATCH_ENTRIES}.", file=sys.stderr)
        return 1
    for i, e in enumerate(runs):
        if not isinstance(e, dict) or not e.get("query", "").strip():
            print(f"Error: Run {i+1} missing or empty 'query'.", file=sys.stderr)
            return 1
        sc = e.get("source_class", "").strip().lower()
        if sc not in SUPPORTED_SOURCE_CLASSES:
            print(f"Error: Run {i+1} source_class '{sc}' not supported.", file=sys.stderr)
            return 1
    results, succeeded, failed = [], 0, 0
    for i, entry in enumerate(runs):
        query = entry.get("query", "").strip()
        source_class = entry.get("source_class", "github").strip().lower()
        max_results = entry.get("max_results", 5) or 5
        exit_code, stdout, stderr = _run_pipeline(query, source_class, max_results)
        result_line, run_id, summary_path = _parse_result_and_summary(stdout, stderr)
        outcome = "SUCCESS" if (exit_code == 0 and result_line == "SUCCESS") else "FAILED"
        if outcome == "SUCCESS": succeeded += 1
        else: failed += 1
        results.append({"index": i+1, "query": query, "source_class": source_class, "outcome": outcome, "run_id": run_id, "summary_path": summary_path})
    batch_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    batch_summary_path = _OUTPUTS / f"pipeline_batch_summary_{batch_id}.md"
    _OUTPUTS.mkdir(parents=True, exist_ok=True)
    lines = ["# Pipeline Batch Summary", "", f"**Batch ID:** {batch_id}", f"**Total runs:** {len(runs)}", f"**Succeeded:** {succeeded}", f"**Failed:** {failed}", "", "## Per-run results", ""]
    for r in results:
        lines.append(f"### Run {r['index']}: {r['outcome']}")
        lines.append(f"- Query: {r['query']}")
        lines.append(f"- Source: {r['source_class']}")
        if r.get("summary_path"): lines.append(f"- Summary: {r['summary_path']}")
        lines.append("")
    batch_summary_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Succeeded: {succeeded} | Failed: {failed}")
    print(f"Batch summary: {batch_summary_path}")
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
```

#### run_discovery.py

Calls `discovery.github_search.search_repositories`, `candidate_filter.filter_and_dedupe`, `triage_helper.triage_candidates`, `queue_writer.write_queue`. Output: `discovery_queue_{run_id}.json`. Freshness-first: sort=updated, order=desc.

#### run_discovery_article.py

Uses DDG search or --urls/--url. Output: `discovery_queue_article_{run_id}.json`. Source class: article. Freshness limited.

#### run_acquisition.py

Uses `source_classifier.classify_from_url`, `handlers.get_handler`, `packet_builder`, `validate_packet`. Output: `source_packet_{run_id}.json`.

#### run_extractor_api.py

Loads packet, calls `extractor_api_client.generate_extraction`, `extractor_api_validate.validate_extraction_report`, writes `extraction_report_{suffix}_api.json`.

---

### Key helpers (selection-related)

#### discovery/triage_helper.py

```python
def triage_candidates(candidates):
    """Assign priority and selection_reason. Freshness-first: candidates pre-sorted by updated desc."""
    for i, c in enumerate(candidates):
        low_signal = (stars == 0 and desc_len < 50)
        if i < 3: base_priority = "high"
        elif i < 7: base_priority = "medium"
        else: base_priority = "low"
        if low_signal and base_priority == "high":
            priority = "medium"  # Demote low-signal
        else:
            priority = base_priority
        # selection_reason combines: "Matches query", stars, "recently updated", "README likely"
```

**Note:** Order is NOT changed. First candidate stays first. Pipeline selects `candidates[0]`.

#### discovery/candidate_filter.py

Filters: placeholder/short description + 0 stars; example/demo repos (-example, -demo in name) with 0 stars. Does NOT filter awesome-*, journey-*, or curated lists.

---

### Schemas

#### source_intake.schema.json (excerpt)

Required: `packet_id`, `source_url`, `source_type`, `raw_content`, `created_at`. `source_type` enum: youtube, reddit, github, article. Supported in acquisition: github, article.

#### extraction_report.schema.json (excerpt)

Required: `report_id`, `packet_id`, `source_url`, `created_at`, `summary`, `methods_tools_patterns`, `key_claims`, `hype_signals`, `open_questions`. `methods_tools_patterns[].category`: method | tool | pattern.

---

### Key proof artifacts

#### pipeline_run_summary (representative)

```markdown
# Pipeline Run Summary
**Run ID:** 20260321-055414
**Query:** LLM agent framework Python
**Source class:** github
**Selection rule:** First candidate in discovery queue (index 0)

## Selected candidate
- URL: https://github.com/manthanguptaa/water
- Priority: high

## Artifacts
- Discovery: .../discovery_queue_20260321-055414.json
- Packet: .../source_packet_20260321-055414.json
- Extraction: .../extraction_report_20260321-055414_api.json
## Result: **SUCCESS**
```

#### pipeline_batch_summary_20260321-060906.md

10 runs, 10 succeeded. Per-run: Query, Source, Selected URL, Discovery/Packet/Extraction/Summary paths.

#### pipeline_batch_collection_review_20260321-061000.md

Per-run quality: 6 strong, 2 medium, 2 thin. Strong: LangChain (2), vector embeddings (4), OpenAI streaming (6), prompt arXiv (8), LLM benchmark (9), MCP (10). Thin: CI/CD journey (3), awesome-pydantic-ai (7).

#### extractor_api_stage_decision.md

Decision: QUALIFIED PASS. Basis: smoke proof, comparison SOFT PASS. Human review mandatory. Weaknesses: generic tools vs concrete patterns; thinner than manual.

#### batch_runs_10_collection.json

```json
{
  "runs": [
    {"query": "RAG pipeline Python implementation", "source_class": "github"},
    {"query": "LangChain agents tutorial 2024", "source_class": "article"},
    {"query": "CI/CD automation GitHub Actions", "source_class": "github"},
    {"query": "vector database embeddings best practices", "source_class": "article"},
    {"query": "LLM tool calling agent framework", "source_class": "github"},
    {"query": "OpenAI API streaming patterns", "source_class": "article"},
    {"query": "structured output Pydantic LLM", "source_class": "github"},
    {"query": "prompt engineering techniques 2024", "source_class": "article"},
    {"query": "evaluation metrics LLM benchmarks", "source_class": "github"},
    {"query": "MCP Model Context Protocol setup", "source_class": "article"}
  ]
}
```

---

### Extraction report excerpts (strong vs thin)

**Strong (Run 2 — LangChain):**
- summary: LangChain docs, tutorials, conceptual guides, LangGraph, deep agents, multi-agent
- methods_tools_patterns: 5 items (Data analysis agent, Semantic Search Engine, RAG agent, SQL agent, Multi-agent support), all category "pattern"
- key_claims: 3 (LangChain for simple cases, LangGraph for deeper customization, resources for learning)

**Thin (Run 7 — awesome-pydantic-ai):**
- summary: Curated collection of Pydantic + AI frameworks
- methods_tools_patterns: 2 items (Resource List, User Contributions) — meta-list, not implementation
- key_claims: easy navigation, 4 GB RAM minimum — not about structured output

---

## 6. Current Bottleneck and Next Recommended Step

**Current bottleneck:** Acquisition reliability on restricted/paywalled article sites (Medium HTTP 403, etc.). Phase A skips and logs these; no retry spam.

**Next step:** Improve acquisition for restricted sites (e.g. different fetch strategy, or accept skip/log for now and expand supported source coverage instead).

---

## 7. New Chat Starter Snippet

Copy-paste into a new conversation:

---

**Attached: RESEARCH_SWARM_NEW_CHAT_HANDOFF_BUNDLE_LATEST.md**

Please read the handoff bundle first. Do not restart from theory.

**Current reality:** Research Swarm Phase A unattended bounded collector runs on operator URL list + optional discovery. Supported: GitHub + article only. Skips restricted/paywalled articles; skips unsupported (video, Reddit). Writes run summary + cumulative ledger. Hourly scheduling via ops scripts (no-overlap). Evaluator and archivist remain manual. Primary bottleneck: acquisition reliability on restricted sites.

**Please confirm:**
1. Phase A collector state (run_phase_a_collector.py, ops scripts, ledger)
2. Supported sources (GitHub + article only; video/X/Reddit skipped)
3. Acquisition bottleneck (restricted sites skip/log)

---
