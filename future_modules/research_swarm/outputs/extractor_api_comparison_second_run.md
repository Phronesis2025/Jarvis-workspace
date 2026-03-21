# Extractor API vs Manual Baseline — Second Run Comparison

**Source:** `source_packet_second_run.json` (Polymarket API Python tutorial)  
**Compared:** `extraction_report_second_run_api.json` (API) vs `extraction_report_second_run.json` (manual)

---

## Verdict: SOFT PASS

Usable with caution. The API produces a credible draft that preserves high-level signal but is thinner than the manual baseline. Clear weaknesses in methods/patterns and key claims. Acceptable for assistive drafting if the operator expects to supplement.

---

## Files Compared

| Role | File |
|------|------|
| Source packet | `source_packet_second_run.json` |
| API extraction | `extraction_report_second_run_api.json` |
| Manual baseline | `extraction_report_second_run.json` |

---

## Summary Quality

**API:** Accurate but vague. Captures "Polymarket API with Python," "place bets," "fetch market data," "authentication," "automate trade placements." Lacks technical detail.

**Manual:** Dense and specific. Names public vs private API boundary, py-clob-client vs direct requests, gamma/data APIs, sign-then-post workflow, authentication flow, order types, automation hooks, security cautions.

**Gap:** API summary is ~60 words; manual is ~120. API misses implementation structure (auth boundaries, library vs direct, workflow).

---

## Methods / Tools / Patterns

**API (3 items):** Polymarket API (generic), Python Requests (generic), Order Management Functions (evidence: "there's a lot of methods you can use" — weak).

**Manual (7 items):** Public vs private API boundary, sign-then-post order flow, yes/no token model, third-party library vs direct API, price tracking as automation hook, user position tracker via data API, private key confidentiality rule.

**Biggest misses:** Sign-then-post flow, yes/no token model, py-clob-client vs direct requests, price tracking, user position tracker, private key rule. API replaced concrete patterns with generic tool labels.

---

## Key Claims

**API (3 claims):** Minimal coding experience, comprehensive API, automation/tracking. All supported by evidence.

**Manual (8 claims):** Public data without auth, order placement needs private auth, derived API keys, cents vs USDC confusion, get balance verification, limit order status live, third-party vs from-scratch, financial advice disclaimer.

**Biggest misses:** Derived API keys, cents/USDC display, get balance as verification, limit order semantics, third-party disclaimer, financial advice disclaimer.

---

## Hype Signals

**API (3):** "biggest prediction market in the world," "everything is open source and free," "super easy." Credible.

**Manual (6):** Adds "10 minutes," "No complicated blockchain stuff," "$2 million in profits." More coverage.

**Gap:** API catches main hype; manual adds time claims and specific numbers.

---

## Open Questions

**API (3):** Safeguards for private keys, API reliability/security, long-term implications of third-party libraries. Reasonable but abstract.

**Manual (5):** Gamma/data API base URLs, py-clob-client repo URL, signature types, derived API key flow, rate limits. Concrete and actionable.

**Gap:** API questions are generic; manual questions are implementation-oriented.

---

## Overall Trustworthiness

- **Credible:** API does not invent content. Evidence is cited. Structure is correct.
- **Lossy:** Implementation patterns and technical nuance are under-represented.
- **Assistive stage:** Acceptable as a first draft. Operator must add missing patterns and claims.

---

## Strongest API Wins

1. Correct high-level framing (tutorial, API, Python, authentication).
2. Hype signals are grounded and not overclaimed.
3. Key claims that are present are well-supported.
4. No fabrication or distortion.

---

## Biggest API Misses

1. **Methods/patterns:** Generic tools instead of concrete patterns (sign-then-post, yes/no tokens, library vs direct).
2. **Key claims:** Missing derived API keys, cents/USDC, get balance verification, limit order status, disclaimers.
3. **Summary:** Vague vs manual’s dense technical summary.
4. **Open questions:** Abstract vs implementation-specific.

---

## Recommendation for Next Move

1. **Use API output as draft:** Treat as starting point; human adds missing patterns and claims.
2. **Prompt tuning:** Consider reinforcing extraction of implementation patterns (workflows, boundaries, concrete tools).
3. **Re-run comparison:** After prompt changes, compare again on first_run packet.
4. **Do not automate evaluator/archivist yet:** Quality gap is real; keep human review in the loop.
