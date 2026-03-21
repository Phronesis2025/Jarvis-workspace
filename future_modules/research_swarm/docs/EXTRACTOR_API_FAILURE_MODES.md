# Extractor API Failure Modes

Realistic failure modes for API-assisted extraction. Implementation should not assume the API extractor is infallible.

---

## Failure Mode Categories

| Category | Description |
|----------|-------------|
| **Schema failure** | Output does not conform to extraction_report schema; malformed JSON; missing required fields |
| **Invented evidence** | Quotes or paraphrases not present in source; fabricated claims |
| **Weak pattern extraction** | Methods/patterns too generic; no actionable reuse value |
| **Over-broad claims** | Claims exceed evidence; confidence overstated |
| **Hype over-detection** | Benign or neutral language flagged as hype |
| **Hype under-detection** | Clear promotional phrases missed |
| **Transcript truncation / partial-content distortion** | Extraction assumes completeness when content is partial |
| **Source-type mismatch** | Treating Reddit like transcript or README like speech |
| **Degraded output on long/noisy transcripts** | Quality drops with length, repetition, or speech-to-text noise |

---

## Detection Signals

| Category | What Operator Notices |
|----------|------------------------|
| Schema failure | Validation error; missing arrays; wrong types |
| Invented evidence | Evidence quote not findable in source; paraphrase does not match |
| Weak pattern extraction | Vague descriptions; "use X" with no detail |
| Over-broad claims | Claim says "always" or "never" but evidence is narrow |
| Hype over-detection | Normal phrasing flagged; too many hype_signals |
| Hype under-detection | Obvious promo language not flagged |
| Transcript truncation | Extraction assumes info not in truncated content |
| Source-type mismatch | Reddit post parsed as monologue; README as transcript |
| Long/noisy transcript | Inconsistent extraction; missed key points; hallucinated filler |

---

## Immediate Response

| Category | Response |
|----------|----------|
| **Schema failure** | Reject output; retry or fall back to manual; fix prompt if systematic |
| **Invented evidence** | Reject; do not proceed; retry with stricter prompt or fall back to manual |
| **Weak pattern extraction** | Revise prompt to demand specificity; retry or manual |
| **Over-broad claims** | Revise output manually if minor; else retry with scope constraints |
| **Hype over-detection** | Revise prompt; reduce sensitivity; retry |
| **Hype under-detection** | Revise prompt; add examples; retry |
| **Transcript truncation** | Mark source partial; extract cautiously; note in open_questions |
| **Source-type mismatch** | Ensure source_type passed correctly; revise prompt for type |
| **Long/noisy transcript** | Consider chunking or summarization strategy; or fall back to manual |

---

## Non-Goals

- The extractor is **not** a truth engine — it surfaces what the source says, not whether it is true.
- The extractor is **not** a trading or financial advisor — no investment or risk advice.
- The extractor is **not** an autonomous researcher — it does not decide what to research or what to believe.
