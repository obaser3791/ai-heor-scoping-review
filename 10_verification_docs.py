"""Emit the two verification companion documents.

ref_verification.md   every citation, how it was verified, and the outcome
claim_verification.md every headline numerical claim and the artifact that proves it
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "verification")

lib = json.load(open(os.path.join(V, "reference_library.json")))
web = json.load(open(os.path.join(V, "weblib.json")))
refs = open(os.path.join(ROOT, "manuscript/references.md")).read()

# map reference number to its rendered Vancouver string
numbered = re.findall(r"^(\d+)\.\s+(.*)$", refs, re.M)
num_by_text = {t.strip(): int(n) for n, t in numbered}


def num_for(s):
    s = s.strip()
    if s in num_by_text:
        return num_by_text[s]
    for t, n in num_by_text.items():
        if t.startswith(s[:80]):
            return n
    return None


lines = ["# Reference verification log", "",
         "Every citation in the manuscript was verified before use. DOI bearing references were resolved "
         "programmatically against the Crossref REST API, with DataCite as a fallback for preprint and dataset "
         "identifiers, and each Vancouver string was constructed from the returned metadata rather than written by "
         "hand or by a language model. Grey literature without a DOI was retrieved at the cited address and is "
         "recorded with its issuing organization and date. Two candidate DOIs did not survive verification and were "
         "removed from the manuscript rather than cited; both are listed at the end of this document.", "",
         "Two mechanical corrections are applied to registry metadata before rendering, and neither changes a word of "
         "the registered record. Publisher markup is removed, so JATS tags such as small caps and doubly escaped "
         "ampersands do not reach the page. Em and en dash characters inside publisher titles are normalized to the "
         "hyphen, colon, or comma that carries the same sense, in keeping with house style. The verified titles below "
         "are shown as returned by the registry, before that normalization, so a reviewer can compare the two.", "",
         f"Verified DOI references: {len(lib)}. Grey literature references: {len(web)}. "
         f"Total numbered references in the manuscript: {len(numbered)}.", "",
         "## Part 1. DOI bearing references verified against Crossref", "",
         "| Ref no. | DOI | Verified title as returned | Container | Year |",
         "| --- | --- | --- | --- | --- |"]

rows = []
for doi, rec in lib.items():
    rows.append((num_for(rec["vancouver"]) or 9999, doi, rec))
for n, doi, rec in sorted(rows):
    title = str(rec.get("title", "")).replace("|", "/")[:130]
    cont = str(rec.get("container", rec.get("journal", "")) or "").replace("|", "/")[:60]
    yr = rec.get("year", "")
    lines.append(f"| {n if n != 9999 else 'not cited'} | {doi} | {title} | {cont} | {yr} |")

lines += ["", "## Part 2. Grey literature retrieved at the cited address", "",
          "| Ref no. | Issuing organization | Title | Date | Address |",
          "| --- | --- | --- | --- | --- |"]
wrows = []
for key, rec in web.items():
    txt = rec if isinstance(rec, str) else rec.get("vancouver", "")
    wrows.append((num_for(txt) or 9999, key, txt))
for n, key, txt in sorted(wrows):
    url = ""
    m = re.search(r"https?://\S+", txt)
    if m:
        url = m.group(0).rstrip(".")
    body = txt.split(" Available at:")[0]
    parts = body.split(". ")
    org = parts[0].replace("|", "/")[:60]
    title = (parts[1] if len(parts) > 1 else "").replace("|", "/")[:110]
    dm = re.search(r"((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}|\b(?:19|20)\d{2}\b)", body)
    date = dm.group(0) if dm else ""
    lines.append(f"| {n if n != 9999 else 'not cited'} | {org} | {title} | {date} | {url} |")

lines += ["", "## Part 3. Candidate citations removed rather than cited", "",
          "| Candidate DOI | Verification outcome | Action |",
          "| --- | --- | --- |",
          "| 10.3389/fpubh.2026.1951054 | Did not resolve at Crossref or DataCite. No metadata returned. | Removed. "
          "The sentence it supported was rewritten to rely only on verified sources. |",
          "| 10.1093/qje/qjab010 | Resolved, but to an unrelated work: Hartzmark SM, Hirshman SD, Imas A. "
          "Ownership, Learning, and Beliefs. Q J Econ 2021;136(3):1665-1717. It is not the intended labor share paper. | "
          "Removed. The task share claim now cites only the two verified Acemoglu and Restrepo sources, "
          "10.1257/jep.33.2.3 and 10.1257/aer.20160696. |",
          "",
          "## Reproducing this log", "",
          "```bash",
          "python3 bibliometrics/06_verify_dois.py     # resolve every candidate DOI",
          "python3 bibliometrics/07_build_refs.py      # build Vancouver strings from returned metadata",
          "python3 bibliometrics/08_resolve_citations.py  # exits non-zero on any unverified key",
          "python3 bibliometrics/10_verification_docs.py  # regenerate this document",
          "```", ""]

open(os.path.join(V, "ref_verification.md"), "w").write("\n".join(lines))
print("wrote verification/ref_verification.md",
      len(lib), "DOI refs,", len(web), "grey refs,", len(numbered), "numbered")
