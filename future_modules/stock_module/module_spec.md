# Stock Module v1 Spec

**Status:** prototype  
**Last updated:** 2026-03-20

## 1. Module Name

Stock Module v1 (read-only market research worker)

## 2. Status

prototype

## 3. Purpose

Produce bounded market research briefs from ticker/watchlist packets. Summarize catalysts, risks, and evidence for human review. No trading, no execution.

## 4. Scope

- **In-bounds:** Catalyst/risk summary; evidence-backed review; risk gate checks; structured brief output
- **Boundaries:** Read-only; no broker APIs; no order flow; no autonomous signals

## 5. Non-Goals

- Not a trader — No order placement or position management
- Not a broker bot — No API integration with brokers or exchanges
- Not an autonomous signal engine — No automated buy/sell recommendations
- No live trading, no execution, no dashboard integration for prototypes

## 6. Inputs

| Field | Required | Description |
|-------|----------|-------------|
| packet_id | Y | Unique packet identifier |
| symbols | Y | List of ticker symbols |
| watch_reason | N | Why these symbols are being watched |
| constraints | N | Time horizon, risk tolerance, etc. |

Schema: `schemas/watchlist_packet.schema.json`

## 7. Outputs

| Artifact | Description |
|----------|-------------|
| Stock research brief | Per-symbol: thesis, catalysts, risks, evidence, confidence |
| Risk gate review | Flags for caution, insufficient evidence, conflicting signals |

Schemas: `schemas/stock_research_brief.schema.json`, `schemas/risk_gate_review.schema.json`

## 8. Evidence Artifacts

- Every catalyst and risk must cite a source (news, filing, data)
- Confidence band must align with evidence strength
- Risk gate must reference specific rule triggers

## 9. Workflow

1. **Intake** — Watchlist packet with symbols and context
2. **Research** — Generate brief per symbol (catalysts, risks, evidence)
3. **Risk gate** — Apply caution rules; flag issues
4. **Output** — Research brief + risk gate review for human review

## 10. QA / Validation

- Manual review of all briefs before any use
- Risk gate flags must be actionable
- No forbidden output language (see RISK_GATE_RULES.md)

## 11. Escalation Rules

- **Stop:** No accessible data; symbol invalid or delisted
- **Defer:** Data stale; conflicting sources; need human input
- **Flag:** Risk gate triggered; insufficient evidence; high uncertainty

## 12. Activation Conditions

- Prototype: manual invocation only
- No scheduled runs

## 13. First Viable Slice

- **Input:** One watchlist packet; exactly one symbol
- **Process:** Research the symbol → produce structured research brief → apply risk gate review
- **Output:** One stock research brief; one risk gate review
- **Success:** Evidence sources cited; risk gate rules applied; confidence band present; no forbidden language

## 14. Known Risks / Failure Modes

- **Stale data:** Mitigation — Include data freshness in brief; risk gate flags staleness
- **Conflicting sources:** Mitigation — Present both; flag for human review
- **Overconfidence:** Mitigation — Forbidden language rules; confidence band required
