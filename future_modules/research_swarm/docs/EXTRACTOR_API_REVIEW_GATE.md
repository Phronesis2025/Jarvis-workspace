# Extractor API Review Gate

Manual acceptance gate for API-generated extraction output. API output is accepted only if it matches the Research Swarm quality bar.

---

## Purpose

The extractor API produces draft output. The operator reviews before passing to the evaluator. This checklist defines the acceptance criteria.

---

## Required Checks

| Check | Pass Criteria |
|-------|----------------|
| **Schema validation** | Output passes `extraction_report.schema.json` |
| **Summary** | Accurate; 2–4 sentences; bounded; no overclaim |
| **methods_tools_patterns** | Reusable; each has evidence; evidence traces to source |
| **key_claims** | Scoped correctly; each has evidence + confidence |
| **Confidence labels** | stated / inferred / speculative used appropriately |
| **hype_signals** | Real phrases from source; not over-flagged |
| **open_questions** | Useful; grounded in real gaps; not speculation |
| **No fabricated content** | Nothing invented; all evidence traceable |
| **No overreach** | Extraction stays within transcript/source |

---

## Acceptance Outcomes

| Outcome | Action |
|---------|--------|
| **Pass** | Proceed to evaluator step |
| **Revise and retry** | Edit output minimally or re-run extractor with adjusted prompt |
| **Reject and fall back to manual** | Operator performs manual extraction per existing checklist |

---

## Common Rejection Reasons

- **Weak/generic patterns** — e.g. "use the API" with no specificity
- **Claim scope too broad** — claim exceeds evidence
- **Invented evidence** — quote or paraphrase not in source
- **Hype over-detection** — flagging benign language as hype
- **Hype under-detection** — missing clear promotional phrases
- **Missing required arrays** — empty or omitted
- **JSON shape drift** — schema violation; malformed structure

---

## Comparison Against Manual Baseline

Periodically compare API output to proven manual runs:

- **First run** — narrative/operator style; calibrate for softer sources
- **Second run** — technical/API style; calibrate for dense, implementation-focused content

If API output consistently misses patterns or over-flags hype, adjust prompt or retain manual extraction path.
