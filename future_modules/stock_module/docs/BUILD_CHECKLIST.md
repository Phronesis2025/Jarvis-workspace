# Stock Module Build Checklist

Checklist-style build plan. Check off as completed.

---

## Phase 1: Contract

- [ ] `module_spec.md` reviewed and approved
- [ ] `README.md` reflects read-only, no-trading scope
- [ ] Non-goals aligned with `FUTURE_MODULE_BUILD_RULES.md`
- [ ] Input/output contracts defined

---

## Phase 2: Input Packet Design

- [ ] `watchlist_packet.schema.json` finalized
- [ ] `WATCHLIST_PACKET_FORMAT.md` documents fields and constraints
- [ ] `example_watchlist_packet.json` validates against schema
- [ ] Required vs optional fields documented

---

## Phase 3: Output Brief Design

- [ ] `stock_research_brief.schema.json` finalized
- [ ] `RESEARCH_BRIEF_FORMAT.md` documents structure
- [ ] `example_stock_research_brief.json` validates
- [ ] Confidence band and evidence requirements defined

---

## Phase 4: Risk Gate Design

- [ ] `risk_gate_review.schema.json` finalized
- [ ] `RISK_GATE_RULES.md` documents triggers and forbidden language
- [ ] `example_risk_gate_review.json` validates
- [ ] Escalation rules documented

---

## Phase 5: Example Runs

- [ ] End-to-end example: watchlist packet → research brief → risk gate review
- [ ] All example files validate against schemas
- [ ] Manual run path documented
- [ ] No integration code; prototype only

---

## Phase 6: Consistency Review

- [ ] Prompts align with schemas
- [ ] Examples match format docs
- [ ] No broker/trading/execution references
- [ ] Output explicitly for human review only
