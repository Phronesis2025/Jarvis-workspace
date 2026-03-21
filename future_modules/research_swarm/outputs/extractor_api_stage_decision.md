# Extractor API v1 — Side-by-Side Stage Decision

**Date:** 2026-03-20  
**Evidence:** Smoke proof (prompt #11), comparison (prompt #12)

---

## Decision: QUALIFIED PASS

Extractor API v1 passes the current side-by-side stage for its bounded assistive role. Approval is qualified: human review remains mandatory; no unattended or production use.

---

## Basis

- **Smoke proof:** Local run succeeded. Packet load → API call → parse → trust checks → schema validation → write. No repair behavior.
- **Comparison:** SOFT PASS. API output is credible, evidence-backed, non-fabricated. Thinner than manual baseline (3 vs 7 methods/patterns, 3 vs 8 key claims) but acceptable as first draft.
- **Weaknesses known:** Generic tools vs concrete patterns; missing technical claims; vague summary; abstract open questions.
- **Human review:** Required. Operator must supplement missing patterns and claims.

---

## What Is Now Allowed

- API-assisted extraction drafting in local/operator-reviewed use
- Side-by-side stage considered passed for the current bounded role
- Use API output as starting draft; human adds missing signal
- Run against repaired production packets; manual review before evaluator step

---

## What Is Still NOT Allowed

- Unattended or unsupervised use
- Evaluator automation
- Archivist automation
- Jarvis integration claims
- Broad production trust
- Removal of human review
- Trusting API output without supplementation

---

## Biggest Remaining Weaknesses

1. **Methods/patterns:** API returns generic tool labels; manual captures concrete implementation patterns (sign-then-post, yes/no tokens, library vs direct).
2. **Key claims:** API misses derived API keys, cents/USDC, get balance verification, limit order semantics, disclaimers.
3. **Single-run proof:** Only second_run packet compared; no repeated-run reliability evidence.
4. **Prompt sensitivity:** One instruction tweak (explicit key list) was needed for complete output; further tuning may be needed.

---

## Recommended Next Step

Run API extraction on `source_packet_first_run.json`, compare against `extraction_report_first_run.json`, and record whether quality holds across a second source. Bounded, single-step validation.
