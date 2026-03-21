# Content Acquisition Layer — Build Packet

**Purpose:** Concrete execution checklist for the first bounded implementation of the Content Acquisition Layer.

**Aligned with:** CONTENT_ACQUISITION_LAYER_IMPLEMENTATION_PLAN.md, CONTENT_ACQUISITION_LAYER_PLAN.md

**Build target:** Packet generation for two source types; operator-reviewed; narrow proof.

---

## 1. Objective

This build packet covers the **first bounded implementation** of the Content Acquisition Layer.

- **Upstream of extraction** — acquisition produces packets; extractor consumes them
- **Downstream of chosen-source selection** — operator or future discovery provides URL
- **Packet generation only** — no extraction, no evaluation, no archiving
- **Narrow proof target** — two source types; honest success criteria
- **Not broad source coverage yet** — YouTube, Twitter, Reddit deferred to later build

---

## 2. First-build scope

**First supported source types:**

- **Generic article / webpage** — HTTP fetch, main-text extraction, metadata from page
- **GitHub** — README or issue body via GitHub raw/API; no auth for public content

**Why this pair:**

- No API keys or OAuth required for public content
- HTTP + parse is simpler than transcript fetch or social API
- Validates packet contract and handler dispatch before harder sources
- Bounded complexity for first proof

**Included in first build:**

- Packet creation for article and GitHub
- Manual/operator-reviewed usage only
- Source classifier (URL → type)
- Packet builder and completeness labeling
- Validation/check helper

**Deferred to later builds:**

- YouTube transcript fetch
- X/Twitter acquisition
- Reddit acquisition
- Full metadata normalizer polish
- Discovery integration

---

## 3. Exact file plan

| File path | One-line responsibility |
|-----------|-------------------------|
| `future_modules/research_swarm/scripts/run_acquisition.py` | CLI entrypoint: parse args, dispatch by source type, write packet, print summary |
| `future_modules/research_swarm/scripts/acquisition/__init__.py` | Package init; expose handler registry |
| `future_modules/research_swarm/scripts/acquisition/source_classifier.py` | Infer source_type from URL (article vs github patterns) |
| `future_modules/research_swarm/scripts/acquisition/packet_builder.py` | Build packet dict; generate packet_id; assign content_completeness; write JSON |
| `future_modules/research_swarm/scripts/acquisition/handlers/article_handler.py` | Fetch webpage; extract main text; extract metadata; return raw_content + metadata + completeness hint |
| `future_modules/research_swarm/scripts/acquisition/handlers/github_handler.py` | Fetch README or issue body; extract metadata; return raw_content + metadata + completeness hint |
| `future_modules/research_swarm/scripts/acquisition/handlers/__init__.py` | Handler registry; map source_type → handler |
| `future_modules/research_swarm/scripts/acquisition/completeness_helper.py` | Assign content_completeness from handler hint + raw_content length; enforce minimum threshold |
| `future_modules/research_swarm/scripts/acquisition/validate_packet.py` | Check packet has required fields; raw_content non-blank; completeness honest |
| `future_modules/research_swarm/outputs/.gitkeep` | Ensure outputs dir exists (if not already) |
| `future_modules/research_swarm/docs/ACQUISITION_SMOKE_CHECKLIST.md` | Optional: one-page smoke checklist for operator. Defer if time-boxed. |

**Total first-build files:** 10 (9 required + 1 optional doc).

---

## 4. Implementation sequence

Recommended build order:

1. **Packet builder** — `packet_builder.py` — core output contract; no fetch yet
2. **Completeness helper** — `completeness_helper.py` — labeling logic; used by packet builder
3. **Source classifier** — `source_classifier.py` — URL → article | github
4. **Article handler** — `handlers/article_handler.py` — first source type
5. **GitHub handler** — `handlers/github_handler.py` — second source type
6. **Handler registry** — `handlers/__init__.py` — wire handlers
7. **Entrypoint** — `run_acquisition.py` — CLI; dispatch; write; summary
8. **Validation helper** — `validate_packet.py` — check packet before/after
9. **Manual smoke path** — run against real URLs; verify packets

Build packet builder first so handlers have a clear output target.

---

## 5. Source-type proof target

### Generic article / webpage

| Aspect | Definition |
|--------|------------|
| **Why first** | No auth; simple HTTP + HTML parse; many test URLs available |
| **Good enough** | Main article text extracted; raw_content > 200 chars; metadata has title or URL; content_completeness = page_text_only |
| **Failure** | 404; timeout; paywall; only nav/ads recovered; raw_content < 200 chars |

### GitHub

| Aspect | Definition |
|--------|------------|
| **Why first** | Public content via raw URLs; no OAuth; README/issue body are structured |
| **Good enough** | README or issue body captured; raw_content > 200 chars; metadata has repo/issue info; content_completeness = page_text_only (or summary_only if README is short) |
| **Failure** | 404; private repo; empty README and no issue; raw_content < 200 chars |

---

## 6. Input / output expectations

**Input:**

| Input | Required | Format |
|-------|----------|--------|
| source_url | Yes | Valid URL string |
| source_type | No | If omitted, infer from URL. Override: article | github |
| output_path | No | Default: `outputs/source_packet_{run_id}.json` |

**Output:**

| Output | Description |
|--------|-------------|
| Packet JSON | Valid JSON with packet_id, source_url, source_type, raw_content, metadata, content_completeness, raw_content_format |
| Summary | STDOUT: success/fail, packet path, content_completeness. On fail: reason. |

**CLI shape (illustrative):**

```
python scripts/run_acquisition.py --url <URL> [--type article|github] [--out <path>]
```

---

## 7. Proof / smoke checklist

**Article smoke:**

| Step | Action | PASS | FAIL |
|------|--------|------|------|
| 1 | Run acquisition on a public article URL (e.g. blog post, docs page) | Packet written; raw_content non-blank; JSON valid | No packet; parse error; raw_content empty |
| 2 | Validate packet | All required fields present; raw_content length reasonable | Missing field; raw_content < 200 chars |
| 3 | Run extractor on packet | Extraction runs without schema error | Extractors fails |

**GitHub smoke:**

| Step | Action | PASS | FAIL |
|------|--------|------|------|
| 1 | Run acquisition on `https://github.com/owner/repo` (README) or `https://github.com/owner/repo/issues/N` | Packet written; raw_content has README/issue text | No packet; empty |
| 2 | Validate packet | Required fields; raw_content non-blank | Missing/invalid |
| 3 | Run extractor on packet | Extraction runs | Fails |

**Artifacts after success:**

- `outputs/source_packet_{run_id}.json` — valid JSON
- Packet parses; required fields exist
- `raw_content` non-blank, > 200 chars
- `content_completeness` honest (not metadata_only when content exists)
- No fake success from metadata-only junk

**Concrete example URLs (operator to choose):**

- Article: any public blog post, Wikipedia article, or docs page
- GitHub: any public repo with README; or public issue with body

---

## 8. Failure boundaries

First build **must fail** or refuse packet creation when:

| Condition | Action |
|-----------|--------|
| Inaccessible page (404, timeout) | Exit non-zero; print reason |
| Unsupported source type | Exit non-zero; "Source type X not yet supported" |
| Too-thin content (< 200 chars) | Refuse packet; print "Content too thin" |
| Only metadata available | Refuse packet; do not write |
| Ambiguous identity (malformed URL) | Exit non-zero; "Could not resolve source" |
| Fetch/parse failure | Exit non-zero; report error |

**Rule:** Bad acquisition must not be disguised as valid packet creation. When in doubt, fail.

---

## 9. Out-of-scope boundaries

First build must **NOT** include:

- YouTube transcript automation
- X/Twitter acquisition
- Reddit acquisition
- Evaluator automation
- Archivist automation
- Discovery automation
- Unattended operation
- Jarvis integration
- Broad production hardening (retries, rate limits, caching)
- Metadata normalizer for all five source types (article + github only)

---

## 10. Recommended next step after build

After first build smoke passes:

1. **Option A:** Add one more source type (YouTube or Reddit) using same handler pattern
2. **Option B:** Document acquisition smoke in ACQUISITION_SMOKE_CHECKLIST.md; compare packet quality on 2–3 examples per type
3. **Option C:** Run extractor on acquisition-generated packets; compare with manually-assembled packets

Do not expand into discovery, scheduling, or integration. Next step stays within acquisition layer.
