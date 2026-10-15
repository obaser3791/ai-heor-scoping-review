#!/usr/bin/env python3
"""
05_figures.py

Figures for "Artificial Intelligence in Health Economics and Outcomes Research:
A Systematic Scoping Review".

Figure 1  PRISMA-ScR flow diagram
Figure 2  Growth of the AI and HEOR literature, 2010 to 2025 (three panels)
Figure 3  Evidence map: HEOR task domain by AI method family, with the
          validation-adjusted evidence density
Figure 4  Classifier agreement and search precision (the automation warning)
Figure 5  Regulatory and governance timeline, 2018 to 2030

House style: single accent, neutral surface, no chartjunk, direct labels,
Arial throughout for consistency with the Word manuscript.
"""

import csv
import json
import os
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
TEAL = "#20808D"
DARKTEAL = "#1B474D"
RUST = "#A84B2F"
GOLD = "#D19900"
BLUE = "#006494"
MAUVE = "#944454"
OLIVE = "#848456"
LIGHT = "#BCE2E7"
INK = "#28251D"
MUTED = "#7A7974"
GRID = "#D4D1CA"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "font.size": 9,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK,
    "axes.titlesize": 10,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "text.color": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.dpi": 400,
    "savefig.bbox": "tight",
})

DATA = "../data"
OUT = "../out"
FIG = "../figures"
os.makedirs(FIG, exist_ok=True)

DOMAIN_ORDER = ["economic_evaluation", "rwd_causal", "governance_reporting",
                "outcome_prediction", "evidence_synthesis", "hta_access",
                "decision_modeling", "pro_preferences"]
DOMAIN_SHORT = {
    "economic_evaluation": "Economic evaluation",
    "rwd_causal": "Real-world data and\ncausal inference",
    "governance_reporting": "Governance, reporting,\nand validity",
    "outcome_prediction": "Outcome and cost\nprediction",
    "evidence_synthesis": "Evidence synthesis",
    "hta_access": "HTA, payer, and\nmarket access",
    "decision_modeling": "Decision modeling\nand simulation",
    "pro_preferences": "Patient-reported outcomes\nand preferences",
}
METHOD_ORDER = ["generative_llm", "nlp", "deep_learning", "classical_ml",
                "ai_general", "none"]
METHOD_SHORT = {
    "generative_llm": "Generative AI\nand LLMs",
    "nlp": "NLP\n(pre-generative)",
    "deep_learning": "Deep learning",
    "classical_ml": "Classical\nmachine learning",
    "ai_general": "AI, unspecified",
    "none": "No AI method\nterm in abstract",
}


def load():
    prisma = json.load(open(f"{DATA}/prisma_counts.json"))
    agree = json.load(open(f"{OUT}/agreement_summary.json"))
    ann = list(csv.DictReader(open(f"{OUT}/tab_annual.csv")))
    counts = list(csv.DictReader(open(f"{DATA}/pubmed_counts.csv")))
    elig = list(csv.DictReader(open(f"{DATA}/eligible.csv")))
    return prisma, agree, ann, counts, elig


# ---------------------------------------------------------------------------
# Figure 1: PRISMA-ScR flow
# ---------------------------------------------------------------------------
def fig1(prisma):
    fig, ax = plt.subplots(figsize=(7.1, 8.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    def box(x, y, w, h, text, fill="#F7F6F2", edge=TEAL, bold_first=True, fs=8.6,
            align="center"):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.9,rounding_size=1.6",
                                    linewidth=1.1, edgecolor=edge, facecolor=fill))
        lines = text.split("\n")
        n = len(lines)
        for i, ln in enumerate(lines):
            yy = y + h - (h / (n + 1)) * (i + 1)
            if align == "left" and i > 0:
                ax.text(x + 2.6, yy, ln, ha="left", va="center", fontsize=fs,
                        color=INK)
            else:
                ax.text(x + w / 2, yy, ln, ha="center", va="center", fontsize=fs,
                        fontweight="bold" if (i == 0 and bold_first) else "normal",
                        color=INK)

    def arrow(x, y0, y1):
        ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>",
                                    mutation_scale=13, linewidth=1.1,
                                    color=DARKTEAL, shrinkA=0, shrinkB=0))

    def harrow(x0, x1, y):
        ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>",
                                    mutation_scale=13, linewidth=1.1,
                                    color=RUST, shrinkA=0, shrinkB=0))

    ri = prisma["records_identified"]
    dup = prisma["duplicates_removed"]
    scr = prisma["records_screened"]
    inc = prisma["records_included"]
    ex = prisma["exclusion_reasons"]

    SHORT = {
        "no abstract available for classification": "No abstract available",
        "not published in English": "Not published in English",
        "excluded publication type (Editorial)": "Editorial or comment",
        "excluded publication type (Preprint)": "Preprint",
        "excluded publication type (Letter)": "Letter",
        "outside publication window 2010-2025": "Outside 2010 to 2025",
        "excluded publication type (Retracted Publication)": "Retracted publication",
    }

    # Stage labels down the left margin
    for yy, lab in [(88, "Identification"), (62, "Screening"), (34, "Included")]:
        ax.text(1.6, yy, lab, rotation=90, ha="center", va="center",
                fontsize=8.4, fontweight="bold", color=TEAL)

    box(7, 84, 48, 12,
        f"Records identified in PubMed\nn = {ri:,}\n"
        "Prespecified search, 2010 to 2025", fill="#EAF3F4")
    arrow(31, 84, 74)

    box(60, 84.5, 37, 11,
        f"Duplicates removed\nn = {dup}\nPMID, then normalized title",
        edge=MUTED, fill="#FBFBF9", fs=8.0)
    harrow(56, 60, 90.0)

    box(7, 63, 48, 11, f"Records screened for eligibility\nn = {scr:,}",
        fill="#EAF3F4")
    arrow(31, 63, 47)

    exl = "\n".join(
        [f"Records excluded, n = {sum(ex.values())}"] +
        [f"{v:>3d}   {SHORT.get(k, k)}"
         for k, v in sorted(ex.items(), key=lambda t: -t[1])])
    box(60, 46, 37, 26, exl, edge=RUST, fill="#FBF4F1", fs=7.8, align="left")
    harrow(56, 60, 68.5)

    box(7, 35, 48, 12,
        f"Records included in the review\nn = {inc:,}\n"
        "Classified by HEOR domain and AI method", fill="#EAF3F4", fs=8.2)
    arrow(31, 35, 22)

    box(7, 10, 48, 12,
        "Validation subsample\nn = 300 records, randomly selected\n"
        "and independently classified, blinded", fill="#FBFBF9", edge=GOLD, fs=8.2)
    harrow(56, 60, 16.0)

    box(60, 9, 37, 14,
        "Search precision\n51.3% judged relevant to HEOR\n(95% CI, 45.7 to 56.9)\n"
        f"Precision adjusted corpus n = 1,271", edge=GOLD, fill="#FDF8EC", fs=7.9)

    ax.text(50, 99.4, "Figure 1. Study selection (PRISMA-ScR flow)",
            ha="center", va="top", fontsize=10.5, fontweight="bold", color=INK)
    fig.savefig(f"{FIG}/figure1_prisma.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2: growth
# ---------------------------------------------------------------------------
def fig2(ann, counts):
    series = {}
    for r in counts:
        series.setdefault(r["query"], {})[int(r["year"])] = int(r["count"])
    yrs = list(range(2010, 2026))

    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.05))
    fig.subplots_adjust(wspace=0.30)

    # Panel A: absolute counts, included corpus and the wider AI literature
    ax = axes[0]
    inc = [int(r["included_total"]) for r in ann]
    ax.plot(yrs, inc, color=TEAL, linewidth=2.3, marker="o", markersize=3.6,
            label="AI and HEOR (this review)")
    ax.set_yscale("log")
    ai = [series["ai_all_medicine"][y] for y in yrs]
    heor = [series["heor_all"][y] for y in yrs]
    ax.plot(yrs, ai, color=MUTED, linewidth=1.5, linestyle="--",
            label="AI in medicine, all")
    ax.plot(yrs, heor, color=RUST, linewidth=1.5, linestyle=":",
            label="HEOR, all")
    ax.set_title("A  Publication volume, log scale", loc="left")
    ax.set_ylabel("PubMed records per year")
    ax.set_xticks([2010, 2014, 2018, 2022, 2025])
    ax.grid(axis="y", color=GRID, linewidth=0.6, alpha=0.7)
    ax.legend(frameon=False, fontsize=7.3, loc="upper left")
    ax.annotate(f"{inc[-1]:,}", (2025, inc[-1]), textcoords="offset points",
                xytext=(-16, 8), fontsize=8, fontweight="bold", color=TEAL)

    # Panel B: HEOR share of the AI literature and AI share of the HEOR literature
    ax = axes[1]
    sh_ai = [100 * series["ai_heor"][y] / series["ai_all_medicine"][y] for y in yrs]
    sh_heor = [100 * series["ai_heor"][y] / series["heor_all"][y] for y in yrs]
    ax.plot(yrs, sh_heor, color=TEAL, linewidth=2.3, marker="o", markersize=3.6,
            label="AI as a share of HEOR")
    ax.plot(yrs, sh_ai, color=RUST, linewidth=2.0, marker="s", markersize=3.2,
            label="HEOR as a share of AI")
    ax.set_title("B  Penetration of each literature", loc="left")
    ax.set_ylabel("Percent of records")
    ax.set_xticks([2010, 2014, 2018, 2022, 2025])
    ax.grid(axis="y", color=GRID, linewidth=0.6, alpha=0.7)
    ax.legend(frameon=False, fontsize=7.3, loc="upper left")
    ax.annotate(f"{sh_heor[-1]:.1f}%", (2025, sh_heor[-1]),
                textcoords="offset points", xytext=(-20, 7), fontsize=8,
                fontweight="bold", color=TEAL)
    ax.annotate(f"{sh_ai[-1]:.2f}%", (2025, sh_ai[-1]), textcoords="offset points",
                xytext=(-26, 9), fontsize=8, fontweight="bold", color=RUST)

    # Panel C: method composition of the included corpus
    ax = axes[2]
    keys = ["generative_llm", "nlp", "deep_learning", "classical_ml",
            "ai_general", "none"]
    cols = [RUST, GOLD, BLUE, TEAL, LIGHT, "#E8E6E1"]
    mats = np.array([[int(r[k]) for r in ann] for k in keys], dtype=float)
    tot = mats.sum(axis=0)
    tot[tot == 0] = 1
    shares = 100 * mats / tot
    ax.stackplot(yrs, shares, colors=cols, edgecolor="white", linewidth=0.4)
    ax.set_title("C  AI method family in included studies", loc="left")
    ax.set_ylabel("Percent of included records")
    ax.set_ylim(0, 100)
    ax.set_xlim(2010, 2025)
    ax.set_xticks([2010, 2014, 2018, 2022, 2025])
    handles = [plt.Rectangle((0, 0), 1, 1, facecolor=c, edgecolor="white")
               for c in cols]
    ax.legend(handles, ["Generative AI and LLMs", "NLP (pre-generative)",
                        "Deep learning", "Classical ML", "AI, unspecified",
                        "No AI term in abstract"],
              frameon=False, fontsize=7.0, loc="upper center", ncol=3,
              bbox_to_anchor=(0.5, -0.14), handlelength=1.1, columnspacing=1.1)

    fig.suptitle("Figure 2. Growth and composition of the artificial intelligence "
                 "literature in health economics and outcomes research, 2010 to 2025",
                 fontsize=10.5, fontweight="bold", y=1.05, x=0.5)
    fig.savefig(f"{FIG}/figure2_growth.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3: evidence map (domain x method heat map + marginal bars)
# ---------------------------------------------------------------------------
def fig3(elig):
    mat = np.zeros((len(DOMAIN_ORDER), len(METHOD_ORDER)))
    dom_tot = np.zeros(len(DOMAIN_ORDER))
    for r in elig:
        doms = [d for d in r["domains"].split("|") if d]
        m = r["method"]
        if m not in METHOD_ORDER:
            continue
        j = METHOD_ORDER.index(m)
        for d in doms:
            if d in DOMAIN_ORDER:
                i = DOMAIN_ORDER.index(d)
                mat[i, j] += 1
                dom_tot[i] += 1

    fig = plt.figure(figsize=(10.4, 5.6))
    gs = fig.add_gridspec(1, 2, width_ratios=[3.05, 1.0], wspace=0.30)
    ax = fig.add_subplot(gs[0, 0])

    im = ax.imshow(mat, cmap="BuGn", aspect="auto")
    ax.set_xticks(range(len(METHOD_ORDER)))
    ax.set_xticklabels([METHOD_SHORT[m] for m in METHOD_ORDER], fontsize=7.4)
    ax.set_yticks(range(len(DOMAIN_ORDER)))
    ax.set_yticklabels([DOMAIN_SHORT[d] for d in DOMAIN_ORDER], fontsize=7.6)
    ax.spines[:].set_visible(False)
    ax.tick_params(length=0)
    vmax = mat.max()
    for i in range(len(DOMAIN_ORDER)):
        for j in range(len(METHOD_ORDER)):
            v = int(mat[i, j])
            ax.text(j, i, f"{v:,}" if v else "0", ha="center", va="center",
                    fontsize=7.4,
                    color="white" if mat[i, j] > 0.55 * vmax else INK,
                    fontweight="bold" if mat[i, j] > 0.55 * vmax else "normal")
    ax.set_title("A  Included studies by HEOR task domain and AI method family",
                 loc="left", fontsize=9.6)

    ax2 = fig.add_subplot(gs[0, 1])
    y = np.arange(len(DOMAIN_ORDER))
    ax2.barh(y, dom_tot, color=TEAL, height=0.62)
    # Precision-adjusted counts drawn as an inner bar
    ax2.barh(y, dom_tot * 0.513, color=DARKTEAL, height=0.30)
    ax2.set_yticks(y)
    ax2.set_yticklabels([])
    ax2.invert_yaxis()
    ax2.set_xlabel("Included studies", fontsize=8)
    ax2.grid(axis="x", color=GRID, linewidth=0.6, alpha=0.7)
    for i, v in enumerate(dom_tot):
        ax2.text(v + vmax * 0.02, i, f"{int(v):,}", va="center", fontsize=7.4,
                 color=INK, fontweight="bold")
    ax2.set_title("B  Domain total\n(inner bar, precision adjusted)",
                  loc="left", fontsize=9.0)
    ax2.spines[:].set_visible(False)
    ax2.tick_params(length=0)

    fig.suptitle("Figure 3. Evidence map of artificial intelligence applications "
                 "across health economics and outcomes research tasks",
                 fontsize=10.5, fontweight="bold", y=1.02)
    fig.savefig(f"{FIG}/figure3_evidence_map.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 4: agreement and precision
# ---------------------------------------------------------------------------
def fig4(agree):
    rows = agree["domain_rows"]
    rows = sorted(rows, key=lambda r: r["cohen_kappa"])
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.5),
                             gridspec_kw={"width_ratios": [1.35, 1.0],
                                          "wspace": 0.42})

    ax = axes[0]
    y = np.arange(len(rows))
    k = [r["cohen_kappa"] for r in rows]
    cols = [RUST if v < 0.40 else (GOLD if v < 0.60 else TEAL) for v in k]
    ax.barh(y, k, color=cols, height=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels([r["label"] for r in rows], fontsize=7.8)
    ax.set_xlabel("Cohen kappa, dictionary classifier vs independent blinded reading",
                  fontsize=7.8, labelpad=9)
    ax.set_xlim(0, 1)
    ax.grid(axis="x", color=GRID, linewidth=0.6, alpha=0.7)
    ax.set_ylim(-1.25, len(rows) - 0.35)
    for thr, lab in [(0.40, "fair"), (0.60, "moderate"), (0.80, "substantial")]:
        ax.axvline(thr, color=MUTED, linewidth=0.8, linestyle=":")
        ax.text(thr, -0.80, lab, fontsize=6.6, color=MUTED, va="center",
                ha="center", style="italic")
    for i, r in enumerate(rows):
        ax.text(r["cohen_kappa"] + 0.014, i,
                f"{r['cohen_kappa']:.2f}   n={r['n_dictionary']} vs {r['n_independent']}",
                va="center", fontsize=7.0, color=INK)
    ax.set_title("A  Agreement on HEOR task domain", loc="left", fontsize=9.4)
    ax.spines[:].set_visible(False)
    ax.tick_params(length=0)

    ax = axes[1]
    pr = agree["precision_rows"]
    x = np.arange(len(pr))
    p = [r["precision_pct"] for r in pr]
    lo = [r["precision_pct"] - r["ci95_lo"] for r in pr]
    hi = [r["ci95_hi"] - r["precision_pct"] for r in pr]
    ax.bar(x, p, color=[DARKTEAL, TEAL, LIGHT], width=0.56,
           yerr=[lo, hi], capsize=4, ecolor=INK,
           error_kw={"elinewidth": 1.0})
    ax.axhline(100, color=MUTED, linewidth=0.8, linestyle=":")
    ax.set_xticks(x)
    ax.set_xticklabels(["\n".join(textwrap.wrap(r["stratum"], 18)) for r in pr],
                       fontsize=7.2)
    ax.set_ylabel("Percent judged relevant to HEOR", fontsize=8)
    ax.set_ylim(0, 108)
    ax.grid(axis="y", color=GRID, linewidth=0.6, alpha=0.7)
    for xi, r in zip(x, pr):
        ax.text(xi, r["ci95_hi"] + 3.0,
                f"{r['precision_pct']:.1f}%\n{r['n_heor_relevant']}/{r['n_sampled']}",
                ha="center", fontsize=7.4, fontweight="bold", color=INK)
    ax.set_title("B  Search precision", loc="left", fontsize=9.4)
    ax.spines[:].set_visible(False)
    ax.tick_params(length=0)

    fig.suptitle("Figure 4. Validation of automated screening and classification "
                 "against independent blinded reading of 300 records",
                 fontsize=10.5, fontweight="bold", y=1.03)
    fig.savefig(f"{FIG}/figure4_validation.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 5: regulatory timeline
# ---------------------------------------------------------------------------
EVENTS = [
    (2019.30, "Proposed regulatory framework for modifications to AI and ML based\nsoftware as a medical device", "FDA"),
    (2021.04, "AI and ML software as a medical device action plan", "FDA"),
    (2021.48, "Ethics and governance of artificial intelligence for health", "WHO"),
    (2023.36, "CDER and CDRH discussion papers on AI in drug development\nand in medical device manufacturing", "FDA"),
    (2024.58, "EU Artificial Intelligence Act enters into force", "EU"),
    (2024.62, "Position statement on the use of AI in evidence generation", "NICE"),
    (2024.71, "Reflection paper on the use of AI across the medicinal product lifecycle", "EMA"),
    (2025.02, "Draft guidance: AI to support regulatory decision-making for drugs\nand biological products (docket FDA-2024-D-4689)", "FDA"),
    (2025.03, "Joint clinical assessments begin under the EU HTA Regulation\nfor oncology medicines and advanced therapies", "EU"),
    (2025.05, "Draft guidance on AI-enabled device software functions", "FDA"),
    (2025.27, "Position statement on artificial intelligence", "CDA"),
    (2025.45, "Elsa large language model tool deployed agency-wide", "FDA"),
    (2025.96, "General Methods version 8.0, incorporating AI provisions", "IQWiG"),
    (2026.05, "Ten joint guiding principles of good AI practice in drug development", "FDA and EMA"),
    (2026.58, "EU AI Act obligations for high-risk systems begin to apply", "EU"),
    (2028.03, "EU HTA Regulation extends to orphan medicines", "EU"),
    (2030.03, "EU HTA Regulation extends to all medicinal products", "EU"),
]
COLORS = {"FDA": DARKTEAL, "EMA": BLUE, "FDA and EMA": TEAL, "EU": MAUVE,
          "NICE": RUST, "CDA": GOLD, "IQWiG": OLIVE, "WHO": "#6E522B"}


def fig5():
    ev = sorted(EVENTS, key=lambda e: e[0])
    n = len(ev)
    fig, ax = plt.subplots(figsize=(10.6, 6.4))
    ax.set_xlim(2018.6, 2031.0)
    ax.set_ylim(-0.9, n - 0.1)

    # Shade the period that has not yet taken effect
    ax.axvspan(2026.19, 2031.0, color="#F4F2ED", zorder=0)
    ax.text(2028.6, n - 0.45, "Scheduled, not yet in effect", fontsize=7.6,
            color=MUTED, ha="center", style="italic", zorder=2)

    for i, (x, txt, body) in enumerate(ev):
        yy = n - 1 - i
        c = COLORS[body]
        ax.hlines(yy, 2018.6, x, color=GRID, linewidth=0.7, zorder=1)
        ax.plot([x], [yy], marker="o", markersize=6.4, color=c,
                markeredgecolor="white", markeredgewidth=1.0, zorder=4)
        ax.text(x + 0.13, yy + 0.03, txt, ha="left", va="center", fontsize=7.5,
                color=INK, zorder=4, linespacing=1.35)
        ax.text(2018.52, yy, body, ha="right", va="center", fontsize=7.4,
                fontweight="bold", color=c, zorder=4)

    ax.set_yticks([])
    ax.set_xticks(range(2019, 2032))
    ax.set_xticklabels([str(y) for y in range(2019, 2032)], fontsize=8)
    ax.tick_params(axis="x", length=4, color=INK, labelcolor=INK)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.grid(axis="x", color=GRID, linewidth=0.6, alpha=0.55, zorder=0)
    ax.set_title(FIG5_LABEL + ". Regulatory and health technology assessment milestones "
                 "for artificial intelligence in evidence generation, 2019 to 2030",
                 fontsize=10.5, fontweight="bold", loc="center", pad=12)
    fig.savefig(f"{FIG}/{FIG5_FILE}")
    plt.close(fig)


FIG5_LABEL = "Figure 5"
FIG5_FILE = "figure5_timeline.png"


def main():
    prisma, agree, ann, counts, elig = load()
    fig1(prisma)
    fig2(ann, counts)
    fig3(elig)
    fig4(agree)
    fig5()
    for f in sorted(os.listdir(FIG)):
        print("wrote", f)


if __name__ == "__main__":
    main()
