#!/usr/bin/env python3
"""Build main tables and supplementary eTables as xlsx plus a JSON spec for docx."""
import csv, json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")
DATA = os.path.join(ROOT, "data")
VER = os.path.join(ROOT, "verification")


def rd(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


annual = rd(os.path.join(OUT, "tab_annual.csv"))
journals = rd(os.path.join(OUT, "tab_journals.csv"))
designs = rd(os.path.join(OUT, "tab_designs.csv"))
domtot = rd(os.path.join(OUT, "tab_domain_totals.csv"))
agree = rd(os.path.join(OUT, "tab_agreement.csv"))
prec = rd(os.path.join(OUT, "tab_precision.csv"))
counts = rd(os.path.join(DATA, "pubmed_counts.csv"))
qstr = rd(os.path.join(DATA, "pubmed_counts_querystrings.csv"))
prisma = json.load(open(os.path.join(DATA, "prisma_counts.json")))
agsum = json.load(open(os.path.join(OUT, "agreement_summary.json")))
reflib = json.load(open(os.path.join(VER, "reference_library.json")))
weblib = json.load(open(os.path.join(VER, "weblib.json")))
fda = rd(os.path.join(ROOT, "fda_ai_device_list.csv"))

from importlib import import_module
clf = import_module("03_screen_classify") if False else None
import re
src = open(os.path.join(ROOT, "bibliometrics", "03_screen_classify.py")).read()
ns = {}
exec(compile(src.split("def main")[0], "clf", "exec"), ns)
DOMAIN_DICT, METHOD_DICT = ns["DOMAIN_DICT"], ns["METHOD_DICT"]
DOMAIN_LABELS, METHOD_LABELS = ns["DOMAIN_LABELS"], ns["METHOD_LABELS"]

TABLES = []  # (id, title, footnote, headers, rows)


def add(tid, title, footnote, headers, rows):
    TABLES.append({"id": tid, "title": title, "footnote": footnote,
                   "headers": headers, "rows": [[("" if c is None else str(c)) for c in r] for r in rows]})


def cn(x):
    try:
        v = int(str(x).replace(",", ""))
        return f"{v:,}"
    except Exception:
        return x


def d3(x):
    try:
        return f"{float(x):.3f}"
    except Exception:
        return x


def d1(x):
    try:
        return f"{float(x):.1f}"
    except Exception:
        return x


def pc2(x):
    try:
        return f"{float(x):.2f}"
    except Exception:
        return x


# ----------------------------------------------------------------- TABLE 1
DOM_KEYS = ["economic_evaluation", "rwd_causal", "governance_reporting", "outcome_prediction",
            "evidence_synthesis", "hta_access", "decision_modeling", "pro_preferences"]
MET_KEYS = ["ai_general", "classical_ml", "deep_learning", "none", "generative_llm", "nlp"]
dom_lookup = {(r["label_type"], r["key"]): r for r in domtot}

rows = [["Publication year", "", "", ""]]
for r in annual:
    rows.append(["  " + r["year"], cn(r["included_total"]),
                 f"{100*int(r['included_total'])/2476:.2f}", ""])
rows.append(["Application domain (non-exclusive)", "", "", "Cohen kappa vs blinded classifier"])
kap = {r["key"]: d3(r["cohen_kappa"]) for r in agree}
for k in DOM_KEYS:
    d = dom_lookup[("domain", k)]
    rows.append(["  " + d["label"], cn(d["n"]), pc2(d["pct_of_included"]), kap.get(k, "")])
d = dom_lookup[("domain", "unclassified")]
rows.append(["  " + d["label"], cn(d["n"]), pc2(d["pct_of_included"]), ""])
rows.append(["Method category (most specific, exclusive)", "", "", ""])
for k in MET_KEYS:
    d = dom_lookup.get(("method", k))
    if d:
        rows.append(["  " + d["label"], cn(d["n"]), pc2(d["pct_of_included"]),
                     "0.667 (6-category multiclass)" if k == "ai_general" else ""])
rows.append(["Leading journals", "", "", ""])
for r in journals[:10]:
    rows.append(["  " + r["journal"], cn(r["n_included"]), pc2(r["pct_of_included"]), ""])
rows.append(["Indexed publication type", "", "", ""])
for r in designs[:12]:
    rows.append(["  " + r["publication_type"], cn(r["n_included"]), pc2(r["pct_of_included"]), ""])
add("Table 1", "Characteristics of the included corpus of AI in HEOR publications, 2010 to 2025 (n = 2,476)",
    "Domain labels are non-exclusive, so column percentages sum to more than 100. Method categories are exclusive. "
    "Percentages are of the 2,476 included records. Cohen kappa is reproduced from the validation analysis in Table 2 so that the "
    "reliability of each domain count can be read alongside its magnitude. Publication types are as indexed in PubMed and a record may carry more than one.",
    ["Characteristic", "Included records (n)", "% of included", "Classification reliability"], rows)

# ----------------------------------------------------------------- TABLE 2
rows = []
for r in agree:
    rows.append([r["label"], r["n_dictionary"], r["n_independent"], d1(r["observed_agreement_pct"]),
                 d3(r["cohen_kappa"]), d3(r["pabak"]), d1(r["dict_precision_vs_independent_pct"]),
                 d1(r["dict_recall_vs_independent_pct"]), d1(r["dict_f1_pct"])])
m = agsum["method_label"]; g = agsum["generative_llm_flag"]
rows.append(["Method category (6-category multiclass)", "300", "300", d1(m["observed_agreement_pct"]),
             d3(m["cohen_kappa"]), "", "", "", ""])
rows.append(["Generative AI or LLM flag", "", "", d1(g["observed_agreement_pct"]), d3(g["cohen_kappa"]), d3(g["pabak"]), "", "", ""])
rows.append(["", "", "", "", "", "", "", "", ""])
rows.append(["Search precision", "n sampled", "n judged HEOR relevant", "Precision (%)", "95% CI lower",
             "95% CI upper", "", "", ""])
for r in prec:
    rows.append([r["stratum"], r["n_sampled"], r["n_heor_relevant"], r["precision_pct"], r["ci95_lo"], r["ci95_hi"], "", "", ""])
pa = agsum["precision_adjusted_included"]
rows.append(["Precision-adjusted corpus size", "2,476 included", f"{pa['point']:,}", "",
             f"{pa['ci95'][0]:,}", f"{pa['ci95'][1]:,}", "", "", ""])
add("Table 2", "Validation of the term dictionary against blinded independent classification of 300 randomly sampled included records",
    "The independent classifier received only the title and abstract and was blinded to all dictionary output. It is treated as a reference "
    "standard, not as truth. PABAK is the prevalence-adjusted bias-adjusted kappa, reported because Cohen kappa is unstable at extreme prevalence. "
    "Precision, recall, and F1 describe the dictionary against the blinded reference. Confidence intervals are exact binomial (Clopper-Pearson). "
    "The precision-adjusted corpus size applies the observed search precision and its interval to the 2,476 included records.",
    ["Label", "Assigned by dictionary (n)", "Assigned by blinded classifier (n)", "Observed agreement (%)",
     "Cohen kappa", "PABAK", "Precision (%)", "Recall (%)", "F1 (%)"], rows)

# ----------------------------------------------------------------- TABLE 3
t3 = [
 ["US FDA", "Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products (docket FDA-2024-D-4689)", "January 2025", "Draft as of September 2026; comments closed 7 April 2025",
  "Seven step risk based credibility assessment framework. Model risk is defined as the combination of model influence and decision consequence. Explicitly excludes AI used in drug discovery and in operational efficiencies."],
 ["US FDA", "Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations (FDA-2024-D-4488)", "January 2025", "Draft",
  "Recommends performance validation at at least three geographically diverse US clinical sites, with two sided 95% confidence intervals reported."],
 ["US FDA", "AI-Enabled Medical Device List", "Current 4 September 2026", "Published list",
  "1,614 authorizations. Radiology 1,230 (76.2%), cardiovascular 154 (9.5%), neurology 73 (4.5%). Rose from 18 authorizations in 2016 to 335 in 2025."],
 ["US FDA", "Considerations for the Use of Real-World Data and Real-World Evidence, electronic health records and medical claims (FDA-2020-D-2307)", "2024", "Final guidance",
  "States that FDA does not endorse any specific AI technology for real-world data curation."],
 ["US FDA and EMA", "Guiding Principles of Good Artificial Intelligence Practice in Drug Development", "January 2026", "Joint guiding principles",
  "Ten principles including human-centric by design, risk based approach, clear context of use, data governance and documentation, risk based performance assessment, and life cycle management."],
 ["US FDA", "Digital Health Advisory Committee on generative AI-enabled devices", "20 to 21 November 2024", "Advisory committee meeting",
  "First dedicated advisory committee consideration of generative AI in regulated devices."],
 ["EMA", "Reflection paper on the use of artificial intelligence in the medicinal product lifecycle (EMA/CHMP/CVMP/83833/2023)", "9 September 2024", "Final reflection paper",
  "States that the use of transparent models is preferred. Applies a risk based approach across the product lifecycle."],
 ["EMA CHMP", "Qualification opinion on prognostic covariate adjustment (PROCOVA)", "2022", "Qualification opinion",
  "Qualified for use, while stating that excluding dropout data would not be acceptable for regulatory purposes."],
 ["European Union", "Regulation (EU) 2024/1689, the AI Act", "In force 1 August 2024", "In force; general purpose AI obligations apply from 2 August 2026",
  "Risk tiered obligations. EFPIA has argued that AI used solely for medicines research and development is exempt under Recital 25 and Articles 2.6 and 2.8."],
 ["European Union", "Regulation (EU) 2021/2282 on health technology assessment", "In force 11 January 2022", "Applies from 12 January 2025 for oncology and ATMPs; 13 January 2028 for orphans; 13 January 2030 for all others in scope",
  "Joint clinical assessment. Approximately 50 assessments of medicines and 5 of devices estimated for 2026, with 12 ongoing and 14 countries involved."],
 ["NICE", "Use of AI in evidence generation: NICE position statement (ECD11)", "15 August 2024", "Final position statement",
  "AI should only be used when there is demonstrable value from doing so. Where more explainable methods are potentially robust, those should be presented in the first instance. Directs submitters to the PALISADE checklist."],
 ["Canada's Drug Agency (CDA-AMC)", "Guidance on Reporting the Use of AI in Evidence Generation", "April 2025", "Final guidance",
  "Built on the principle of augmentation, not replacement. Permits AI generated search strategies, screening, extraction, meta-analysis code, and synthetic or external controls subject to transparent reporting."],
 ["IQWiG", "General Methods, version 8.0", "2025", "Final methods manual",
  "German reference methods manual, incorporating requirements applicable to AI derived evidence."],
 ["ICER and Peterson Health Technology Institute", "Assessment framework for digital health technologies", "2024", "Published framework",
  "Extends value assessment methods to digital and algorithm based technologies."],
 ["CMS", "HPMS memorandum on Medicare Advantage utilization management (CMS-4201-F)", "6 February 2024", "Final rule guidance",
  "Algorithms or artificial intelligence alone cannot be used as the basis to deny admission."],
 ["State of California", "Senate Bill 1120, Chapter 879, Statutes of 2024", "2024", "Enacted statute",
  "Requires licensed physician review of medical necessity determinations rather than reliance on an algorithm alone."],
 ["WHO", "Ethics and governance of AI for health: guidance on large multi-modal models", "2024", "Guidance",
  "Notes hallucination rates of at least 3 percent and as high as 27 percent."],
 ["ISPOR", "Generative AI taxonomy, ELEVATE-GenAI reporting guideline, and Working Group report for HTA", "2024 to 2025", "Published society guidance",
  "First HEOR specific reporting instruments for generative AI. AI ranked first among HEOR trends for 2026 to 2027."],
]
add("Table 3", "Regulatory and health technology assessment instruments governing artificial intelligence in evidence generation",
    "Status is as of 9 September 2026. Quoted text is verbatim from the cited instrument. Full citations with uniform resource locators appear in the reference list.",
    ["Issuing body", "Instrument", "Date", "Status", "Operative requirement"], t3)

# ----------------------------------------------------------------- TABLE 4
P_PEER = "Peer reviewed"; P_PRE = "Preprint"; P_ABS = "Conference abstract"; P_CO = "Company communication"
t4 = [
 ["Evidence synthesis", "Title and abstract screening", "Sensitivity 0.962, specificity 0.996; approximately 110 records per minute at US$59", "Human reviewer decisions in 1,381 and 3,146 record sets", P_PEER],
 ["Evidence synthesis", "Title and abstract screening", "Sensitivity 81.1% to 96.5%, specificity 25.8% to 80.4%; 10,279 false positives in the worst configuration", "Human reviewers across 22,665 citations", P_PEER],
 ["Evidence synthesis", "Title and abstract screening", "Sensitivity 0.85, specificity 0.98, with a median specificity gap of 0.48 across reviews", "Human reviewers across 16,669 citations", P_PEER],
 ["Evidence synthesis", "Title and abstract screening", "Sensitivity 0.42, kappa 0.34 against human reviewer kappa 0.77", "Two human reviewers", P_PEER],
 ["Evidence synthesis", "Screening prioritisation", "Work saved over sampling 0.55; approximately 75% of screening effort saved at recall above 95%", "Exhaustive human screening of 11,984 records", P_PEER],
 ["Evidence synthesis", "Agentic screening and extraction, human in the loop", "Screening F1 0.917 to 0.977, kappa 0.844 to 0.906; extraction F 0.96 to 0.998", "Human reviewers", P_PEER],
 ["Evidence synthesis", "Data extraction", "96.3% accuracy across 160 extracted items", "Human extraction", P_PEER],
 ["Evidence synthesis", "Data extraction", "94.8% accuracy at 88 seconds per randomized trial", "Human extraction", P_PEER],
 ["Evidence synthesis", "Data extraction", "Model 96.2%, human 95.3%, human assisted by model 97.9%; time 86.9 to 14.7 minutes", "Human extraction across 12,814 extractions in 107 trials", P_PEER],
 ["Evidence synthesis", "Time and cost", "17 of 25 studies reported time reductions above 50%, range 36.0% to more than 99.0%", "Unaided human workflow", P_PEER],
 ["Evidence synthesis", "Time and motion, hybrid vs autonomous", "Hybrid 97.0% accuracy, 80.6% recall, 51.4% time saved; autonomous 81.1% time saved but 48.4% recall; unaided humans 90.1% accuracy, 88.7% recall", "Unaided human workflow across 234 publications", P_ABS],
 ["Economic modeling", "Automated model coding in R", "14 of 15 scripts error free in the lung cancer set; every error free script reproduced the published ICER to within 1%", "Published cost effectiveness results", P_PEER],
 ["Economic modeling", "Network meta-analysis input extraction", "Greater than 99% extraction accuracy", "Human extraction", P_PEER],
 ["Economic modeling", "Expected value of partial perfect information by metamodeling", "12.5 million model runs reduced from more than 1,000 days to approximately 2 days, a roughly 500 fold reduction", "Brute force nested simulation", P_PEER],
 ["Economic modeling", "Generative AI in health economic evaluation, evidence base composition", "25 studies included from 2,322 screened; 92% conference abstracts, 92% published 2024, 96% company authored", "Not applicable", P_PRE],
 ["RWD and causal inference", "High dimensional propensity score", "Estimated relative risk moved from 1.09 crude to 0.94 with 15 investigator specified covariates to 0.88 with 500 algorithmically selected covariates", "Investigator specified propensity score", P_PEER],
 ["RWD and causal inference", "High dimensional propensity score weighting, simulation", "Bias 0.094 with 23.6% confidence interval coverage, against 0.018 bias and 91.4% coverage for a modified procedure", "Known simulated truth", P_PEER],
 ["RWD and causal inference", "Trial emulation, PARADIGM-HF", "Logistic propensity model AUC 0.79 gave HR 0.93; gradient boosted model AUC 0.95 gave HR 0.61", "Randomized trial HR 0.81 (95% CI 0.61 to 1.06)", P_PRE],
 ["Unstructured data", "Social and behavioral determinants from notes", "Prevalence recorded rose from 0.03% to 8.3% in claims to 1.40% to 36.3% with notes; lack of social support text only in 99.8% of cases", "Structured claims and Z codes", P_PEER],
 ["Unstructured data", "ECOG performance status extraction", "AUROC 0.95 across 79,698 patients and 495,862 notes; imputed poor performance status HR 11.9", "Documented performance status", P_PEER],
 ["Unstructured data", "Oncology variable extraction", "Stage value precision 98.8% and recall 92%, but histology linked to neoplasm recall 79%", "Human abstraction of 200 patients", P_PEER],
 ["Unstructured data", "Cancer registry staging extraction", "T stage F1 0.89, M stage F1 0.24", "Registry abstraction", P_PEER],
 ["Unstructured data", "Real-world progression free survival derivation", "Sentence level accuracy 98.2%; patient level within 30 days 88%; median rwPFS 20 months (95% CI 18 to 25) computationally vs 25 months (15 to 35) manually; 30 months from radiology reports vs 23 months from clinical notes", "Manual curation in a 100 patient subset", P_PEER],
 ["Unstructured data", "Human abstracted real-world response, the reference standard", "Inter-abstractor agreement 0.94 (0.92 to 0.96) on assessment presence and 0.82 (0.78 to 0.86) on best response; 15.0 minutes per patient line; Spearman 0.99 vs trial ORR", "Second human abstractor", P_PEER],
 ["Unstructured data", "Scaled machine learning real-world response", "r = 0.86 against human abstraction in a test subset of 4,047", "Human abstraction", P_ABS],
 ["Unstructured data", "AI augmented vs traditional real-world data", "Recall 49.9% to 93.2%, precision 73.6% to 93.5%, completeness 46.1% (38.2 to 54.0) to 96.6% (85.8 to 107.4)", "Traditional structured approach", P_PEER],
 ["Unstructured data", "Vendor accuracy claim", "Greater than 92% accuracy", "Not stated", P_CO],
 ["Synthetic data", "Control arm simulation, generator comparison", "CART based generation recovered the real median PFS inside the 95% CI in 88.8% to 98.1% of replicates, against 6.5% to 37.8% for a conditional tabular GAN", "Real trial control arm", P_PEER],
 ["Synthetic data", "Synthetic control arm in myelodysplastic syndromes", "Clinical fidelity 93%, genomic fidelity 90%, 7,133 patients, 187 matched synthetic controls", "Real patient records", P_PEER],
 ["Synthetic data", "Reporting completeness", "70 of 73 studies (95%) evaluated utility; 31 of 67 (46%) claiming privacy purpose evaluated privacy; 8 of 73 (11%) used a differentially private generator", "Not applicable", P_PEER],
 ["Regulatory writing", "Clinical study report first draft", "40% faster first draft; manuscript submission timeline 15% shorter", "Historical internal process", P_CO],
 ["Regulatory writing", "Clinical study report first draft", "180 hours to 80 hours per fully human reviewed draft; errors reduced 50%; first draft in as little as five minutes", "Historical internal process", P_CO],
 ["Regulatory writing", "Clinical study documentation", "More than ten weeks to ten minutes; 90% reduction in CSR writing time; review cycles halved; 95% reduction for device verification protocols", "Historical internal process, baseline 2.3 CSRs per writer per year", P_CO],
 ["Regulatory writing", "Analysis and tabulation process", "20 week process projected to be cut approximately in half", "Historical internal process", P_CO],
 ["Regulatory writing", "IND document generation", "Approximately 100 hours to 3.7 hours for 18,870 pages across 61 documents; to 2.6 hours for 11,425 pages across 58 documents", "Historical estimate, no concurrent control, n = 2 INDs", P_PRE],
 ["Regulatory writing", "Industry baseline", "Approximately 120 hours of regulatory writing over four weeks; 83 days from database lock to approved CSR", "Not applicable, baseline only", P_CO],
 ["Clinical development", "Site selection for a 14,000 patient cardiovascular outcomes trial", "Four to six weeks reduced to a two hour meeting; enrolment closed 13 patients above target", "Historical internal process", P_CO],
 ["Clinical development", "Late stage study cost", "Approximately GBP 8 million saved; all trials targeted 15% faster", "Historical internal process", P_CO],
 ["Market access", "Payer dossier drafting per AMCP Format v5.0", "Draft approximately 90% complete; approximately 80% less development time; 70% to 75% lower cost; authors noted repetition in all sections", "Single team, no comparator, 110 source documents", P_ABS],
 ["Market access", "Payer policy monitoring", "Policy and formulary alerts within 24 to 48 hours; analysis in minutes rather than days or weeks", "Not stated", P_CO],
 ["Market access", "Pricing, gross to net, contracting, and international reference pricing analytics", "No primary source with a measured, attributable efficiency or accuracy figure was located", "Not applicable", "Not available"],
 ["Drug discovery", "AI discovered molecule phase success", "Phase 1 success 80% to 90%; phase 2 success approximately 40%", "Historical benchmarks of 13.8% phase 1 to approval overall and 3.4% in oncology", P_PEER],
 ["Drug discovery", "AI discovered assets in clinical development", "31 assets across eight companies; 117 assets across 63 companies, with 60 of 117 (51.3%) completing phase 1 and 8 of 117 (6.8%) completing phase 2", "Total clinical pipeline of several thousand", P_PEER],
]
add("Table 4", "Reported performance and efficiency of artificial intelligence across HEOR workflows, with the provenance of every claim",
    "Provenance is classified as peer reviewed, preprint, conference abstract, or company communication. Company communication denotes a figure reported by the "
    "organization deploying or selling the tool, without independent replication or a concurrent control. Every company reported efficiency figure in this table "
    "falls into that category. Where no primary source with a measured figure could be located, the cell records that absence rather than an estimate. "
    "AUC denotes area under the curve, AUROC area under the receiver operating characteristic curve, HR hazard ratio, ICER incremental cost effectiveness ratio, "
    "ORR objective response rate, and rwPFS real-world progression free survival.",
    ["HEOR workflow", "Task", "Reported result", "Comparator", "Provenance"], t4)

# ----------------------------------------------------------------- TABLE 5
t5 = [
 ["1", "Function, not tool", "Declare, for each AI component, which function it performed: evidence identification or screening, data extraction, cohort or exposure definition, outcome or endpoint derivation, covariate or confounder selection, effect estimation, parameter derivation, model code generation, synthetic data or external control generation, or narrative drafting. Name the model, version, vendor, and dates of use.",
  "Disclosure instruments currently ask whether AI wrote the text. Disclosed AI use was 3 of 1,391 HTA documents (0.2%) and 0.6% of Lancet submissions, against self reported use of 25% to 69%.", "Yes"],
 ["2", "Context of use and model risk", "State the question of interest, the context of use, and the model risk using the two factor definition of model influence and decision consequence, and name the decision the model influences.",
  "Adopts the FDA credibility assessment framework verbatim so that a single characterisation serves both regulatory and HTA review.", "Yes"],
 ["3", "Calibration, not only discrimination", "Report calibration in the deployment population and time period, not only discrimination. Where the estimate depends on absolute risk or absolute cost, discrimination alone is insufficient.",
  "Across four deployed clinical AI systems, calibration degraded earlier and more consistently than discrimination. Cost effectiveness results depend on calibration.", "Yes"],
 ["4", "Reliability of the human reference", "Where AI output is validated against human abstraction, report the reliability of that human reference, including inter-abstractor agreement.",
  "The reference standard for scaled machine learning response abstraction itself had agreement of 0.94 on assessment presence and 0.82 on best response category.", "Yes"],
 ["5", "Disaggregated, variable level performance", "Report performance separately for each variable the analysis depends on. Aggregate F1 or accuracy is not sufficient.",
  "Stage value reached 98.8% precision while histology linkage reached 79% recall in the same model; T stage reached F1 0.89 while M stage reached 0.24.", "Yes"],
 ["6", "Decision reversal analysis", "Re-estimate the primary result with the AI component replaced by the pre-AI alternative or by a plausible worst case, and state whether the incremental cost effectiveness ratio crosses the relevant threshold or whether the recommendation changes.",
  "No existing instrument requires this. Deriving real-world progression from radiology reports rather than clinical notes moved median survival by seven months, which is decision relevant.", "Yes"],
 ["7", "Bias and subgroup performance", "Report performance for the subgroups the decision affects, and report the demographic composition of any training or synthetic population.",
  "A commercial risk algorithm applied to approximately 200 million people identified 17.7% of Black patients for extra help where a corrected target identified 46.5%.", "Yes"],
 ["8", "Synthetic data and external controls", "Report generator family, fidelity against the real target quantity rather than against summary statistics, and a privacy evaluation.",
  "Generator choice alone moved recovery of the true median progression free survival from 6.5% to 98.1% of replicates. Only 11% of studies used a differentially private generator.", "Yes"],
 ["9", "Human oversight actually performed", "Report quantitatively what fraction of AI output was reviewed, by whom, with what qualifications, and what the disagreement rate was.",
  "A biased AI lowered clinician diagnostic accuracy by 11.3 percentage points and explanations did not protect; experienced radiologists fell from 82.3% to 45.5% with an incorrect suggestion.", "Yes"],
 ["10", "Archive prompts, code, and versions", "Deposit prompts, code, model versions, random seeds, and intermediate outputs in a citable archive at the time of submission.",
  "Five percent of health economic evaluations mention code availability. An AI assisted analysis is not auditable without the prompts.", "Yes"],
]
add("Table 5", "TRACE-HEOR: proposed ten item standard for Transparent Reporting of Artificial intelligence Components in health Economics and Outcomes Research",
    "TRACE-HEOR is designed as an extension to CHEERS 2022 and PALISADE rather than as a replacement, and is aligned to the FDA credibility assessment framework "
    "and to ELEVATE-GenAI. Items 1, 2, 6, 9, and 10 constitute the minimum set. Item 6 is the item no current instrument requires and the item a reimbursement "
    "committee needs most. Every item is stated so that it can be verified by a reviewer with access only to the submission.",
    ["Item", "Short name", "Requirement", "Empirical basis", "Reviewer verifiable"], t5)

# ================================================================ eTABLES
add("eTable 1", "Complete PubMed search strings",
    "All searches were executed on 9 September 2026 through the PubMed E-utilities interface. The primary review search is the ai_heor string restricted to publication years 2010 through 2025. The remaining strings are the denominator series reported in eTable 5.",
    ["Series", "PubMed query string"], [[r["query"], r["pubmed_query_string"]] for r in qstr])

rows = []
for key, terms in DOMAIN_DICT.items():
    rows.append([DOMAIN_LABELS.get(key, key), "Application domain", key, "; ".join(terms)])
for key, terms in METHOD_DICT:
    rows.append([METHOD_LABELS.get(key, key), "Method category (evaluated in order of specificity)", key, "; ".join(terms)])
add("eTable 2", "Complete classification dictionary",
    "Terms are regular expressions applied case insensitively to the concatenated title, abstract, and MeSH terms. Domain labels are non-exclusive. Method categories are "
    "evaluated in the order shown and the first match is assigned, so that generative AI takes precedence over classical machine learning and unspecified AI is assigned only "
    "when no more specific term is present. The measured error rates of this dictionary are reported in Table 2 and eTable 8.",
    ["Label", "Label type", "Key", "Terms and patterns"], rows)

rows = [["Records identified in PubMed", prisma["records_identified"]],
        ["Duplicate records removed", prisma["duplicates_removed"]],
        ["Records screened", prisma["records_screened"]],
        ["Records excluded, total", prisma["records_excluded"]]]
for k, v in sorted(prisma["exclusion_reasons"].items(), key=lambda x: -x[1]):
    rows.append(["  " + k, v])
rows.append(["Records included", prisma["records_included"]])
rows.append(["Precision-adjusted included records (point estimate)", agsum["precision_adjusted_included"]["point"]])
rows.append(["Precision-adjusted included records (95% CI)",
             f"{agsum['precision_adjusted_included']['ci95'][0]} to {agsum['precision_adjusted_included']['ci95'][1]}"])
add("eTable 3", "PRISMA-ScR flow with itemized exclusion reasons",
    "Exclusions were applied programmatically in the order listed and each record is counted once, under the first applicable reason. The precision-adjusted estimate applies the "
    "search precision measured in Table 2 to the included count and is reported for interpretation, not as a screening result.",
    ["Stage or reason", "Records (n)"], rows)

SHORT_DOM = {"economic_evaluation": "Econ eval", "rwd_causal": "RWD causal", "governance_reporting": "Governance",
             "outcome_prediction": "Prediction", "evidence_synthesis": "Evidence synth", "hta_access": "HTA access",
             "decision_modeling": "Decision model", "pro_preferences": "PRO pref"}
SHORT_MET = {"ai_general": "AI unspec", "classical_ml": "Classical ML", "deep_learning": "Deep learn",
             "none": "No method", "generative_llm": "Generative", "nlp": "NLP"}
hdr = ["Year", "Total"] + [SHORT_DOM[k] for k in DOM_KEYS] + ["No domain"] + [SHORT_MET[k] for k in MET_KEYS]
rows = []
for r in annual:
    rows.append([r["year"], cn(r["included_total"])] + [r[k] for k in DOM_KEYS] + [r["none"]] + [r[k] for k in MET_KEYS])
add("eTable 4", "Included records per year by application domain and method category, 2010 to 2025",
    "Domain columns are non-exclusive and do not sum to the included total. Method columns are exclusive and sum to the included total. Column abbreviations, in order: Econ eval, economic evaluation; RWD causal, real-world data and causal inference; Governance, governance, reporting, and validity; Prediction, outcome and cost prediction; Evidence synth, evidence synthesis; HTA access, HTA, payer, and market access; Decision model, decision modeling and simulation; PRO pref, patient-reported outcomes and preferences; No domain, records to which the dictionary assigned no domain label; AI unspec, artificial intelligence unspecified; Classical ML, classical machine learning; Deep learn, deep learning; No method, no AI method term identified; Generative, generative AI and large language models; NLP, natural language processing before the generative era.",
    hdr, rows)

series = sorted({r["query"] for r in counts})
years = sorted({r["year"] for r in counts})
cmap = {(r["query"], r["year"]): r["count"] for r in counts}
rows = [[s] + [cmap.get((s, y), "") for y in years] for s in series]
add("eTable 5", "Annual PubMed denominator series, 2010 to 2025",
    "All series retrieved 9 September 2026. Query strings are given in eTable 1. The range form of the ai_heor query returned 2,656 records where the sum of the sixteen per year "
    "queries was 2,929, a difference of 273 records. The most likely explanation is records with a MedlineDate spanning two calendar years, which are counted in both per year queries. "
    "The per year series was used for trend estimation and the range query for the PRISMA flow.",
    ["Series"] + years, rows)

add("eTable 6", "Forty most frequent publication venues among included records",
    "Journal names are as indexed in PubMed. The 2,476 included records appeared in more than 900 distinct venues, so the concentration shown here is low by design.",
    ["Journal", "Included records (n)", "% of included"],
    [[r["journal"], cn(r["n_included"]), pc2(r["pct_of_included"])] for r in journals[:40]])

add("eTable 7", "Indexed publication types among included records",
    "Publication types are as indexed in PubMed and a record may carry more than one, so counts sum to more than 2,476. Randomized controlled trials account for 38 records (1.5%) and validation studies for 17 (0.7%).",
    ["Publication type", "Included records (n)", "% of included"],
    [[r["publication_type"], cn(r["n_included"]), pc2(r["pct_of_included"])] for r in designs])

rows = [[r["label"], r["n_dictionary"], r["n_independent"], d1(r["observed_agreement_pct"]), d3(r["cohen_kappa"]),
         d3(r["pabak"]), d1(r["dict_precision_vs_independent_pct"]), d1(r["dict_recall_vs_independent_pct"]), d1(r["dict_f1_pct"])] for r in agree]
rows.append(["Method category, 6-category multiclass", "300", "300", d1(agsum["method_label"]["observed_agreement_pct"]), d3(agsum["method_label"]["cohen_kappa"]), "", "", "", ""])
rows.append(["Generative AI or LLM flag", "", "", d1(agsum["generative_llm_flag"]["observed_agreement_pct"]), d3(agsum["generative_llm_flag"]["cohen_kappa"]), d3(agsum["generative_llm_flag"]["pabak"]), "", "", ""])
rows.append(["Mean domain kappa (median observed agreement)", "", "", d1(agsum["median_domain_observed_agreement_pct"]), d3(agsum["mean_domain_kappa"]), "", "", "", ""])
add("eTable 8", "Full agreement statistics for the validation analysis",
    "Paired records: 300. Cohen kappa below 0.20 indicates slight agreement, 0.21 to 0.40 fair, 0.41 to 0.60 moderate, 0.61 to 0.80 substantial. The final row reports the mean domain kappa and the median observed agreement across the eight domains.",
    ["Label", "Dictionary (n)", "Blinded classifier (n)", "Observed agreement (%)", "Cohen kappa", "PABAK", "Precision (%)", "Recall (%)", "F1 (%)"], rows)

add("eTable 9", "Search precision, overall and stratified by dictionary domain assignment",
    "Precision is the proportion of sampled records judged genuinely relevant to health economics and outcomes research by the blinded independent classifier. Confidence intervals are exact binomial (Clopper-Pearson). The stratification shows that the dictionary carries signal, since precision is higher among records to which it assigned at least one domain, but not enough of it.",
    ["Stratum", "n sampled", "n judged HEOR relevant", "Precision (%)", "95% CI lower", "95% CI upper"],
    [[r["stratum"], r["n_sampled"], r["n_heor_relevant"], r["precision_pct"], r["ci95_lo"], r["ci95_hi"]] for r in prec])

add("eTable 10", "Primary studies of large language model performance in study screening",
    "Sensitivity is the proportion of truly eligible records retained. Specificity is the proportion of truly ineligible records correctly excluded. Where a range is given, it spans models or reviews within the same study. The consistent pattern is acceptable sensitivity with unstable specificity, and between-review variance exceeding between-model variance.",
    ["Study focus", "Records screened", "Model", "Sensitivity", "Specificity or agreement", "Reported efficiency", "Provenance"],
    [["Two systematic review data sets", "1,381 and 3,146", "GPT-4, adjusted prompting", "0.962", "0.996", "Approximately 110 records per minute at US$59", P_PEER],
     ["Multiple reviews", "22,665 citations", "Multiple LLMs", "0.811 to 0.965", "0.258 to 0.804", "10,279 false positives in the worst configuration", P_PEER],
     ["Multiple reviews", "16,669 citations", "GPT-4", "0.85", "0.98, with a median specificity gap of 0.48 across reviews", "Not reported", P_PEER],
     ["Human versus LLM screening", "Not applicable", "GPT-4", "0.42", "Kappa 0.34 vs human kappa 0.77", "Not reported", P_PEER],
     ["Environmental and health evidence", "11,984 records", "LLM prioritisation", "Recall above 95% target", "Work saved over sampling 0.55", "Approximately 75% of screening effort saved", P_PEER],
     ["Agentic HEOR literature review", "Not stated", "Multi-agent, human in the loop", "F1 0.917 to 0.977", "Kappa 0.844 to 0.906 vs human", "Not reported separately", P_PEER],
     ["Time and motion, hybrid vs autonomous", "234 publications", "Not stated", "Hybrid recall 80.6%; autonomous recall 48.4%; unaided human recall 88.7%", "Hybrid accuracy 97.0%; unaided human accuracy 90.1%", "Hybrid 51.4% time saved; autonomous 81.1% time saved", P_ABS]])

add("eTable 11", "Primary studies of large language model performance in data extraction and downstream analysis",
    "Where both a model and a human arm are reported, the comparison of interest is the combination arm rather than either alone.",
    ["Task", "Scale", "Model", "Result", "Human comparator", "Provenance"],
    [["Extraction of 160 predefined items", "Not stated", "Claude 2", "96.3% accuracy", "Human extraction", P_PEER],
     ["Randomized trial extraction", "Not stated", "Not stated", "94.8% accuracy at 88 seconds per trial", "Human extraction", P_PEER],
     ["Extraction across 107 randomized trials", "12,814 extractions", "Claude 3.5", "96.2% accuracy; time 86.9 to 14.7 minutes", "Human 95.3%; human assisted by model 97.9%", P_PEER],
     ["Automated cost effectiveness model coding in R", "30 scripts", "GPT-4", "14 of 15 error free in the lung cancer set; every error free script within 1% of the published ICER", "Published model results", P_PEER],
     ["Network meta-analysis input extraction", "Not stated", "GPT-4", "Greater than 99% extraction accuracy", "Human extraction", P_PEER],
     ["Expected value of partial perfect information", "12.5 million model runs", "Metamodel", "More than 1,000 days reduced to approximately 2 days", "Brute force nested simulation", P_PEER],
     ["Reference generation, a cautionary comparison", "471 references", "GPT-3.5, GPT-4, Bard", "Hallucination 39.6%, 28.6%, 91.4%; DOI correct in 16% and 20%", "Verified bibliographic records", P_PEER],
     ["Reference generation, a cautionary comparison", "636 citations", "GPT-3.5, GPT-4", "55% and 18% fabricated, rising to 70% for book chapters", "Verified bibliographic records", P_PEER]])

add("eTable 12", "Machine learning methods for causal inference and their translation into HEOR",
    "The recurring finding is that predictive performance and evidentiary performance are separable. Optimizing discrimination in a propensity model can degrade the covariate balance that identification requires.",
    ["Method or study", "Contribution", "Key quantitative finding"],
    [["High dimensional propensity score", "Algorithmic covariate selection from claims", "Relative risk moved from 1.09 crude to 0.94 with 15 investigator covariates to 0.88 with 500 selected covariates in 49,653 users; a conventional estimate of 0.84 (0.56 to 1.26) became 0.62 (0.43 to 0.91)"],
     ["Performance under unmeasured confounding", "Empirical assessment of hdPS robustness", "Characterises the conditions under which the approach reduces or fails to reduce bias"],
     ["Targeted maximum likelihood estimation", "Doubly robust semiparametric estimation", "Foundational method, with pharmacoepidemiologic translation"],
     ["Super learning", "Ensemble selection by cross validation", "Foundational method underlying doubly robust implementations"],
     ["Causal forests", "Heterogeneous treatment effect estimation with valid inference", "Foundational method; applied to heterogeneity in cost effectiveness analysis"],
     ["Double or debiased machine learning", "Orthogonalised estimation of treatment effects", "Foundational method for high dimensional nuisance parameters"],
     ["hdPS weighting failure mode", "Simulation of estimator behaviour", "Bias 0.094 with 23.6% confidence interval coverage, against 0.018 and 91.4% for a modified procedure"],
     ["Trial emulation, PARADIGM-HF", "Comparison of propensity model classes against a trial benchmark", "AUC 0.79 gave HR 0.93; AUC 0.95 gave HR 0.61; trial HR 0.81 (0.61 to 1.06)"],
     ["Heterogeneous treatment effects with real-world data", "Scoping review", "1,743 records screened, 74 studies included"],
     ["Transportability and generalisability", "Methods for moving estimates between populations", "Reviewed methods for target population extrapolation in HEOR contexts"],
     ["Target trial framework", "Design discipline for real-world evidence", "Recommended as the organizing framework for observational comparative effectiveness"],
     ["PALISADE checklist", "Credibility instrument for real-world data studies", "Written for precisely the failure modes above and referenced by NICE"]])

add("eTable 13", "Natural language processing performance for HEOR relevant variable extraction from unstructured data",
    "Approximately 80% of clinical data is unstructured. The pattern across studies is that the variable a cohort definition or an endpoint depends on is frequently the variable extracted worst, which is why item 5 of TRACE-HEOR requires disaggregated reporting.",
    ["Variable or task", "Scale", "Reported performance", "Reference standard", "Provenance"],
    [["Social and behavioral determinants", "Not stated", "Recorded prevalence rose from 0.03% to 8.3% in claims to 1.40% to 36.3% with notes; walking difficulty 10.7% to 38.0%; lack of social support text only in 99.8% of cases", "Structured claims", P_PEER],
     ["Adverse social determinants in oncology", "48 patients with documented determinants", "44 of 48 (91.7%) had no corresponding Z code; fewer than 2% of inpatient hospitalizations carried any Z coded diagnosis", "Structured coding", P_PEER],
     ["ECOG performance status", "79,698 patients, 495,862 notes", "AUROC 0.95; imputed poor performance status HR 11.9", "Documented performance status", P_PEER],
     ["Performance status, Veterans Affairs implementation", "Not stated", "98.5% accuracy", "Manual review", P_PEER],
     ["PD-L1 status", "Not stated", "Micro F1 0.925", "Manual abstraction", P_PEER],
     ["Oncology staging and histology", "200 patients drawn from more than 27 million", "Lung neoplasm 100% precision and 100% recall; NSCLC histology 99% and 88%; histology linked to neoplasm 98% and 79%; stage value 98.8% and 92%; metastasis site 97% and 89%", "Human abstraction", P_PEER],
     ["Cancer registry TNM staging", "Not stated", "T stage F1 0.89; M stage F1 0.24", "Registry abstraction", P_PEER],
     ["Real-world progression free survival", "316 metastatic breast cancer patients", "Sentence level 98.2%; patient level within 30 days 88%; median rwPFS 20 months (18 to 25) computational, 22 months (15 to 35) in the validation subset, 25 months (15 to 35) manual; 30 months from radiology reports vs 23 months from clinical notes", "Manual curation of 100 patients", P_PEER],
     ["Human abstracted real-world response, reference standard", "3,248 patients, 85.4% with at least one radiographic assessment", "Inter-abstractor agreement 0.94 (0.92 to 0.96) and 0.82 (0.78 to 0.86); 15.0 minutes per patient line (IQR 7.8 to 28.1); Spearman 0.99 vs trial ORR", "Second human abstractor", P_PEER],
     ["Scaled machine learning real-world response", "Test subset of 4,047", "r = 0.86 against human abstraction", "Human abstraction", P_ABS],
     ["Cross tumor LLM extraction", "14 cancer types", "F1 similar to expert human abstractors; numerical values not disclosed", "Expert abstraction", P_ABS],
     ["AI augmented real-world data", "Not stated", "Recall 49.9% to 93.2%; precision 73.6% to 93.5%; completeness 46.1% (38.2 to 54.0) to 96.6% (85.8 to 107.4)", "Traditional structured approach", P_PEER],
     ["Vendor accuracy claim", "Not stated", "Greater than 92% accuracy", "Not stated", P_CO],
     ["AI derived HEOR variables, second vendor", "Not applicable", "No published validation located", "Not applicable", "Not available"]])

add("eTable 14", "Synthetic data, digital twins, and model based external control arms",
    "The regulatory record on external controls is more restrictive than the synthetic data literature acknowledges, and generator choice dominates whether the target quantity is recovered at all.",
    ["Study or instrument", "Setting", "Key quantitative finding"],
    [["Generator comparison for control arm simulation", "Oncology control arms", "CART based generation recovered the real median progression free survival inside the 95% CI in 88.8% to 98.1% of replicates, against 6.5% to 37.8% for a conditional tabular GAN"],
     ["Synthetic control arm in myelodysplastic syndromes", "7,133 patients", "Clinical fidelity 93%, genomic fidelity 90%; 187 luspatercept matched synthetic controls"],
     ["Synthetic data as external controls in scarce single arm trials", "Rare disease", "Evaluates feasibility and the conditions for acceptable inference"],
     ["AI generated digital twins", "6,736 subjects in Alzheimer disease", "6,236 of 6,728 subjects with recorded race were White and 152 were Black, which bounds what the synthetic population can be used to claim"],
     ["Training on synthetic electronic health records", "Not stated", "Model trained on synthetic records performed 0.026 lower in AUC than one trained on real records"],
     ["Reporting practices in synthetic health data", "73 studies", "70 (95%) evaluated utility; 31 of 67 (46%) claiming a privacy purpose evaluated privacy; 8 of 73 (11%) used a differentially private generator"],
     ["FDA approvals accepting external control data", "45 approvals, 2000 to 2019", "36 of 45 (80%) in rare disease; none used prospectively collected natural history controls"],
     ["Statistical limits of external controls for regulatory use", "Methodological analysis", "Characterises the bias and inference constraints for regulatory acceptance"],
     ["EMA qualification opinion on prognostic covariate adjustment", "Regulatory opinion", "Qualified, while stating that excluding dropout data would not be acceptable for regulatory purposes"]])

add("eTable 15", "Published economic evaluations of artificial intelligence in health care",
    "A systematic review identified 19 economic evaluations of AI in health care published between 2020 and 2024, with CHEERS scores between 21 and 27 of 28, against 1,614 FDA authorized AI enabled devices. The examples below illustrate why the price of the algorithm is frequently the wrong parameter to negotiate.",
    ["Study or intervention", "Setting", "Result", "Interpretation"],
    [["Systematic review of economic evaluations of AI", "2020 to 2024", "19 economic evaluations identified; CHEERS scores 21 to 27 of 28", "One published economic evaluation for approximately every 85 authorized devices"],
     ["AI versus polygenic risk scores for breast cancer risk stratification", "United States", "ICER US$23,755 per QALY in 2020 US dollars; AI cost threshold US$318 per mammogram", "Cost effective within conventional thresholds under the modelled assumptions"],
     ["AI intervention, dual perspective analysis", "Not stated", "US$1,107.63 per QALY health system perspective; US$10,347.12 per QALY societal perspective", "Perspective choice moved the ratio by roughly an order of magnitude"],
     ["AI in the UK national breast screening programme", "United Kingdom", "A scenario was identified in which no price per scan made the technology cost effective", "Cost effectiveness was determined by the downstream care pathway rather than by algorithm price"],
     ["Risk based breast cancer screening model", "United States", "Deep learning risk model enabling risk stratified screening intervals", "Provides the clinical basis that the economic evaluations above assess"],
     ["Framework for valuing clinical decision support", "Methodological", "Sets out how decision support value accrues through changes in downstream care", "Explains the mechanism behind the UK screening result"],
     ["Reinforcement learning for tuberculosis screening", "Not stated", "Illustrates the sequential decision variant of the evaluation problem", "Extends the framework to adaptive interventions"]])

pan = collections.Counter(); yr = collections.Counter(); pan_yr = collections.Counter()
for r in fda:
    p = (r.get("Panel (Lead)") or "Unknown").strip()
    d = (r.get("Date of Final Decision") or "").strip()
    y = d[-4:] if len(d) >= 4 else "Unknown"
    pan[p] += 1; yr[y] += 1; pan_yr[(p, y)] += 1
years_f = [y for y in sorted(yr) if y.isdigit() and int(y) >= 2016]
EARLY = [y for y in sorted(yr) if y.isdigit() and int(y) < 2016]


def early(p=None):
    return sum(pan_yr[(p, y)] for y in EARLY) if p else sum(yr[y] for y in EARLY)


rows = []
for p, n in pan.most_common():
    rows.append([p, f"{n:,}", f"{100*n/len(fda):.1f}", early(p)] + [pan_yr.get((p, y), 0) for y in years_f])
rows.append(["All panels", f"{len(fda):,}", "100.0", early()] + [yr[y] for y in years_f])
add("eTable 16", "FDA authorized AI-enabled medical devices by review panel and year of final decision",
    f"Retrieved from the FDA AI-Enabled Medical Device List, current as of 4 September 2026, and tabulated in full: {len(fda):,} authorizations. "
    "The 2026 count covers decisions through the retrieval date only. Three quarters of authorized AI in United States medicine operates in a single specialty, "
    "which bounds how far the cost effectiveness literature reviewed in eTable 15 can generalize. Decisions before 2016 are collapsed into a single column.",
    ["Review panel (lead)", "Authorizations (n)", "% of all", "Before 2016"] + years_f, rows)

add("eTable 17", "Industry reported artificial intelligence deployment in pharmaceutical evidence generation, with provenance",
    "Every efficiency figure in this table is reported by the organization deploying or selling the tool. None has been independently replicated, and none is accompanied by a "
    "concurrent control. The most methodologically explicit, the IND document generation preprint, compares against a historical estimate with n = 2. Provenance labels are as in Table 4.",
    ["Organization or partnership", "Application", "Reported figure", "Baseline or comparator", "Provenance"],
    [["Pfizer", "Clinical study report and manuscript authoring", "First draft CSR 40% faster; manuscript submission timeline 15% shorter; enrollment target plus 20%", "Historical internal process", P_CO],
     ["Merck", "Clinical study report authoring", "180 hours to 80 hours per fully human reviewed first draft; errors reduced 50%; first draft in as little as five minutes; team of more than 80 across three continents", "Historical internal process", P_CO],
     ["Merck and Google Cloud", "Enterprise AI platform", "Agreement valued at up to US$1 billion over multiple years, announced 22 April 2026, covering 75,000 employees", "Not applicable", P_CO],
     ["Novo Nordisk, NovoScribe", "Clinical study documentation", "More than ten weeks to ten minutes; 95% reduction for device verification protocols; CSR writing time cut 90%; review cycles halved; baseline 2.3 CSRs per writer per year with a team of 11", "Historical internal process", P_CO],
     ["Takeda", "Analysis and tabulation, document summarisation", "A 20 week process projected to be cut approximately in half; 70 pages summarised in two sentences", "Historical internal process", P_CO],
     ["Takeda and Weave Bio", "IND document generation", "Approximately 100 hours to 3.7 hours for 18,870 pages across 61 documents in IND-1; to 2.6 hours for 11,425 pages across 58 documents in IND-2", "Historical estimate, no concurrent control, n = 2 INDs, vendor co-authored", P_PRE],
     ["Certara, CoAuthor", "Regulatory writing", "Baseline of approximately 120 hours over four weeks and 83 days from database lock to approved CSR; no time saving reported for the product itself", "Not applicable, baseline only", P_CO],
     ["Novartis", "Site selection for a 14,000 patient cardiovascular outcomes trial", "Four to six weeks reduced to a two hour meeting; enrolment closed 13 patients above target", "Historical internal process", P_CO],
     ["Novartis", "Responsible AI programme", "More than 100 use cases; adverse events reported within 24 hours; targets of two years faster development and US$1 billion to US$2 billion cost reduction", "Historical internal process", P_CO],
     ["GSK", "Late stage study efficiency", "Approximately GBP 8 million (US$10.87 million) saved in late stage asthma studies; all trials targeted 15% faster", "Historical internal process", P_CO],
     ["Eli Lilly and NVIDIA", "Compute infrastructure", "More than 1,000 B300 graphics processing units, announced 28 October 2025", "Not applicable", P_CO],
     ["Tempus, AstraZeneca, and Pathos", "Multimodal oncology foundation model", "US$200 million in data licensing and model development fees, announced 23 April 2025", "Not applicable", P_CO],
     ["Moderna and OpenAI", "Enterprise generative AI adoption", "750 custom assistants deployed in two months; internal assistant adoption above 80%", "Not applicable", P_CO],
     ["Pharmacoevidence", "AMCP Format v5.0 payer dossier drafting", "Draft approximately 90% complete; approximately 80% less development time; 70% to 75% lower cost; authors noted repetition in all sections and only somewhat complete SME agreement", "Single team, no comparator, 110 source documents", P_ABS],
     ["Norstella", "Payer policy and formulary monitoring", "Alerts within 24 to 48 hours; analysis in minutes rather than days or weeks", "Not stated", P_CO],
     ["IQVIA", "Market access analytics", "No quantitative figure reported on the product materials", "Not applicable", "Not available"],
     ["Exscientia and Sumitomo, DSP-1181", "AI designed candidate", "Entered the clinic January 2020, abandoned January 2022 for failing to meet study criteria", "Not applicable", P_PEER],
     ["Exscientia, EXS-21546", "AI designed candidate", "Discontinued after modelling suggested a suitable therapeutic index would be difficult to reach", "Not applicable", P_PEER],
     ["Exscientia, BenevolentAI, and Recursion", "AI discovery platforms", "Combined accumulated deficit above US$1.5 billion; equity values down at least 75%", "Not applicable", P_PEER],
     ["Recursion, REC-994", "Phase 2 in cerebral cavernous malformation", "62 patients; trend toward reduced lesion volume on imaging but no improvement on patient reported outcomes or physician led measures at 12 months", "Placebo controlled", P_CO],
     ["AI discovered molecules, independent analysis", "Phase transition success", "Phase 1 success 80% to 90%; phase 2 success approximately 40%", "Historical 13.8% phase 1 to approval overall; 3.4% in oncology", P_PEER],
     ["AI enabled assets, industry wide analysis", "Clinical pipeline", "117 assets across 63 companies; 60 of 117 (51.3%) completed phase 1; 8 of 117 (6.8%) completed phase 2", "Total clinical pipeline of several thousand", P_PEER]])

add("eTable 18", "Journal, publisher, and society policies on the disclosure of artificial intelligence use",
    "Observed disclosure runs far below reported use. The Lancet editors checked every submission received in February 2024 and found 0.6% declaring ChatGPT, 0.6% Grammarly, and 1.8% AI as a research tool, against 3.6% reporting a medical writer. The common structural gap is that these instruments govern authorship of text rather than the analytic functions that move an estimate.",
    ["Body", "Requirement", "Notable provision"],
    [["ICMJE", "Disclosure at submission; AI cannot be an author", "Authors are accountable for all content, including AI generated portions"],
     ["COPE", "AI tools cannot be listed as authors", "Authors must be able to assert the presence or absence of AI generated content"],
     ["NEJM AI", "Disclosure of authoring tools; reviewer disclosure", "Reviewers must disclose AI use and protect manuscript confidentiality"],
     ["JAMA Network", "Disclosure of model name, version, manufacturer, and dates of use", "The most specific technical disclosure requirement among general medical journals"],
     ["Health Affairs", "Disclosure in the cover letter and in Methods or Acknowledgements", "Requires disclosure in the manuscript body, not only to editors"],
     ["The Lancet", "Disclosure required; AI peer review prohibited", "States that use of AI for peer reviewing is not currently permitted"],
     ["Elsevier", "Named declaration section required", "Separates permitted language improvement from reportable analytic use"],
     ["Springer Nature", "Documentation in Methods; copy editing exempt", "Large language models do not satisfy authorship criteria"],
     ["ISPOR and Value in Health", "Disclosure of AI generated content; AI may not be cited as a reference", "States that authors may not attempt to hide or disguise their use of AI"]])

add("eTable 19", "Adoption, workforce, and transparency surveys bearing on AI in HEOR",
    "Self reported use ranges from 25% to 81% depending on population and year, against disclosed use of 0.2% in HTA documents and 0.6% in journal submissions. Within HEOR specifically, proficiency is low and team level adoption lags individual use.",
    ["Source and population", "Field date", "n", "Key finding"],
    [["HEOR leaders at 72 companies", "2025 to 2026", "100 leaders, 58 to 59 AI items", "69% personally use AI; 80% say the employer supports it; 29% expect AI to replace HEOR staff within two years against 47% who disagree; 59% report the team does not use AI for any listed workflow"],
     ["HEOR, real-world data, and medical affairs professionals", "April 2026", "133", "Expert 4%, advanced 11%, moderate 24%, basic 52%, very limited 9%, so 61% basic or very limited"],
     ["Physicians, AMA augmented intelligence survey", "2023, 2024, 2026", "1,081; 1,183; 1,692", "38% using in 2023; 66% in 2024; 81% aware or using in 2026, with average use cases rising from 1.1 to 2.3; 88% concerned about skill loss; 88% want safety and efficacy validation"],
     ["US healthcare leaders, generative AI implementation", "Q4 2023 to Q4 2025", "150", "25% to 47% to 50% implemented; agentic AI implemented 19% with 51% in proof of concept; 82% expect positive return but only 45% have quantified it"],
     ["Medical affairs professionals", "2026", "Not stated", "86% confident AI improves efficiency; leading edge 20%, cautious 41%, fast followers 33%, wait and see 6%; top barrier validation and accuracy 47%; 49% use full manual SME review of every AI generated piece"],
     ["Life sciences generative AI budgets", "2024 to 2025", "82", "Budgets of at least US$5 million rose from 20% to 32%"],
     ["Life sciences executives", "January 2026", "200", "74% rate AI crucial or very important; 60% expect budget increases overall and 71% in human pharma; 82% concerned about intellectual property liability"],
     ["ISPOR and ISPE conference abstracts", "1 January 2020 to 6 December 2024", "28,184 abstracts", "1,153 AI related; 89% of applications in systematic literature review automation and 9% in economic modeling; CRO 44%, academia 40%, pharmaceutical 16%"],
     ["HTA agency practice and submissions", "2023 to 2025", "1,309 screened, 37 included", "Seven agencies adopting AI internally; NICE recorded 49 AI initiatives across 25 HTAs"],
     ["HTA dossier disclosure audit", "2023 to 2025", "1,391 documents", "3 documents (0.2%) disclosed AI or machine learning, all at NICE (TA1154, TA1071, TA962); no explicit reporting in CDA or IQWiG dossiers"],
     ["Journal submission disclosure audit", "February 2024", "All submissions in one month", "0.6% declared ChatGPT, 0.6% Grammarly, 1.8% AI as a research tool, against 3.6% reporting a medical writer"],
     ["Researchers, Nature survey", "2025", "5,229", "Divided on acceptability, with roughly a quarter reporting use of AI to edit papers"],
     ["Academics on AI in peer review", "2025", "Approximately 1,600 across 111 countries", "More than half reported having used AI in peer review"],
     ["Health economic evaluation transparency", "2019 sample", "200 evaluations in 147 journals", "10 (5%) mentioned access to raw data and analytic code; 112 (56%) reported data to recreate the base case ICER; 31 (16%) reported working from a protocol"],
     ["Discrete event simulation model sharing", "2019 to 2022", "564 studies", "47 (8.3%) cited an openly available model, rising from 4.0% to 9.0%"],
     ["Open source health economic models", "Not stated", "8,664 screened, 182 models", "74% hosted on GitHub, 64% written in R, 49% Markov structure"],
     ["US digital health venture funding", "2019 to 2025", "482 deals in 2025", "AI enabled companies took 37% of funding across 191 deals in 2024, rising to 54% of funding and 50% of deals in 2025, with a deal size premium of approximately 19%"]])

rows = []
for doi in sorted(reflib):
    e = reflib[doi]
    rows.append([doi, "DOI, Crossref verified", e.get("journal", ""), str(e.get("year", "")), e.get("vancouver", "")])
for k in sorted(weblib):
    rows.append([k, "Grey literature, retrieved at the cited URL", "", "", weblib[k]])
rows.append(["10.3389/fpubh.2026.1951054", "FAILED TO RESOLVE, removed from the manuscript rather than cited", "", "", "Candidate DOI did not resolve against Crossref or DataCite and is not cited anywhere in this manuscript."])
rows.append(["10.1093/qje/qjab010", "RESOLVED TO AN UNRELATED WORK, removed", "The Quarterly Journal of Economics", "2021", "Resolved to Ownership, Learning, and Beliefs, which does not support the claim it was attached to, and was therefore removed rather than cited."])
add("eTable 20", "Reference verification log",
    "Every DOI cited in this manuscript was resolved programmatically against the Crossref REST application programming interface, with a DataCite fallback for preprint and dataset "
    "identifiers, and the returned metadata was used to construct the reference list. Of 173 candidate DOIs, 172 resolved. One failed to resolve and one resolved to an unrelated work; "
    "both were removed rather than cited, and both are recorded here. Grey literature without a DOI was retrieved at the cited uniform resource locator. Crossref returns lowercased DOIs.",
    ["Identifier or key", "Verification status", "Journal", "Year", "Verified reference"], rows)

# ----------------------------------------------------------------- WRITE
HFILL = PatternFill("solid", fgColor="1B474D")
TFILL = PatternFill("solid", fgColor="E8EEEF")
thin = Side(style="thin", color="B8C3C5")
BORD = Border(left=thin, right=thin, top=thin, bottom=thin)


def write_wb(tabs, path):
    wb = Workbook(); wb.remove(wb.active)
    for t in tabs:
        ws = wb.create_sheet(t["id"].replace(" ", ""))
        ws["A1"] = f"{t['id']}. {t['title']}"
        ws["A1"].font = Font(bold=True, size=12, color="1B474D")
        ws["A1"].alignment = Alignment(wrap_text=True, vertical="center")
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(2, len(t["headers"])))
        ws.row_dimensions[1].height = 34
        for j, h in enumerate(t["headers"], start=1):
            c = ws.cell(row=3, column=j, value=str(h))
            c.font = Font(bold=True, color="FFFFFF", size=10)
            c.fill = HFILL; c.border = BORD
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.row_dimensions[3].height = 32
        for i, row in enumerate(t["rows"], start=4):
            for j, v in enumerate(row, start=1):
                c = ws.cell(row=i, column=j, value=v)
                c.font = Font(size=9, bold=(j == 1 and v and not v.startswith("  ") and len(t["headers"]) == 4))
                c.border = BORD
                c.alignment = Alignment(wrap_text=True, vertical="top")
            if i % 2 == 0:
                for j in range(1, len(t["headers"]) + 1):
                    ws.cell(row=i, column=j).fill = TFILL
        fr = len(t["rows"]) + 5
        ws.cell(row=fr, column=1, value="Note. " + t["footnote"]).font = Font(size=8, italic=True)
        ws.cell(row=fr, column=1).alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=fr, start_column=1, end_row=fr, end_column=max(2, len(t["headers"])))
        ws.row_dimensions[fr].height = 60
        n = len(t["headers"])
        for j in range(1, n + 1):
            col = ws.cell(row=3, column=j).column_letter
            vals = [len(str(r[j - 1])) for r in t["rows"] if j - 1 < len(r)]
            mx = max(vals) if vals else 10
            ws.column_dimensions[col].width = min(60, max(12, mx * 0.55 if mx > 40 else mx + 4))
        ws.freeze_panes = "A4"
    wb.save(path)
    return path


main = [t for t in TABLES if t["id"].startswith("Table")]
supp = [t for t in TABLES if t["id"].startswith("eTable")]
os.makedirs(os.path.join(ROOT, "tables"), exist_ok=True)
p1 = write_wb(main, os.path.join(ROOT, "tables", "main_tables.xlsx"))
p2 = write_wb(supp, os.path.join(ROOT, "tables", "supplementary_tables.xlsx"))
json.dump(TABLES, open(os.path.join(ROOT, "tables", "tables_spec.json"), "w"), indent=1)
print(f"Wrote {p1} ({len(main)} tables)")
print(f"Wrote {p2} ({len(supp)} eTables)")
for t in TABLES:
    print(f"  {t['id']}: {len(t['rows'])} rows x {len(t['headers'])} cols")
