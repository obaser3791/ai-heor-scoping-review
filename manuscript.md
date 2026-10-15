---
title: "Faster but Not Truer: A Systematic Scoping Review of Artificial Intelligence in Health Economics and Outcomes Research"
subtitle: "The Evidence, the Regulatory Record, and the TRACE-HEOR Reporting Standard"
author: "Onur Baser, Ph.D."
type: "Review"
---

**Onur Baser, Ph.D.**^1,2^

^1^Department of Internal Medicine, University of Michigan, Ann Arbor, MI
^2^Graduate School of Public Health and Health Policy, City University of New York, New York, NY

The author affiliations are listed at the end of the article.

## Short Summary

Artificial intelligence now appears in one of every sixteen health economics and outcomes research publications, yet in a systematic audit of 1,391 health technology assessment documents submitted to three agencies, only three disclosed using it. This review pairs an original scoping review of 2,476 indexed studies published between 2010 and 2025 with the regulatory and submission record, and finds a field whose measured performance, disclosed practice, and marketed promise have come apart. A validation exercise on our own search shows why: half of what a competent query returns is not health economics at all, and the label that grows fastest is the one a classifier can least reliably assign. We propose TRACE-HEOR, a ten item reporting standard, and a research agenda built around the question regulators actually ask, which is not whether a model is accurate but whether a decision made with it would have been different.

## Abstract

**BACKGROUND**

Artificial intelligence (AI) is being introduced into every stage of the health economics and outcomes research (HEOR) production line, from literature screening to causal estimation to the drafting of reimbursement dossiers. Claims about efficiency have outpaced evidence about validity, and the regulatory frameworks that will govern this evidence are being written now.

**METHODS**

We conducted a systematic scoping review following PRISMA-ScR. We searched PubMed for AI terms co-occurring with HEOR terms for publications from 2010 through 2025, retrieved 2,642 records, and included 2,476 after screening. Records were classified into eight application domains and six method categories using a preregistered term dictionary. To quantify classification error, an independent large language model classifier, blinded to the dictionary labels, re-classified a random sample of 300 included records; we report Cohen kappa, prevalence-adjusted bias-adjusted kappa, precision, recall, and F1 for every label, and a precision-adjusted corpus size. We separately assembled the regulatory record from primary agency documents, the submission record from published audits of health technology assessment (HTA) dossiers, and the performance record from primary methods studies. Every cited digital object identifier (DOI) was verified programmatically against Crossref, with DataCite fallback.

**RESULTS**

Included publications rose from 29 in 2010 to 852 in 2025, a factor of 29.4, and AI reached 6.0% of all indexed HEOR output in 2025 while HEOR fell to 0.86% of all indexed medical AI output. Economic evaluation was the most frequently assigned domain (1,559 of 2,476, 63.0%), followed by real-world data and causal inference (496, 20.0%) and governance, reporting, and validity (494, 20.0%). Generative AI appeared in no record before 2021 and in 103 records in 2025. Validation was sobering. Only 154 of 300 sampled records (51.3%, 95% confidence interval [CI] 45.7 to 56.9) were judged genuinely HEOR relevant by the blinded classifier, implying a precision-adjusted corpus of 1,271 studies (95% CI 1,131 to 1,410). Agreement was moderate to substantial for real-world data and causal inference (kappa 0.729) and evidence synthesis (kappa 0.666) but negligible for economic evaluation (kappa 0.144), the largest and fastest growing label. Against this literature, AI or machine learning was disclosed in 3 of 1,391 HTA documents (0.2%) across three agencies, all three at the National Institute for Health and Care Excellence, and in 0.6% of Lancet submissions in a one month audit. Company reported time savings in regulatory writing ranged from 40% to 97%, none independently replicated. No regulator or HTA body has been documented accepting or rejecting an AI derived endpoint as such. The US Food and Drug Administration (FDA) has authorized 1,614 AI enabled medical devices, 76.2% of them in radiology, but its January 2025 draft guidance on AI for drug and biological product decisions remains draft as of September 2026.

**CONCLUSIONS**

The AI in HEOR literature is growing faster than its own measurement infrastructure and far faster than its disclosure into decision grade submissions. The binding constraint is not model accuracy but decision relevance, and the field currently reports almost none of what a payer or regulator would need to audit. We propose TRACE-HEOR (Transparent Reporting of Artificial intelligence Components in health Economics and Outcomes Research), a ten item standard aligned to the FDA credibility framework and the ELEVATE-GenAI guidance, and a research agenda whose first deliverable is a public benchmark of decision reversal rather than of prediction.

## Introduction

Two facts about artificial intelligence in health economics and outcomes research sit uneasily beside each other.

The first is that the field has been reorganized around it. Since 2016 the US Food and Drug Administration has received more than 500 drug and biological product submissions containing AI components, and its Center for Biologics Evaluation and Research alone has logged more than 70 investigational new drug applications with an AI element^1-3^. The agency issued its first draft guidance on AI for regulatory decision making in January 2025^4^, joined the European Medicines Agency in publishing ten guiding principles for good AI practice in drug development in January 2026^5,6^, and has now authorized 1,614 AI enabled medical devices^7^. The International Society for Pharmacoeconomics and Outcomes Research moved AI from the third ranked HEOR trend for 2024 to 2025 to the first ranked trend for 2026 to 2027^8^, and published a taxonomy, a reporting guideline, and a policy report for generative AI in HEOR within a single year^9-11^.

The second fact is that almost none of this has yet reached the documents on which reimbursement decisions are made. In a systematic audit of 1,391 health technology assessment (HTA) documents submitted to the National Institute for Health and Care Excellence (NICE), Canada's Drug Agency, and the Institute for Quality and Efficiency in Health Care between 2023 and 2025, exactly three disclosed the use of AI or machine learning in a systematic literature review, an adoption rate of 0.2%, and all three were at NICE^12^. When The Lancet editors checked every submission received during February 2024, 0.6% declared use of ChatGPT^13^. A survey of 100 HEOR leaders at 72 companies found that 69% personally use AI in their work while 59% said their team does not use AI for any listed HEOR workflow^14^.

The gap between those two facts is the subject of this review. It is not simply a lag. It is a measurement problem, a governance problem, and an economics problem at once, and the three are entangled in a way that has not been set out systematically.

The measurement problem is that we do not have a defensible count of what has actually been done. Prior reviews of machine learning in HEOR have been deliberately partial: Lee and colleagues screened 148 records for wearable applications and included 32^15^, then sampled 161 of 805 records for non-wearable applications and included 92^16^. A 2026 scoping review of the economic aspects of machine learning in health care screened 6,332 references and included 18^17^. A protocol for a scoping review of machine learning in health economic evaluation screened 4,141 records and found 30 eligible reports^18^. Each of these is careful work, and each answers a narrower question than the one practitioners now ask, which is how large the field is, what it is actually doing, and how fast the composition is changing.

The governance problem is that the standards being written for AI in evidence generation are being written against an evidence base whose reliability nobody has quantified. NICE requires that AI methods "should only be used when there is demonstrable value from doing so" and points submitters to the PALISADE checklist^19,20^. Canada's Drug Agency adopted a parallel position built on the principle of augmentation rather than replacement^21^. The FDA's credibility framework asks sponsors to establish, in seven steps, that a model is fit for a specified context of use, and defines model risk as the combination of model influence and decision consequence^4^. All of these are risk based, and all of them presume the submitter can characterize the risk. Yet the prediction model literature these frameworks inherit is dominated by high risk of bias: 545 of 606 COVID-19 prediction models were rated at high risk of bias^22^, as were 148 of 171 studies of machine learning based prediction models^23^.

The economics problem is the one Daron Acemoglu has pressed hardest, and it applies to HEOR with unusual directness. In the published version of his macroeconomic assessment, Acemoglu estimates that AI will raise total factor productivity by no more than 0.66% over ten years, roughly 0.064% per year, with gross domestic product effects of about 1%^24,25^. His argument for why the number is small is a claim about task structure, not about model quality: many high value tasks are hard learning tasks, in the sense that the outcome of the decision is rarely observed cleanly and no large well curated data set of correct answers exists. He names diagnosis as his example, writing that "diagnosing the cause of a persistent cough and proposing a course of treatment is a hard problem" and that "there is no large, well-curated data set of successful diagnoses and cures"^24^. Health economics is the same kind of problem in a purer form. The counterfactual is never observed. There is no ground truth label for the incremental cost effectiveness ratio that would have obtained under a different treatment strategy, and therefore no supervised target against which a model can be trained or benchmarked. If Acemoglu is right about hard learning tasks, HEOR is close to the worst case, and the field's productivity gains should be expected in the clerical layer rather than in the inferential layer.

This review therefore does four things. First, it reports an original systematic scoping review of the indexed literature, following PRISMA-ScR, covering 2010 through 2025, with a full and reproducible search rather than a sample. Second, and unusually for a scoping review, it validates its own classification against an independent blinded classifier and reports the resulting error rates, because a bibliometric claim without a measured error rate is an assertion. Third, it assembles the regulatory record, the submission record, and the primary performance record side by side, so that what is claimed, what is measured, and what is disclosed can be compared directly. Fourth, it proposes TRACE-HEOR, a ten item reporting standard for Transparent Reporting of Artificial intelligence Components in health Economics and Outcomes Research, together with a research agenda organized around decision reversal rather than prediction accuracy.

The intended readers are the people who will have to defend this evidence: HEOR scientists and biostatisticians in industry and academia, regulatory and market access leaders who must decide what to disclose and how, HTA methodologists writing the next generation of position statements, and reviewers at FDA, EMA, NICE, and their counterparts who will receive dossiers built with these tools whether or not the dossiers say so.

## Methods

We followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR). The protocol, all search strings, the classification dictionary, the analysis code, and the verification logs are archived in a public replication package^26^. No patient level data were used and no ethics approval was required.

### SEARCH STRATEGY AND ELIGIBILITY

We searched PubMed on 9 September 2026 using a structured Boolean query requiring co-occurrence of at least one AI term and at least one HEOR term in the title, abstract, or MeSH terms, restricted to publication years 2010 through 2025. AI terms covered artificial intelligence, machine learning, deep learning, neural networks, natural language processing, large language models, generative AI, and named model families. HEOR terms covered cost effectiveness, cost utility, economic evaluation, decision analytic modeling, budget impact, health technology assessment, real world evidence, comparative effectiveness, patient reported outcomes, utilities, quality adjusted life years, and health care resource utilization. The complete query strings are reproduced in eTable 1 in the Supplementary Appendix.

Records were eligible if they were journal articles, reviews, or conference proceedings published in English between 2010 and 2025 with a retrievable abstract. We excluded editorials, letters, comments, preprints, retracted publications, records without abstracts, non-English records, and records whose registered publication year fell outside the window. Duplicate records were removed on PubMed identifier and normalized title.

To place the included corpus in context we retrieved six annual denominator series from PubMed using the same interface: all indexed publications, all AI in medicine publications, all HEOR publications, the AI and HEOR intersection, AI in evidence synthesis, and AI in reporting and governance, together with a large language model specific series. These are reported in eTable 5. We note one discrepancy honestly. The range form of the query, using a single date range, returned 2,656 records where the sum of the sixteen per year queries was 2,929, a difference of 273. The most likely explanation is PubMed MedlineDate records that span two calendar years and are therefore counted in both per year queries. We used the per year series for trend estimation and the range query for the PRISMA flow, and we report both.

### CLASSIFICATION

Each included record was classified by a deterministic term dictionary applied to the concatenated title, abstract, and MeSH terms. The dictionary assigns eight non-exclusive application domains: economic evaluation; decision modeling and simulation; evidence synthesis; real-world data and causal inference; outcome and cost prediction; patient-reported outcomes and preferences; HTA, payer, and market access; and governance, reporting, and validity. It separately assigns a single most specific method category from six: generative AI and large language models; natural language processing before the generative era; deep learning; classical machine learning; artificial intelligence unspecified; and no AI method term identified. Domain labels are non-exclusive because a single paper frequently reports, for example, a natural language processing pipeline used to construct a cohort for a cost outcome. The full dictionary, with every term and its label, is given in eTable 2.

### VALIDATION OF THE CLASSIFIER

A dictionary is fast, transparent, and reproducible, and it is also wrong in ways that are invisible unless measured. We therefore drew a simple random sample of 300 of the 2,476 included records and had an independent large language model classifier, blinded to the dictionary output and given only the title and abstract, answer two questions: whether the record was genuinely relevant to health economics and outcomes research as a practitioner would define it, and which of the same eight domains and six method categories applied. Prompts and raw outputs are archived in the replication package.

We report, for every label, the number assigned by each classifier, observed agreement, Cohen kappa, prevalence-adjusted bias-adjusted kappa (PABAK), and the precision, recall, and F1 of the dictionary treating the blinded classifier as the reference. We report PABAK alongside kappa because kappa is unstable at extreme prevalence and several labels are rare. We also report search precision, defined as the proportion of sampled records judged genuinely HEOR relevant, with an exact binomial 95% confidence interval, and a precision-adjusted corpus size obtained by applying that proportion and its interval to the full included count. We treat the blinded classifier as a reference standard, not as truth, and we discuss the consequences of that choice in the Limitations section.

### NARRATIVE EVIDENCE REVIEW

Alongside the bibliometric review we assembled a source grounded evidence base on five questions: the regulatory and HTA position; the measured performance of AI in each HEOR workflow; adoption, workforce, and transparency; industry deployment and market access; and the economics of AI as it bears on this field. For regulatory and policy content we used primary agency documents only, retrieved directly from the issuing body, including the FDA device authorization list, which we downloaded in full as a 1,614 row file and tabulated by review panel and decision year. For performance content we required a primary study reporting a quantitative metric. For company reported efficiency figures we retained the figure and labelled its provenance explicitly, distinguishing peer reviewed evidence, vendor co-authored preprints, conference abstracts, and press releases. Where a figure could not be confirmed from a retrieved page we recorded it as not available rather than estimating it.

### REFERENCE VERIFICATION

Every DOI cited in this manuscript was resolved programmatically against the Crossref REST application programming interface, with a DataCite fallback for preprint and dataset identifiers, and the returned author list, journal, volume, issue, pages, and year were used to build the reference list. Of 173 candidate DOIs, 172 resolved and were verified; one did not resolve and was removed from the manuscript rather than cited. Grey literature without a DOI, including agency guidance, position statements, conference posters, and press releases, is cited with the issuing organization, date, and uniform resource locator. The verification log and the full verified reference library are provided as eTable 20 and in the replication package. We adopt this procedure not as a courtesy but because citation fabrication is now a documented failure mode of the tools this paper is about^27,28^.

### STATISTICAL ANALYSIS

Counts are reported with percentages of the relevant denominator. Confidence intervals for proportions are exact binomial (Clopper-Pearson). Agreement statistics are as defined above. Growth is expressed as a ratio of endpoint counts and, where a rate is more informative, as a compound annual growth rate. No hypothesis tests are reported for the bibliometric series because the series are complete counts rather than samples. Analyses were conducted in Python 3.11 with pandas, scikit-learn, and matplotlib; version numbers are pinned in the replication package.

## Results

### THE SIZE AND SHAPE OF THE LITERATURE

The search identified 2,642 records. After removal of 14 duplicates, 2,628 records were screened and 152 were excluded: 70 without a retrievable abstract, 38 not published in English, 19 editorials, 10 preprints, 7 letters, 4 retracted publications, and 4 with a registered publication year outside the window. This left 2,476 included records. Figure 1 presents the PRISMA-ScR flow diagram and Table 1 summarizes the corpus.

Annual output rose from 29 records in 2010 to 852 in 2025, a factor of 29.4, with the inflection at 2018 to 2019 rather than at the release of ChatGPT. The series was 29, 28, 47, 31, 34, 24, 23, 36, 48, 91, 130, 163, 232, 270, 438, and 852 for 2010 through 2025 respectively. The largest single year increase in absolute terms was 2024 to 2025, an addition of 414 records, and the largest proportional increase was 2018 to 2019, a rise of 89.6%. Figure 2 shows the annual series against its denominators.

Two ratios matter more than the raw count. AI containing publications reached 6.0% of all indexed HEOR output in 2025, having been 0.8% in 2010. Over the same period HEOR fell to 0.86% of all indexed medical AI output, from 0.70% in 2010 with an intervening peak. In other words, AI is becoming a normal feature of health economics far faster than health economics is becoming a recognized destination for AI research. The asymmetry is large: in 2025 PubMed indexed 110,494 AI in medicine records against 15,641 HEOR records, and the intersection was 945 by the denominator query and 852 after our screening. For the field's methodological standards, that asymmetry means HEOR will be a consumer of externally developed tools far more often than a producer of them, and will therefore inherit validation practices set elsewhere.

Domain composition is reported in Table 1 and mapped in Figure 3. Economic evaluation was the most frequently assigned domain, appearing in 1,559 of 2,476 records (63.0%), followed by real-world data and causal inference (496, 20.0%), governance, reporting, and validity (494, 20.0%), outcome and cost prediction (393, 15.9%), evidence synthesis (283, 11.4%), HTA, payer, and market access (209, 8.4%), decision modeling and simulation (115, 4.6%), and patient-reported outcomes and preferences (76, 3.1%). Two hundred seventy eight records (11.2%) carried no domain term. Method composition was artificial intelligence unspecified in 682 records (27.5%), classical machine learning in 615 (24.8%), deep learning in 445 (18.0%), no identifiable AI method term in 445 (18.0%), generative AI or large language models in 159 (6.4%), and pre-generative natural language processing in 130 (5.3%).

The generative series deserves separate comment because it is the one everyone is arguing about. It is empty before 2021, then 1, 4, 13, 38, and 103 records for 2021 through 2025. Growth is steep, and the level is low: even in 2025 generative AI appeared in 103 of 852 records, 12.1% of that year's output. Meanwhile the fastest growing domain label in absolute terms was governance, reporting, and validity, which rose from 82 records in 2024 to 237 in 2025. The field is currently writing more about how to govern these tools than it is publishing applications of them, which is either encouraging or an indication that the applications are happening where they are not indexed.

Publication venues were highly dispersed. The 2,476 records appeared in more than 900 distinct journals. The most frequent were Scientific Reports (79 records, 3.2%), Sensors (60, 2.4%), Cureus (43, 1.7%), Journal of Medical Internet Research (41, 1.7%), BMJ Open (36, 1.5%), PLoS One (35, 1.4%), Value in Health (32, 1.3%), Journal of Clinical Medicine (27, 1.1%), and npj Digital Medicine (26, 1.1%). The single most important observation here is that the field's own specialty journal, Value in Health, accounts for 1.3% of the corpus. The literature that HEOR practitioners will be asked to appraise is overwhelmingly published outside HEOR venues and therefore reviewed by people who do not routinely apply HEOR reporting standards. eTable 6 lists the 40 most frequent journals.

Study designs were correspondingly weak on the dimensions HTA reviewers care about. Of 2,476 records, 2,471 were indexed as journal articles, 674 (27.2%) as reviews, 121 (4.9%) as systematic reviews, 91 (3.7%) as comparative studies, 42 (1.7%) as scoping reviews, 38 (1.5%) as randomized controlled trials, 27 (1.1%) as meta-analyses, and 17 (0.7%) as validation studies. Thirty eight randomized trials in a corpus of 2,476 is 1.5%, and 17 validation studies is 0.7%. eTable 7 gives the full distribution.

### WHAT VALIDATION REVEALS

The blinded independent classification of 300 randomly sampled included records produced the most consequential result in this review, and it is not a flattering one.

Only 154 of 300 sampled records (51.3%, 95% CI 45.7 to 56.9) were judged genuinely relevant to health economics and outcomes research. Applying that proportion to the full corpus gives a precision-adjusted estimate of 1,271 genuinely HEOR relevant studies (95% CI 1,131 to 1,410) rather than 2,476. Precision was 52.4% (95% CI 46.5 to 58.3) among the 271 sampled records to which the dictionary had assigned at least one domain and 41.4% (95% CI 25.5 to 59.3) among the 29 to which it had assigned none, so the dictionary carries signal, but not nearly enough of it. Table 2 and Figure 4 report the full validation results, and eTable 9 gives the stratified precision.

Per label agreement was heterogeneous in a way that maps almost exactly onto how well specified each concept is. Agreement was substantial for real-world data and causal inference (Cohen kappa 0.729, observed agreement 90.3%, F1 79.1%) and moderate to substantial for evidence synthesis (kappa 0.666, 92.3%, F1 70.9%), decision modeling and simulation (kappa 0.579, 94.0%, F1 60.9%), HTA, payer, and market access (kappa 0.576, 94.0%, F1 60.9%), and governance, reporting, and validity (kappa 0.546, 84.3%, F1 64.7%). It was fair for outcome and cost prediction (kappa 0.453, 85.7%, F1 53.8%) and poor for patient-reported outcomes and preferences (kappa 0.306, 93.3%, F1 33.3%). Method classification agreed at kappa 0.667 across six categories and the generative AI flag agreed at kappa 0.674 with 97.0% observed agreement.

The exception is the finding that should change how bibliometric claims about this field are read. For economic evaluation, the largest and fastest growing label in the corpus, Cohen kappa was 0.144 with observed agreement of 51.7% and PABAK of 0.033. The dictionary assigned this label to 186 of 300 sampled records; the blinded classifier assigned it to 69. Dictionary precision against the blinded reference was 29.6% with recall 79.7%. In plain terms, the term dictionary treats any paper that mentions cost, resource use, or efficiency as an economic evaluation, and roughly seven in ten of those are not economic evaluations in the sense a reimbursement reviewer would use.

This has three implications that we carry into the Discussion. First, our own headline count of 1,559 economic evaluation records should be read as an upper bound with an implied true value near 574 by the precision ratio, and any published bibliometric claim about the growth of AI in health economic evaluation that does not report a measured classification error rate should be treated as an upper bound too. Second, the labels that a keyword classifier handles best, real-world data and evidence synthesis, are precisely the workflows where AI is being deployed operationally, so the operational picture is better measured than the inferential one. Third, and most usefully, the ranking of kappa values is a diagnostic of conceptual clarity in the field itself. Real-world data and causal inference has a shared vocabulary and scores well. Patient-reported outcomes and preferences does not, and scores worst.

### EVIDENCE SYNTHESIS: THE BEST MEASURED WORKFLOW

Evidence synthesis is where the performance evidence is strongest, and it is also where the strongest evidence is most consistently misread.

On title and abstract screening, the best result in the literature is Matsui and colleagues, who applied GPT-4 to 1,381 and 3,146 record sets and reported adjusted sensitivity of 0.962 and specificity of 0.996, processing about 110 records per minute at a cost of US$59^29^. That result has not been reproduced at scale by independent teams. Tran and colleagues applied large language models to 22,665 citations and reported sensitivity between 81.1% and 96.5% but specificity between 25.8% and 80.4%, generating 10,279 false positives out of 22,665 citations in the worst configuration^30^. Oami and colleagues, on 16,669 citations, reported GPT-4 sensitivity of 0.85 and specificity of 0.98 but a median specificity gap of 0.48 across reviews^31^. Khraisha and colleagues found GPT-4 sensitivity of 0.42 with kappa 0.34 against human reviewer kappa of 0.77^32^. Nykvist and colleagues, screening 11,984 records, reported work saved over sampling of 0.55 and about 75% of screening effort saved at recall above 95%^33^.

Read together, these five studies say something specific and actionable: sensitivity is usually acceptable, specificity is unstable across topics, and the variance between reviews is larger than the difference between models. That is the profile of a tool that can be used as a second screener with human adjudication and cannot be used as a sole screener. It is also exactly the conclusion reached by the joint position statement of Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence^34^, and it is why the ISPOR agentic framework for HEOR literature review reports screening F1 between 0.917 and 0.977 with human agreement kappa between 0.844 and 0.906 under a human in the loop design rather than an autonomous one^35^.

Data extraction performs better than screening. Gartlehner and colleagues extracted 160 items with Claude 2 at 96.3% accuracy^36^. Liu and colleagues reported 94.8% accuracy at 88 seconds per randomized trial^37^. The most informative study is Lai and colleagues, who ran 12,814 extractions across 107 randomized trials and found Claude 3.5 at 96.2% accuracy against human extractors at 95.3% and human extraction assisted by the model at 97.9%, with extraction time falling from 86.9 minutes to 14.7 minutes^38^. The point is not that the model beat the humans, since the difference is inside plausible noise. The point is that the combination beat both, and that the time saving is real and large.

Automation of the downstream analytic steps is now documented as well. Reason and colleagues had GPT-4 write 30 R scripts to replicate published cost effectiveness models; in the non-small cell lung cancer set 14 of 15 scripts were error free, and every error free script reproduced the published incremental cost effectiveness ratio to within 1%, for example US$117,600 against a published US$117,739, and CHF107,284 against a published CHF108,326^39^. The same group reported greater than 99% extraction accuracy for network meta-analysis inputs^40^. A systematic review of generative AI in health economic evaluation screened 2,322 records and included 25 studies, of which 92% were conference abstracts, 92% appeared in 2024, and 96% were company authored^41^. That composition is the finding.

The economic case rests on a smaller base than the enthusiasm suggests. Abogunrin and colleagues reviewed 25 studies and found 17 reporting time reductions above 50%, with savings between 36.0% and more than 99.0%, and cited a per review cost above US$141,000 in the United States^42^. That per review figure traces to Michelson and Reuter, who estimated US$141,194.80 per systematic review and annual review expenditure of US$16.8 million per pharmaceutical company and US$18.7 million per academic institution^43^. Against those numbers, an ISPOR time and motion study of 234 publications is the most honest comparison available: a hybrid human and AI workflow achieved 97.0% accuracy with 80.6% recall and 51.4% time savings, a fully automated workflow achieved 81.1% time savings but recall of only 48.4%, and unaided humans achieved 90.1% accuracy with 88.7% recall. A workflow that misses half the eligible evidence is not 81% cheaper. It is a different study.

### REAL-WORLD DATA AND CAUSAL INFERENCE

This is the domain our validation ranked most coherent, and it is also the domain where the evidence most directly contradicts the intuition that better prediction yields better inference.

The foundational result is Schneeweiss and colleagues on high dimensional propensity scores, in which the estimated relative risk in a cohort of 49,653 users moved from 1.09 crude to 0.94 with fifteen investigator specified covariates and to 0.88 with 500 algorithmically selected covariates^44^. A subsequent application found the conventional propensity score estimate of 0.84 (95% CI 0.56 to 1.26) becoming 0.62 (95% CI 0.43 to 0.91) under the high dimensional approach, which is to say the qualitative conclusion changed. Guertin and colleagues examined performance under unmeasured confounding^45^, Pang and colleagues brought targeted maximum likelihood estimation into pharmacoepidemiology^46^, and Benasseur and colleagues showed the failure mode plainly: high dimensional propensity score weighting produced bias of 0.094 with 23.6% confidence interval coverage where a modified procedure achieved bias of 0.018 with 91.4% coverage^47^. Coverage of 23.6% for a nominal 95% interval is not a subtle problem.

The machinery is mature. Targeted maximum likelihood estimation^48^, super learning^49^, causal forests^50^, and double or debiased machine learning^51^ are all in routine use, and their translation into HEOR has been mapped: causal forests for heterogeneity in cost effectiveness analysis^52^, machine learning for individualized treatment effects in medical decision making^53^, integration of decision modeling with machine learning based causal estimation^54^, a scoping review of 1,743 screened records yielding 74 studies of heterogeneous treatment effect estimation with real-world data^55^, and transportability methods for moving estimates between populations^56-58^.

What the field lacks is not method but calibration of expectations, and the clearest demonstration is a trial emulation. Wang and colleagues emulated PARADIGM-HF in Veterans Affairs data, where the randomized trial hazard ratio was 0.81 (95% CI 0.61 to 1.06). A logistic propensity score model with area under the curve of 0.79 yielded a hazard ratio of 0.93. A gradient boosted model with area under the curve of 0.95 yielded 0.61^59^. The model with the best discrimination produced the estimate furthest from the trial benchmark. This is not a paradox once stated carefully: propensity score models are not prediction problems, and optimizing separation of treated from untreated can degrade the covariate balance that identification actually requires. It is, however, precisely the inference a reviewer would draw from an area under the curve reported without a balance diagnostic, and it is why the FDA's guidance on real-world data explicitly declines to endorse any specific AI technology^60^ and why the target trial framework has been recommended as the organizing discipline for real-world evidence^61^. The PALISADE checklist was written for exactly this failure mode^20^, and empirical work in the health economics literature has estimated that a material fraction of database studies can switch direction of statistical significance under defensible alternative specifications.

### UNSTRUCTURED DATA AND AI DERIVED ENDPOINTS

Approximately 80% of clinical data is unstructured, and this is the strongest affirmative case for AI in HEOR^62^. The gains are not marginal. Social and behavioral determinants recorded in claims at prevalences between 0.03% and 8.3% were recorded at between 1.40% and 36.3% once notes were processed, with walking difficulty rising from 10.7% to 38.0% and lack of social support identifiable only from text in 99.8% of cases^63^. In an oncology cohort, 44 of 48 patients (91.7%) with adverse social determinants documented in text had no corresponding Z code^64^. Fewer than 2% of inpatient hospitalizations carried a Z coded diagnosis at all^62^.

Performance on specific extraction tasks is good and uneven. Xu and colleagues, across 79,698 patients and 495,862 notes, achieved area under the receiver operating characteristic curve of 0.95 for Eastern Cooperative Oncology Group performance status and found that imputed poor performance status in notes lacking an explicit score carried a hazard ratio of 11.9^65^. A Veterans Affairs implementation reported 98.5% accuracy^66^, programmed death ligand 1 extraction reached micro F1 of 0.925^67^, and Optum's oncology natural language processing model reported precision of 98.8% and recall of 92% for stage value but recall of only 79% for correctly linking histology to neoplasm^68^. In another cancer registry task, T stage extraction reached F1 of 0.89 while M stage reached 0.24^69^. The pattern is that the variable a cohort definition depends on is often the variable extracted worst.

Two studies show why this matters for an estimate rather than for a metric. Varma and colleagues derived real-world progression free survival two ways in the same cohort and obtained 30 months from radiology reports against 23 months from clinical notes^70^. In their metastatic breast cancer cohort of 316 patients, sentence level progression capture accuracy was 98.2% and patient level initial progression was captured within 30 days with 88% accuracy, yielding median real-world progression free survival of 20 months (95% CI 18 to 25), against 25 months (95% CI 15 to 35) by manual curation in a 100 patient validation subset and 22 months (95% CI 15 to 35) by the computational workflow^70^. A seven month difference in a median attributable to which document type was read is a difference that changes a cost effectiveness result. Separately, adding natural language processing features raised propensity score model area under the curve from 0.66 to 0.77 and from 0.80 to 0.89 while the estimated hazard ratios barely moved, which is the same lesson as the PARADIGM-HF emulation in a different guise.

Vendor validation frameworks have begun to respond. Flatiron Health published the VALID framework, which requires variable level benchmarking against expert human abstraction, internal consistency and plausibility checks, replication against human abstracted or external standards, and subgroup stratified bias assessment^71^, and states that every large language model enabled data set is subject to it^72^. Its human abstracted real-world response variable, the reference standard for the machine learning work that followed, reported inter-abstractor agreement of 0.94 (95% CI 0.92 to 0.96) on presence of an assessment and 0.82 (95% CI 0.78 to 0.86) on best confirmed response category, at a median abstraction time of 15.0 minutes per patient line, and Spearman correlation of 0.99 between real-world response rates in 12 cohorts and trial objective response rates^73^. The scaled machine learning version correlated with human abstraction at r = 0.86 in a test subset of 4,047^74^. A cross tumor evaluation reported F1 similar to expert abstractors and nearly identical progression free survival estimates without disclosing the numbers^75^. Verantos and coauthors from Amgen, Johnson and Johnson, and GSK reported recall improving from 49.9% to 93.2%, precision from 73.6% to 93.5%, and completeness from 46.1% (95% CI 38.2 to 54.0) to 96.6% (95% CI 85.8 to 107.4) when an AI augmented approach replaced a traditional one^76^. We note that a reported confidence interval with an upper bound of 107.4% for a proportion is itself a reporting problem, and that all three of these validation efforts are authored by parties with a commercial interest in the result. Truveta's 92% accuracy figure appears only in a conference deck^77^, and no peer reviewed validation of Tempus derived HEOR variables was located.

The decisive gap is regulatory. FDA has accepted electronic health record derived real-world data in a label expansion, approving palbociclib for men with hormone receptor positive, human epidermal growth factor receptor 2 negative advanced breast cancer on the basis of records from three databases^78^. That establishes acceptance of an electronic health record derived source. It does not establish acceptance of an AI derived endpoint. We were unable to document a single instance of any regulator or HTA body explicitly accepting or rejecting an AI or natural language processing derived endpoint as such. For a pharmaceutical sponsor deciding whether to build a submission on real-world progression, that absence is the single most important fact in this review.

### DECISION MODELING AND SIMULATION

This is the smallest domain in the corpus (115 records, 4.6%) and it contains the cleanest efficiency results, because the tasks are computational rather than inferential.

Metamodeling reduced an expected value of partial perfect information calculation requiring 12.5 million model runs from more than 1,000 days of brute force computation to about two days, a roughly 500 fold reduction^79^. Automated model coding replicated published incremental cost effectiveness ratios to within 1% as described above^39^. The ISPOR working group report on generative AI for HTA sets out where these tools plausibly help and where they do not^11,80^, drawing on evidence that large language models can support systematic review tasks^81,82^.

The structural point is that decision modeling is the part of HEOR where uncertainty is already formalized, and therefore the part where AI is most easily disciplined. Otten and colleagues catalogued 80 methods for assessing uncertainty in decision analytic models, nearly all of which presuppose that the uncertainty has been quantified^83^. That presupposition is what an opaque model breaks. Structural uncertainty characterization^84^, value of information analysis^85-88^, and the requirement in CHEERS 2022 that inputs and their sources be reported^89^ together define what an AI assisted model must still deliver. A model whose parameter provenance cannot be traced cannot be subjected to any of them.

### SYNTHETIC DATA AND EXTERNAL CONTROL ARMS

Synthetic data is where the promise is largest and the reporting is weakest.

The utility evidence is genuine. A model trained on synthetic electronic health records performed only 0.026 lower in area under the curve than one trained on real records. D'Amico and colleagues generated synthetic data for 7,133 patients with clinical fidelity of 93% and genomic fidelity of 90%, and constructed a synthetic control arm of 187 luspatercept matched patients^90^. Elvatun and colleagues examined synthetic data as external control arms in scarce single arm trials^91^. Wang and colleagues built AI generated digital twins from 6,736 subjects in Alzheimer disease^92^, in which 6,236 of 6,728 subjects with recorded race were White and 152 were Black, a composition that determines what the resulting synthetic population can be used to claim.

Generator choice dominates the result. Akiya and colleagues compared techniques for control arm simulation and found that classification and regression tree based generation produced synthetic data sets whose median progression free survival fell inside the real 95% confidence interval in 88.8% to 98.1% of replicates, against 6.5% to 37.8% for a conditional tabular generative adversarial network^93^. A generator that recovers the target quantity in 6.5% of replicates is not a lower quality version of one that recovers it in 98%; it is unusable for that purpose, and nothing in the summary statistics of the synthetic data would tell you which one you had.

Reporting has not kept pace. Kaabachi and colleagues reviewed 73 studies and found that 70 (95%) evaluated utility while only 31 of 67 (46%) that claimed a privacy purpose evaluated privacy, and only 8 of 73 (11%) used a differentially private generator^94^. A literature that markets privacy and measures utility is inviting exactly the regulatory response it will get.

The regulatory record on external controls is more informative than the synthetic data literature acknowledges. Jahanshahi and colleagues identified 45 FDA approvals between 2000 and 2019 that accepted external control data, of which 36 (80%) were in rare disease, and none of the 45 used prospectively collected natural history controls^95^. Yin and colleagues examined the statistical potential and limits of the approach for regulatory purposes^96^. And in its qualification opinion on prognostic covariate adjustment, the EMA Committee for Medicinal Products for Human Use stated that excluding dropout data "would not be acceptable for regulatory purposes"^97^. That is the clearest available signal of how a European regulator will reason about a model based control: the model may be qualified, and the analysis population still has to be complete.

### THE ECONOMIC EVALUATION OF AI ITSELF

HEOR is being asked to evaluate AI, and has barely done so. El Arab and colleagues systematically reviewed cost effectiveness and budget impact analyses of AI in health care from 2020 through 2024 and found 19 economic evaluations, with CHEERS scores between 21 and 27 of 28^98^. Nineteen evaluations, against 1,614 authorized AI enabled devices, is the field's most direct self indictment.

The evaluations that exist are instructive. Yala and colleagues developed risk based breast cancer screening^99^, and Mital and Nguyen estimated an incremental cost effectiveness ratio of US$23,755 per quality adjusted life year in 2020 US dollars for AI versus polygenic risk scores in breast cancer risk stratification, with an AI cost threshold of US$318 per mammogram^100^. Huang and colleagues reported US$1,107.63 per quality adjusted life year from the health system perspective and US$10,347.12 from the societal perspective for an AI intervention^101^. Against these, Vargas-Palacios and colleagues modelled AI in the UK breast screening programme and found a scenario in which no price per scan made the technology cost effective^102^. That result is the one to hold onto: for a diagnostic AI, cost effectiveness is frequently determined by the downstream care pathway rather than by the price of the algorithm, so a procurement negotiated on price per scan is negotiating the wrong parameter. Hendrix and colleagues set out the framework for valuing clinical decision support that makes this explicit^103^, and Kalavadekar and colleagues illustrate the reinforcement learning variant of the problem in tuberculosis screening^104^.

### THE REGULATORY RECORD

The FDA's position is the most developed and the least finished. Table 3 summarizes the instruments now in force or in draft.

For drugs and biologics, the January 2025 draft guidance proposes a seven step credibility assessment framework in which a sponsor defines the question of interest, the context of use, and the model risk, then establishes credibility proportionate to that risk^4^. The definition of model risk is the operative sentence: "Model risk is a combination of two factors: (a) model influence... and (b) decision consequence." Two features of the guidance are routinely missed. It explicitly excludes AI used in drug discovery and in operational efficiencies, so the majority of publicly announced pharmaceutical AI deployments fall outside it. And it remains a draft as of September 2026, with the comment period closed on 7 April 2025. The agency's own account of the evidence behind it names an FDA sponsored workshop convened by the Duke Margolis Institute for Health Policy in December 2022, more than 800 comments from 65 entities on two discussion papers published in May 2023, and experience with more than 500 submissions containing AI components since 2016^1,105^. PhRMA's comments asked the agency to clarify which device guidance provisions apply, to explain how human in the loop mitigation affects the risk assessment, to acknowledge that the seven steps are interrelated and iterative, and to address models composed of multiple models^106^. Those four requests are a fair summary of what the framework does not yet answer.

For devices, the record is quantitative. We downloaded the FDA AI enabled medical device list in full: 1,614 authorizations current as of 4 September 2026, of which 1,230 (76.2%) are in radiology, 154 (9.5%) in cardiovascular, and 73 (4.5%) in neurology, rising from 18 authorizations in 2016 to 335 in 2025 and 181 in the first eight months of 2026^7^. eTable 16 gives the full panel by year matrix. The January 2025 draft guidance on AI enabled device software functions asks for validation at "at least three geographically diverse US clinical sites" with two sided 95% confidence intervals^107^, and the Digital Health Advisory Committee met on 20 and 21 November 2024 specifically on generative AI enabled devices^108^. The concentration in radiology is the number a health economist should notice: three quarters of authorized AI in American medicine operates in one specialty, which means the cost effectiveness literature reviewed above is being asked to generalize from a very narrow deployment base.

The agency is also now a user. Elsa was deployed agency wide in June 2025 on a FedRAMP High environment, with the explicit statement that it does not train on data submitted by regulated industry^109^, and the FDA has appointed a Chief AI Officer. A regulator that uses these tools internally will develop views about their failure modes faster than a regulator that only reviews them.

The European position is more prescriptive on one dimension. The EMA reflection paper states that "the use of transparent models is preferred"^110^, a preference NICE echoes in requiring that where more explainable methods are potentially robust "those should be presented in the first instance, with supplementary use of less transparent approaches"^19^. The EU AI Act entered into force on 1 August 2024 with general purpose AI obligations applying from 2 August 2026^111^, and EFPIA has argued that AI used solely for medicines research and development is exempt under Recital 25 and Articles 2.6 and 2.8^112^. Industry association frameworks converge on similar content: six IFPMA AI ethics principles^113^, six EFPIA recommendations^112^, and company level commitments at Novartis^114^ and Roche^115^.

Payer side regulation has moved faster than either. CMS stated in February 2024 that "algorithms or artificial intelligence alone cannot be used as the basis to deny admission" in Medicare Advantage^116^, and California enacted Senate Bill 1120 requiring physician review of medical necessity determinations^117^. The World Health Organization's guidance on large multi-modal models notes hallucination rates of "at least 3 percent" and "as high as 27 percent"^118,119^. The asymmetry is worth stating plainly: the use of AI to deny care is now regulated in US statute, while the use of AI to generate the evidence that determines whether care is covered at all is governed by voluntary position statements.

### THE HTA RECORD

Table 4 sets the claims against the record.

NICE published its position statement on 15 August 2024, requiring demonstrable value, a preference for explainable methods, justification of assumptions using instruments such as PALISADE, and naming algorithmic bias, cybersecurity, and reduced human oversight as the principal risks^19^. Canada's Drug Agency followed in April 2025, drawing explicitly on NICE, permitting large language model generated search strategies, automated screening and extraction, model generated meta-analysis code, and synthetic data and external control arms subject to transparent reporting, and framing the whole under augmentation rather than replacement^21,120^. IQWiG's General Methods version 8.0 is the German reference^121^, and ICER and the Peterson Health Technology Institute have set out an assessment approach for digital health^122^.

The workload argument for AI is real. Regulation (EU) 2021/2282 entered into force on 11 January 2022 and applies from 12 January 2025 for new oncology active substances and advanced therapy medicinal products, from 13 January 2028 for orphan medicinal products, and from 13 January 2030 for all other products in scope^123,124^. Sponsors must submit the summary of product characteristics and clinical overview to the HTA secretariat simultaneously with the marketing authorization application^125^. The HTA Coordination Group estimated approximately 50 joint clinical assessments of medicines and approximately 5 of medical devices for 2026, with 12 assessments ongoing and 14 countries involved at the time of a December 2025 Commission presentation^126,127^. A doubling of dossier volume with no increase in HEOR headcount is the strongest business case for automation anyone has.

And yet the disclosed use remains three documents out of 1,391, at NICE technology appraisals TA1154 for AI assisted study screening, TA1071 for AI assisted ad hoc literature searches to identify treatment effect modifiers, and TA962 for a natural language processing approach, with no explicit reporting in any Canada's Drug Agency or IQWiG dossier^12^. A separate audit of 1,309 screened records yielded 37 records of AI in HTA submissions and agency practice, distributed across Canada's Drug Agency (7), HAS (6), NICE (6), IQWiG (6), FIMEA (4), NIPH (3), EUnetHTA (2), KCE (1), PBAC (1), and INESSS (1), and reported that seven agencies are adopting AI internally with NICE recording 49 AI initiatives across 25 HTAs^128^. Agencies are adopting faster than submitters are disclosing.

Conference activity confirms both the volume and the concentration. Of 28,184 abstracts submitted to ISPOR and ISPE between 1 January 2020 and 6 December 2024, 1,153 addressed AI, with 89% of applications in systematic literature review automation and 9% in economic modeling, and affiliations split between contract research organizations (44%), academia (40%), and pharmaceutical companies (16%)^129^. A separate review of 152 AI in HEOR articles found publications rising from 5 in 2020 to 46 in 2024^130^. An earlier scoping review of AI tools in HTA found 61 publications, the first in 2006, with 72% from Canada, the United States, or the United Kingdom, and evidence synthesis in 96%^131^.

### THE INDUSTRY RECORD

For a pharmaceutical reader the relevant question is not whether these tools work but whether the reported gains are the kind a budget can be built on. Table 4 and eTable 17 present the claims with their provenance labelled.

Reported reductions in regulatory writing time span Pfizer at 40% faster first draft clinical study reports and a 15% shorter manuscript submission timeline^132^, Merck at 180 hours to 80 hours per fully human reviewed first draft with errors reduced by 50%^133^, Novo Nordisk at more than ten weeks to ten minutes for clinical study documentation with a 90% reduction in clinical study report writing time^134^, Takeda at a projected halving of a 20 week analysis and tabulation process^135^, and a Takeda and Weave Bio preprint at a 97% reduction, from about 100 hours to 3.7 hours for 18,870 pages across 61 source documents in one investigational new drug application and to 2.6 hours for 11,425 pages across 58 documents in a second^136^. Certara's white paper states the baseline that all of these are measured against, about 120 hours of regulatory writing over four weeks and an average of 83 days from database lock to an approved clinical study report, without reporting a time saving for its own product^137^.

Every one of those figures is reported by the party deploying or selling the tool. None has been independently replicated. The most methodologically explicit of them, the Weave and Takeda preprint, compares against a historical estimate with no concurrent control and an n of two. Elsewhere in the development pipeline, Novartis reported a site selection process falling from four to six weeks to a two hour meeting for a 14,000 patient cardiovascular outcomes trial that closed enrolment 13 patients above target, and GSK reported approximately £8 million saved in late stage asthma studies^138^. Enterprise commitments are large and recent: Merck and Google Cloud at up to US$1 billion^139^, Eli Lilly and NVIDIA at more than 1,000 B300 graphics processing units^140^, Tempus with AstraZeneca and Pathos at US$200 million in data licensing and model development fees^141^, Moderna targeting complete generative AI adoption within six months^142^, and Sanofi's plai platform^143^.

On the market access side the quantified evidence reduces to a single conference abstract. A retrieval augmented generation multi-agent pipeline built on Claude 3.7 Sonnet, ingesting 110 documents and generating sections per AMCP Format version 5.0, produced a draft reported as approximately 90% complete with approximately 80% less development time and 70% to 75% lower cost, while the authors themselves noted repetition in all sections and subject matter experts who only somewhat agreed that responses were largely complete^144,145^. For payer landscape monitoring, vendor claims are unaudited: Norstella states policy and formulary alerts within 24 to 48 hours and analysis in minutes rather than weeks^146^, and IQVIA's market access product page reports no quantitative figures at all^147^. For pricing, gross to net, contracting analytics, and international reference pricing we located no primary source with a measured, attributable efficiency or accuracy figure. That absence is itself a finding.

Against the efficiency claims stand the failures. DSP-1181, presented as the first AI designed drug when it entered the clinic in January 2020, was abandoned by Sumitomo in January 2022 for failing to meet study criteria, and EXS-21546 was discontinued after modelling suggested a suitable therapeutic index would be difficult to reach; Exscientia, BenevolentAI, and Recursion had accumulated a combined deficit above US$1.5 billion^148^. Recursion subsequently deprioritized three clinical stage programmes including REC-994, whose 62 patient phase 2 trial showed a trend toward reduced lesion volume on imaging but no improvement on patient reported outcomes or physician led measures at 12 months^149^. Independent analyses of AI discovered molecules report phase 1 success of 80% to 90% and phase 2 success of approximately 40%^150^, against historical benchmarks of 13.8% overall probability of success from phase 1 to approval and 3.4% in oncology across 406,038 trial entries and 21,143 compounds^151,152^. Counts of AI discovered candidates in trials range from 31 across eight leading companies^153^ to 117 assets across 63 companies in a 2026 industry wide analysis^154^, against a total clinical pipeline of several thousand. The comparison that matters for a health economist is that phase 2 is where efficacy is tested, and phase 2 success for AI discovered molecules is at the historical average. The cost per approved drug against which any of this must be judged is US$2,558 million capitalized pre-approval in 2013 dollars^155^ or a median of US$985.3 million (95% CI 683.6 to 1,228.9) in 2018 dollars^156-158^.

### FAILURE MODES

Four failure modes are documented well enough to be treated as expected rather than exceptional.

Bias in deployed algorithms. Obermeyer and colleagues showed that a commercial risk algorithm applied to approximately 200 million Americans, by using cost as a proxy for need, identified 17.7% of Black patients for extra help where correcting the target would have identified 46.5%^159^. The mechanism was label choice, not model class, which is why it is a HEOR problem: the outcome variable was a health economics variable.

Weak external validity. The Epic sepsis model, evaluated externally across 38,455 hospitalizations, achieved area under the curve of 0.63 (95% CI 0.62 to 0.64) with positive predictive value of 12% and number needed to evaluate of 8 at hospitalization and 109 at four hours, against a vendor reported range of 0.76 to 0.83^160^. High risk of bias is the norm rather than the exception in this literature^22,23^.

Post deployment decay. Rahmani and colleagues documented data drift across 112,972 encounters^161^, and Kopanitsa found across four deployed clinical AI systems that calibration degraded earlier and more consistently than discrimination^162^. For HEOR this is the crux, because a cost effectiveness result depends on calibration, not on ranking. A model that still discriminates well and no longer calibrates will keep passing the metric that is monitored and stop supporting the estimate that is used.

Human factors. Jabbour and colleagues showed in a randomized vignette study of 457 clinicians that a standard AI raised diagnostic accuracy from a baseline of 73.0% by 2.9 percentage points without explanations and 4.4 points with them, while a systematically biased AI lowered it by 11.3 points and 9.1 points respectively, with explanations providing no significant protection^163^. Dratsch and colleagues found experienced radiologists falling from 82.3% to 45.5% accuracy when shown an incorrect AI suggestion^164^, an effect also studied as AI suppression^165^ and trust calibration^166^. Budzyń and colleagues reported adenoma detection rates in non-AI-assisted colonoscopies falling from 28.4% before AI exposure to 22.4% after, a difference of 6.0 percentage points (95% CI 10.5 to 1.6 lower; p = 0.0089; odds ratio 0.69, 95% CI 0.53 to 0.89), in an observational multicentre analysis^167,168^. And Goh and colleagues randomized 50 physicians and found diagnostic reasoning scores of 76% with a large language model against 74% without, an adjusted difference of 2 percentage points (95% CI 4 lower to 8 higher; p = 0.60), while the model alone scored 16 points higher than physicians (95% CI 2 to 30; p = 0.03)^169^. The model beat the physician and beat the physician using the model. Any HEOR workflow that assumes a human reviewer will catch the model's errors is assuming away the best measured finding in this literature.

Fabrication is the failure mode most specific to this manuscript's own methods. Chelli and colleagues assessed 471 references and found hallucination rates of 39.6% for GPT-3.5, 28.6% for GPT-4, and 91.4% for Bard, with the DOI correct in only 16% and 20% of GPT-3.5 and GPT-4 references respectively^27^. Walters and Wilder examined 636 citations and found 55% fabricated by GPT-3.5 and 18% by GPT-4, rising to 70% for book chapters^28^. This has already reached consequential documents. A US federal health policy report cited studies that do not appear to exist, with a listed first author confirming she had never written the paper attributed to her, and the citations were quietly replaced hours after the errors were reported^170^. A filed expert declaration in federal court contained a citation to a nonexistent statistics article^171^, an expert was excluded in a separate federal case for AI hallucinated citations^172^, and one Springer Nature journal retracted 129 papers in the first six weeks of 2025^173^. No equivalent incident has yet been documented inside a drug regulatory or HTA submission. That is the state of the record, not a reassurance.

### TRANSPARENCY, REPRODUCIBILITY, AND WORKFORCE

The baseline is poor before AI is introduced. In a random sample of 200 health economic evaluations, 10 (5%) mentioned access to raw data and analytic code, 112 (56%) reported the data needed to recreate the base case incremental cost effectiveness ratio, and 31 (16%) reported working from a protocol^174^. In healthcare discrete event simulation, 47 of 564 studies (8.3%) cited an openly available model, rising from 4.0% in 2019 to 9.0% in 2022^175^. A systematic database review identified 182 unique open source health economic models, 74% on GitHub and 64% in R^176^. Broader transparency indicators are no better^177,178^. Replication attempts on published models are sobering: of five economic analyses re-implemented, two were fully replicated, two were unequivocally not replicable, and one was potentially replicable but failed in the attempt, with discrepancies even where replication succeeded^179^; four obesity models re-built from 87 identified publications showed cost deviations from 3.9% lower to 16.1% higher and cost utility ratio deviations from 3.0% lower to 17.9% higher^180^.

Disclosure of AI use runs far below reported use. Journals and societies have converged on rules: ICMJE requires disclosure at submission and prohibits AI authorship^181^, COPE states that AI tools cannot be listed as authors^182^, NEJM AI requires disclosure of authoring tools and asks reviewers to disclose AI use and to protect confidentiality^183,184^, JAMA requires the model name, version, manufacturer, and dates of use^185^, Health Affairs requires disclosure in the cover letter and in Methods or Acknowledgements^186^, Elsevier requires a named declaration section^187^, Springer Nature requires documentation in Methods while exempting copy editing^188^, and ISPOR prohibits citing AI as a reference and requires disclosure of AI generated content^189,190^. Against those rules, 0.6% of Lancet submissions in February 2024 declared ChatGPT use and 1.8% declared AI as a research tool^13^, while surveys report use between 25% and 58%: 5,229 respondents to a Nature survey split on acceptability with about a quarter having used AI to edit papers^191^, more than half of about 1,600 academics across 111 countries having used AI in peer review^192^, 81% of 1,692 physicians aware of or using AI in 2026 against 38% using it in 2023^193,194^, and 50% of 150 US healthcare leaders reporting generative AI implementation in Q4 2025 against 25% in Q4 2023^195,196^.

Within HEOR specifically the workforce is not yet equipped. Of 133 HEOR, real-world data, and medical affairs professionals surveyed in April 2026, 61% rated their AI proficiency as basic or very limited and 4% as expert^197^. Among 100 HEOR leaders at 72 companies, 69% personally use AI, 80% say their employer supports it, 29% expect AI to replace some HEOR staff within two years against 47% who disagree, and 59% report that their team does not use AI for any listed HEOR workflow^14^. Medical affairs reports higher confidence than capability, with 86% confident AI will improve efficiency, 20% describing their organization as leading edge, and 49% still using full manual subject matter expert review of every AI generated output^198,199^. Competency frameworks are appearing^200-204^ and can be mapped onto the existing HEOR competency literature^205^, but none is yet HEOR specific. Meanwhile capital has moved: AI enabled startups took 54% of US digital health funding and 50% of deals in 2025, against 37% of funding in 2024^206,207^, 71% of human pharma respondents in a 200 executive survey expect AI budgets to rise over 24 months^208^, and 32% of life sciences leaders expected generative AI budgets of at least US$5 million in 2025 against 20% in 2024^209^. Commercial market forecasts should be read as vendor estimates rather than evidence^210^.

## Discussion

Three findings organize everything else in this review.

The first is a measurement finding. A literature of 2,476 records reduces to approximately 1,271 genuinely HEOR relevant studies (95% CI 1,131 to 1,410) under blinded independent classification, and the label that grew fastest, economic evaluation, is the label our classifier got most wrong (Cohen kappa 0.144). We report this against our own analysis deliberately. The field is now producing bibliometric claims about AI adoption at a rapid rate, and almost none of them report a measured classification error rate. A count without an error rate is a marketing figure. If our dictionary, built specifically for this task and published in full, achieves precision of 29.6% on the single most important label, then keyword based counts of AI in health economic evaluation circulating in conference abstracts and market reports should be read as upper bounds of unknown looseness.

The second is a governance finding, and it is the sharpest contrast in the paper. Adoption claims run at 40% to 97% time savings in pharmaceutical regulatory writing and approximately 80% in payer dossier drafting, while disclosed use in HTA submissions is 3 of 1,391 documents (0.2%) and declared use in journal submissions is 0.6%. There are only three explanations. Either the tools are not actually being used in submission grade work, which the industry evidence makes implausible. Or they are being used and not disclosed, which the survey evidence makes likely. Or the disclosure requirement is understood to apply to authorship rather than to method, so a systematic review screened by a large language model is not thought to require declaration in the way a manuscript drafted by one would be. We believe the third explanation carries most of the weight, and it is fixable, because it is a definitional failure rather than a compliance failure. Current instruments ask whether AI wrote the text. Reviewers need to know whether AI selected the evidence, defined the cohort, extracted the parameter, or generated the code. Those are the operations that move an incremental cost effectiveness ratio.

The third is a methodological finding that recurs in three independent places and should be stated as a rule. In the PARADIGM-HF emulation, a propensity model with area under the curve of 0.95 produced a hazard ratio of 0.61 against a trial value of 0.81, while a weaker model with area under the curve of 0.79 produced 0.93^59^. In the natural language processing augmented propensity work, discrimination rose substantially while the effect estimates barely moved. In drift monitoring across four deployed systems, calibration degraded before discrimination did^162^. The rule is that predictive performance is not evidentiary performance. HEOR quantities are calibrated, counterfactual, and decision relevant, and none of those properties is measured by a receiver operating characteristic curve. A dossier that reports model performance without reporting the sensitivity of the decision to that model has reported the wrong thing.

### WHAT ACEMOGLU'S CRITIQUE MEANS FOR THIS FIELD

Acemoglu's estimate of total factor productivity gains no greater than 0.66% over ten years, roughly 0.064% annually, with GDP effects near 1%, is derived from a task based decomposition rather than from pessimism about model capability^24,25^. His central mechanism is the distinction between easy and hard learning tasks. A task is easy to learn when outcomes are observed, labels are abundant, and feedback is fast. It is hard to learn when the correct answer is not observed. His illustration is clinical: diagnosing a persistent cough is hard because "there is no large, well-curated data set of successful diagnoses and cures."

Health economics is the limiting case of a hard learning task, and the reason is structural rather than technological. The quantity of interest is a counterfactual. No patient is observed under both the treatment and the comparator, so no data set of correct incremental cost effectiveness ratios exists, will exist, or could exist. There is no supervised target. This is why the empirical pattern in our review is exactly what his framework predicts: the measured gains cluster in tasks with observable ground truth, such as extraction accuracy against human abstraction (96.2% against 95.3%)^38^, screening recall against a human reference^35^, code generation against a published result^39^, and computation against brute force^79^. The gains disappear precisely where the label disappears. There is no reported instance of AI improving the accuracy of a cost effectiveness estimate, because accuracy of a cost effectiveness estimate is not measurable.

Acemoglu's second mechanism is task share. Even large improvements on a small share of total task time yield small aggregate gains^211,212^. Applied to HEOR, the clerical layer, screening, extraction, formatting, code drafting, dossier assembly, is where the 40% to 97% figures live, and it is a minority of the total work and the least remunerated portion of it. The judgment layer, choosing the comparator, specifying the model structure, defending the extrapolation, negotiating the price, is unaffected. Under Acemoglu's arithmetic, an 80% reduction in a task that is 20% of the total yields a 16% aggregate gain in the best case, before accounting for the review burden the automation creates.

The counterargument deserves fair statement, because it is empirically supported and it matters for how HEOR should organize. Field evidence is more favorable than Acemoglu's aggregate: Noy and Zhang found writing time down 40% and quality up 18% across 453 professionals with the largest gains for weaker performers^213^, Brynjolfsson and colleagues found 14% to 15% more resolutions per hour across 5,179 support agents with 34% gains for novices and minimal gains for the experienced^214,215^, and Peng and colleagues found programmers 55.8% faster^216^. Three features of these results are uncomfortable for HEOR. The gains are concentrated in the least experienced, which compresses the junior training pathway through which HEOR expertise has historically been built. The gains are largest where output is verifiable, which HEOR output is not. And the direction reverses outside the frontier of capability: in a randomized study of 758 BCG consultants, those using AI on tasks inside the technology's frontier completed 12.2% more tasks 25.1% faster, while on a task outside that frontier they were 19 percentage points less likely to be correct, with accuracy falling from 84.5% in the control arm to 70.6% with AI and to 60.0% with AI plus an overview of its limits^217^. The overview made it worse. HEOR's hardest tasks are outside the frontier, and its practitioners are not yet able to tell which side of the frontier a given task sits on, since 61% rate themselves as having basic or very limited AI proficiency^197^.

What follows for the field is not that AI will not matter. It is that the mechanism by which it matters will be cost structure rather than evidence quality, and that the two are separable. The realistic ten year expectation is a HEOR function that produces more dossiers per analyst at similar quality, with a compressed junior tier, a widened tail of low quality submissions from parties who could not previously afford to submit at all, and a corresponding increase in the burden on reviewers. Reviewers, not producers, absorb the externality. That is the case for the reporting standard below, and it is an economic case, not an ethical one.

### TRACE-HEOR: A REPORTING STANDARD FOR AI ASSISTED HEOR EVIDENCE

Existing instruments cover the parts of this problem that resemble clinical prediction or clinical trials. TRIPOD+AI and PROBAST+AI govern prediction model reporting and bias^218,219^, CONSORT-AI and SPIRIT-AI govern trials of AI interventions^220,221^, DECIDE-AI governs early live clinical evaluation^222^, STARD-AI addresses diagnostic accuracy^223^, TRIPOD-LLM addresses large language model studies^224^, CANGARU addresses disclosure in scholarly writing^225^, CHEERS 2022 governs economic evaluation reporting^89^, PALISADE governs real-world data study credibility^20^, and ELEVATE-GenAI, the ISPOR taxonomy, and the ISPOR working group report begin the HEOR specific work^9-11^. None of them answers the question an HTA reviewer actually has, which is whether the reimbursement recommendation would change if the AI component were removed.

We propose TRACE-HEOR, for Transparent Reporting of Artificial intelligence Components in health Economics and Outcomes Research: ten items designed as an extension to CHEERS 2022 and PALISADE rather than as a replacement, and stated so that each is verifiable by a reviewer with access only to the submission. Table 5 presents them in full with the evidence supporting each.

1. Declare the function, not the tool. State, for each AI component, which of the following it performed: evidence identification or screening, data extraction, cohort or exposure definition, outcome or endpoint derivation, covariate or confounder selection, effect estimation, parameter derivation, model code generation, synthetic data or external control generation, or narrative drafting. Name the model, version, vendor, and dates of use, as JAMA already requires^185^.
2. Specify the context of use and the model risk, using the FDA's two factor definition of model influence and decision consequence^4^, and state which decision the model influences.
3. Report calibration, not only discrimination, and report it in the deployment population and time period. Where an estimate depends on absolute risk or absolute cost, discrimination alone is insufficient^162^.
4. Report the human reference standard and its own reliability. Where AI output is validated against human abstraction, report inter-abstractor agreement for the reference, as Flatiron's real-world response work does at 0.94 and 0.82^71,73^.
5. Report performance for the variables the analysis depends on, disaggregated, not as an aggregate. Aggregate F1 conceals the pattern in which stage extraction reaches 0.988 precision while histology linkage reaches 0.79 recall^68^ and T stage reaches F1 0.89 while M stage reaches 0.24^69^.
6. Report a decision reversal analysis. Re-estimate the primary result with the AI component replaced by the pre-AI alternative, or by a plausible worst case, and state whether the incremental cost effectiveness ratio crosses the relevant threshold or whether the recommendation changes. This is the item that does not exist in any current instrument and the item reviewers need most.
7. Report bias and subgroup performance for the populations the decision affects, and state the demographic composition of any training or synthetic population^92,159^.
8. For synthetic data or model based external controls, report generator family, fidelity against the real target quantity rather than against summary statistics, and a privacy evaluation. Generator choice alone moved recovery of the true median progression free survival from 6.5% to 98.1% of replicates^93^, and only 11% of studies used a differentially private generator^94^.
9. Report the human oversight actually performed, quantitatively: what fraction of AI output was reviewed, by whom, with what qualifications, and what the disagreement rate was. Full manual review is currently reported by 49% of medical affairs teams^198^, and the evidence that oversight fails silently is strong^163,164,169^.
10. Deposit prompts, code, model versions, seeds, and intermediate outputs in a citable archive at submission. Five percent of health economic evaluations currently mention code availability^174^, and an AI assisted analysis is not auditable without the prompts.

Items 1, 2, 6, 9, and 10 are the TRACE-HEOR minimum set, and a submission that reports only those five is materially more auditable than any submission we located. If an HTA agency were to adopt only one, it should be item 6, because decision reversal is the only item that converts a technical property of a model into the currency a reimbursement committee reasons in.

### A RESEARCH AGENDA

We propose seven priorities, ordered by the ratio of decision relevance to current investment.

First, benchmark AI derived endpoints against regulatory grade human abstraction in a multi-sponsor, multi-vendor study with a pre-registered protocol, and publish the discordant cases. The seven month difference in median real-world progression free survival by document source^70^ is the kind of finding that only appears when the comparison is designed rather than incidental. Current validation is vendor authored^71,76^, which is a conflict rather than a failing, and the remedy is independent replication.

Second, obtain a regulatory precedent. No documented instance exists of a regulator or HTA body accepting or rejecting an AI derived endpoint as such. Sponsors should seek scientific advice or a qualification opinion, and agencies should publish the reasoning when they give it, as the EMA did on prognostic covariate adjustment^97^. One published opinion would be worth more to the field than fifty conference abstracts.

Third, establish an empirical decision reversal literature. Take completed cost effectiveness analyses and HTA submissions, substitute AI assisted components for the original ones, and measure how often the recommendation changes. The replication literature suggests the base rate of non-replication is already high before AI is introduced^179,180^, which makes the marginal question answerable and urgent.

Fourth, run randomized trials of AI assisted HEOR workflows with quality, not speed, as the primary endpoint. Every existing efficiency figure in industry is single arm and self reported. The designs already exist in adjacent fields^169,213,217^, and the ISPOR time and motion approach shows what a fair comparison looks like when recall is reported alongside time saved^35^.

Fifth, close the calibration drift gap for economic models. Discrimination monitoring is standard and is the wrong monitor for HEOR^161,162^. Prospective calibration surveillance of models feeding reimbursement relevant estimates is a tractable methodological programme.

Sixth, evaluate AI itself economically at a scale proportionate to its deployment. Nineteen published economic evaluations^98^ against 1,614 authorized devices^7^ is a ratio of about one to eighty five. The finding that no price per scan made an AI cost effective in a national screening programme^102^ should be reproduced or refuted in other pathways, and the frameworks for doing so are available^103^.

Seventh, build HEOR specific competency and audit capacity. Existing frameworks are general^200,201,204^, self assessed proficiency is low^197^, and the deskilling and automation bias evidence indicates that unstructured oversight is not protective^163,167^. Reviewer side capacity is the binding constraint, because the EU joint clinical assessment volume is rising on a fixed schedule^123,127^ whether or not submitters disclose their methods.

### LIMITATIONS

Our limitations are substantial and we state them without softening.

We searched a single database. PubMed does not index much of the conference and grey literature where AI in HEOR is most active, and 92% of the studies in one review of generative AI in health economic evaluation were conference abstracts^41^. Our corpus therefore understates operational activity and overstates the peer reviewed share. We compensated partially by assembling the conference and agency record narratively, but that portion is not systematic.

Our classifier is a term dictionary and its errors are large, measured, and reported rather than hidden. Precision against blinded independent classification was 51.3% overall and 29.6% for economic evaluation. All domain counts should be read as upper bounds.

Our reference standard is itself a large language model rather than a human expert panel. This is a genuine circularity in a paper about the reliability of these tools, and it cuts both ways: the blinded classifier may be systematically strict about what counts as HEOR, in which case our precision estimate is too low, or systematically lenient on unfamiliar subfields, in which case some labels are understated. A human dual review of the same 300 records would be the correct next step, and the sample and both label sets are archived so that anyone may perform it^26^.

Our denominator series contains an unresolved discrepancy of 273 records between the range query and the sum of per year queries, most likely from records with publication dates spanning two calendar years. We report both and used the per year series for trends.

We restricted to English language records, which biases the corpus toward North American and European practice, consistent with the 72% concentration reported in the prior HTA scoping review^131^.

Finally, the industry evidence we assembled is overwhelmingly self reported by parties with a commercial interest, and we could not verify any of the efficiency figures independently. We have labelled provenance for every claim in eTable 17, but labelling is not verification.

## Conclusions

The literature on artificial intelligence in health economics and outcomes research has grown by a factor of 29 since 2010 and reached 852 indexed records in 2025. Under blinded independent classification, approximately half of it is about something else. Of 1,391 health technology assessment documents submitted to three major agencies over three years, three disclosed the use of AI. Nineteen published economic evaluations exist for 1,614 authorized AI enabled devices. Thirty eight of 2,476 records were randomized trials and 17 were validation studies. No regulator or health technology assessment body has yet been documented accepting or rejecting an AI derived endpoint as such.

Against that record, the field is being told that its tasks are 40% to 97% faster. Both things can be true, and the reason they are compatible is that the accelerated tasks are the ones with observable ground truth and the unimproved tasks are the ones on which reimbursement decisions turn. That is Acemoglu's distinction, and health economics is its purest case, because the counterfactual is never observed and no training set of correct incremental cost effectiveness ratios can exist. The realistic expectation is a cheaper HEOR function rather than a more accurate one, with a compressed junior tier, more submissions of more variable quality, and the burden of detecting the difference falling on reviewers who have not been given the information they would need.

The remedy is unglamorous and available now, and TRACE-HEOR states it in ten items. Report the function rather than the tool. Report calibration rather than discrimination. Report the reliability of the human standard. Deposit the prompts. And above all, report whether the recommendation changes when the AI component is removed. A field that has spent thirty years insisting that a point estimate is meaningless without its uncertainty should not accept a model output without its decision consequence. The tools are already in the workflow. The disclosure, the validation, and the standards are not, and the interval between those two facts is the field's current exposure.

## Disclosures

The author reports no conflicts of interest related to this work. No funding was received for this study. The author is affiliated with an academic institution and a health economics consultancy that conducts real-world evidence studies for pharmaceutical and life sciences clients; no client had any role in the conception, conduct, analysis, or reporting of this review, and no client reviewed the manuscript before submission.

Generative AI disclosure, following ICMJE, ISPOR, and NEJM AI policy^181,183,189^. Large language models were used in this work in three declared functions. First, for evidence identification support alongside the structured PubMed query. Second, as the independent blinded classifier described in the Methods, which is a measured object of study rather than an assistive tool, with prompts, inputs, and outputs archived. Third, for drafting and editing assistance on manuscript text, with all content verified by the author. No AI tool is listed as an author. No citation in this manuscript was generated by an AI tool without programmatic verification: every DOI was resolved against Crossref and every non-DOI source was retrieved at the cited address, and one candidate DOI that failed to resolve was removed rather than cited. The verification logs are provided in the Supplementary Appendix and the replication package^26^.

## Data Availability

All search strings, retrieved records, the classification dictionary, the blinded classifier prompts and outputs, the analysis scripts, the figure generation code, the DOI verification log, and the complete verified reference library are available in the public replication package^26^. The FDA AI enabled medical device list was retrieved in full and is redistributed in the package as retrieved^7^. No individual patient data were used.

## Author Affiliations

¹ Department of Internal Medicine, University of Michigan, Ann Arbor, Michigan

² Graduate School of Public Health and Health Policy, City University of New York, New York, New York

## Figures

**Figure 1. PRISMA-ScR flow of study identification, screening, and inclusion.** Records identified in PubMed for publication years 2010 through 2025, with duplicate removal, itemized exclusions, and the 2,476 included records. The precision-adjusted corpus estimate derived from blinded independent classification of 300 randomly sampled included records is shown for comparison.

**Figure 2. Growth and composition of the AI and HEOR literature, 2010 to 2025, against its denominators.** Panel A shows publication volume on a logarithmic scale for the included corpus, for all indexed medical AI publications, and for all indexed HEOR publications. Panel B shows the penetration of each literature into the other, that is AI containing HEOR publications as a percentage of all indexed HEOR publications, which reached 6.0% in 2025, and HEOR publications as a percentage of all indexed medical AI publications, which reached 0.86%. Panel C shows the method family composition of the included corpus as a percentage of records per year, with generative AI and large language models, pre-generative natural language processing, deep learning, classical machine learning, artificial intelligence unspecified, and records with no AI method term in the abstract.

**Figure 3. Evidence map of AI applications across HEOR tasks.** Panel A cross-tabulates the eight application domains against the six method families; cell values are counts of included records and domain labels are non-exclusive, so rows do not sum to the corpus. Panel B gives the domain total for each row, with the precision-adjusted total shown as an inner bar so that the measured and the nominal size of each literature can be read together.

**Figure 4. Validation of the term dictionary against blinded independent classification of 300 randomly sampled included records.** Panel A shows Cohen kappa for agreement on each HEOR task domain, annotated with the number of records the dictionary and the blinded classifier each assigned to that domain, and shaded by the conventional interpretive bands for fair, moderate, and substantial agreement. Panel B shows search precision overall and stratified by whether the dictionary assigned at least one domain label or none, with exact binomial 95% confidence intervals. Full agreement statistics, including prevalence-adjusted bias-adjusted kappa, precision, recall, and F1, are given in Table 2 and eTable 8.

**Figure 5. Timeline of regulatory, health technology assessment, and reporting standard milestones for AI in evidence generation, 2019 to 2030.** Each marker is dated at the instrument's issue or entry into force and labeled with the instrument. Rows are grouped and color coded by issuing body. The shaded region marks obligations that are scheduled but not yet in effect, including the staged application of the European Union Health Technology Assessment Regulation and the general purpose AI obligations of the AI Act. The full instrument list with status and operative requirement is given in Table 3.

## Tables

**Table 1.** Characteristics of the included corpus: annual output, application domains, method categories, leading journals, and indexed publication types (n = 2,476).

**Table 2.** Validation of the classification against blinded independent classification of 300 randomly sampled records: per label counts, observed agreement, Cohen kappa, PABAK, precision, recall, and F1, with search precision and the precision-adjusted corpus estimate.

**Table 3.** Regulatory and health technology assessment instruments governing AI in evidence generation, with issuing body, date, status, and the operative requirement.

**Table 4.** Reported performance and efficiency of AI across HEOR workflows, with the measured value, the comparator, and the provenance of the claim classified as peer reviewed, preprint, conference abstract, or company communication.

**Table 5.** TRACE-HEOR: proposed ten item standard for Transparent Reporting of Artificial intelligence Components in health Economics and Outcomes Research, with the reviewer verifiable requirement and the empirical basis for each item.

## References

1. US Food and Drug Administration. FDA proposes framework to advance credibility of AI models used for drug and biological product submissions. Press announcement, January 6, 2025. Available at: https://www.fda.gov/news-events/press-announcements/fda-proposes-framework-advance-credibility-ai-models-used-drug-and-biological-product-submissions

2. Liu Q, Huang R, Hsieh J, Zhu H, Tiwari M, Liu G, et al. Landscape Analysis of the Application of Artificial Intelligence and Machine Learning in Regulatory Submissions for Drug Development From 2016 to 2021. Clin Pharma and Therapeutics 2022;113(4):771-774. DOI: 10.1002/cpt.2668.

3. Naik K, Goyal RK, Foschini L, Chak CW, Thielscher C, Zhu H, et al. Current Status and Future Directions: The Application of Artificial Intelligence/Machine Learning for Precision Medicine. Clin Pharma and Therapeutics 2024;115(4):673-686. DOI: 10.1002/cpt.3152.

4. US Food and Drug Administration. Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products. Draft guidance for industry. Docket FDA-2024-D-4689. Silver Spring, MD: FDA; January 2025. Available at: https://www.fda.gov/media/184830/download

5. US Food and Drug Administration and European Medicines Agency. Guiding Principles of Good AI Practice in Drug Development. January 2026. Available at: https://www.fda.gov/media/189581/download

6. European Medicines Agency. EMA and FDA set common principles for AI in medicine development. News, January 2026. Available at: https://www.ema.europa.eu/en/news/ema-fda-set-common-principles-ai-medicine-development-0

7. US Food and Drug Administration. Artificial Intelligence-Enabled Medical Devices. Device list current as of September 4, 2026. Available at: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices

8. International Society for Pharmacoeconomics and Outcomes Research. ISPOR Top 10 HEOR Trends. Available at: https://www.ispor.org/heor-resources/about-heor/top-10-heor-trends

9. Fleurence RL, Wang X, Bian J, Higashi MK, Ayer T, Xu H, et al. A Taxonomy of Generative Artificial Intelligence in Health Economics and Outcomes Research: An ISPOR Working Group Report. Value in Health 2025;28(11):1601-1610. DOI: 10.1016/j.jval.2025.04.2167.

10. Fleurence RL, Dawoud D, Bian J, Higashi MK, Wang X, Xu H, et al. ELEVATE-GenAI: Reporting Guidelines for the Use of Large Language Models in Health Economics and Outcomes Research: An ISPOR Working Group Report. Value in Health 2025;28(11):1611-1625. DOI: 10.1016/j.jval.2025.06.018.

11. Fleurence RL, Bian J, Wang X, Xu H, Dawoud D, Higashi M, et al. Generative Artificial Intelligence for Health Technology Assessment: Opportunities, Challenges, and Policy Considerations: An ISPOR Working Group Report. Value in Health 2025;28(2):175-183. DOI: 10.1016/j.jval.2024.10.3846.

12. Use of artificial intelligence and machine learning in evidence synthesis for health technology assessment submissions: a review of NICE, CDA, and IQWiG documents. Poster presented at ISPOR 2026, Philadelphia, PA, May 17-20, 2026. Available at: https://www.ispor.org/docs/default-source/cti-meeting-21463-documents/9774d614-3a98-4fba-bcf4-c1ab426db452.pdf

13. The Lancet Infectious Diseases. The use of artificial intelligence in scientific publishing. Editorial. Lancet Infect Dis 2024. Available at: https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(24)00160-9/fulltext

14. Center for the Evaluation of Value and Risk in Health, Tufts Medical Center. HEOR trends: results of a survey of HEOR leaders. Poster presented at ISPOR 2026, April 7, 2026. Available at: https://cevr.tuftsmedicalcenter.org/assets/images/2026_04_07_ISPOR_Poster_HEOR_Trends.pdf

15. Lee W, Schwartz N, Bansal A, Khor S, Hammarlund N, Basu A, et al. A Scoping Review of the Use of Machine Learning in Health Economics and Outcomes Research: Part 1: Data From Wearable Devices. Value in Health 2023;26(2):292-299. DOI: 10.1016/j.jval.2022.08.005.

16. Lee W, Schwartz N, Bansal A, Khor S, Hammarlund N, Basu A, et al. A Scoping Review of the Use of Machine Learning in Health Economics and Outcomes Research: Part 2: Data From Nonwearables. Value in Health 2022;25(12):2053-2061. DOI: 10.1016/j.jval.2022.07.011.

17. von GH, Helenius M, Hörhammer I, Moen H, Peltonen L. Scoping review on the economic aspects of machine learning applications in healthcare. International Journal of Medical Informatics 2026;205:106103. DOI: 10.1016/j.ijmedinf.2025.106103.

18. Daghash H, Kernohan A, Brownson-Smith R, Pandey R, Ananthakrishnan A, Cong C, et al. Machine Learning in Health Economic Evaluations: Protocol for a Scoping Review. JMIR Res Protoc 2025;14:e77494. DOI: 10.2196/77494.

19. National Institute for Health and Care Excellence. Use of AI in evidence generation: NICE position statement. ECD11. August 15, 2024. Available at: https://www.nice.org.uk/corporate/ecd11

20. Padula WV, Kreif N, Vanness DJ, Adamson B, Rueda J, Felizzi F, et al. Machine Learning Methods in Health Economics and Outcomes Research: The PALISADE Checklist: A Good Practices Report of an ISPOR Task Force. Value in Health 2022;25(7):1063-1080. DOI: 10.1016/j.jval.2022.03.022.

21. Canada's Drug Agency. Position Statement on the Use of Artificial Intelligence in the Generation and Reporting of Evidence. April 2025. Available at: https://www.cda-amc.ca/sites/default/files/MG%20Methods/Position_Statement_AI_Renumbered.pdf

22. Wynants L, Van CB, Collins GS, Riley RD, Heinze G, Schuit E, et al. Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal. BMJ 2020:m1328. DOI: 10.1136/bmj.m1328.

23. Andaur NCL, Damen JAA, Takada T, Nijman SWJ, Dhiman P, Ma J, et al. Risk of bias in studies on prediction models developed using supervised machine learning techniques: systematic review. BMJ 2021:n2281. DOI: 10.1136/bmj.n2281.

24. Acemoglu D. The simple macroeconomics of AI. Economic Policy 2024;40(121):13-58. DOI: 10.1093/epolic/eiae042.

25. Acemoglu D. The Simple Macroeconomics of AI. 2024. DOI: 10.3386/w32487.

26. Baser O. Replication package for Artificial Intelligence in Health Economics and Outcomes Research: A Systematic Scoping Review. GitHub repository; 2026. Available at: https://github.com/obaser/ai-heor-scoping-review

27. Chelli M, Descamps J, Lavoué V, Trojani C, Azar M, Deckert M, et al. Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis. J Med Internet Res 2024;26:e53164. DOI: 10.2196/53164.

28. Walters WH, Wilder EI. Fabrication and errors in the bibliographic citations generated by ChatGPT. Sci Rep 2023;13(1):14045. DOI: 10.1038/s41598-023-41032-5.

29. Matsui K, Utsumi T, Aoki Y, Maruki T, Takeshima M, Takaesu Y. Human-Comparable Sensitivity of Large Language Models in Identifying Eligible Studies Through Title and Abstract Screening: 3-Layer Strategy Using GPT-3.5 and GPT-4 for Systematic Reviews. J Med Internet Res 2024;26:e52758. DOI: 10.2196/52758.

30. Tran V, Gartlehner G, Yaacoub S, Boutron I, Schwingshackl L, Stadelmaier J, et al. Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses. Ann Intern Med 2024;177(6):791-799. DOI: 10.7326/m23-3389.

31. Oami T, Okada Y, Nakada T. GPT-3.5 Turbo and GPT-4 Turbo in Title and Abstract Screening for Systematic Reviews. JMIR Med Inform 2025;13:e64682-e64682. DOI: 10.2196/64682.

32. Khraisha Q, Put S, Kappenberg J, Warraitch A, Hadfield K. Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages. Research Synthesis Methods 2024;15(4):616-626. DOI: 10.1002/jrsm.1715.

33. Nykvist B, Macura B, Xylia M, Olsson E. Testing the utility of GPT for title and abstract screening in environmental systematic evidence synthesis. Environ Evid 2025;14(1):7. DOI: 10.1186/s13750-025-00360-x.

34. Flemyng E, Noel-Storr A, Macura B, Gartlehner G, Thomas J, Meerpohl JJ, et al. Position statement on artificial intelligence (AI) use in evidence synthesis across Cochrane, the Campbell Collaboration, JBI and the Collaboration for Environmental Evidence 2025. Environ Evid 2025;14(1):20. DOI: 10.1186/s13750-025-00374-5.

35. Lee K, Paek H, Ofoegbu N, Rube S, Higashi MK, Dawoud D, et al. A4SLR: An Agentic Artificial Intelligence-Assisted Systematic Literature Review Framework to Augment Evidence Synthesis for Health Economics and Outcomes Research and Health Technology Assessment. Value in Health 2025;28(11):1655-1664. DOI: 10.1016/j.jval.2025.08.002.

36. Gartlehner G, Kahwati L, Hilscher R, Thomas I, Kugley S, Crotty K, et al. Data extraction for evidence synthesis using a large language model: A proof-of-concept study. Research Synthesis Methods 2024;15(4):576-589. DOI: 10.1002/jrsm.1710.

37. Liu J, Lai H, Zhao W, Huang J, Xia D, Liu H, et al. AI-driven evidence synthesis: data extraction of randomized controlled trials with large language models. International Journal of Surgery 2025;111(3):2722-2726. DOI: 10.1097/js9.0000000000002215.

38. Lai H, Liu J, Bai C, Liu H, Pan B, Luo X, et al. Language models for data extraction and risk of bias assessment in complementary medicine. npj Digit. Med. 2025;8(1):74. DOI: 10.1038/s41746-025-01457-w.

39. Reason T, Rawlinson W, Langham J, Gimblett A, Malcolm B, Klijn S. Artificial Intelligence to Automate Health Economic Modelling: A Case Study to Evaluate the Potential Application of Large Language Models. PharmacoEconomics Open 2024;8(2):191-203. DOI: 10.1007/s41669-024-00477-8.

40. Reason T, Benbow E, Langham J, Gimblett A, Klijn SL, Malcolm B. Artificial Intelligence to Automate Network Meta-Analyses: Four Case Studies to Evaluate the Potential Application of Large Language Models. PharmacoEconomics Open 2024;8(2):205-220. DOI: 10.1007/s41669-024-00476-9.

41. Sharp S, Lokuge K, Elvidge J, Hudson T, Dawoud D. Systematic literature review of the use of generative AI in health economic evaluation. 2025. DOI: 10.1101/2025.04.25.25326412.

42. Abogunrin S, Muir JM, Zerbini C, Sarri G. How much can we save by applying artificial intelligence in evidence synthesis? Results from a pragmatic review to quantify workload efficiencies and cost savings. Front. Pharmacol. 2025;16:1454245. DOI: 10.3389/fphar.2025.1454245.

43. Michelson M, Reuter K. The significant cost of systematic reviews and meta-analyses: A call for greater involvement of machine learning to assess the promise of clinical trials. Contemporary Clinical Trials Communications 2019;16:100443. DOI: 10.1016/j.conctc.2019.100443.

44. Schneeweiss S, Rassen JA, Glynn RJ, Avorn J, Mogun H, Brookhart MA. High-dimensional Propensity Score Adjustment in Studies of Treatment Effects Using Health Care Claims Data. Epidemiology 2009;20(4):512-522. DOI: 10.1097/ede.0b013e3181a663cc.

45. Guertin JR, Rahme E, LeLorier J. Performance of the high-dimensional propensity score in adjusting for unmeasured confounders. Eur J Clin Pharmacol 2016;72(12):1497-1505. DOI: 10.1007/s00228-016-2118-x.

46. Pang M, Schuster T, Filion KB, Eberg M, Platt RW. Targeted Maximum Likelihood Estimation for Pharmacoepidemiologic Research. Epidemiology 2016;27(4):570-577. DOI: 10.1097/ede.0000000000000487.

47. Benasseur I, Talbot D, Durand M, Holbrook A, Matteau A, Potter BJ, et al. A comparison of confounder selection and adjustment methods for estimating causal effects using large healthcare databases. Pharmacoepidemiology and Drug 2022;31(4):424-433. DOI: 10.1002/pds.5403.

48. van DLMJ, Rubin D. Targeted Maximum Likelihood Learning. The International Journal of Biostatistics 2006;2(1). DOI: 10.2202/1557-4679.1043.

49. van DLMJ, Polley EC, Hubbard AE. Super Learner. Statistical Applications in Genetics and Molecular Biology 2007;6(1). DOI: 10.2202/1544-6115.1309.

50. Wager S, Athey S. Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association 2018;113(523):1228-1242. DOI: 10.1080/01621459.2017.1319839.

51. Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, et al. Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal 2018;21(1):C1-C68. DOI: 10.1111/ectj.12097.

52. Bonander C, Svensson M. Using causal forests to assess heterogeneity in cost-effectiveness analysis. Health Economics 2021;30(8):1818-1832. DOI: 10.1002/hec.4263.

53. Zhang Y, Kreif N, GC VS, Manca A. Machine Learning Methods to Estimate Individualized Treatment Effects for Use in Health Technology Assessment. Med Decis Making 2024;44(7):756-769. DOI: 10.1177/0272989x241263356.

54. Glynn D, Giardina J, Hatamyar J, Pandya A, Soares M, Kreif N. Integrating decision modeling and machine learning to inform treatment stratification. Health Economics 2024;33(8):1772-1792. DOI: 10.1002/hec.4834.

55. Möller M, Wild E, Tan W, Schreyögg J. Estimating Heterogeneous Treatment Effects With Real-World Health Data: A Scoping Review of Machine Learning Methods. Value in Health 2026;29(5):905-913. DOI: 10.1016/j.jval.2026.01.013.

56. Manke-Reimers F, Brugger V, Bärnighausen T, Kohler S. When, why and how are estimated effects transported between populations? A scoping review of studies applying transportability methods. Eur J Epidemiol 2025;40(3):255-273. DOI: 10.1007/s10654-025-01217-w.

57. Turner AJ, Sammon C, Latimer N, Adamson B, Beal B, Subbiah V, et al. Transporting Comparative Effectiveness Evidence Between Countries: Considerations for Health Technology Assessments. PharmacoEconomics 2023;42(2):165-176. DOI: 10.1007/s40273-023-01323-1.

58. Weise A, Büchter RB, Pieper D, Mathes T. Assessing transferability in systematic reviews of health economic evaluations, a review of methodological guidance. BMC Med Res Methodol 2022;22(1):52. DOI: 10.1186/s12874-022-01536-6.

59. Wang K, Rosman LA, Lu H. Machine Learning Versus Logistic Regression for Propensity Score Estimation: A Benchmark Trial Emulation Against the PARADIGM-HF Randomized Trial. 2025. DOI: 10.1101/2025.06.16.25329708.

60. US Food and Drug Administration. Real-World Data: Assessing Electronic Health Records and Medical Claims Data To Support Regulatory Decision-Making for Drug and Biological Products. Guidance for industry. Docket FDA-2020-D-2307. July 2024. Available at: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/real-world-data-assessing-electronic-health-records-and-medical-claims-data-support-regulatory

61. Gruber S, Phillips RV, Lee H, Concato J, van DLM. Evaluating and improving real-world evidence with Targeted Learning. BMC Med Res Methodol 2023;23(1):178. DOI: 10.1186/s12874-023-01998-2.

62. Patra BG, Sharma MM, Vekaria V, Adekkanattu P, Patterson OV, Glicksberg B, et al. Extracting social determinants of health from electronic health records using natural language processing: a systematic review. Journal of the American Medical Informatics Association 2021;28(12):2716-2727. DOI: 10.1093/jamia/ocab170.

63. Kharrazi H, Anzaldi LJ, Hernandez L, Davison A, Boyd CM, Leff B, et al. The Value of Unstructured Electronic Health Record Data in Geriatric Syndrome Case Identification. J American Geriatrics Society 2018;66(8):1499-1507. DOI: 10.1111/jgs.15411.

64. Guevara M, Chen S, Thomas S, Chaunzwa TL, Franco I, Kann BH, et al. Large language models to identify social determinants of health in electronic health records. npj Digit. Med. 2024;7(1):6. DOI: 10.1038/s41746-023-00970-0.

65. Xu W, Gu B, Lotter WE, Kehl KL. Extraction and Imputation of Eastern Cooperative Oncology Group Performance Status From Unstructured Oncology Notes Using Language Models. JCO Clin Cancer Inform 2024:e2300269. DOI: 10.1200/cci.23.00269.

66. Maghsoudi A, Sada YH, Nowakowski S, Guffey D, Zhu H, Yarlagadda SR, et al. A Multi-Institutional Natural Language Processing Pipeline to Extract Performance Status From Electronic Health Records. Cancer Control 2024;31:10732748241279518. DOI: 10.1177/10732748241279518.

67. Lin E, Zwolinski R, Wu JT, La J, Goryachev S, Huhmann L, et al. Machine learning-based natural language processing to extract PD-L1 expression levels from clinical notes. Health Informatics J 2023;29(3):14604582231198021. DOI: 10.1177/14604582231198021.

68. Kenney RC, Chen X, Shintani K, Gagnon C, Liu J, DaCosta BS, et al. Validation of Non-Small Cell Lung Cancer Clinical Insights Using a Generalized Oncology Natural Language Processing Model. JCO Clin Cancer Inform 2024:e2300099. DOI: 10.1200/cci.23.00099.

69. Abedian S, Sholle ET, Adekkanattu PM, Cusick MM, Weiner SE, Shoag JE, et al. Automated Extraction of Tumor Staging and Diagnosis Information From Surgical Pathology Reports. JCO Clinical Cancer Informatics 2021:1054-1061. DOI: 10.1200/cci.21.00065.

70. Varma G, Yenukoti RK, Kumar MP, Ashrit BS, Purushotham K, Subash C, et al. A Deep Learning-Enabled Workflow to Estimate Real-World Progression-Free Survival in Patients With Metastatic Breast Cancer: Study Using Deidentified Electronic Health Records. JMIR Cancer 2025;11:e64697-e64697. DOI: 10.2196/64697.

71. Estevez M, Singh N, Dyson L, Adamson B, Krismer K, Magee K, et al. Ensuring Reliability of Curated Electronic Health Record-Derived Data: The Validation of Accuracy for Large Language Model-/Machine Learning-Extracted Information and Data (VALID) Framework. JCO Clin Cancer Inform 2026;10(1):e2500215. DOI: 10.1200/cci-25-00215.

72. Flatiron Health. Flatiron Health publishes first peer-reviewed validation framework for AI-extracted real-world oncology data. Press release. Available at: https://resources.flatiron.com/press/flatiron-health-publishes-first-peer-reviewed-validation-framework-for-ai-extracted-real-world-oncology-data-in-journal-of-clinical-oncology

73. Ma X, Bellomo L, Magee K, Bennette CS, Tymejczyk O, Samant M, et al. Characterization of a Real-World Response Variable and Comparison with RECIST-Based Response Rates from Clinical Trials in Advanced NSCLC. Adv Ther 2021;38(4):1843-1859. DOI: 10.1007/s12325-021-01659-0.

74. Development and validation of a machine learning approach to scale real-world response in oncology. Poster presented at ISPOR. Available at: https://www.ispor.org/docs/default-source/cti-meeting-21021-documents/6f2aef20-5193-4ad1-b198-1156a7ea80f7.pdf

75. Flatiron Health. Flatiron Health research on AI-driven cancer progression extraction presented at AACR Special Conference in Cancer Research: Artificial Intelligence. Press release. Available at: https://resources.flatiron.com/press/flatiron-health-research-on-ai-driven-cancer-progression-extraction-presented-at-aacr-special-conference-in-cancer-research-artificial-intelligence

76. Riskin DJ, Monda KL, Gagne JJ, Reynolds R, Garan AR, Dreyer N, et al. Implementing Accuracy, Completeness, and Traceability for Data Reliability. JAMA Netw Open 2025;8(3):e250128. DOI: 10.1001/jamanetworkopen.2025.0128.

77. Truveta. Truveta Studio and data quality. Presentation at ISPOR Europe 2024. Available at: https://www.ispor.org/docs/default-source/euro2024/ispor-eu-2024---truveta-final.pdf

78. Pfizer. US FDA approves IBRANCE (palbociclib) for the treatment of men with HR+, HER2- metastatic breast cancer. Press release. Available at: https://www.pfizer.com/news/press-release/press-release-detail/u_s_fda_approves_ibrance_palbociclib_for_the_treatment_of_men_with_hr_her2_metastatic_breast_cancer

79. Degeling K, IJzerman MJ, Lavieri MS, Strong M, Koffijberg H. Introduction to Metamodeling for Reducing Computational Burden of Advanced Analyses with Health Economic Models: A Structured Overview of Metamodeling Methods in a 6-Step Application Process. Med Decis Making 2020;40(3):348-363. DOI: 10.1177/0272989x20912233.

80. Fleurence, R, Bian, J, Wang, X, Xu, H, Dawoud, D, Higashi, M, et al. Generative AI for Health Technology Assessment: Opportunities, Challenges, and Policy Considerations. arXiv 2024. DOI: 10.48550/arxiv.2407.11054.

81. Hasan B, Saadi S, Rajjoub NS, Hegazi M, Al-Kordi M, Fleti F, et al. Integrating large language models in systematic reviews: a framework and case study using ROBINS-I for risk of bias assessment. BMJ EBM 2024;29(6):394-398. DOI: 10.1136/bmjebm-2023-112597.

82. Qureshi R, Shaughnessy D, Gill KAR, Robinson KA, Li T, Agai E. Are ChatGPT and large language models “the answer” to bringing us closer to systematic review automation? Syst Rev 2023;12(1):72. DOI: 10.1186/s13643-023-02243-z.

83. Otten TM, Grimm SE, Ramaekers B, Joore MA. Comprehensive Review of Methods to Assess Uncertainty in Health Economic Evaluations. PharmacoEconomics 2023;41(6):619-632. DOI: 10.1007/s40273-023-01242-1.

84. Bojke L, Claxton K, Sculpher M, Palmer S. Characterizing Structural Uncertainty in Decision Analytic Models: A Review and Application of Methods. Value in Health 2009;12(5):739-749. DOI: 10.1111/j.1524-4733.2008.00502.x.

85. Fenwick E, Steuten L, Knies S, Ghabri S, Basu A, Murray JF, et al. Value of Information Analysis for Research Decisions: An Introduction: Report 1 of the ISPOR Value of Information Analysis Emerging Good Practices Task Force. Value in Health 2020;23(2):139-150. DOI: 10.1016/j.jval.2020.01.001.

86. Rothery C, Strong M, Koffijberg H, Basu A, Ghabri S, Knies S, et al. Value of Information Analytical Methods: Report 2 of the ISPOR Value of Information Analysis Emerging Good Practices Task Force. Value in Health 2020;23(3):277-286. DOI: 10.1016/j.jval.2020.01.004.

87. Sculpher M, Claxton K. Establishing the Cost-Effectiveness of New Pharmaceuticals under Conditions of Uncertainty: When Is There Sufficient Evidence? Value in Health 2005;8(4):433-446. DOI: 10.1111/j.1524-4733.2005.00033.x.

88. Fenwick E, Claxton K, Sculpher M. The Value of Implementation and the Value of Information: Combined and Uneven Development. Med Decis Making 2007;28(1):21-32. DOI: 10.1177/0272989x07308751.

89. Husereau D, Drummond M, Augustovski F, de BE, Briggs AH, Carswell C, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) Statement: Updated Reporting Guidance for Health Economic Evaluations. Value in Health 2022;25(1):3-9. DOI: 10.1016/j.jval.2021.11.1351.

90. D'Amico S, Dall’Olio D, Sala C, Dall’Olio L, Sauta E, Zampini M, et al. Synthetic Data Generation by Artificial Intelligence to Accelerate Research and Precision Medicine in Hematology. JCO Clinical Cancer Informatics 2023:e2300021. DOI: 10.1200/cci.23.00021.

91. Elvatun S, Knoors D, Brant S, Jonasson C, Nygård JF. Synthetic data as external control arms in scarce single-arm clinical trials. PLOS Digit Health 2025;4(1):e0000581. DOI: 10.1371/journal.pdig.0000581.

92. Wang D, Florian H, Lynch S, Robieson W, Zhuang R, Kusiak C, et al. Using AI-generated digital twins to boost clinical trial efficiency in Alzheimer's disease. A&D Transl Res & Clin Interv 2025;11(4):e70181. DOI: 10.1002/trc2.70181.

93. Akiya I, Ishihara T, Yamamoto K. Comparison of Synthetic Data Generation Techniques for Control Group Survival Data in Oncology Clinical Trials: Simulation Study. JMIR Med Inform 2024;12:e55118-e55118. DOI: 10.2196/55118.

94. Kaabachi B, Despraz J, Meurers T, Otte K, Halilovic M, Kulynych B, et al. A scoping review of privacy and utility metrics in medical synthetic data. npj Digit. Med. 2025;8(1):60. DOI: 10.1038/s41746-024-01359-3.

95. Jahanshahi M, Gregg K, Davis G, Ndu A, Miller V, Vockley J, et al. The Use of External Controls in FDA Regulatory Decision Making. Ther Innov Regul Sci 2021;55(5):1019-1035. DOI: 10.1007/s43441-021-00302-y.

96. Yin X, Mishra-Kalyan PS, Sridhara R, Stewart MD, Stuart EA, Davi RC. Exploring the Potential of External Control Arms created from Patient Level Data: A case study in non-small cell lung cancer. Journal of Biopharmaceutical Statistics 2022;32(1):204-218. DOI: 10.1080/10543406.2021.2011901.

97. European Medicines Agency. Qualification opinion for Prognostic Covariate Adjustment (PROCOVA). Committee for Medicinal Products for Human Use. Available at: https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/qualification-opinion-prognostic-covariate-adjustment-procovatm_en.pdf

98. El ARA, Al MOA. Systematic review of cost effectiveness and budget impact of artificial intelligence in healthcare. npj Digit. Med. 2025;8(1):548. DOI: 10.1038/s41746-025-01722-y.

99. Yala A, Mikhael PG, Lehman C, Lin G, Strand F, Wan Y, et al. Optimizing risk-based breast cancer screening policies with reinforcement learning. Nat Med 2022;28(1):136-143. DOI: 10.1038/s41591-021-01599-w.

100. Mital S, Nguyen HV. Cost-effectiveness of using artificial intelligence versus polygenic risk score to guide breast cancer screening. BMC Cancer 2022;22(1):501. DOI: 10.1186/s12885-022-09613-1.

101. Huang X, Yang B, Zheng W, Liu Q, Xiao F, Ouyang P, et al. Cost-effectiveness of artificial intelligence screening for diabetic retinopathy in rural China. BMC Health Serv Res 2022;22(1):260. DOI: 10.1186/s12913-022-07655-6.

102. Vargas-Palacios A, Sharma N, Sagoo GS. Cost-effectiveness requirements for implementing artificial intelligence technology in the Women’s UK Breast Cancer Screening service. Nat Commun 2023;14(1):6110. DOI: 10.1038/s41467-023-41754-0.

103. Hendrix N, Veenstra DL, Cheng M, Anderson NC, Verguet S. Assessing the Economic Value of Clinical Artificial Intelligence: Challenges and Opportunities. Value in Health 2022;25(3):331-339. DOI: 10.1016/j.jval.2021.08.015.

104. Kalavadekar PN, Khandarkar KR, Dhotre DR, Chincholkar A, Swarnkar SK, Joshi HJ. Reinforcement learning to optimize tuberculosis screening strategies in resource-limited settings. Indian Journal of Tuberculosis 2025;72:S159-S167. DOI: 10.1016/j.ijtb.2025.11.019.

105. Poddar A, Samson M, Innes GK, Liu Q, Saha A, Hanger M, et al. Leveraging Artificial Intelligence in Drug and Biological Product Development: An FDA and Clinical Trial Transformation Initiative Workshop Report. NEJM AI 2025;2(12). DOI: 10.1056/aipc2500801.

106. Pharmaceutical Research and Manufacturers of America. PhRMA comments on Docket FDA-2024-D-4689. Available at: https://cdn.aglty.io/phrma/global/resources/import/pdfs/FDA-2024-D-4689_PhRMA%20Comments.pdf

107. US Food and Drug Administration. Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations. Draft guidance. Docket FDA-2024-D-4488. January 2025. Available at: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing

108. US Food and Drug Administration. Digital Health Advisory Committee Meeting: Total Product Life Cycle Considerations for Generative AI-Enabled Devices. November 20-21, 2024. Available at: https://www.fda.gov/advisory-committees/advisory-committee-calendar/digital-health-advisory-committee-meeting-november-20-21-2024

109. US Food and Drug Administration. FDA launches agency-wide AI tool to optimize performance for the American people. News release, June 2, 2025. Available at: https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people

110. European Medicines Agency. Reflection paper on the use of artificial intelligence in the lifecycle of medicines. EMA/CHMP/CVMP/83833/2023. September 9, 2024. Available at: https://www.ema.europa.eu/en/documents/scientific-guideline/reflection-paper-use-artificial-intelligence-ai-medicinal-product-lifecycle_en.pdf

111. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Official Journal of the European Union. Available at: https://eur-lex.europa.eu/eli/reg/2024/1689/oj

112. European Federation of Pharmaceutical Industries and Associations. EFPIA position on the use of artificial intelligence in the medicinal product lifecycle. October 2024. Available at: https://efpia.eu/media/tzeavw1t/efpia-position-on-the-use-of-artificial-intelligence-in-the-medicinal-product-lifecycle.pdf

113. International Federation of Pharmaceutical Manufacturers and Associations. IFPMA Artificial Intelligence Ethics Principles. July 2022. Available at: https://www.ifpma.org/wp-content/uploads/2023/01/i2023_IFPMA-Artificial-Intelligence-AI-Ethics-Principles.pdf

114. Novartis. Novartis commitment to the ethical and responsible use of AI systems. Available at: https://www.novartis.com/sites/novartis_com/files/novartis-responsible-use-of-ai-systems.pdf

115. Roche. Roche AI Ethics Principles. Updated April 1, 2025. Available at: https://assets.roche.com/f/176343/x/401c28049f/roche-ai-ethics-principles.pdf

116. Centers for Medicare and Medicaid Services. Coverage criteria and utilization management requirements in CMS-4201-F. Health Plan Management System memorandum, February 6, 2024. Available at: https://www.cms.gov/files/document/faq-contract-year-2024-policy-and-technical-changes-medicare-advantage-program-final-rule-utilization.pdf

117. California Senate Bill 1120, Chapter 879, Statutes of 2024 (Physicians Make Decisions Act). Available at: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1120

118. World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. Geneva: WHO; 2024. ISBN 978-92-4-008475-9.

119. World Health Organization. Ethics and governance of artificial intelligence for health: WHO guidance. Geneva: WHO; 2021. ISBN 978-92-4-002920-0.

120. CDA-AMC. Development of an Evaluation Instrument on Artificial Intelligence Search Tools for Evidence Synthesis. cjht 2024;4(10). DOI: 10.51731/cjht.2024.1004.

121. Institute FQAEIHC. General Methods; Version 8.0. IQWiG 2026. DOI: 10.60584/general-methods_v8.0.

122. Pearson SD, Singh P, Beaudoin F, Campbell J, Schapiro L, Emond SK, et al. Institute for Clinical and Economic Review: Peterson Health Technology Institute value assessment framework for digital health technologies. J. Comp. Eff. Res. 2023;12(12):e230154. DOI: 10.57264/cer-2023-0154.

123. Regulation (EU) 2021/2282 of the European Parliament and of the Council of 15 December 2021 on health technology assessment. Official Journal of the European Union. Available at: https://eur-lex.europa.eu/eli/reg/2021/2282/oj/eng

124. European Commission. Implementation of the Regulation on health technology assessment. Available at: https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment_en

125. European Commission. Joint Clinical Assessments. Available at: https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment/joint-clinical-assessments_en

126. Barbuto V, European Commission DG SANTE. The HTA Regulation. Presentation to the 15th EMA Industry Standing Group, December 11, 2025. Available at: https://www.ema.europa.eu/en/documents/presentation/presentation-hta-regulation-v-barbuto-ec_en.pdf

127. Health Technology Assessment Coordination Group. Annual Work Programme 2026. November 28, 2025. Available at: https://health.ec.europa.eu/document/download/81db097f-a9cb-4404-837c-115b4289321d_en

128. Use of artificial intelligence in health technology assessment submissions and agency practice. Poster MSR96 presented at ISPOR 2026, Philadelphia, PA. Available at: https://www.ispor.org/docs/default-source/cti-meeting-21463-documents/edf7be4a-ac97-45e7-82f1-ed3fc505aa61.pdf

129. Emerging trends in AI applications shaping pharmacoepidemiology and health technology assessments. Poster presented at ISPOR 2025. Available at: https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2025/poster-session-3/emerging-trends-in-ai-applications-shaping-pharmacoepidemiology-and-health-technology-assessments

130. Assessing the use of artificial intelligence in publication-grade research: a literature review of applications in HEOR. Poster SA14 presented at ISPOR Europe 2025. Available at: https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-europe-2025/poster-session-1-2/assessing-the-use-of-artificial-intelligence-in-publication-grade-research-a-literature-review-of-applications-in-heor

131. Artificial intelligence tools in health technology assessment: a scoping review. Conference proceeding OP07. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC11718724/

132. Pfizer. How AI is already reshaping cancer care. Available at: https://www.pfizer.com/news/articles/how_ai_is_already_reshaping_cancer_care

133. Merck and Co. Merck expands innovative internal generative AI solutions, helping to deliver medicines to patients faster. Press release, June 25, 2025. Available at: https://www.merck.com/news/merck-expands-innovative-internal-generative-ai-solutions-helping-to-deliver-medicines-to-patients-faster/

134. Anthropic. Novo Nordisk transforms clinical documentation with Claude. Customer story. Available at: https://claude.com/customers/novo-nordisk

135. Takeda. Aiming to enhance regulatory submissions with GenAI. December 12, 2024. Available at: https://www.takeda.com/our-impact/our-stories/aiming-to-enhance-regulatory-submissions-with-genai/

136. Automated generation of investigational new drug applications with large language models. arXiv preprint 2509.09738. Available at: https://arxiv.org/pdf/2509.09738

137. Certara. CoAuthor and GPTs: transforming regulatory writing. White paper, November 2024. Available at: https://www.certara.com/wp-content/uploads/2024/11/2024-11-08-White-Paper-CoAuthor-and-GPTs.pdf

138. Reuters. Drugmakers turn to AI to speed trials, regulatory submissions. January 26, 2026. Available at: https://www.reuters.com/legal/litigation/drugmakers-turn-ai-speed-trials-regulatory-submissions-2026-01-26/

139. Merck and Co. Merck and Google Cloud partner to accelerate agentic AI enterprise transformation. Press release, April 22, 2026. Available at: https://www.merck.com/news/merck-and-google-cloud-partner-to-accelerate-agentic-ai-enterprise-transformation/

140. Eli Lilly and Company. Lilly partners with NVIDIA to build industry's most powerful AI supercomputer owned and operated by a pharmaceutical company. October 28, 2025. Available at: https://investor.lilly.com/news-releases/news-release-details/lilly-partners-nvidia-build-industrys-most-powerful-ai

141. Tempus AI. Tempus signs expanded strategic agreements with AstraZeneca and Pathos AI. April 23, 2025. Available at: https://investors.tempus.com/news-releases/news-release-details/tempus-signs-expanded-strategic-agreements-astrazeneca-and/

142. OpenAI. Moderna: advancing mRNA medicine with generative AI. Customer story. Available at: https://openai.com/index/moderna/

143. Sanofi. Sanofi to become the first pharma company powered by artificial intelligence at scale. Press release, June 13, 2023. Available at: https://www.sanofi.com/en/media-room/press-releases/2023/2023-06-13-12-00-00-2687072

144. Automated AMCP dossier development using a retrieval-augmented generation (RAG) based multi-agent approach. Abstract MSR207. Value Health 2026;29(S6). Available at: https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2026/poster-session-5-3/automated-amcp-dossier-development-using-a-retrieval-augmented-generation-rag-based-multi-agent-approach

145. Academy of Managed Care Pharmacy. AMCP Format for Formulary Submissions. Available at: https://www.amcp.org/resource/amcp-format-formulary-submissions-guidance

146. Norstella. Norstella AI: principles and product capabilities. Available at: https://ai.norstella.com/

147. IQVIA. Market Access Insights. Fact sheet, November 7, 2023. Available at: https://www.iqvia.com/library/fact-sheets/market-access-insights

148. Endpoints News. The first AI-designed drugs fall short in the clinic following years of hype. Available at: https://endpoints.news/first-ai-designed-drugs-fall-short-in-the-clinic-following-years-of-hype/

149. Fierce Biotech. Several months after Exscientia merger, AI outfit Recursion reworks pipeline. Available at: https://www.fiercebiotech.com/biotech/several-months-after-exscientia-merge-ai-outfit-recursion-reworks-pipeline

150. KP JM, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. Drug Discovery Today 2024;29(6):104009. DOI: 10.1016/j.drudis.2024.104009.

151. Wong CH, Siah KW, Lo AW. Estimation of clinical trial success rates and related parameters. Biostatistics 2018;20(2):273-286. DOI: 10.1093/biostatistics/kxx069.

152. Wong CH, Siah KW, Lo AW. Corrigendum: Estimation of clinical trial success rates and related parameters. Biostatistics 2018;20(2):366-366. DOI: 10.1093/biostatistics/kxy072.

153. Wilczok D, Zhavoronkov A. Progress, Pitfalls, and Impact of AI-Driven Clinical Trials. Clin Pharma and Therapeutics 2024;117(4):887-890. DOI: 10.1002/cpt.3542.

154. Haque W, Sai-Palm K, Kasparcova MZ, Rana I, Verlingue L, Garassino MC, et al. Clinical-stage AI-enabled therapeutic assets: An industry-wide analysis of scale, clinical progression, and company characteristics. J Clin Oncol 2026;44(16_suppl):11072-11072. DOI: 10.1200/jco.2026.44.16_suppl.11072.

155. DiMasi JA, Grabowski HG, Hansen RW. Innovation in the pharmaceutical industry: New estimates of R&D costs. Journal of Health Economics 2016;47:20-33. DOI: 10.1016/j.jhealeco.2016.01.012.

156. Wouters OJ, McKee M, Luyten J. Estimated Research and Development Investment Needed to Bring a New Medicine to Market, 2009-2018. JAMA 2020;323(9):844. DOI: 10.1001/jama.2020.1166.

157. Wouters OJ, McKee M, Luyten J. Errors in Source Data for Study of Drug Development Costs. JAMA 2022;328(11):1110. DOI: 10.1001/jama.2022.14317.

158. Error in Data in Study of Estimated Cost of Bringing a Drug to Market. JAMA 2022;328(11):1111. DOI: 10.1001/jama.2022.14733.

159. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. Dissecting racial bias in an algorithm used to manage the health of populations. Science 2019;366(6464):447-453. DOI: 10.1126/science.aax2342.

160. Wong A, Otles E, Donnelly JP, Krumm A, McCullough J, DeTroyer-Cooley O, et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Intern Med 2021;181(8):1065. DOI: 10.1001/jamainternmed.2021.2626.

161. Rahmani K, Thapa R, Tsou P, Chetty SC, Barnes G, Lam C, et al. Assessing the effects of data drift on the performance of machine learning models used in clinical sepsis prediction. 2022. DOI: 10.1101/2022.06.06.22276062.

162. Kopanitsa G. Validation is not enough: Longitudinal evidence of post-deployment fragility in clinical AI systems. PLOS Digit Health 2026;5(7):e0001534. DOI: 10.1371/journal.pdig.0001534.

163. Jabbour S, Fouhey D, Shepard S, Valley TS, Kazerooni EA, Banovic N, et al. Measuring the Impact of AI in the Diagnosis of Hospitalized Patients. JAMA 2023;330(23):2275. DOI: 10.1001/jama.2023.22295.

164. Dratsch T, Chen X, Rezazade MM, Kloeckner R, Mähringer-Kunz A, Püsken M, et al. Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance. Radiology 2023;307(4):e222176. DOI: 10.1148/radiol.222176.

165. Wang D, Ding J, Sun A, Liu S, Jiang D, Li N, et al. Artificial intelligence suppression as a strategy to mitigate artificial intelligence automation bias. Journal of the American Medical Informatics Association 2023;30(10):1684-1692. DOI: 10.1093/jamia/ocad118.

166. Sakamoto T, Harada Y, Shimizu T. Facilitating Trust Calibration in Artificial Intelligence-Driven Diagnostic Decision Support Systems for Determining Physicians’ Diagnostic Accuracy: Quasi-Experimental Study. JMIR Form Res 2024;8:e58666-e58666. DOI: 10.2196/58666.

167. Budzyń K, Romańczyk M, Kitala D, Kołodziej P, Bugajski M, Adami HO, et al. Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. The Lancet Gastroenterology & Hepatology 2025;10(10):896-903. DOI: 10.1016/s2468-1253(25)00133-5.

168. Budzyń K, Romańczyk M, Mori Y. Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: Authors' reply. The Lancet Gastroenterology & Hepatology 2025;10(12):1062. DOI: 10.1016/s2468-1253(25)00324-3.

169. Goh E, Gallo R, Hom J, Strong E, Weng Y, Kerman H, et al. Large Language Model Influence on Diagnostic Reasoning. JAMA Netw Open 2024;7(10):e2440969. DOI: 10.1001/jamanetworkopen.2024.40969.

170. Science. Trump officials downplay fake citations in high-profile report on children's health. Available at: https://www.science.org/content/article/trump-officials-downplay-fake-citations-high-profile-report-children-s-health

171. Reuters. Anthropic expert accused of using AI-fabricated source in copyright case. May 13, 2025. Available at: https://www.reuters.com/legal/litigation/anthropic-expert-accused-using-ai-fabricated-source-copyright-case-2025-05-13/

172. Washington State Bar Association. Federal court excludes expert for AI-hallucinated citations. NWSidebar, August 31, 2026. Available at: https://nwsidebar.wsba.org/2026/08/31/federal-court-excludes-expert-for-ai-hallucinated-citations/

173. Retraction Watch. As Springer Nature journal clears AI papers, one university's retractions rise drastically. February 10, 2025. Available at: https://retractionwatch.com/2025/02/10/as-springer-nature-journal-clears-ai-papers-one-universitys-retractions-rise-drastically/

174. Catalá-López F, Ridao M, Tejedor-Romero L, Caulley L, Hutton B, Husereau D, et al. Transparency, openness, and reproducible research practices are frequently underused in health economic evaluations. Journal of Clinical Epidemiology 2024;165:111208. DOI: 10.1016/j.jclinepi.2023.10.024.

175. Monks T, Harper A. Computer model and code sharing practices in healthcare discrete-event simulation: a systematic scoping review. Journal of Simulation 2023;19(1):108-123. DOI: 10.1080/17477778.2023.2260772.

176. Henderson RH, Sampson C, Pouwels XG, Harvard S, Handels R, Feenstra T, et al. Mapping the Landscape of Open Source Health Economic Models: A Systematic Database Review and Analysis: An ISPOR Special Interest Group Report. Value in Health 2025;28(6):813-820. DOI: 10.1016/j.jval.2025.01.019.

177. Zavalis EA, Ioannidis JPA. A meta-epidemiological assessment of transparency indicators of infectious disease models. PLoS ONE 2022;17(10):e0275380. DOI: 10.1371/journal.pone.0275380.

178. Naudet F, Sakarovitch C, Janiaud P, Cristea I, Fanelli D, Moher D, et al. Data sharing and reanalysis of randomized controlled trials in leading biomedical journals with a full data sharing policy: survey of studies published in The BMJ and PLOS Medicine. BMJ 2018:k400. DOI: 10.1136/bmj.k400.

179. Bermejo I, Tappenden P, Youn J. Replicating Health Economic Models: Firm Foundations or a House of Cards? PharmacoEconomics 2017;35(11):1113-1121. DOI: 10.1007/s40273-017-0553-x.

180. Schwander B, Nuijten M, Evers S, Hiligsmann M. Replication of Published Health Economic Obesity Models: Assessment of Facilitators, Hurdles and Reproduction Success. PharmacoEconomics 2021;39(4):433-446. DOI: 10.1007/s40273-021-01008-7.

181. International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals: Artificial intelligence use by authors. Available at: https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html

182. Committee on Publication Ethics. Authorship and AI tools. COPE position statement. Available at: https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools

183. NEJM AI. Editorial policies. Available at: https://ai.nejm.org/about/editorial-policies

184. NEJM AI. About NEJM AI. Available at: https://ai.nejm.org/about

185. JAMA. Instructions for Authors. Available at: https://jamanetwork.com/journals/jama/pages/instructions-for-authors

186. Health Affairs. New article requirements. Available at: https://www.healthaffairs.org/help-for-authors/journal/new-article-requirements

187. Elsevier. Generative AI policies for journals. Available at: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals

188. Springer Nature. Artificial intelligence: editorial policies. Available at: https://www.nature.com/nature-portfolio/editorial-policies/ai

189. International Society for Pharmacoeconomics and Outcomes Research. ISPOR Artificial Intelligence Policy. Available at: https://www.ispor.org/ai-policy

190. Value in Health. Guide for authors. Available at: https://www.sciencedirect.com/journal/value-in-health/publish/guide-for-authors

191. Kwon D. Is it OK for AI to write science papers? Nature survey shows researchers are split. Nature 2025;641(8063):574-578. DOI: 10.1038/d41586-025-01463-8.

192. Naddaf M. More than half of researchers now use AI for peer review, often against guidance. Nature 2025;649(8096):273-274. DOI: 10.1038/d41586-025-04066-5.

193. American Medical Association. Augmented Intelligence Research: Physician Sentiments Around the Use of AI in Health Care. Chicago, IL: AMA; 2026. Available at: https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf

194. American Medical Association. AI usage among doctors doubles, confidence in technology grows. Press release, 2026. Available at: https://www.ama-assn.org/press-center/ama-press-releases/ama-ai-usage-among-doctors-doubles-confidence-technology-grows

195. McKinsey and Company. Generative AI in healthcare: current trends and future outlook. 2026. Available at: https://www.mckinsey.com/industries/healthcare/our-insights/generative-ai-in-healthcare-current-trends-and-future-outlook

196. HIMSS and Medscape. AI Adoption by Health Systems Report 2024. Available at: https://www.himss.org/news-center/himss-and-medscape-unveil-groundbreaking-report-ai-adoption-health-systems/

197. Polygon Health Analytics. AI in HEOR, RWD and medical affairs: what 133 professionals told us. April 2026. Available at: https://polygonhealthanalytics.com/ai-in-heor-rwd-medical-affairs-what-133-professionals-told-us-and-what-it-means-for-the-industry/

198. Medical Affairs Professional Society. Workflows, not chatbots: findings from the 2026 AI in Medical Affairs Industry Benchmark Survey. Available at: https://medicalaffairs.org/solution-provider-perspective/workflows-not-chatbots/

199. ZS Associates. Medical Affairs Outlook Report 2025. Available at: https://www.zs.com/content/dam/global/master/pdfs/zs-medical-affairs-outlook-report-2025.pdf

200. Cai C, Zhu G, Zhou S, Ng O, Duell J, Ho WK, et al. A Competency Framework for Medical AI Education: Mixed Methods Study. JMIR Med Educ 2026;12:e91116-e91116. DOI: 10.2196/91116.

201. Acosta JA. Perspective: advancing public health education by embedding AI literacy. Front. Digit. Health 2025;7:1584883. DOI: 10.3389/fdgth.2025.1584883.

202. Semi MMA, Das S, Utsho MR, Hossain A, Kamal MB, Sizan AA, et al. Artificial Intelligence in Public Health Education: A Scoping Review of Workforce Competency Development. Health Science Reports 2026;9(3):e72066. DOI: 10.1002/hsr2.72066.

203. Wolthusen RPF, El-tohami M, Hendler RA, Riordan PA, Stoklosa JB. A Framework for Artificial Intelligence in Medical Education: Could I, Would I, Should I? Journal of Graduate Medical Education 2025;17(4):430-433. DOI: 10.4300/jgme-d-25-00009.1.

204. Gordon M, Daniel M, Ajiboye A, Uraiby H, Xu NY, Bartlett R, et al. A scoping review of artificial intelligence in medical education: BEME Guide No. 84. Medical Teacher 2024;46(4):446-470. DOI: 10.1080/0142159x.2024.2314198.

205. Pizzi LT, Onukwugha E, Corey R, Albarmawi H, Murray J. Competencies for Professionals in Health Economics and Outcomes Research: The ISPOR Health Economics and Outcomes Research Competencies Framework. Value in Health 2020;23(9):1120-1127. DOI: 10.1016/j.jval.2020.04.1834.

206. Rock Health. 2025 year-end digital health funding overview: a tale of two markets. Available at: https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/

207. Rock Health. 2024 year-end market overview: Davids and Goliaths. Available at: https://rockhealth.com/insights/2024-year-end-market-overview-davids-and-goliaths/

208. White and Case and Mergermarket. Life Sciences and AI Report. January 2026. Available at: https://www.whitecase.com/sites/default/files/2026-01/W%26C_Life%20Sciences%20%26%20AI%20Report_January%202026.pdf

209. McKinsey and Company. AI budgets grow in life sciences. Week in Charts, 2025. Available at: https://www.mckinsey.com/featured-insights/week-in-charts/ai-budgets-grow-in-life-sciences

210. Grand View Research. Artificial intelligence in healthcare market size, share and trends analysis report. Available at: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market

211. Acemoglu D, Restrepo P. Automation and New Tasks: How Technology Displaces and Reinstates Labor. Journal of Economic Perspectives 2019;33(2):3-30. DOI: 10.1257/jep.33.2.3.

212. Acemoglu D, Restrepo P. The Race between Man and Machine: Implications of Technology for Growth, Factor Shares, and Employment. American Economic Review 2018;108(6):1488-1542. DOI: 10.1257/aer.20160696.

213. Noy S, Zhang W. Experimental evidence on the productivity effects of generative artificial intelligence. Science 2023;381(6654):187-192. DOI: 10.1126/science.adh2586.

214. Brynjolfsson E, Li D, Raymond L. Generative AI at Work. The Quarterly Journal of Economics 2025;140(2):889-942. DOI: 10.1093/qje/qjae044.

215. Brynjolfsson E, Li D, Raymond L. Generative AI at Work. 2023. DOI: 10.3386/w31161.

216. Peng, S, Kalliamvakou, E, Cihon, P, Demirer, M. The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. arXiv 2023. DOI: 10.48550/arxiv.2302.06590.

217. Dell’Acqua F, McFowland E, Mollick E, Lifshitz H, Kellogg KC, Rajendran S, et al. Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. Organization Science 2026;37(2):403-423. DOI: 10.1287/orsc.2025.21838.

218. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van CB, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ 2024;385:e078378. DOI: 10.1136/bmj-2023-078378.

219. Moons KGM, Damen JAA, Kaul T, Hooft L, Andaur NC, Dhiman P, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ 2025;388:e082505. DOI: 10.1136/bmj-2024-082505.

220. Liu X, Cruz RS, Moher D, Calvert MJ, Denniston AK, The SACWG, et al. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nat Med 2020;26(9):1364-1374. DOI: 10.1038/s41591-020-1034-x.

221. Cruz RS, Liu X, Chan A, Denniston AK, Calvert MJ, The SACWG, et al. Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. Nat Med 2020;26(9):1351-1363. DOI: 10.1038/s41591-020-1037-7.

222. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. Nat Med 2022;28(5):924-933. DOI: 10.1038/s41591-022-01772-9.

223. Sounderajah V, Ashrafian H, Golub RM, Shetty S, De FJ, Hooft L, et al. Developing a reporting guideline for artificial intelligence-centred diagnostic test accuracy studies: the STARD-AI protocol. BMJ Open 2021;11(6):e047709. DOI: 10.1136/bmjopen-2020-047709.

224. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med 2025;31(1):60-69. DOI: 10.1038/s41591-024-03425-5.

225. Cacciamani, GE, Eppler, MB, Ganjavi, C, Pekan, A, Biedermann, B, Collins, GS, et al. Development of the ChatGPT, Generative Artificial Intelligence and Natural Large Language Models for Accountable Reporting and Use (CANGARU) Guidelines. arXiv 2023. DOI: 10.48550/arxiv.2307.08974.

