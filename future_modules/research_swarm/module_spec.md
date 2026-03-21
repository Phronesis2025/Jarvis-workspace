# Research Swarm Module Spec

**Status:** prototype  
**Last updated:** 2026-03-20

## 1. Module Name

Research Swarm (input-learning engine)

## 2. Status

prototype

## 3. Purpose

Transform raw research sources into structured, evaluated knowledge. Research Swarm ingests content from YouTube, Reddit, and GitHub, extracts useful patterns and methods, evaluates credibility and hype, and produces archived knowledge entries for future use by other Jarvis modules.

## 4. Scope

- **In-bounds:** Read-only source analysis; structured extraction; credibility/hype review; knowledge-base entry generation
- **Boundaries:** No live posting, no autonomous browsing loops, no task creation from research

## 5. Non-Goals

- No live posting to Reddit, YouTube, or GitHub
- No autonomous browsing or discovery loops
- No automatic task creation from research findings
- No modification of source content
- No broker, trading, or dashboard integration

## 6. Inputs

| Field | Required | Description |
|-------|----------|-------------|
| source_url | Y | Canonical URL of the source |
| source_type | Y | youtube, reddit, github |
| raw_content | Y | Transcript, post body, or file content |
| metadata | N | Title, author, date, etc. |

Schema: `schemas/source_intake.schema.json`

## 7. Outputs

| Artifact | Description |
|----------|-------------|
| Extraction report | Structured summary, methods, patterns, claims |
| Evaluation report | Credibility score, hype warnings, usefulness |
| Archive update | Knowledge-base entry with source metadata |

Schemas: `schemas/extraction_report.schema.json`, `schemas/evaluation_report.schema.json`, `schemas/archive_update.schema.json`

## 8. Evidence Artifacts

- Every claim must reference specific source text (quote or paraphrase with location)
- Extraction must distinguish: stated fact vs inference vs speculation
- Evaluation must cite evidence for credibility/hype judgments

## 9. Workflow

1. **Intake** — Source packet with URL, type, raw content
2. **Extract** — Structured extraction (summary, methods, patterns, hype signals)
3. **Evaluate** — Credibility and hype review
4. **Archive** — Knowledge-base entry per Archive Decision Rules (see below)

### Archive Decision Rules

| Decision | Conditions |
|----------|------------|
| **ARCHIVE** | Source is relevant to AI tooling, automation, agents, research workflows, or systems building; at least one actionable method/tool/pattern extracted; evidence exists in source text |
| **ARCHIVE WITH WARNING** | Source contains useful ideas but shows hype signals or weak evidence; archive entry must include hype warning and open questions |
| **SKIP ARCHIVE** | Source is off-topic; source has no actionable ideas; source credibility is extremely low |

## 10. QA / Validation

- Manual review of extraction and evaluation outputs
- Cross-check: does evaluation align with extraction evidence?
- Archive entries must have source metadata and conform to Archive Decision Rules

## 11. Escalation Rules

- **Stop:** Source is inaccessible, corrupted, or off-topic
- **Defer:** Source too long; split or sample first
- **Flag:** Conflicting evidence, high hype, low credibility

## 12. Activation Conditions

- Prototype: manual invocation only
- No scheduled runs

## 13. First Viable Slice

- **Input:** One source (e.g., one YouTube transcript)
- **Process:** Extract → Evaluate → Archive
- **Output:** One knowledge-base entry with source metadata, summary, methods, hype warnings
- **Success:** Structured output; evaluation cites evidence; archive format valid

## 14. Known Risks / Failure Modes

- **Source quality varies:** Mitigation — evaluator flags low-quality; archivist applies SKIP ARCHIVE when conditions met
- **Hype over-detection:** Mitigation — evaluator must cite specific language
- **Out-of-date content:** Mitigation — metadata includes date; follow-up questions surface staleness
