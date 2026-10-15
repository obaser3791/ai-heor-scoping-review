#!/usr/bin/env python3
"""
03_screen_classify.py

Eligibility screening and prespecified dictionary classification for the
systematic scoping review "Artificial Intelligence in Health Economics and
Outcomes Research".

Stage 1  Eligibility screening (fully automated, auditable rules)
Stage 2  Multi-label classification of eligible records into HEOR task domains
Stage 3  Single-label classification of the dominant AI method family
Stage 4  Descriptive tabulation: annual counts, growth, journals, study designs

The classifier is a transparent regular-expression dictionary applied to the
concatenated title and abstract. It is prespecified in DOMAIN_DICT and
METHOD_DICT below and is released with the manuscript so that any reader can
re-run, inspect, or modify it. It is deliberately not a black box.

Outputs (all to ../data/ and ../out/)
  screened.jsonl              one line per retrieved record with screening result
  eligible.csv                eligible records with assigned labels
  prisma_counts.json          PRISMA-ScR flow numbers
  tab_annual.csv              annual counts overall and by domain
  tab_journals.csv            journal distribution
  tab_designs.csv             publication type distribution
  sample_for_llm_audit.jsonl  random sample for independent LLM classification

Usage
  python 03_screen_classify.py
"""

import argparse
import csv
import json
import random
import re
import collections
import os

# ---------------------------------------------------------------------------
# Prespecified eligibility criteria
# ---------------------------------------------------------------------------

YEAR_MIN, YEAR_MAX = 2010, 2025

# Publication types that do not report or review primary work and are therefore
# excluded from the analytic set.
EXCLUDED_PUBTYPES = {
    "Comment", "Editorial", "Letter", "Published Erratum", "Retraction of Publication",
    "Retracted Publication", "News", "Newspaper Article", "Biography", "Interview",
    "Preprint", "Expression of Concern", "Autobiography", "Personal Narrative",
}

# ---------------------------------------------------------------------------
# Prespecified domain dictionary (multi-label)
# ---------------------------------------------------------------------------

DOMAIN_DICT = {
    "economic_evaluation": [
        r"cost[- ]effectiveness", r"cost[- ]utility", r"cost[- ]benefit",
        r"incremental cost", r"\bICER\b", r"quality[- ]adjusted life",
        r"\bQALY", r"budget impact", r"economic evaluation",
        r"cost[- ]consequence", r"willingness[- ]to[- ]pay threshold",
        r"net monetary benefit", r"health economic model",
    ],
    "decision_modeling": [
        r"microsimulation", r"markov model", r"discrete event simulation",
        r"decision[- ]analytic", r"decision tree model", r"state[- ]transition model",
        r"simulation model", r"agent[- ]based model", r"metamodel", r"emulator",
        r"probabilistic sensitivity analysis", r"value of information",
    ],
    "evidence_synthesis": [
        r"systematic review", r"scoping review", r"meta[- ]analys",
        r"evidence synthesis", r"literature screening", r"abstract screening",
        r"title and abstract", r"data extraction", r"rapid review",
        r"umbrella review", r"living review", r"network meta",
    ],
    "rwd_causal": [
        r"real[- ]world evidence", r"real[- ]world data", r"claims data",
        r"administrative claims", r"administrative data", r"electronic health record",
        r"\bEHR\b", r"registry data", r"causal inference", r"propensity score",
        r"confound", r"target trial", r"instrumental variable",
        r"difference[- ]in[- ]difference", r"treatment effect heterogeneity",
        r"causal forest", r"targeted maximum likelihood", r"double machine learning",
        r"external control arm", r"synthetic control",
    ],
    "outcome_prediction": [
        r"prognostic model", r"prediction model", r"predictive model",
        r"risk prediction", r"risk stratification", r"readmission",
        r"mortality prediction", r"predicting (?:cost|expenditure|utilization|length of stay)",
        r"length of stay", r"resource utilization prediction", r"clinical deterioration",
        r"\bAUC\b", r"\bAUROC\b", r"c[- ]statistic", r"discrimination and calibration",
    ],
    "pro_preferences": [
        r"patient[- ]reported outcome", r"\bPROM\b", r"\bPROs\b",
        r"health[- ]related quality of life", r"\bHRQoL\b", r"\bEQ[- ]5D\b",
        r"\bSF[- ]36\b", r"utility (?:value|elicitation|score)",
        r"discrete choice experiment", r"stated preference", r"conjoint analysis",
        r"patient preference",
    ],
    "hta_access": [
        r"health technology assessment", r"\bHTA\b", r"reimburse",
        r"market access", r"formulary", r"payer", r"coverage decision",
        r"pricing", r"value dossier", r"\bNICE\b", r"\bIQWiG\b", r"\bCADTH\b",
        r"\bICER (?:report|review)", r"joint clinical assessment",
        r"managed entry agreement", r"value[- ]based",
    ],
    "governance_reporting": [
        r"reporting guideline", r"reporting standard", r"transparen",
        r"reproducib", r"replicab", r"algorithmic bias", r"algorithmic fairness",
        r"risk of bias", r"\bTRIPOD\b", r"\bPROBAST\b", r"\bCHEERS\b",
        r"\bCONSORT\b", r"\bSPIRIT\b", r"\bDECIDE[- ]AI\b", r"\bPRISMA\b",
        r"regulatory (?:approval|submission|guidance|acceptance)",
        r"governance", r"ethic", r"explainab", r"interpretab", r"accountab",
        r"hallucinat", r"fabricat",
    ],
}

# ---------------------------------------------------------------------------
# Prespecified AI method dictionary (hierarchical, most specific wins)
# ---------------------------------------------------------------------------

METHOD_DICT = [
    ("generative_llm", [
        r"large language model", r"\bLLM\b", r"\bLLMs\b", r"\bGPT-?[345]\b",
        r"ChatGPT", r"generative (?:AI|artificial intelligence|pre[- ]?trained)",
        r"\bBERT\b", r"transformer", r"foundation model", r"Claude",
        r"Gemini", r"\bLlama\b", r"prompt engineering", r"retrieval[- ]augmented",
        r"\bGPT\b",
    ]),
    ("nlp", [
        r"natural language processing", r"\bNLP\b", r"text mining",
        r"named entity recognition", r"clinical notes", r"unstructured text",
        r"free[- ]text", r"topic model", r"word embedding",
    ]),
    ("deep_learning", [
        r"deep learning", r"neural network", r"convolutional",
        r"recurrent neural", r"\bCNN\b", r"\bLSTM\b", r"deep neural",
        r"autoencoder", r"generative adversarial", r"\bGAN\b",
    ]),
    ("classical_ml", [
        r"machine learning", r"random forest", r"gradient boosting",
        r"\bXGBoost\b", r"support vector", r"\bLASSO\b", r"elastic net",
        r"decision tree", r"\bk[- ]means\b", r"clustering", r"ensemble learning",
        r"supervised learning", r"unsupervised learning", r"reinforcement learning",
    ]),
    ("ai_general", [
        r"artificial intelligence", r"\bAI\b",
    ]),
]

DOMAIN_LABELS = {
    "economic_evaluation": "Economic evaluation",
    "decision_modeling": "Decision modeling and simulation",
    "evidence_synthesis": "Evidence synthesis",
    "rwd_causal": "Real-world data and causal inference",
    "outcome_prediction": "Outcome and cost prediction",
    "pro_preferences": "Patient-reported outcomes and preferences",
    "hta_access": "HTA, payer, and market access",
    "governance_reporting": "Governance, reporting, and validity",
}

METHOD_LABELS = {
    "generative_llm": "Generative AI and large language models",
    "nlp": "Natural language processing (pre-generative)",
    "deep_learning": "Deep learning",
    "classical_ml": "Classical machine learning",
    "ai_general": "Artificial intelligence, unspecified",
    "none": "No AI method term identified",
}


def compile_dict(d):
    return {k: [re.compile(p, re.I) for p in pats] for k, pats in d.items()}


DOMAIN_RX = compile_dict(DOMAIN_DICT)
METHOD_RX = [(k, [re.compile(p, re.I) for p in pats]) for k, pats in METHOD_DICT]


def screen(rec) -> tuple[bool, str]:
    """Apply eligibility criteria. Returns (eligible, reason_if_excluded)."""
    y = rec.get("year", "")
    if not (y.isdigit() and YEAR_MIN <= int(y) <= YEAR_MAX):
        return False, "outside publication window 2010-2025"
    langs = rec.get("languages") or []
    if langs and "eng" not in langs:
        return False, "not published in English"
    if not (rec.get("abstract") or "").strip():
        return False, "no abstract available for classification"
    pts = set(rec.get("pubtypes") or [])
    bad = pts & EXCLUDED_PUBTYPES
    if bad and not (pts & {"Journal Article", "Review", "Systematic Review"}):
        return False, f"excluded publication type ({sorted(bad)[0]})"
    if pts & {"Retracted Publication", "Published Erratum", "Preprint"}:
        return False, f"excluded publication type ({sorted(pts & {'Retracted Publication', 'Published Erratum', 'Preprint'})[0]})"
    return True, ""


def classify_domains(text: str) -> list[str]:
    hits = []
    for k, rxs in DOMAIN_RX.items():
        if any(rx.search(text) for rx in rxs):
            hits.append(k)
    return hits


def classify_method(text: str) -> str:
    for k, rxs in METHOD_RX:
        if any(rx.search(text) for rx in rxs):
            return k
    return "none"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", default="../data/records.jsonl")
    ap.add_argument("--datadir", default="../data")
    ap.add_argument("--outdir", default="../out")
    ap.add_argument("--sample-n", type=int, default=300)
    ap.add_argument("--seed", type=int, default=20260909)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    recs = [json.loads(l) for l in open(args.records)]

    # Deduplicate on PMID, then on lowercase title.
    seen_pmid, seen_title, deduped, dup_n = set(), set(), [], 0
    for r in recs:
        key_t = re.sub(r"\W+", " ", (r.get("title") or "").lower()).strip()
        if r["pmid"] in seen_pmid or (key_t and key_t in seen_title):
            dup_n += 1
            continue
        seen_pmid.add(r["pmid"])
        if key_t:
            seen_title.add(key_t)
        deduped.append(r)

    eligible, excluded = [], collections.Counter()
    with open(os.path.join(args.datadir, "screened.jsonl"), "w") as fh:
        for r in deduped:
            ok, why = screen(r)
            r["eligible"] = ok
            r["exclusion_reason"] = why
            if ok:
                text = f"{r['title']} {r['abstract']}"
                r["domains"] = classify_domains(text)
                r["method"] = classify_method(text)
                eligible.append(r)
            else:
                excluded[why] += 1
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    prisma = {
        "records_identified": len(recs),
        "duplicates_removed": dup_n,
        "records_screened": len(deduped),
        "records_excluded": sum(excluded.values()),
        "exclusion_reasons": dict(excluded),
        "records_included": len(eligible),
    }
    with open(os.path.join(args.datadir, "prisma_counts.json"), "w") as fh:
        json.dump(prisma, fh, indent=2)

    # ---- eligible.csv
    with open(os.path.join(args.datadir, "eligible.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["pmid", "doi", "year", "journal", "title", "method",
                    "n_domains", "domains", "pubtypes"])
        for r in eligible:
            w.writerow([r["pmid"], r["doi"], r["year"], r["journal"], r["title"],
                        r["method"], len(r["domains"]), "|".join(r["domains"]),
                        "|".join(r["pubtypes"])])

    # ---- annual counts overall and by domain
    years = list(range(YEAR_MIN, YEAR_MAX + 1))
    ann = {y: 0 for y in years}
    ann_dom = {k: {y: 0 for y in years} for k in DOMAIN_DICT}
    ann_meth = {k: {y: 0 for y in years} for k in list(METHOD_LABELS)}
    for r in eligible:
        y = int(r["year"])
        ann[y] += 1
        for d in r["domains"]:
            ann_dom[d][y] += 1
        ann_meth[r["method"]][y] += 1

    with open(os.path.join(args.outdir, "tab_annual.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["year", "included_total"] + list(DOMAIN_DICT) + list(METHOD_LABELS))
        for y in years:
            w.writerow([y, ann[y]] + [ann_dom[k][y] for k in DOMAIN_DICT]
                       + [ann_meth[k][y] for k in METHOD_LABELS])

    # ---- journals
    jc = collections.Counter(r["journal"] for r in eligible)
    with open(os.path.join(args.outdir, "tab_journals.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["journal", "n_included", "pct_of_included"])
        for j, n in jc.most_common():
            w.writerow([j, n, round(100 * n / len(eligible), 2)])

    # ---- designs
    pc = collections.Counter(p for r in eligible for p in r["pubtypes"])
    with open(os.path.join(args.outdir, "tab_designs.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["publication_type", "n_included", "pct_of_included"])
        for p, n in pc.most_common():
            w.writerow([p, n, round(100 * n / len(eligible), 2)])

    # ---- domain totals
    dt_ = collections.Counter(d for r in eligible for d in r["domains"])
    mt_ = collections.Counter(r["method"] for r in eligible)
    with open(os.path.join(args.outdir, "tab_domain_totals.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["label_type", "key", "label", "n", "pct_of_included"])
        for k, n in dt_.most_common():
            w.writerow(["domain", k, DOMAIN_LABELS[k], n, round(100 * n / len(eligible), 2)])
        for k, n in mt_.most_common():
            w.writerow(["method", k, METHOD_LABELS[k], n, round(100 * n / len(eligible), 2)])
        w.writerow(["domain", "unclassified", "No domain term identified",
                    sum(1 for r in eligible if not r["domains"]),
                    round(100 * sum(1 for r in eligible if not r["domains"]) / len(eligible), 2)])

    # ---- random sample for independent LLM classification (validation)
    rng = random.Random(args.seed)
    samp = rng.sample(eligible, min(args.sample_n, len(eligible)))
    with open(os.path.join(args.datadir, "sample_for_llm_audit.jsonl"), "w") as fh:
        for r in samp:
            fh.write(json.dumps({"pmid": r["pmid"], "title": r["title"],
                                 "abstract": r["abstract"][:2400]},
                                ensure_ascii=False) + "\n")
    with open(os.path.join(args.datadir, "sample_dictionary_labels.json"), "w") as fh:
        json.dump({r["pmid"]: {"domains": r["domains"], "method": r["method"]}
                   for r in samp}, fh, indent=2)

    # ---- console summary
    print(json.dumps(prisma, indent=2))
    print(f"\nincluded: {len(eligible):,}")
    print("\nannual included:", {y: ann[y] for y in years})
    print("\ndomain totals:")
    for k, n in dt_.most_common():
        print(f"  {DOMAIN_LABELS[k]:44s} {n:5,}  {100*n/len(eligible):5.1f}%")
    print(f"  {'No domain term identified':44s} "
          f"{sum(1 for r in eligible if not r['domains']):5,}")
    print("\nmethod totals:")
    for k, n in mt_.most_common():
        print(f"  {METHOD_LABELS[k]:44s} {n:5,}  {100*n/len(eligible):5.1f}%")
    print(f"\nsample of {len(samp)} written for independent LLM classification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
