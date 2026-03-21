# First Run Packet Template

Template for building the source intake packet for the first Research Swarm run.

---

## Required Inputs

| Field | Description |
|-------|-------------|
| packet_id | Unique identifier (e.g., rs-intake-001) |
| source_url | Canonical YouTube video URL |
| source_type | `youtube` |
| raw_content | Full or partial transcript text |
| created_at | ISO 8601 timestamp |

## Optional Metadata

| Field | Description |
|-------|-------------|
| title | Video title |
| author | Channel or creator name |
| channel | Channel name |
| published_at | ISO 8601 when video was published |
| content_completeness | full, partial, summary_only |
| raw_content_format | transcript, markdown, plain_text, code, mixed |
| captured_at | ISO 8601 when transcript was captured |

---

## Example Packet Structure

Schema: `schemas/source_intake.schema.json`

```json
{
  "packet_id": "rs-intake-001",
  "source_url": "https://www.youtube.com/watch?v=PLACEHOLDER",
  "source_type": "youtube",
  "raw_content": "[Paste transcript here. Placeholder: This is where the operator inserts the captured transcript text. Replace this entire bracket with the actual transcript.]",
  "created_at": "2026-03-20T10:00:00Z",
  "metadata": {
    "title": "Video Title Here",
    "author": "Channel Name",
    "channel": "Channel Name",
    "published_at": "2025-01-15T00:00:00Z"
  },
  "content_completeness": "full",
  "raw_content_format": "transcript",
  "captured_at": "2026-03-20T09:55:00Z"
}
```

---

## Operator Notes

### Capturing a Transcript Manually

1. Open the YouTube video.
2. Click the three dots (⋮) below the video.
3. Select "Show transcript" (or "Transcript").
4. Copy the transcript text. Timestamps may be kept or removed. Preserve readable transcript text; do not materially alter source wording except optional timestamp cleanup.
5. Paste into `raw_content` in the packet JSON.
6. If transcript is truncated or partial, set `content_completeness: "partial"`.
7. Set `raw_content_format: "transcript"`.
