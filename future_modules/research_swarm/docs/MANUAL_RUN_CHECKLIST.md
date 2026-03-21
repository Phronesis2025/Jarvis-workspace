# Research Swarm Manual Run Checklist

Step-by-step operator checklist for one end-to-end run.

---

## Pre-Run

- [ ] Source is a YouTube video with accessible transcript
- [ ] Transcript captured (manual copy or tool)
- [ ] Source is relevant to AI tooling, automation, agents, research workflows, or systems building

---

## 1. Select Source

- [ ] Choose one YouTube video
- [ ] Confirm transcript is available (video captions or external tool)
- [ ] Note: canonical URL, title, channel

---

## 2. Capture Transcript

- [ ] Copy full transcript or representative portion
- [ ] If partial: set `content_completeness: "partial"` in packet
- [ ] Store in plain text for raw_content

---

## 3. Build Source Intake Packet

- [ ] Create JSON with required fields per `schemas/source_intake.schema.json`
- [ ] Required: packet_id, source_url, source_type, raw_content, created_at
- [ ] Optional: metadata (title, author, channel, published_at), content_completeness, raw_content_format, captured_at
- [ ] Validate packet structure

---

## 4. Run Extractor Prompt

- [ ] Use `prompts/extractor_prompt.md`
- [ ] Input: source intake packet (source_url, source_type, raw_content)
- [ ] Output: extraction report JSON
- [ ] Ensure all required arrays exist: methods_tools_patterns, key_claims, hype_signals, open_questions

---

## 5. Validate Extraction Report

- [ ] Validate against `schemas/extraction_report.schema.json`
- [ ] **Review 1:** Evidence quotes exist for each method/tool/pattern and key_claim
- [ ] **Review 1:** No invented content; all evidence traces to source
- [ ] Fix or re-run extraction if invalid

---

## 6. Run Evaluator Prompt

- [ ] Use `prompts/evaluator_prompt.md`
- [ ] Input: extraction report
- [ ] Output: evaluation report JSON
- [ ] **Review 2:** Credibility and hype scores cite extraction evidence
- [ ] **Review 2:** archive_recommendation is justified

---

## 7. Apply Archive Decision Rules

- [ ] Use `docs/KNOWLEDGE_ARCHIVE_DECISION_RULES.md`
- [ ] Apply relevance, actionability, evidence, and hype/credibility criteria
- [ ] Decide: archive | archive_with_warning | skip_archive
- [ ] **Review 3:** Decision matches rules; document rationale
- [ ] If skip_archive: stop; do not create archive entry. v1 manual runs do NOT persist skip-archive disposition records. Skip records may be supported later.

---

## 8. Produce Archive Entry JSON

- [ ] Use `prompts/archivist_prompt.md` (only if archive or archive_with_warning)
- [ ] Input: source packet + extraction report + evaluation report
- [ ] Output: knowledge archive entry JSON
- [ ] Ensure all required fields present per `schemas/knowledge_archive_entry.schema.json`

---

## 9. Validate Archive Entry Against Schema

- [ ] Validate against `schemas/knowledge_archive_entry.schema.json`
- [ ] Required arrays: useful_patterns, key_claims, hype_warnings, build_ideas, module_mapping, open_questions
- [ ] hype_warnings: each item has signal, evidence, why_flagged, severity; evidence quotes/paraphrases source language
- [ ] archive_decision matches step 7
- [ ] Fix or re-run archivist if invalid

---

## 10. Store Result in Outputs Folder

- [ ] Write artifacts to `outputs/`
- [ ] Suggested filenames: source_packet_*.json, extraction_report_*.json, evaluation_report_*.json, archive_entry_*.json
- [ ] Use run identifier (e.g., date or packet_id) in filenames
