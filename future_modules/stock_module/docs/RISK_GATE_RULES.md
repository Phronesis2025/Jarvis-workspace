# Stock Module Risk Gate Rules

Rules for when to trigger caution, defer, or flag. Output is for human review only.

---

## What Should Trigger Caution

- **Insufficient evidence** — Few or no cited sources for key claims
- **Conflicting evidence** — Multiple sources disagree on catalyst or risk
- **Stale data** — Key data older than threshold (e.g., 30 days for news)
- **High uncertainty** — Confidence band "low" but brief reads as decisive
- **Single-source dependency** — Entire thesis rests on one source
- **Regulatory or legal risk** — Pending litigation, investigations, sanctions

---

## Insufficient Evidence Rules

- If catalyst_summary has no evidence_sources → flag
- If risk_summary has no evidence_sources → flag
- If confidence_band is "high" but evidence_sources < 2 → flag

---

## Conflicting Evidence Rules

- If two sources contradict on same point → present both, flag for human review
- Do not resolve conflicts automatically
- Include "conflicting_evidence" in open_questions

---

## Forbidden Output Language

The brief must NOT contain:
- "Buy" or "Sell" recommendations
- "You should" or "I recommend" in trading context
- Price targets or specific entry/exit levels
- Guarantees or certainty language ("will", "guaranteed", "certain")
- Urgency language ("act now", "don't miss out")

Allowed: "monitor", "watch", "consider researching further", "flag for discussion"

---

## Human Review Reminder

All Stock Module output is:
- **Advisory only** — No automated trading decisions
- **For human review** — Human must validate before any use
- **Evidence-based** — Claims must cite sources; flag when they don't
