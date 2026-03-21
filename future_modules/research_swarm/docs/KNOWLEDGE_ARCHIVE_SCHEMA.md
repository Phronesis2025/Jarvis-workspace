# Knowledge Archive Schema

Operator reference for the archive entry format.

---

## Purpose

The knowledge archive stores structured research-memory records. Entries support:

- Search and review of prior sources
- Comparison of recurring methods/tools/patterns
- Distinction between good sources and hype-heavy sources
- Mapping of findings into future module branches
- Surfacing build ideas without treating them as approved tasks

---

## What an Archive Entry Is

- A structured research-memory record
- Produced by the archivist from validated extraction + evaluation
- Append-only; no in-place edits
- Keyed by `archive_entry_id`; traceable via `packet_id` and `report_id`

---

## What It Is Not

- A task packet
- A dashboard record
- An execution record
- A live integration object

---

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| archive_entry_id | string | Unique ID |
| packet_id | string | Source intake packet ID |
| report_id | string | Extraction report ID |
| source_url | uri | Canonical source URL |
| source_type | enum | youtube, reddit, github |
| archived_at | date-time | When archived |
| archive_decision | enum | archive, archive_with_warning, skip_archive |
| title | string | Source title |
| source_metadata | object | author, channel, subreddit, repo_name, published_at, captured_at, content_completeness, raw_content_format |
| summary | string | 2–4 sentence summary |
| useful_patterns | array | name, category, description, evidence, reuse_value |
| key_claims | array | claim, evidence, confidence |
| hype_warnings | array | signal, why_flagged, severity |
| build_ideas | array | idea, why_it_matters, suggested_stage, status_note |
| module_mapping | array | module_name, relevance_reason, priority_hint |
| open_questions | array | strings |

Schema: `schemas/knowledge_archive_entry.schema.json`

---

## How Archive Entries Are Used

- **Search:** Filter by source_type, archive_decision, module_mapping
- **Compare:** Group by useful_patterns.category; compare reuse_value
- **Quality:** archive_decision + hype_warnings indicate trust level
- **Planning:** module_mapping + build_ideas inform backlog; do not auto-create tasks

---

## Future Synthesis and Module Planning

- `module_mapping` suggests which modules might consume this knowledge
- `build_ideas` with `suggested_stage` indicate maturity (research_only → future_module_refinement → backlog_candidate_later)
- `priority_hint` (now, next, future, parked) guides sequencing
- Synthesis across entries: compare patterns, aggregate hype signals, surface recurring build ideas

---

## Build Ideas vs Approved Tasks

**Build ideas are NOT approved tasks.**

- `suggested_stage` indicates where the idea sits: research_only, future_module_refinement, backlog_candidate_later
- No build idea becomes a task without explicit human approval
- `status_note` can capture constraints or blockers

---

## Archive Decisions

| Decision | Meaning |
|----------|---------|
| **archive** | Source meets relevance, actionability, and evidence criteria; no significant hype; clean entry |
| **archive_with_warning** | Source has useful content but hype signals or weak evidence; entry includes hype_warnings and open_questions |
| **skip_archive** | Source is off-topic, has no actionable ideas, or credibility is extremely low; no entry created (or audit record only) |

See `KNOWLEDGE_ARCHIVE_DECISION_RULES.md` for full rules.
