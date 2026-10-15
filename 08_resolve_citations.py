#!/usr/bin/env python3
"""Resolve {{c:key1;key2}} citation groups in the manuscript source into
sequential Vancouver numbers and emit a numbered reference list.

Keys beginning with "10." are looked up in verification/reference_library.json
(Crossref/DataCite verified). All other keys are looked up in
verification/weblib.json (grey literature, guidance documents, press releases).

Any unresolved key aborts the build, so no citation can silently vanish.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Usage:
#   08_resolve_citations.py                      resolve the single manuscript
#   08_resolve_citations.py SRC OUT REFS_OUT     resolve any source, used for the
#                                                two part series, where each part
#                                                carries its own numbering drawn
#                                                from the same verified library
if len(sys.argv) == 4:
    SRC, OUT, REFS_OUT = (Path(a) for a in sys.argv[1:4])
else:
    SRC = ROOT / "manuscript" / "manuscript_src.md"
    OUT = ROOT / "manuscript" / "manuscript.md"
    REFS_OUT = ROOT / "manuscript" / "references.md"

# DOIs that failed verification and must never be cited.
BLOCKED = {"10.3389/fpubh.2026.1951054"}

doilib = json.loads((ROOT / "verification" / "reference_library.json").read_text())
weblib = json.loads((ROOT / "verification" / "weblib.json").read_text())
doilib_lower = {k.lower(): v for k, v in doilib.items()}

text = SRC.read_text()

order = []          # keys in order of first appearance
numbers = {}        # key -> number
missing = []
blocked_used = []

TOKEN = re.compile(r"\{\{c:([^}]+)\}\}")


def resolve(key):
    key = key.strip()
    if key.lower() in BLOCKED:
        blocked_used.append(key)
        return None
    if key.startswith("10."):
        rec = doilib_lower.get(key.lower())
        if rec is None:
            missing.append(key)
            return None
        return rec["vancouver"]
    rec = weblib.get(key)
    if rec is None:
        missing.append(key)
        return None
    return rec


strings = {}


def repl(m):
    keys = [k.strip() for k in m.group(1).split(";") if k.strip()]
    nums = []
    for k in keys:
        s = resolve(k)
        if s is None:
            continue
        if k not in numbers:
            numbers[k] = len(order) + 1
            order.append(k)
            strings[k] = s
        nums.append(numbers[k])
    if not nums:
        return ""
    # collapse runs of consecutive numbers
    nums = sorted(set(nums))
    parts = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            parts.append(f"{nums[i]}-{nums[j]}")
        else:
            parts.extend(str(n) for n in nums[i:j + 1])
        i = j + 1
    return "^" + ",".join(parts) + "^"


resolved = TOKEN.sub(repl, text)

if missing:
    print("UNRESOLVED CITATION KEYS:", file=sys.stderr)
    for k in sorted(set(missing)):
        print("  " + k, file=sys.stderr)
    sys.exit(1)
if blocked_used:
    print("BLOCKED (UNVERIFIED) DOIs USED:", file=sys.stderr)
    for k in sorted(set(blocked_used)):
        print("  " + k, file=sys.stderr)
    sys.exit(1)

ref_lines = ["## References", ""]
for k in order:
    ref_lines.append(f"{numbers[k]}. {strings[k]}")
    ref_lines.append("")
ref_block = "\n".join(ref_lines)

if "<!--REFERENCES-->" in resolved:
    resolved = resolved.replace("<!--REFERENCES-->", ref_block)
else:
    resolved = resolved.rstrip() + "\n\n" + ref_block

OUT.write_text(resolved)
REFS_OUT.write_text(ref_block)

n_doi = sum(1 for k in order if k.startswith("10."))
print(f"Resolved {len(order)} unique references "
      f"({n_doi} with verified DOIs, {len(order) - n_doi} grey literature).")
print(f"Wrote {OUT}")
print(f"Wrote {REFS_OUT}")
