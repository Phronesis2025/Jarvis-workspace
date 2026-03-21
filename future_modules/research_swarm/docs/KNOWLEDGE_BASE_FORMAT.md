# Research Knowledge-Base Format

Target structure for archived knowledge entries produced by Research Swarm.

---

## Entry Structure

Each knowledge-base entry contains:

| Field | Description |
|-------|-------------|
| **source_metadata** | URL, type, title, author, date |
| **summary** | 2–4 sentence summary of the source |
| **useful_methods_tools_patterns** | Extracted methods, tools, or patterns with evidence |
| **hype_warnings** | Overclaimed or speculative content flagged by evaluator |
| **build_ideas** | Potential applications or follow-up experiments |
| **module_mapping** | Which Jarvis modules might use this (pathfinder, stock_module, etc.) |
| **follow_up_questions** | Open questions for future research |

---

## Source Metadata

```json
{
  "url": "canonical URL",
  "source_type": "youtube | reddit | github",
  "title": "source title",
  "author": "channel, username, or org",
  "captured_at": "ISO 8601",
  "evaluation_passed": true
}
```

---

## Evidence Requirements

- Every method/tool/pattern must cite source text
- Hype warnings must cite specific language
- Build ideas must trace to extracted content

---

## Module Mapping

Optional field suggesting which future modules might consume this knowledge:

- `pathfinder` — Discovery, docs, implementation options
- `stock_module` — Market context, catalyst research
- `research_swarm` — Meta: research methods, source quality
- `other` — Custom or TBD

---

## Versioning

- Entries are append-only; no in-place edits
- New versions add new entries with updated `captured_at`
- Source URL + captured_at can serve as composite key
