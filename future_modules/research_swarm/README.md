# Research Swarm

**Status:** prototype  
**Location:** `future_modules/research_swarm/`

## Purpose

Research Swarm is the planned Jarvis input-learning engine. It transforms raw research sources (YouTube, Reddit, GitHub) into structured, evaluated knowledge that can feed other modules.

## Current v1 Role Set

| Role | Responsibility |
|------|----------------|
| **Collector** | Gathers source URLs and metadata (manual or scripted; not yet implemented) |
| **Extractor** | Extracts structured content from raw source text |
| **Evaluator** | Reviews credibility, hype, and usefulness |
| **Archivist** | Produces knowledge-base entries from validated extractions |

## Allowed Source Types (v1)

- **YouTube** — Transcripts, descriptions, titles; tech talks, tutorials, product demos
- **Reddit** — Post body, top comments; discussions, AMAs, community insights
- **GitHub** — README, key files, issue summaries; projects, libraries, patterns

## What the Module Does Now vs Later

| Now | Later |
|-----|-------|
| Specs, schemas, prompts, examples | Collector scripts, API integrations |
| Manual extraction/evaluation/archiving | Automated pipelines |
| Local knowledge-base entries | Shared knowledge base, cross-module consumption |
| Read-only source analysis | Task creation from research (out of scope for v1) |

## Operating Stance

- **Read-only** — No posting, commenting, or modifying sources
- **Packet-first** — Source intake → extraction → evaluation → archive
- **Evidence-focused** — Claims must reference source content
- **Isolated** — No live Jarvis integration until promotion
