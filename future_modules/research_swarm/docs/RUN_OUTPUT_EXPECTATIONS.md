# Research Swarm Run Output Expectations

What a correct run produces.

---

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| Source intake packet | JSON with packet_id, source_url, source_type, raw_content, created_at, metadata |
| Extraction report | JSON with summary, methods_tools_patterns, key_claims, hype_signals, open_questions |
| Evaluation report | JSON with credibility_score, hype_level, archive_recommendation, evidence |
| Knowledge archive entry | JSON with full archive structure (only if archive or archive_with_warning) |

---

## File Locations

All outputs go to:

```
future_modules/research_swarm/outputs/
```

Example filenames (use run identifier):

- `source_packet_20260320_001.json`
- `extraction_report_20260320_001.json`
- `evaluation_report_20260320_001.json`
- `archive_entry_20260320_001.json`

---

## Validation Rules

- **All JSON must validate against schemas:**
  - Source packet → `schemas/source_intake.schema.json`
  - Extraction report → `schemas/extraction_report.schema.json`
  - Evaluation report → `schemas/evaluation_report.schema.json`
  - Archive entry → `schemas/knowledge_archive_entry.schema.json`

- **Required arrays must exist even if empty:**
  - Extraction: methods_tools_patterns, key_claims, hype_signals, open_questions
  - Archive: useful_patterns, key_claims, hype_warnings, build_ideas, module_mapping, open_questions

- **archive_decision must match rules:**
  - Applied per `docs/KNOWLEDGE_ARCHIVE_DECISION_RULES.md`
  - archive | archive_with_warning | skip_archive
  - If skip_archive: no archive entry created; v1 does not persist skip records

- **hype_warnings must include evidence:**
  - Each warning has signal, evidence, why_flagged, severity
  - evidence must quote, paraphrase, or cite the source language that triggered the warning

---

## Operator Review

Before considering the run complete, operator confirms:

| Check | Description |
|-------|-------------|
| Evidence quotes exist | Every method/tool/pattern and key_claim has evidence field with source quote or paraphrase |
| Claims align with source | No invented content; all claims trace to raw_content |
| Archive decision is reasonable | Decision follows relevance, actionability, evidence, hype/credibility rules |
| Build ideas are not inflated | Build ideas use suggested_stage; none presented as approved tasks |
