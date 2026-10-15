#!/usr/bin/env python3
"""
06_verify_dois.py

Programmatic verification of every DOI that appears in the evidence base
against the Crossref REST API. For each DOI the script records whether it
resolves, and the registered title, container title, year, volume, issue,
pages, and publisher exactly as Crossref returns them.

Usage
  python3 06_verify_dois.py --inputs ../research_*.md --out ../verification/doi_crossref.json
"""

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

MAILTO = "heor.review.verification@example.org"
UA = f"heor-ai-scoping-review/1.0 (mailto:{MAILTO})"

# DOIs are matched permissively then trimmed of trailing punctuation and markup.
# Parentheses are legal inside DOIs (for example Elsevier suffixes such as
# 10.1016/S2468-1253(25)00133-5), so they are matched and then balanced,
# rather than treated as terminators.
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\]},;]+", re.IGNORECASE)
TRAIL = ".,;:]}>\"'`*_"


def normalize(d: str) -> str:
    d = d.strip().replace("\\", "")
    while True:
        while d and d[-1] in TRAIL:
            d = d[:-1]
        # Drop a trailing close paren only when it is unbalanced.
        if d.endswith(")") and d.count("(") < d.count(")"):
            d = d[:-1]
            continue
        break
    return d.lower()


def harvest(paths: list[str]) -> dict[str, list[str]]:
    found: dict[str, set[str]] = {}
    for p in paths:
        try:
            txt = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in DOI_RE.finditer(txt):
            d = normalize(m.group(0))
            if len(d) < 8:
                continue
            found.setdefault(d, set()).add(os.path.basename(p))
    return {k: sorted(v) for k, v in sorted(found.items())}


def datacite(doi: str, retries: int = 2) -> dict:
    """Fallback registry. arXiv preprints and some agency reports register their
    DOIs with DataCite rather than Crossref, so a Crossref 404 alone does not
    mean the DOI is invalid."""
    url = "https://api.datacite.org/dois/" + urllib.parse.quote(doi, safe="")
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                a = json.load(r)["data"]["attributes"]
            return {
                "status": "verified",
                "registry": "DataCite",
                "title": (a.get("titles") or [{}])[0].get("title", ""),
                "container": (a.get("container") or {}).get("title", "")
                             or a.get("publisher", ""),
                "short_container": "",
                "year": a.get("publicationYear"),
                "volume": "", "issue": "", "page": "", "article_number": "",
                "publisher": a.get("publisher", ""),
                "type": (a.get("types") or {}).get("resourceTypeGeneral", ""),
                "authors": [c.get("name", "") for c in (a.get("creators") or [])][:12],
                "n_authors": len(a.get("creators") or []),
                "is_referenced_by_count": None,
                "url": a.get("url", ""),
            }
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {"status": "not_found", "http": 404, "registry": "DataCite"}
            if attempt < retries - 1:
                time.sleep(2.0)
                continue
            return {"status": "error", "http": e.code, "registry": "DataCite"}
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2.0)
                continue
            return {"status": "error", "message": type(e).__name__,
                    "registry": "DataCite"}
    return {"status": "error", "message": "exhausted", "registry": "DataCite"}


def crossref(doi: str, retries: int = 3) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    url += "?mailto=" + urllib.parse.quote(MAILTO)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                msg = json.load(r)["message"]
            return {
                "status": "verified",
                "title": (msg.get("title") or [""])[0],
                "container": (msg.get("container-title") or [""])[0],
                "short_container": (msg.get("short-container-title") or [""])[0],
                "year": ((msg.get("issued", {}).get("date-parts") or [[None]])[0] or [None])[0],
                "volume": msg.get("volume", ""),
                "issue": msg.get("issue", ""),
                "page": msg.get("page", ""),
                "article_number": msg.get("article-number", ""),
                "publisher": msg.get("publisher", ""),
                "type": msg.get("type", ""),
                "authors": [
                    ((a.get("family", "") + " " + (a.get("given", "") or "")).strip()
                     or a.get("name", ""))
                    for a in (msg.get("author") or [])
                ][:12],
                "n_authors": len(msg.get("author") or []),
                "is_referenced_by_count": msg.get("is-referenced-by-count"),
                "url": msg.get("URL", ""),
                "registry": "Crossref",
            }
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return datacite(doi)
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(2.5 * (attempt + 1))
                continue
            return {"status": "error", "http": e.code}
        except Exception as e:  # network, timeout, decode
            if attempt < retries - 1:
                time.sleep(2.0 * (attempt + 1))
                continue
            return {"status": "error", "message": type(e).__name__}
    return {"status": "error", "message": "exhausted"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--out", default="../verification/doi_crossref.json")
    ap.add_argument("--sleep", type=float, default=0.12)
    args = ap.parse_args()

    paths = []
    for pat in args.inputs:
        paths.extend(sorted(glob.glob(pat)))
    print(f"scanning {len(paths)} files")
    found = harvest(paths)
    print(f"unique candidate DOIs: {len(found)}")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    cache = {}
    if os.path.exists(args.out):
        try:
            cache = json.load(open(args.out)).get("records", {})
            print(f"reusing {len(cache)} cached results")
        except Exception:
            cache = {}

    records = {}
    ok = bad = err = 0
    for i, (doi, srcs) in enumerate(found.items(), 1):
        if doi in cache and cache[doi].get("status") == "verified":
            rec = cache[doi]
        else:
            rec = crossref(doi)
            time.sleep(args.sleep)
        rec["sources"] = srcs
        records[doi] = rec
        if rec["status"] == "verified":
            ok += 1
        elif rec["status"] == "not_found":
            bad += 1
        else:
            err += 1
        if i % 25 == 0 or i == len(found):
            print(f"  {i}/{len(found)}  verified={ok} not_found={bad} error={err}",
                  flush=True)

    out = {"generated": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
           "api": "https://api.crossref.org/works/{doi}",
           "n_candidates": len(found), "n_verified": ok,
           "n_not_found": bad, "n_error": err, "records": records}
    json.dump(out, open(args.out, "w"), indent=1)
    print(f"\nwrote {args.out}")
    print(f"verified {ok} / {len(found)}   not found {bad}   error {err}")

    if bad:
        print("\n--- DOIs that did NOT resolve in Crossref ---")
        for d, r in records.items():
            if r["status"] == "not_found":
                print(f"  {d}   cited in: {', '.join(r['sources'])}")
    if err:
        print("\n--- DOIs with retrieval errors (retry before use) ---")
        for d, r in records.items():
            if r["status"] == "error":
                print(f"  {d}   {r.get('http') or r.get('message')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
