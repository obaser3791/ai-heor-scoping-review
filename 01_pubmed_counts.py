#!/usr/bin/env python3
"""
01_pubmed_counts.py

Original bibliometric analysis for the manuscript
"Artificial Intelligence in Health Economics and Outcomes Research".

Queries the NCBI PubMed E-utilities esearch endpoint for annual publication
counts for a prespecified set of query strings, using the Date of Publication
(dp) field. Only counts are retrieved (rettype=count), so no record-level data
are stored. Results are written to a tidy CSV.

Reproducibility notes
  * PubMed is a living database. Counts drift as records are indexed,
    corrected, or reclassified. The retrieval date is stamped into the output.
  * No API key is required for the volume of requests issued here, but the
    script respects the NCBI rate limit of 3 requests per second.

Usage
  python 01_pubmed_counts.py --out ../data/pubmed_counts.csv
"""

import argparse
import csv
import datetime as dt
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# ----------------------------------------------------------------------------
# Query blocks
# ----------------------------------------------------------------------------

AI_BLOCK = (
    '("artificial intelligence"[tiab] OR "machine learning"[tiab] OR '
    '"deep learning"[tiab] OR "neural network"[tiab] OR "neural networks"[tiab] OR '
    '"large language model"[tiab] OR "large language models"[tiab] OR '
    '"natural language processing"[tiab] OR "generative AI"[tiab] OR '
    '"Artificial Intelligence"[Mesh])'
)

HEOR_BLOCK = (
    '("health economics"[tiab] OR "outcomes research"[tiab] OR '
    '"pharmacoeconomics"[tiab] OR "cost-effectiveness"[tiab] OR '
    '"cost effectiveness"[tiab] OR "cost-utility"[tiab] OR '
    '"budget impact"[tiab] OR "health technology assessment"[tiab] OR '
    '"economic evaluation"[tiab] OR "quality-adjusted life"[tiab] OR '
    '"real-world evidence"[tiab] OR "real world evidence"[tiab] OR '
    '"Cost-Benefit Analysis"[Mesh] OR "Economics, Pharmaceutical"[Mesh] OR '
    '"Technology Assessment, Biomedical"[Mesh])'
)

QUERIES = {
    # Denominators
    "all_pubmed": "all[sb]",
    "ai_all_medicine": AI_BLOCK,
    "heor_all": HEOR_BLOCK,
    # Primary intersection
    "ai_heor": f"{AI_BLOCK} AND {HEOR_BLOCK}",
    # HEOR task domains
    "ai_economic_evaluation": (
        f"{AI_BLOCK} AND (\"cost-effectiveness\"[tiab] OR \"cost effectiveness\"[tiab] "
        'OR "cost-utility"[tiab] OR "economic evaluation"[tiab] OR '
        '"Cost-Benefit Analysis"[Mesh])'
    ),
    "ai_hta": (
        f"{AI_BLOCK} AND (\"health technology assessment\"[tiab] OR "
        '"Technology Assessment, Biomedical"[Mesh] OR "reimbursement"[tiab] OR '
        '"payer"[tiab] OR "market access"[tiab])'
    ),
    "ai_rwe": (
        f"{AI_BLOCK} AND (\"real-world evidence\"[tiab] OR \"real world evidence\"[tiab] "
        'OR "real-world data"[tiab] OR "claims data"[tiab] OR '
        '"administrative claims"[tiab] OR "electronic health record"[tiab] OR '
        '"Electronic Health Records"[Mesh])'
    ),
    "ai_evidence_synthesis": (
        f"{AI_BLOCK} AND (\"systematic review\"[tiab] OR \"evidence synthesis\"[tiab] "
        'OR "meta-analysis"[tiab] OR "literature screening"[tiab] OR '
        '"abstract screening"[tiab] OR "data extraction"[tiab])'
    ),
    "ai_causal_inference": (
        f"{AI_BLOCK} AND (\"causal inference\"[tiab] OR \"propensity score\"[tiab] "
        'OR "confounding"[tiab] OR "target trial"[tiab] OR '
        '"treatment effect"[tiab] OR "causal forest"[tiab] OR '
        '"targeted maximum likelihood"[tiab] OR "double machine learning"[tiab])'
    ),
    "ai_decision_modeling": (
        f"{AI_BLOCK} AND (\"microsimulation\"[tiab] OR \"decision model\"[tiab] "
        'OR "Markov model"[tiab] OR "discrete event simulation"[tiab] OR '
        '"decision-analytic"[tiab] OR "simulation model"[tiab])'
    ),
    "ai_patient_reported": (
        f"{AI_BLOCK} AND (\"patient-reported outcome\"[tiab] OR "
        '"patient reported outcome"[tiab] OR "health-related quality of life"[tiab] '
        'OR "utility elicitation"[tiab] OR "EQ-5D"[tiab])'
    ),
    # Governance and reporting counterweight
    "ai_reporting_governance": (
        f"{AI_BLOCK} AND (\"reporting guideline\"[tiab] OR \"reporting standard\"[tiab] "
        'OR "transparency"[tiab] OR "reproducibility"[tiab] OR "governance"[tiab] OR '
        '"algorithmic bias"[tiab] OR "risk of bias"[tiab])'
    ),
    "llm_heor": (
        '("large language model"[tiab] OR "large language models"[tiab] OR '
        '"GPT-4"[tiab] OR "GPT-3"[tiab] OR "ChatGPT"[tiab] OR "generative AI"[tiab] OR '
        f'"generative artificial intelligence"[tiab]) AND {HEOR_BLOCK}'
    ),
}

YEARS = list(range(2010, 2026))


def esearch_count(term: str, year: int, api_key: str | None = None,
                  retries: int = 4) -> int:
    """Return the PubMed record count for `term` restricted to publication `year`."""
    full = f"({term}) AND {year}[dp]"
    params = {"db": "pubmed", "term": full, "rettype": "count", "retmode": "xml",
              "tool": "heor-ai-bibliometrics", "email": "bibliometrics@example.org"}
    if api_key:
        params["api_key"] = api_key
    url = ESEARCH + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                root = ET.fromstring(resp.read())
            node = root.find("Count")
            if node is None or node.text is None:
                raise ValueError("no Count element in esearch response")
            return int(node.text)
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"esearch failed for {term!r} {year}: {last}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../data/pubmed_counts.csv")
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--delay", type=float, default=0.40,
                    help="seconds between requests (NCBI limit is 3/s without a key)")
    args = ap.parse_args()

    stamp = dt.date.today().isoformat()
    rows = []
    for name, term in QUERIES.items():
        for year in YEARS:
            n = esearch_count(term, year, args.api_key)
            rows.append({"query": name, "year": year, "count": n,
                         "retrieved": stamp})
            print(f"{name:28s} {year}  {n:>9,}", file=sys.stderr)
            time.sleep(args.delay)

    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["query", "year", "count", "retrieved"])
        w.writeheader()
        w.writerows(rows)

    # Persist the exact query strings alongside the counts for auditability.
    qpath = args.out.replace(".csv", "_querystrings.csv")
    with open(qpath, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["query", "pubmed_query_string"])
        for name, term in QUERIES.items():
            w.writerow([name, term])

    print(f"\nwrote {len(rows)} rows to {args.out}", file=sys.stderr)
    print(f"wrote query strings to {qpath}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
