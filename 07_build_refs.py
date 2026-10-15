#!/usr/bin/env python3
"""
07_build_refs.py

Builds a Vancouver-style reference library from the verified registry metadata
produced by 06_verify_dois.py. Bibliographic details come from Crossref or
DataCite rather than from any secondary summary, so author lists, journal names,
volumes, pages, and years are as registered by the publisher.

Outputs
  ../verification/reference_library.md    human-readable, grouped by journal
  ../verification/reference_library.json  machine-readable
"""

import html
import json
import os
import re

_TAG = re.compile(r"<[^>]{1,40}>")


def clean_markup(s: str) -> str:
    """Remove publisher JATS markup and unescape entities in registry metadata.

    Crossref returns some titles with <scp>, <i>, and <sub> tags and with doubly
    escaped ampersands. Those artifacts must not reach the rendered reference
    list. No word of the registered metadata is changed.
    """
    if not isinstance(s, str):
        return s
    out = s
    for _ in range(3):
        prev = out
        out = html.unescape(out)
        if out == prev:
            break
    out = _TAG.sub(" ", out)
    out = out.replace("\u2010", "-").replace("\u2011", "-")
    out = re.sub(r"\s+-(?=\w)", "-", out)
    out = re.sub(r"(?<=\w)-\s+(?=\w)", "-", out)
    out = re.sub(r"\s+(?=['\u2019]s\b)", "", out)
    # House style admits no em or en dashes. Publisher titles that use them are
    # normalized without changing a single word: a dash inside a compound term
    # becomes a hyphen, a dash separating a subtitle becomes a colon, and a dash
    # separating a trailing clause becomes a comma.
    out = re.sub(r"(?<=[A-Za-z0-9])\u2013(?=[A-Za-z0-9/])", "-", out)
    out = re.sub(r"(?<=[A-Za-z0-9])\u2014(?=[a-z])", "-", out)
    out = re.sub(r"(?<=[A-Za-z0-9])\u2014(?=[A-Z])", ": ", out)
    out = re.sub(r"\s[\u2013\u2014]\s(?=[A-Z])", ": ", out)
    out = re.sub(r"\s[\u2013\u2014]\s(?=[a-z])", ", ", out)
    out = re.sub(r"[\u2013\u2014]", "-", out)
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()

SRC = "../verification/doi_crossref.json"
OUTMD = "../verification/reference_library.md"
OUTJSON = "../verification/reference_library.json"


def surname_initials(name: str) -> str:
    """Convert 'Obermeyer Ziad' to 'Obermeyer Z'. Leave group authors intact."""
    name = re.sub(r"\s+", " ", name).strip()
    if not name:
        return ""
    parts = name.split(" ")
    if len(parts) == 1:
        return parts[0]
    family = parts[0]
    initials = "".join(p[0].upper() for p in parts[1:] if p and p[0].isalpha())
    return f"{family} {initials}" if initials else family


def vancouver(rec: dict, doi: str) -> str:
    au = [surname_initials(a) for a in rec.get("authors", []) if a]
    n = rec.get("n_authors") or len(au)
    if not au:
        authors = ""
    elif n > 6:
        authors = ", ".join(au[:6]) + ", et al. "
    else:
        authors = ", ".join(au) + ". "

    title = clean_markup(rec.get("title") or "").rstrip(".")
    journal = clean_markup(rec.get("short_container") or rec.get("container") or "")
    year = rec.get("year") or ""
    vol = rec.get("volume") or ""
    iss = rec.get("issue") or ""
    pg = rec.get("page") or rec.get("article_number") or ""

    loc = f"{year}"
    if vol:
        loc += f";{vol}"
        if iss:
            loc += f"({iss})"
    if pg:
        loc += f":{pg}"

    tsep = "" if title.endswith(("?", "!")) else "."
    s = f"{authors}{title}{tsep} {journal} {loc}."
    s = re.sub(r"\s+", " ", s).replace(" .", ".").strip()
    return f"{s} DOI: {doi}."


def main():
    data = json.load(open(SRC))
    recs = data["records"]
    out = {}
    for doi, r in recs.items():
        if r.get("status") != "verified":
            continue
        out[doi] = {
            "vancouver": vancouver(r, doi),
            "title": clean_markup(r.get("title", "")),
            "journal": clean_markup(r.get("short_container") or r.get("container", "")),
            "year": r.get("year"),
            "registry": r.get("registry", ""),
            "type": r.get("type", ""),
            "citations": r.get("is_referenced_by_count"),
            "sources": r.get("sources", []),
        }

    json.dump(out, open(OUTJSON, "w"), indent=1)

    by_year = {}
    for doi, v in out.items():
        by_year.setdefault(v["year"] or 0, []).append((doi, v))

    with open(OUTMD, "w") as fh:
        fh.write("# Verified reference library\n\n")
        fh.write(f"Generated from registry metadata on {data['generated']}.\n\n")
        fh.write(f"Candidate DOIs scanned: {data['n_candidates']}. "
                 f"Verified: {data['n_verified']}. "
                 f"Not found: {data['n_not_found']}. "
                 f"Retrieval errors: {data['n_error']}.\n\n")
        fh.write("Every entry below was retrieved from the Crossref or DataCite "
                 "REST API using the DOI as the key. Author lists, journal names, "
                 "volumes, issues, pages, and years are reproduced as registered "
                 "by the publisher.\n\n")
        for yr in sorted(by_year, reverse=True):
            fh.write(f"\n## {yr if yr else 'Year not registered'}\n\n")
            for doi, v in sorted(by_year[yr], key=lambda t: t[1]["vancouver"]):
                cit = v["citations"]
                tail = f"  _[{v['registry']}"
                if cit is not None:
                    tail += f", cited {cit}"
                tail += "]_"
                fh.write(f"- {v['vancouver']}{tail}\n")

    print(f"wrote {OUTMD} and {OUTJSON}: {len(out)} verified references")
    # Show a sample for inspection
    for doi in list(out)[:6]:
        print("\n ", out[doi]["vancouver"])


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
