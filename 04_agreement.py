#!/usr/bin/env python3
"""
04_agreement.py

Validation of the prespecified dictionary classifier against an independent,
blinded classification of a random sample of included records performed by a
large language model (Claude Opus, accessed September 2026). The language model
received only the title and abstract of each sampled record. It did not have
access to the dictionary, the classifier code, or the dictionary labels.

Outputs
  ../out/tab_agreement.csv        per-label agreement, Cohen kappa, PABAK
  ../out/tab_precision.csv        search precision estimate with Wilson interval
  ../out/agreement_summary.json   machine-readable summary

Statistics
  Cohen kappa for each binary domain label and for the multiclass method label.
  Prevalence-adjusted bias-adjusted kappa (PABAK) is reported alongside kappa
  because several domain labels are rare in the sample, which depresses kappa
  even when raw agreement is high (the first paradox of kappa).
  Wilson score intervals are used for all proportions.
"""

import argparse
import csv
import json
import math
import os
import collections

DOMAINS = ["economic_evaluation", "decision_modeling", "evidence_synthesis",
           "rwd_causal", "outcome_prediction", "pro_preferences",
           "hta_access", "governance_reporting"]

METHODS = ["generative_llm", "nlp", "deep_learning", "classical_ml",
           "ai_general", "none"]

LABELS = {
    "economic_evaluation": "Economic evaluation",
    "decision_modeling": "Decision modeling and simulation",
    "evidence_synthesis": "Evidence synthesis",
    "rwd_causal": "Real-world data and causal inference",
    "outcome_prediction": "Outcome and cost prediction",
    "pro_preferences": "Patient-reported outcomes and preferences",
    "hta_access": "HTA, payer, and market access",
    "governance_reporting": "Governance, reporting, and validity",
}


def wilson(k: int, n: int, z: float = 1.959963985) -> tuple[float, float, float]:
    """Wilson score interval for a binomial proportion. Returns (p, lo, hi) in percent."""
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (100 * p, 100 * max(0.0, c - h), 100 * min(1.0, c + h))


def cohen_kappa_binary(a: list[bool], b: list[bool]) -> tuple[float, float, float]:
    """Return (kappa, observed_agreement, pabak) for two binary raters."""
    n = len(a)
    n11 = sum(1 for x, y in zip(a, b) if x and y)
    n00 = sum(1 for x, y in zip(a, b) if (not x) and (not y))
    po = (n11 + n00) / n
    pa1 = sum(a) / n
    pb1 = sum(b) / n
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    kappa = float("nan") if pe == 1 else (po - pe) / (1 - pe)
    pabak = 2 * po - 1
    return kappa, po, pabak


def cohen_kappa_multiclass(a: list[str], b: list[str], classes: list[str]):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in classes)
    kappa = float("nan") if pe == 1 else (po - pe) / (1 - pe)
    return kappa, po


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dict-labels", default="../data/sample_dictionary_labels.json")
    ap.add_argument("--llm-labels", default="../data/llm_audit_labels.json")
    ap.add_argument("--outdir", default="../out")
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    dl = json.load(open(args.dict_labels))
    ll = json.load(open(args.llm_labels))
    pmids = [p for p in dl if p in ll]
    n = len(pmids)
    print(f"paired records: {n}")

    rows = []
    for d in DOMAINS:
        a = [d in dl[p]["domains"] for p in pmids]
        b = [d in ll[p]["domains"] for p in pmids]
        kappa, po, pabak = cohen_kappa_binary(a, b)
        # Treat the independent LLM reading as the reference to describe how the
        # dictionary behaves, without asserting that either rater is ground truth.
        tp = sum(1 for x, y in zip(a, b) if x and y)
        fp = sum(1 for x, y in zip(a, b) if x and not y)
        fn = sum(1 for x, y in zip(a, b) if (not x) and y)
        prec = 100 * tp / (tp + fp) if tp + fp else float("nan")
        rec = 100 * tp / (tp + fn) if tp + fn else float("nan")
        f1 = (2 * prec * rec / (prec + rec)) if (prec == prec and rec == rec
                                                and prec + rec > 0) else float("nan")
        rows.append({
            "label": LABELS[d], "key": d,
            "n_dictionary": sum(a), "n_independent": sum(b),
            "observed_agreement_pct": round(100 * po, 1),
            "cohen_kappa": round(kappa, 3),
            "pabak": round(pabak, 3),
            "dict_precision_vs_independent_pct": round(prec, 1) if prec == prec else "n.a.",
            "dict_recall_vs_independent_pct": round(rec, 1) if rec == rec else "n.a.",
            "dict_f1_pct": round(f1, 1) if f1 == f1 else "n.a.",
        })

    ma = [dl[p]["method"] for p in pmids]
    mb = [ll[p]["method"] for p in pmids]
    mk, mpo = cohen_kappa_multiclass(ma, mb, METHODS)

    # Collapsed method comparison: any generative or language model work vs other.
    ga = [x in ("generative_llm",) for x in ma]
    gb = [x in ("generative_llm",) for x in mb]
    gk, gpo, gpabak = cohen_kappa_binary(ga, gb)

    with open(os.path.join(args.outdir, "tab_agreement.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    # ---- Search precision: share of included records judged HEOR relevant
    rel = [bool(ll[p].get("heor_relevant")) for p in pmids]
    k = sum(rel)
    p, lo, hi = wilson(k, n)

    # Precision within the subset the dictionary assigned to at least one domain
    has_dom = [len(dl[p]["domains"]) > 0 for p in pmids]
    k2 = sum(1 for r, h in zip(rel, has_dom) if r and h)
    n2 = sum(has_dom)
    p2, lo2, hi2 = wilson(k2, n2)

    # Precision within the subset the dictionary assigned NO domain
    k3 = sum(1 for r, h in zip(rel, has_dom) if r and not h)
    n3 = n - n2
    p3, lo3, hi3 = wilson(k3, n3)

    prec_rows = [
        {"stratum": "All included records", "n_sampled": n, "n_heor_relevant": k,
         "precision_pct": round(p, 1), "ci95_lo": round(lo, 1), "ci95_hi": round(hi, 1)},
        {"stratum": "Dictionary assigned at least one HEOR domain",
         "n_sampled": n2, "n_heor_relevant": k2, "precision_pct": round(p2, 1),
         "ci95_lo": round(lo2, 1), "ci95_hi": round(hi2, 1)},
        {"stratum": "Dictionary assigned no HEOR domain",
         "n_sampled": n3, "n_heor_relevant": k3, "precision_pct": round(p3, 1),
         "ci95_lo": round(lo3, 1), "ci95_hi": round(hi3, 1)},
    ]
    with open(os.path.join(args.outdir, "tab_precision.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(prec_rows[0]))
        w.writeheader()
        w.writerows(prec_rows)

    # ---- Precision-adjusted corpus size
    prisma = json.load(open("../data/prisma_counts.json"))
    inc = prisma["records_included"]
    adj = [round(inc * x / 100) for x in (p, lo, hi)]

    summary = {
        "paired_records": n,
        "method_label": {"cohen_kappa": round(mk, 3),
                         "observed_agreement_pct": round(100 * mpo, 1)},
        "generative_llm_flag": {"cohen_kappa": round(gk, 3),
                                "observed_agreement_pct": round(100 * gpo, 1),
                                "pabak": round(gpabak, 3)},
        "mean_domain_kappa": round(
            sum(r["cohen_kappa"] for r in rows) / len(rows), 3),
        "median_domain_observed_agreement_pct": round(
            sorted(r["observed_agreement_pct"] for r in rows)[len(rows) // 2], 1),
        "search_precision_pct": {"point": round(p, 1), "ci95": [round(lo, 1), round(hi, 1)]},
        "included_records": inc,
        "precision_adjusted_included": {"point": adj[0], "ci95": [adj[1], adj[2]]},
        "domain_rows": rows,
        "precision_rows": prec_rows,
    }
    with open(os.path.join(args.outdir, "agreement_summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)

    print("\n--- domain agreement ---")
    for r in rows:
        print(f"  {r['label']:44s} dict={r['n_dictionary']:3d} ind={r['n_independent']:3d} "
              f"agree={r['observed_agreement_pct']:5.1f}%  kappa={r['cohen_kappa']:+.3f} "
              f"PABAK={r['pabak']:+.3f}  F1={r['dict_f1_pct']}")
    print(f"\nmethod label: kappa={mk:.3f} agreement={100*mpo:.1f}%")
    print(f"generative LLM flag: kappa={gk:.3f} agreement={100*gpo:.1f}%")
    print(f"\nsearch precision: {p:.1f}% (95% CI {lo:.1f} to {hi:.1f}); "
          f"{k}/{n} judged HEOR relevant")
    print(f"  with >=1 dictionary domain: {p2:.1f}% ({k2}/{n2})")
    print(f"  with no dictionary domain:  {p3:.1f}% ({k3}/{n3})")
    print(f"\nprecision-adjusted included corpus: {adj[0]:,} "
          f"(95% CI {adj[1]:,} to {adj[2]:,}) of {inc:,} included")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
