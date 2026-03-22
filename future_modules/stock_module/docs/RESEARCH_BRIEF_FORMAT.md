# Stock Research Brief Format

Output structure for Stock Module v1 research briefs.

---

## Per-Symbol Brief Structure

| Field | Description |
|-------|-------------|
| **symbol** | Ticker symbol |
| **thesis_or_watch_reason** | Why this symbol is being researched |
| **catalyst_summary** | Upcoming or recent catalysts (earnings, product, regulatory) |
| **risk_summary** | Key risks (competitive, macro, company-specific) |
| **evidence_sources** | Citations: news, filings, data sources |
| **open_questions** | Unresolved items requiring follow-up |
| **confidence_band** | low \| medium \| high |
| **review_recommendation** | Suggested next step (e.g., "monitor", "dig deeper", "pass") |

---

## Evidence Sources

Each catalyst and risk should reference:
- News article (title, date, outlet)
- SEC filing (type, date)
- Data source (e.g., "company 10-K", "industry report")
- No unsourced assertions

---

## Confidence Band

- **low** — Limited evidence; high uncertainty; conflicting signals
- **medium** — Adequate evidence; some uncertainty
- **high** — Strong evidence; clear thesis; low conflict

Confidence must align with evidence strength. Overconfidence is forbidden (see RISK_GATE_RULES).

---

## Review Recommendation

Advisory only. Examples:
- "monitor" — Watch for catalyst; no action
- "dig deeper" — More research needed before any decision
- "pass" — Does not meet criteria; skip
- "flag for discussion" — Human review required

---

## Multi-Symbol Output

When packet contains multiple symbols, output one brief per symbol plus a risk gate review covering all.
