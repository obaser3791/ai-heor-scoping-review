#!/usr/bin/env python3
"""
02_fetch_records.py

Retrieve the full record set for the primary search of the systematic scoping
review, "Artificial Intelligence in Health Economics and Outcomes Research".

Uses NCBI E-utilities esearch (with usehistory) followed by paged efetch to
collect PMID, DOI, year, journal, title, abstract, publication types, and
MeSH descriptors for every record returned by the primary search string.

Output: JSONL, one record per line, written to ../data/records.jsonl

Usage
  python 02_fetch_records.py --out ../data/records.jsonl
"""

import argparse
import datetime as dt
import json
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from importlib.machinery import SourceFileLoader

_mod = SourceFileLoader("q", "01_pubmed_counts.py").load_module()
AI_BLOCK = _mod.AI_BLOCK
HEOR_BLOCK = _mod.HEOR_BLOCK

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

PRIMARY = f"({AI_BLOCK} AND {HEOR_BLOCK}) AND 2010:2025[dp]"


def _get(url: str, retries: int = 5) -> bytes:
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"request failed: {url[:120]}... {last}")


def text_of(node) -> str:
    """Flatten an element's text, including nested markup such as <i> or <sup>."""
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def parse_article(art) -> dict:
    med = art.find("MedlineCitation")
    if med is None:
        return {}
    pmid = text_of(med.find("PMID"))
    art_node = med.find("Article")
    if art_node is None:
        return {}

    title = text_of(art_node.find("ArticleTitle"))

    # Abstract: concatenate all labelled sections.
    parts = []
    abst = art_node.find("Abstract")
    if abst is not None:
        for at in abst.findall("AbstractText"):
            label = at.get("Label")
            body = text_of(at)
            parts.append(f"{label}: {body}" if label else body)
    abstract = " ".join(p for p in parts if p)

    journal = ""
    jn = art_node.find("Journal")
    if jn is not None:
        journal = text_of(jn.find("Title")) or text_of(jn.find("ISOAbbreviation"))

    # Publication year: prefer ArticleDate, fall back to JournalIssue PubDate.
    year = ""
    ad = art_node.find("ArticleDate/Year")
    if ad is not None:
        year = text_of(ad)
    if not year and jn is not None:
        y = jn.find("JournalIssue/PubDate/Year")
        if y is not None:
            year = text_of(y)
        else:
            md = jn.find("JournalIssue/PubDate/MedlineDate")
            if md is not None:
                year = text_of(md)[:4]

    pubtypes = [text_of(p) for p in art_node.findall("PublicationTypeList/PublicationType")]
    mesh = [text_of(m) for m in med.findall("MeshHeadingList/MeshHeading/DescriptorName")]

    doi = ""
    for eid in art_node.findall("ELocationID"):
        if eid.get("EIdType") == "doi":
            doi = text_of(eid)
            break
    if not doi:
        pubmed = art.find("PubmedData")
        if pubmed is not None:
            for aid in pubmed.findall("ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = text_of(aid)
                    break

    lang = [text_of(l) for l in art_node.findall("Language")]

    return {"pmid": pmid, "doi": doi, "year": year, "journal": journal,
            "title": title, "abstract": abstract, "pubtypes": pubtypes,
            "mesh": mesh, "languages": lang}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../data/records.jsonl")
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--batch", type=int, default=200)
    args = ap.parse_args()

    params = {"db": "pubmed", "term": PRIMARY, "usehistory": "y", "retmode": "xml",
              "retmax": "0", "tool": "heor-ai-bibliometrics",
              "email": "bibliometrics@example.org"}
    if args.api_key:
        params["api_key"] = args.api_key
    root = ET.fromstring(_get(ESEARCH + "?" + urllib.parse.urlencode(params)))
    total = int(root.findtext("Count", "0"))
    webenv = root.findtext("WebEnv", "")
    qkey = root.findtext("QueryKey", "")
    print(f"primary search returned {total:,} records", file=sys.stderr)

    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    n = 0
    with open(args.out, "w") as fh:
        for start in range(0, total, args.batch):
            fp = {"db": "pubmed", "query_key": qkey, "WebEnv": webenv,
                  "retstart": str(start), "retmax": str(args.batch),
                  "retmode": "xml", "tool": "heor-ai-bibliometrics",
                  "email": "bibliometrics@example.org"}
            if args.api_key:
                fp["api_key"] = args.api_key
            data = _get(EFETCH + "?" + urllib.parse.urlencode(fp))
            try:
                rroot = ET.fromstring(data)
            except ET.ParseError as exc:
                print(f"  parse error at {start}: {exc}", file=sys.stderr)
                time.sleep(2)
                continue
            for art in rroot.findall("PubmedArticle"):
                rec = parse_article(art)
                if rec:
                    rec["retrieved"] = stamp
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n += 1
            print(f"  fetched {min(start + args.batch, total):,}/{total:,}", file=sys.stderr)
            time.sleep(0.40)

    print(f"wrote {n:,} records to {args.out}", file=sys.stderr)
    with open(args.out.replace(".jsonl", "_search.json"), "w") as fh:
        json.dump({"primary_query": PRIMARY, "esearch_count": total,
                   "records_written": n, "retrieved_utc": stamp}, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
