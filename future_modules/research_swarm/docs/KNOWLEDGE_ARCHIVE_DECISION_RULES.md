# Knowledge Archive Decision Rules

Rules for when a source becomes archive, archive_with_warning, or skip_archive.

---

## Relevance Criteria

Source must be relevant to at least one of:

- AI tooling
- Automation
- Agents
- Research workflows
- Systems building

If off-topic → **skip_archive**.

---

## Actionability Criteria

Source must yield at least one actionable method, tool, or pattern.

- Actionable = extractable, evidence-backed, reusable
- No actionable ideas → **skip_archive**

---

## Evidence Criteria

- At least one method/tool/pattern must have evidence in source text
- Key claims must cite source (quote or paraphrase)
- No evidence for core content → **skip_archive**

---

## Hype / Credibility Handling

| Credibility | Hype | Decision |
|-------------|------|----------|
| High | Low | **archive** |
| High | Medium | **archive_with_warning** |
| Medium | Low | **archive_with_warning** |
| Medium | High | **archive_with_warning** (if useful) or **skip_archive** |
| Low | Any | **skip_archive** |

---

## When to Archive With Warning (Instead of Skip)

Preserve the source when:

- Useful architecture or pattern, but some hype or weak claims
- Good discussion, but incomplete transcript or partial content
- Interesting repo, but poor documentation
- Evidence exists for core ideas; hype is in peripheral claims

Include hype_warnings and open_questions. Do not drop useful content because of non-fatal flaws.

---

## When to Skip Entirely

- Source is off-topic
- No actionable methods, tools, or patterns
- No evidence for any key claim
- Credibility extremely low (fabrication, known bad actor)
- Content is pure promotion with no substance

---

## Edge Cases

| Scenario | Decision | Rationale |
|----------|----------|-----------|
| Useful architecture, exaggerated profit claims | **archive_with_warning** | Preserve architecture; flag profit claims in hype_warnings |
| Interesting repo, poor documentation | **archive_with_warning** | Repo may still be useful; note doc gaps in open_questions |
| Good discussion, incomplete transcript | **archive_with_warning** | Extract what exists; note content_completeness: partial |
| Off-topic content with high engagement | **skip_archive** | Engagement does not override relevance |
| Source mixes solid methods with speculative ROI | **archive_with_warning** | Archive methods; flag ROI in hype_warnings |
| Single useful pattern, rest is filler | **archive** | One actionable pattern is enough; omit filler |
