# Research Swarm Source Types

v1 supports three source types. Each has specific capture requirements and limitations.

---

## YouTube

### What to Capture

- **Transcript** — Full or partial; prefer official/auto-generated if available
- **Title** — Video title
- **Description** — Video description (first 500 chars or full if short)
- **Channel** — Channel name
- **Published date** — When available
- **URL** — Canonical video URL

### Why It Matters

- Tech talks, tutorials, product demos
- Often contains methods, patterns, and tool recommendations
- High signal for "how to" and "what works" content

### Risks / Limitations

- Transcripts may be auto-generated and error-prone
- Promotional content common; evaluator must flag
- No guarantee of accuracy; date matters for tool versions

---

## Reddit

### What to Capture

- **Post body** — Full text of the post
- **Title** — Post title
- **Subreddit** — Subreddit name
- **Author** — Username (for context; may be anonymized in output)
- **Top comments** — First N comments by score (configurable; e.g., 5–10)
- **Score** — Upvotes (optional; useful for signal)
- **URL** — Canonical post URL

### Why It Matters

- Community discussions, AMAs, real-world experiences
- Often surfaces edge cases and pitfalls
- Good for "what went wrong" and "alternatives" content

### Risks / Limitations

- Quality varies widely; evaluator must assess
- Memes and jokes can pollute extraction
- Recency bias; older valuable posts may be buried

---

## GitHub

### What to Capture

- **README** — Full README content
- **Key files** — Selected file contents (e.g., main entry, config)
- **Repo metadata** — Stars, forks, last updated
- **Language** — Primary language
- **URL** — Canonical repo URL

### Why It Matters

- Projects, libraries, patterns
- Code examples and usage patterns
- Documentation and architecture decisions

### Risks / Limitations

- README may be outdated vs actual code
- Large repos; must scope to relevant files
- Stars/forks are popularity signals, not quality guarantees
