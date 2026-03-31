"""Tranche 32 evidence: review 10 cannot-classify cohort snapshots + optional FR document JSON. Not production."""
from __future__ import annotations

import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "lane_b_real_observation"
LOG = ROOT / "tranche21_fr_slot_runs.jsonl"
COHORT_IDS = [
    "t21_fr_full_20260328T160000Z",
    "t21_fr_full_20260328T180000Z",
    "t21_fr_full_20260328T200000Z",
    "t21_fr_full_20260328T220000Z",
    "t21_fr_full_20260329T000000Z",
    "t21_fr_full_20260329T020000Z",
    "t21_fr_full_20260329T040000Z",
    "t21_fr_full_20260329T060000Z",
    "t21_fr_full_20260329T080000Z",
    "t21_fr_full_20260329T100000Z",
]


def extract_results0_fields(preview: str) -> tuple[str | None, str | None]:
    idx = preview.find('"results":[{')
    if idx < 0:
        return None, None
    sub = preview[idx:]
    m = re.search(r'"document_number"\s*:\s*"([^"]+)"', sub)
    p = re.search(r'"publication_date"\s*:\s*"([^"]+)"', sub)
    return (m.group(1) if m else None, p.group(1) if p else None)


def fetch_document_json(document_number: str) -> dict | None:
    url = f"https://www.federalregister.gov/api/v1/documents/{document_number}.json"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"_error": str(e)}


def main() -> None:
    by_id: dict[str, dict] = {}
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        by_id[o["task_id"]] = o

    rows = []
    for tid in COHORT_IDS:
        o = by_id[tid]
        name = pathlib.Path(o["artifact_path"]).name
        snap = json.loads((ROOT / name).read_text(encoding="utf-8"))
        prev = snap.get("response_preview_utf8") or ""
        doc_num, pub_d = extract_results0_fields(prev)
        t_obs = o["actual_started_at_utc"]
        rows.append(
            {
                "task_id": tid,
                "actual_started_at_utc": t_obs,
                "document_number_results0": doc_num,
                "publication_date_results0": pub_d,
            }
        )

    distinct_docs = sorted({r["document_number_results0"] for r in rows if r["document_number_results0"]})
    api = {}
    for dn in distinct_docs:
        api[dn] = fetch_document_json(dn)

    out = {"cohort_rows": rows, "distinct_document_numbers": distinct_docs, "api_documents": api}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
