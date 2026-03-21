# Research Swarm Build Checklist

Phase-based build pathway. Check off as completed.

---

## Phase 1: Foundation

- [ ] `module_spec.md` reviewed and approved
- [ ] `README.md` reflects current scope
- [ ] Schemas defined for all artifacts
- [ ] Examples created for each schema
- [ ] Prompts drafted for extractor, evaluator, archivist

---

## Phase 2: Source Intake

- [ ] `source_intake.schema.json` finalized
- [ ] `example_source_packet.json` validates against schema
- [ ] Source types documented in `SOURCE_TYPES.md`
- [ ] Intake format supports YouTube, Reddit, GitHub

---

## Phase 3: Extraction

- [ ] `extraction_report.schema.json` finalized
- [ ] `extractor_prompt.md` defines output structure
- [ ] `example_extraction_report.json` validates
- [ ] Extraction distinguishes fact vs inference vs speculation

---

## Phase 4: Evaluation

- [ ] `evaluation_report.schema.json` finalized
- [ ] `evaluator_prompt.md` defines credibility/hype criteria
- [ ] `example_evaluation_report.json` validates
- [ ] Evaluation cites evidence from extraction

---

## Phase 5: Archiving

- [ ] `archive_update.schema.json` finalized
- [ ] `archivist_prompt.md` defines knowledge-base format
- [ ] `KNOWLEDGE_BASE_FORMAT.md` documents target structure
- [ ] Archive entries include source metadata and evaluation pass

---

## Phase 6: Example Runs

- [ ] End-to-end example: one source → extraction → evaluation → archive
- [ ] All example files validate against schemas
- [ ] Manual run path documented in README
- [ ] No integration code; prototype only
