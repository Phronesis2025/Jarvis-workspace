# Research Swarm — Side Quest Handoff Bundle

**Last updated:** 2026-03-20  
**Purpose:** New-chat handoff for continuing Research Swarm work. Attach to new chat for context continuity.

---

## Bundle Purpose

This bundle provides the minimum context for a new chat to continue Research Swarm work without re-discovering the module. It does not replace the full canon docs (JARVIS_LIVE_HANDOFF_BUNDLE, etc.) but supplements them for this side quest.

---

## Current Live Truth Summary

- **Research Swarm** is a prototype input-learning engine in `future_modules/research_swarm/`
- **Manual flow proven:** source packet → extract → evaluate → archive (2 full runs)
- **Extractor API v1 scaffold hardened** and locally smoke-proven
- **First real smoke path passed** on `source_packet_second_run.json`
- **Comparisons completed** on both first_run and second_run — both SOFT PASS
- **Stage decision:** QUALIFIED PASS (bounded assistive drafting only)
- **Current allowed use:** local/operator-reviewed drafting; human must supplement API output
- **Known weakness profile:** generic methods/patterns, thinner key claims, abstract open questions
- **Evaluator and archivist remain manual**
- **Not integrated with Jarvis** — no dashboard, no export, no orchestration
- **Human review mandatory**

---

## Critical File List

| File | Path | Why It Matters |
|------|------|----------------|
| Context anchor | `future_modules/research_swarm/docs/SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md` | What this quest is, current direction, next steps |
| Stage decision | `future_modules/research_swarm/outputs/extractor_api_stage_decision.md` | QUALIFIED PASS; what is allowed vs not |
| Comparison (second_run) | `future_modules/research_swarm/outputs/extractor_api_comparison_second_run.md` | API vs manual; SOFT PASS |
| Comparison (first_run) | `future_modules/research_swarm/outputs/extractor_api_comparison_first_run.md` | Second-source validation; SOFT PASS |
| API extraction (second_run) | `future_modules/research_swarm/outputs/extraction_report_second_run_api.json` | API output artifact |
| API extraction (first_run) | `future_modules/research_swarm/outputs/extraction_report_first_run_api.json` | API output artifact |
| Module spec | `future_modules/research_swarm/module_spec.md` | Purpose, scope, non-goals |
| Build packet | `future_modules/research_swarm/docs/EXTRACTOR_API_V1_BUILD_PACKET.md` | Execution checklist, validation gates |
| Review gate | `future_modules/research_swarm/docs/EXTRACTOR_API_REVIEW_GATE.md` | Manual acceptance criteria for API output |
| Extraction schema | `future_modules/research_swarm/schemas/extraction_report.schema.json` | Output contract for extractor |
| Source packet (second run) | `future_modules/research_swarm/outputs/source_packet_second_run.json` | Repaired; smoke test input |
| Source packet (first run) | `future_modules/research_swarm/outputs/source_packet_first_run.json` | Repaired |
| Manual extraction (second run) | `future_modules/research_swarm/outputs/extraction_report_second_run.json` | Baseline |
| Manual extraction (first run) | `future_modules/research_swarm/outputs/extraction_report_first_run.json` | Baseline |
| Extractor API runner | `future_modules/research_swarm/scripts/run_extractor_api.py` | CLI entry point |
| Extractor API client | `future_modules/research_swarm/scripts/extractor_api_client.py` | OpenAI API calls |
| Extractor API validator | `future_modules/research_swarm/scripts/extractor_api_validate.py` | Schema validation |

---

## Important Files — Tight Summary

### Run Command

```
python future_modules/research_swarm/scripts/run_extractor_api.py --packet future_modules/research_swarm/outputs/source_packet_second_run.json
```

- **Status:** Proven locally on repaired production packets
- **Scope:** Bounded assistive drafting; human review mandatory
- Requires: `OPENAI_API_KEY`, `pip install openai jsonschema`

### Review Gate Outcomes

- **PASS** → proceed to evaluator (manual)
- **REVISE** → retry API or minor edit
- **REJECT** → fall back to manual extraction

---

## Files Intentionally Excluded

- Full JARVIS canon (JARVIS_LIVE_HANDOFF_BUNDLE, etc.) — reference as needed
- Pathfinder, WCS, n8n, dashboard — out of scope
- Transcript acquisition implementation — separate work

---

## Suggested First Files to Inspect

1. `future_modules/research_swarm/docs/SIDE_QUEST_CONTEXT_ANCHOR_RESEARCH_SWARM_CURRENT.md`
2. `future_modules/research_swarm/outputs/extractor_api_stage_decision.md`
3. `future_modules/research_swarm/outputs/extractor_api_comparison_second_run.md`
4. `future_modules/research_swarm/outputs/extractor_api_comparison_first_run.md`
5. `future_modules/research_swarm/scripts/run_extractor_api.py`

---

## Module Integration Status

| Label | Status |
|-------|--------|
| Concept only | No — designed and partially proven |
| Design-only | No — manual flow proven |
| Implementation started | Yes — Extractor API scaffolding |
| Partially proven | Yes — manual flow + API assistive drafting |
| Locally operational | Yes — for bounded assistive extraction drafting |
| Human review mandatory | Yes |
| Not integrated with Jarvis | Yes |
| Integrated with Jarvis | No |
| Safe for unattended use | No |
