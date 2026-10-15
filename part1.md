---
title: "Faster but Not Truer, Part 1: A Systematic Scoping Review of Artificial Intelligence in Health Economics and Outcomes Research"
subtitle: "How Large the Literature Is, What It Actually Does, and What Validation Reveals"
author: "Onur Baser, Ph.D."
type: "Review"
series: "Part 1 of a two part series"
---

**Onur Baser, Ph.D.**^1,2^

^1^Department of Internal Medicine, University of Michigan, Ann Arbor, MI
^2^Graduate School of Public Health and Health Policy, City University of New York, New York, NY

The author affiliations are listed at the end of the article.

This is the first of two articles. Part 1 measures the literature and validates the measurement. Part 2 assembles the regulatory, health technology assessment, and industry record, examines the economics of automation as it applies to this field, and proposes the TRACE-HEOR reporting standard.

## Short Summary

Artificial intelligence now appears in one of every sixteen health economics and outcomes research publications. This first article of a two part series reports an original systematic scoping review of 2,476 indexed studies published between 2010 and 2025, and then does something scoping reviews rarely do, which is measure its own error rate. An independent blinded classifier judged only half of the corpus genuinely relevant to health economics, and the label that grew fastest, economic evaluation, is the label the classifier could least reliably assign. Read alongside the primary performance evidence workflow by workflow, the pattern is consistent: measured gains cluster where ground truth is observable, and vanish where the counterfactual is not.

## Abstract

**BACKGROUND**

Artificial intelligence (AI) is being introduced into every stage of the health economics and outcomes research (HEOR) production line, from literature screening to causal estimation. The field lacks a defensible count of what has been done, and bibliometric claims about AI adoption circulate without measured error rates.

**METHODS**

Following PRISMA-ScR, we searched PubMed for AI terms co-occurring with HEOR terms for publications from 2010 through 2025, retrieved 2,642 records, and included 2,476 after screening. Records were classified into eight non-exclusive application domains and one of six method categories using a published term dictionary. To quantify classification error, an independent large language model classifier, blinded to the dictionary labels and given only title and abstract, re-classified a random sample of 300 included records. We report per label counts, agreement, Cohen kappa, prevalence-adjusted bias-adjusted kappa, precision, recall, F1, and a precision-adjusted corpus size with exact binomial intervals. We separately assembled the primary performance evidence for each HEOR workflow, requiring a quantitative metric from a primary study.

**RESULTS**

Included publications rose from 29 in 2010 to 852 in 2025, a factor of 29.4, with the inflection at 2018 to 2019 rather than at the release of ChatGPT. AI reached 6.0% of all indexed HEOR output in 2025 while HEOR fell to 0.86% of all indexed medical AI output. Economic evaluation was the most frequently assigned domain (1,559 of 2,476, 63.0%), followed by real-world data and causal inference (496, 20.0%) and governance, reporting, and validity (494, 20.0%). Generative AI appeared in no record before 2021 and in 103 in 2025. Only 154 of 300 sampled records (51.3%, 95% confidence interval [CI] 45.7 to 56.9) were judged genuinely HEOR relevant, implying a precision-adjusted corpus of 1,271 studies (95% CI 1,131 to 1,410). Agreement was substantial for real-world data and causal inference (kappa 0.729) but negligible for economic evaluation (kappa 0.144), where dictionary precision was 29.6%. Of 2,476 records, 38 (1.5%) were randomized trials and 17 (0.7%) validation studies.

**CONCLUSIONS**

The literature is growing faster than its own measurement infrastructure. Measured gains concentrate in tasks with observable ground truth, and predictive performance repeatedly fails to predict evidentiary performance.

## Introduction

Two facts about artificial intelligence in health economics and outcomes research sit uneasily beside each other, and this series is about the distance between them.

The first is that the field has been reorganized around it. Since 2016 the US Food and Drug Administration (FDA) has received more than 500 drug and biological product submissions containing AI components^1-3^. The agency issued its first draft guidance on AI for regulatory decision making in January 2025^4^, joined the European Medicines Agency in publishing ten guiding principles for good AI practice in drug development in January 2026^5,6^, and has now authorized 1,614 AI enabled medical devices^7^. The International Society for Pharmacoeconomics and Outcomes Research moved AI from the third ranked HEOR trend for 2024 to 2025 to the first ranked trend for 2026 to 2027^8^, and published a taxonomy, a reporting guideline, and a policy report for generative AI in HEOR within a single year^9-11^.

The second is that almost none of it has reached the documents on which reimbursement decisions are made. In a systematic audit of 1,391 health technology assessment (HTA) documents submitted to three agencies between 2023 and 2025, exactly three disclosed the use of AI or machine learning, an adoption rate of 0.2%^12^. When The Lancet editors checked every submission received during February 2024, 0.6% declared use of ChatGPT^13^.

That gap is a measurement problem before it is anything else, and the measurement problem is the subject of this first article. We do not have a defensible count of what has actually been done. Prior reviews have been deliberately partial. Lee and colleagues screened 148 records for wearable applications and included 32^14^, then sampled 161 of 805 records for non-wearable applications and included 92^15^. A 2026 scoping review of the economic aspects of machine learning in health care screened 6,332 references and included 18^16^, and a protocol for a review of machine learning in health economic evaluation screened 4,141 records and found 30 eligible reports^17^. Each answers a narrower question than the one practitioners now ask, which is how large the field is, what it is actually doing, and how fast its composition is changing.

The reason the answer matters beyond bibliometrics is that the standards now being written for AI in evidence generation are being written against an evidence base whose reliability nobody has quantified. All of the current frameworks are risk based, and all of them presume the submitter can characterize the risk. Yet the prediction model literature they inherit is dominated by high risk of bias: 545 of 606 COVID-19 prediction models were rated at high risk of bias^18^, as were 148 of 171 studies of machine learning based prediction models^19^.

This article therefore does three things. First, it reports an original systematic scoping review of the indexed literature following PRISMA-ScR, covering 2010 through 2025, with a full and reproducible search rather than a sample. Second, and unusually for a scoping review, it validates its own classification against an independent blinded classifier and reports the resulting error rates, because a bibliometric claim without a measured error rate is an assertion. Third, it sets the measured performance evidence for each HEOR workflow beside that map, so that the size and the quality of a literature can be read together. Part 2 takes up the regulatory, health technology assessment, and industry record, the economics of automation as it applies to this field, and a proposed reporting standard. The intended readers are the people who will have to defend this evidence: HEOR scientists and biostatisticians in industry and academia, HTA methodologists writing the next generation of position statements, and reviewers who will receive dossiers built with these tools whether or not the dossiers say so.

## Methods

We followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR). The protocol, all search strings, the classification dictionary, and the analysis code are archived in a public replication package^20^. No patient level data were used and no ethics approval was required.

### SEARCH STRATEGY AND ELIGIBILITY

We searched PubMed on 9 September 2026 using a structured Boolean query requiring co-occurrence of at least one AI term and at least one HEOR term in the title, abstract, or MeSH terms, restricted to publication years 2010 through 2025. AI terms covered artificial intelligence, machine learning, deep learning, neural networks, natural language processing, large language models, generative AI, and named model families. HEOR terms covered cost effectiveness, cost utility, economic evaluation, decision analytic modeling, budget impact, health technology assessment, real world evidence, comparative effectiveness, patient reported outcomes, utilities, quality adjusted life years, and health care resource utilization. The complete query strings are reproduced in eTable 1.

Records were eligible if they were journal articles, reviews, or conference proceedings published in English between 2010 and 2025 with a retrievable abstract. We excluded editorials, letters, comments, preprints, retracted publications, and records dated outside the window, and removed duplicates on PubMed identifier and normalized title.

To place the corpus in context we retrieved annual denominator series from PubMed using the same interface, reported in eTable 5. One discrepancy should be noted. The range form of the query returned 2,656 records where the sum of the sixteen per year queries was 2,929, a difference of 273, most likely from MedlineDate records counted in two calendar years. We used the per year series for trends and the range query for the PRISMA flow.

### CLASSIFICATION

Each included record was classified by a deterministic term dictionary applied to the concatenated title, abstract, and MeSH terms. The dictionary assigns eight non-exclusive application domains: economic evaluation; decision modeling and simulation; evidence synthesis; real-world data and causal inference; outcome and cost prediction; patient-reported outcomes and preferences; HTA, payer, and market access; and governance, reporting, and validity. It separately assigns a single most specific method category from six: generative AI and large language models; natural language processing before the generative era; deep learning; classical machine learning; artificial intelligence unspecified; and no AI method term identified. Domain labels are non-exclusive because a single paper frequently reports, for example, a natural language processing pipeline used to construct a cohort for a cost outcome. The full dictionary is given in eTable 2.

### VALIDATION OF THE CLASSIFIER

A dictionary is fast, transparent, and reproducible, and it is also wrong in ways that are invisible unless measured. We drew a simple random sample of 300 of the 2,476 included records and had an independent large language model classifier, blinded to the dictionary output and given only title and abstract, answer two questions: whether the record was genuinely relevant to HEOR as a practitioner would define it, and which of the same eight domains and six method categories applied. Prompts and raw outputs are archived.

We report, for every label, the number assigned by each classifier, observed agreement, Cohen kappa, prevalence-adjusted bias-adjusted kappa (PABAK), and the precision, recall, and F1 of the dictionary treating the blinded classifier as the reference. PABAK is reported alongside kappa because kappa is unstable at extreme prevalence and several labels are rare. We also report search precision, defined as the proportion of sampled records judged genuinely HEOR relevant, with an exact binomial 95% confidence interval, and a precision-adjusted corpus size obtained by applying that proportion and its interval to the full included count. We treat the blinded classifier as a reference standard, not as truth, and return to that choice in the Limitations.

### NARRATIVE EVIDENCE REVIEW

Alongside the bibliometric review we assembled a source grounded evidence base on the measured performance of AI in each HEOR workflow, requiring a primary study reporting a quantitative metric. Where a figure could not be confirmed from a retrieved page we recorded it as not available rather than estimating it. Grey literature without a digital object identifier is cited with the issuing organization, date, and uniform resource locator.

### STATISTICAL ANALYSIS

Counts are reported with percentages of the relevant denominator and confidence intervals for proportions are exact binomial (Clopper-Pearson). Growth is expressed as a ratio of endpoint counts. No hypothesis tests are reported for the bibliometric series because the series are complete counts rather than samples. Analyses used Python 3.11, with versions pinned in the replication package.

## Results

### THE SIZE AND SHAPE OF THE LITERATURE

The search identified 2,642 records. After removal of 14 duplicates, 2,628 were screened and 152 excluded: 70 without a retrievable abstract, 38 not in English, 19 editorials, 10 preprints, 7 letters, 4 retracted, and 4 with a publication year outside the window. This left 2,476 included records. Figure 1 presents the PRISMA-ScR flow, itemized in eTable 3, and Table 1 summarizes the corpus.

Annual output rose from 29 records in 2010 to 852 in 2025, a factor of 29.4, with the inflection at 2018 to 2019 rather than at the release of ChatGPT. The series was 29, 28, 47, 31, 34, 24, 23, 36, 48, 91, 130, 163, 232, 270, 438, and 852, the largest proportional increase being the rise of 89.6% from 2018 to 2019. Figure 2 shows the series against its denominators and eTable 4 gives counts per year by domain.

Two ratios matter more than the raw count. AI containing publications reached 6.0% of all indexed HEOR output in 2025, having been 0.8% in 2010, while HEOR fell to 0.86% of all indexed medical AI output, since PubMed indexed 110,494 AI in medicine records against 15,641 HEOR records that year. That asymmetry means HEOR will be a consumer of externally developed tools far more often than a producer of them, inheriting validation practices set elsewhere.

Domain composition is reported in Table 1 and mapped in Figure 3. Economic evaluation was the most frequently assigned domain, appearing in 1,559 of 2,476 records (63.0%), followed by real-world data and causal inference (496, 20.0%), governance, reporting, and validity (494, 20.0%), outcome and cost prediction (393, 15.9%), evidence synthesis (283, 11.4%), HTA, payer, and market access (209, 8.4%), decision modeling and simulation (115, 4.6%), and patient-reported outcomes and preferences (76, 3.1%). Two hundred seventy eight records (11.2%) carried no domain term. Method composition was artificial intelligence unspecified in 682 records (27.5%), classical machine learning in 615 (24.8%), deep learning in 445 (18.0%), no identifiable AI method term in 445 (18.0%), generative AI or large language models in 159 (6.4%), and pre-generative natural language processing in 130 (5.3%).

The generative series is empty before 2021, then 1, 4, 13, 38, and 103 records for 2021 through 2025. Growth is steep and the level is low: even in 2025 generative AI appeared in 12.1% of output. The fastest growing domain label in absolute terms was governance, reporting, and validity, which rose from 82 records in 2024 to 237 in 2025. The field is now writing more about how to govern these tools than it is publishing indexed applications of them.

Venues were highly dispersed across more than 900 distinct journals, led by Scientific Reports (79 records, 3.2%), Sensors (60, 2.4%), Cureus (43, 1.7%), Journal of Medical Internet Research (41, 1.7%), and Value in Health (32, 1.3%). That the field's own specialty journal accounts for 1.3% of the corpus is the important observation: the literature HEOR practitioners will be asked to appraise is overwhelmingly published outside HEOR venues and therefore reviewed by people who do not routinely apply HEOR reporting standards. eTable 6 lists the 40 most frequent journals.

Study designs were correspondingly weak on the dimensions HTA reviewers care about. Of 2,476 records, 674 (27.2%) were indexed as reviews and 121 (4.9%) as systematic reviews, against 38 (1.5%) randomized controlled trials and 17 (0.7%) validation studies. eTable 7 gives the full distribution.

### WHAT VALIDATION REVEALS

The blinded independent classification of 300 randomly sampled records produced the most consequential result in this review, and it is not a flattering one.

Only 154 of 300 sampled records (51.3%, 95% CI 45.7 to 56.9) were judged genuinely relevant to health economics and outcomes research. Applying that proportion to the corpus gives a precision-adjusted estimate of 1,271 genuinely HEOR relevant studies (95% CI 1,131 to 1,410) rather than 2,476. Precision was 52.4% (95% CI 46.5 to 58.3) among the 271 sampled records to which the dictionary had assigned at least one domain and 41.4% (95% CI 25.5 to 59.3) among the 29 to which it had assigned none, so the dictionary carries signal, but not nearly enough of it. Table 2 and Figure 4 report the validation in full, with the stratified precision in eTable 9.

Per label agreement was heterogeneous in a way that maps almost exactly onto how well specified each concept is. Agreement was substantial for real-world data and causal inference (Cohen kappa 0.729, observed agreement 90.3%, F1 79.1%) and moderate to substantial for evidence synthesis (kappa 0.666, F1 70.9%), decision modeling and simulation (kappa 0.579), HTA, payer, and market access (kappa 0.576), and governance, reporting, and validity (kappa 0.546). It was fair for outcome and cost prediction (kappa 0.453) and poor for patient-reported outcomes and preferences (kappa 0.306, F1 33.3%). Method classification agreed at kappa 0.667 across six categories and the generative AI flag at kappa 0.674. Full statistics are in eTable 8.

The exception should change how bibliometric claims about this field are read. For economic evaluation, the largest and fastest growing label in the corpus, Cohen kappa was 0.144 with observed agreement of 51.7% and PABAK of 0.033. The dictionary assigned this label to 186 of 300 sampled records; the blinded classifier assigned it to 69. Dictionary precision was 29.6% with recall 79.7%. In plain terms, the dictionary treats any paper that mentions cost, resource use, or efficiency as an economic evaluation, and roughly seven in ten of those are not economic evaluations in the sense a reimbursement reviewer would use.

Two implications follow. First, our own headline count of 1,559 economic evaluation records is an upper bound with an implied true value near 574 by the precision ratio, and any bibliometric claim about the growth of AI in health economic evaluation that does not report a measured classification error rate should be treated the same way. Second, the ranking of kappa values is a diagnostic of conceptual clarity in the field itself: real-world data and causal inference has a shared vocabulary and scores well, patient-reported outcomes and preferences does not and scores worst.

### EVIDENCE SYNTHESIS: THE BEST MEASURED WORKFLOW

Evidence synthesis is where the performance evidence is strongest and where it is most consistently misread. eTable 10 lists the screening studies. The best result in the literature is Matsui and colleagues, who applied GPT-4 to 1,381 and 3,146 record sets and reported adjusted sensitivity of 0.962 and specificity of 0.996 at about 110 records per minute and a cost of US$59^21^. It has not been reproduced at scale independently. Tran and colleagues, on 22,665 citations, reported sensitivity between 81.1% and 96.5% but specificity between 25.8% and 80.4%, generating 10,279 false positives in the worst configuration^22^. Oami and colleagues, on 16,669 citations, reported sensitivity of 0.85 and specificity of 0.98 but a median specificity gap of 0.48 across reviews^23^. Khraisha and colleagues found GPT-4 sensitivity of 0.42 with kappa 0.34 against human reviewer kappa of 0.77^24,25^.

Read together these say something actionable: sensitivity is acceptable, specificity is unstable across topics, and the variance between reviews exceeds the difference between models. That is the profile of a second screener with human adjudication, not of a sole screener. It is the conclusion of the joint position statement of Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence^26^, and why the ISPOR agentic framework reports screening F1 between 0.917 and 0.977 under a human in the loop design rather than an autonomous one^27^.

Data extraction performs better than screening, and eTable 11 gives the studies. Gartlehner and colleagues extracted 160 items with Claude 2 at 96.3% accuracy^28^ and Liu and colleagues reported 94.8% accuracy at 88 seconds per randomized trial^29^. The most informative study ran 12,814 extractions across 107 randomized trials and found Claude 3.5 at 96.2% accuracy against human extractors at 95.3% and human extraction assisted by the model at 97.9%, with extraction time falling from 86.9 minutes to 14.7^30^. The point is not that the model beat the humans, since the difference sits inside plausible noise. The point is that the combination beat both.

Downstream analytic steps automate as well. Reason and colleagues had GPT-4 write 30 R scripts to replicate published cost effectiveness models; in the non-small cell lung cancer set 14 of 15 scripts were error free, and every error free script reproduced the published incremental cost effectiveness ratio to within 1%^31,32^. A systematic review of generative AI in health economic evaluation screened 2,322 records and included 25 studies, of which 92% were conference abstracts and 96% were company authored^33^. That composition is the finding.

The economic case rests on a smaller base than the enthusiasm suggests. Abogunrin and colleagues found 17 of 25 studies reporting time reductions above 50%, against a per review cost above US$141,000^34,35^. The most honest comparison available is the ISPOR time and motion study of 234 publications: a hybrid human and AI workflow achieved 97.0% accuracy with 80.6% recall and 51.4% time savings, a fully automated workflow achieved 81.1% time savings with recall of only 48.4%, and unaided humans achieved 90.1% accuracy with 88.7% recall^27^. A workflow that misses half the eligible evidence is not 81% cheaper. It is a different study.

### REAL-WORLD DATA AND CAUSAL INFERENCE

This is the domain our validation ranked most coherent, and the domain where the evidence most directly contradicts the intuition that better prediction yields better inference. eTable 12 maps the methods.

The foundational result is Schneeweiss and colleagues on high dimensional propensity scores, where the estimated relative risk in a cohort of 49,653 users moved from 1.09 crude to 0.94 with fifteen investigator specified covariates and to 0.88 with 500 algorithmically selected covariates^36-38^. Benasseur and colleagues showed the failure mode plainly: high dimensional propensity score weighting produced bias of 0.094 with 23.6% confidence interval coverage where a modified procedure achieved bias of 0.018 with 91.4% coverage^39^. Coverage of 23.6% for a nominal 95% interval is not a subtle problem.

The machinery is mature. Targeted maximum likelihood estimation^40^, super learning^41^, causal forests^42^, and double or debiased machine learning^43^ are in routine use, and their translation into HEOR has been mapped through causal forests for heterogeneity in cost effectiveness analysis^44,45^, integration of decision modeling with machine learning based causal estimation^46^, a scoping review yielding 74 studies of heterogeneous treatment effect estimation with real-world data^47^, and transportability methods^48-50^.

What the field lacks is calibration of expectations, and the clearest demonstration is a trial emulation. Wang and colleagues emulated PARADIGM-HF in Veterans Affairs data, where the randomized hazard ratio was 0.81 (95% CI 0.61 to 1.06). A logistic propensity score model with area under the curve of 0.79 yielded 0.93; a gradient boosted model with area under the curve of 0.95 yielded 0.61^51^. The model with the best discrimination produced the estimate furthest from the trial benchmark. Propensity score models are not prediction problems, and optimizing separation of treated from untreated can degrade the covariate balance that identification requires. It is, however, exactly the inference a reviewer would draw from an area under the curve reported without a balance diagnostic, and it is why FDA guidance on real-world data declines to endorse any specific AI technology^52^, why the target trial framework has been recommended as the organizing discipline^53^, and why the PALISADE checklist was written^54^.

### UNSTRUCTURED DATA AND AI DERIVED ENDPOINTS

Approximately 80% of clinical data is unstructured, and this is the strongest affirmative case for AI in HEOR^55^. The gains are not marginal. Social and behavioral determinants recorded in claims at prevalences between 0.03% and 8.3% were recorded at between 1.40% and 36.3% once notes were processed, with lack of social support identifiable only from text in 99.8% of cases^56^. In an oncology cohort, 44 of 48 patients (91.7%) with adverse social determinants documented in text had no corresponding Z code^57^.

Performance on specific extraction tasks is good and uneven, as eTable 13 shows. Xu and colleagues, across 79,698 patients and 495,862 notes, achieved area under the receiver operating characteristic curve of 0.95 for performance status and found that imputed poor performance status carried a hazard ratio of 11.9^58^. A Veterans Affairs implementation reported 98.5% accuracy^59^ and programmed death ligand 1 extraction reached micro F1 of 0.925^60^, while one commercial oncology model reported precision of 98.8% for stage value but recall of only 79% for linking histology to neoplasm^61^, and in another registry task T stage extraction reached F1 of 0.89 while M stage reached 0.24^62^. The pattern is that the variable a cohort definition depends on is often the variable extracted worst.

Two results show why this matters for an estimate rather than for a metric. Varma and colleagues derived real-world progression free survival two ways in the same cohort and obtained 30 months from radiology reports against 23 months from clinical notes, with median real-world progression free survival of 20 months (95% CI 18 to 25) against 25 months (95% CI 15 to 35) by manual curation in a validation subset^63^. A seven month difference in a median attributable to which document type was read is a difference that changes a cost effectiveness result. Separately, adding natural language processing features raised propensity score model area under the curve from 0.66 to 0.77 and from 0.80 to 0.89 while the estimated hazard ratios barely moved, which is the PARADIGM-HF lesson in another guise.

Vendor validation frameworks have begun to respond. Flatiron Health published the VALID framework, requiring variable level benchmarking against expert human abstraction, internal consistency checks, replication, and subgroup stratified bias assessment^64,65^, and its machine learning extracted real-world response correlated with human abstraction at r = 0.86 in a test subset of 4,047^66-68^. Verantos and coauthors from Amgen, Johnson and Johnson, and GSK reported recall improving from 49.9% to 93.2% and completeness from 46.1% (95% CI 38.2 to 54.0) to 96.6% (95% CI 85.8 to 107.4)^69^. A reported confidence interval with an upper bound of 107.4% for a proportion is itself a reporting problem, and all of these validation efforts are authored by parties with a commercial interest in the result^70^.

The decisive gap is regulatory. FDA has accepted electronic health record derived real-world data in a label expansion, approving palbociclib for men with advanced breast cancer on the basis of records from three databases^71^. That establishes acceptance of an electronic health record derived source, not acceptance of an AI derived endpoint, and we were unable to document a single instance of any regulator or HTA body explicitly accepting or rejecting one as such. For a sponsor deciding whether to build a submission on real-world progression, that absence is the single most important fact in this series.

### DECISION MODELING, SIMULATION, AND SYNTHETIC DATA

Decision modeling is the smallest domain (115 records, 4.6%) and contains the cleanest efficiency results, because its tasks are computational rather than inferential. Metamodeling reduced an expected value of partial perfect information calculation requiring 12.5 million model runs from more than 1,000 days of brute force computation to about two days^72^, and automated model coding replicated published incremental cost effectiveness ratios to within 1%^11,31,73-75^.

Decision modeling is also the part of HEOR where uncertainty is already formalized, and therefore the part where AI is most easily disciplined. Otten and colleagues catalogued 80 methods for assessing uncertainty in decision analytic models, nearly all of which presuppose that the uncertainty has been quantified^76,77^, and that presupposition is what an opaque model breaks. Value of information analysis^78-81^ and the CHEERS 2022 requirement that inputs and their sources be reported^82^ define what an AI assisted model must still deliver.

Synthetic data is where the promise is largest and the reporting weakest, and eTable 14 collects the studies. The utility evidence is genuine: D'Amico and colleagues generated synthetic data for 7,133 patients with clinical fidelity of 93% and genomic fidelity of 90% and constructed a synthetic control arm of 187 matched patients^83,84^, and Wang and colleagues built AI generated digital twins from 6,736 subjects in Alzheimer disease in which 6,236 of 6,728 subjects with recorded race were White and 152 were Black^85^, a composition that determines what the resulting population can be used to claim.

Generator choice dominates the result. Akiya and colleagues found that classification and regression tree based generation produced synthetic data sets whose median progression free survival fell inside the real 95% confidence interval in 88.8% to 98.1% of replicates, against 6.5% to 37.8% for a conditional tabular generative adversarial network^86^. A generator that recovers the target quantity in 6.5% of replicates is not a lower quality version of one that recovers it in 98%; it is unusable for that purpose, and nothing in the summary statistics of the synthetic data would tell you which one you had. Reporting has not kept pace: of 73 studies, 70 (95%) evaluated utility while only 31 of 67 (46%) claiming a privacy purpose evaluated privacy, and only 8 of 73 (11%) used a differentially private generator^87^.

## Discussion

Two findings organize this first article, and both are about measurement.

The first is that the size of this literature is not known to within a factor of two. A corpus of 2,476 records reduces to approximately 1,271 genuinely HEOR relevant studies (95% CI 1,131 to 1,410) under blinded independent classification, and the label that grew fastest, economic evaluation, is the label our own classifier got most wrong (Cohen kappa 0.144, precision 29.6%). A count without an error rate is a marketing figure, and if a dictionary built specifically for this task and published in full achieves precision of 29.6% on the single most important label, then keyword based counts circulating in conference abstracts and market reports should be read as upper bounds of unknown looseness.

The second is a methodological finding that recurs in three independent places and should be stated as a rule. In the PARADIGM-HF emulation, a propensity model with area under the curve of 0.95 produced a hazard ratio of 0.61 against a trial value of 0.81, while a weaker model at 0.79 produced 0.93^51^. In the natural language processing augmented propensity work, discrimination rose substantially while the effect estimates barely moved. In drift monitoring across four deployed systems, calibration degraded before discrimination did^88^. The rule is that predictive performance is not evidentiary performance: HEOR quantities are calibrated, counterfactual, and decision relevant, and none of those properties is measured by a receiver operating characteristic curve. A dossier that reports model performance without reporting the sensitivity of the decision to that model has reported the wrong thing.

The two findings share a structure. Where a task has an observable answer, the gains are real, replicated, and often large: extraction accuracy against human abstraction at 96.2% against 95.3%^30^, screening recall against a human reference^27^, code generation against a published incremental cost effectiveness ratio^31^, and computation against brute force^72^. Where the answer is not observable, there is no reported instance of AI improving the accuracy of a cost effectiveness estimate, because accuracy of a cost effectiveness estimate is not measurable. The kappa ranking in our own validation reproduces the same division from the outside.

The consequence for practice is that the two layers should be governed differently. Clerical automation needs throughput and audit trails. Inferential use needs a decision level sensitivity analysis, because nothing else in the toolkit will detect the failure. Part 2 takes up what regulators and HTA agencies have actually said about this division, what industry reports, and what a reporting standard built for it would require.

### LIMITATIONS

We searched a single database. PubMed does not index much of the conference and grey literature where AI in HEOR is most active, and 92% of the studies in one review of generative AI in health economic evaluation were conference abstracts^33^, so our corpus understates operational activity.

Our classifier is a term dictionary and its errors are large, measured, and reported rather than hidden. Precision against blinded independent classification was 51.3% overall and 29.6% for economic evaluation, so all domain counts should be read as upper bounds.

Our reference standard is itself a large language model rather than a human expert panel. This is a genuine circularity in an article about the reliability of these tools, and it cuts both ways: the blinded classifier may be systematically strict about what counts as HEOR, in which case our precision estimate is too low, or lenient on unfamiliar subfields, in which case some labels are understated. A human dual review of the same 300 records is the correct next step, and the sample and both label sets are archived so that anyone may perform it^20^.

Our denominator series contains an unresolved discrepancy of 273 records between the range query and the sum of per year queries, and we restricted to English language records, which biases the corpus toward North American and European practice^89^.

## Conclusions

The literature on artificial intelligence in health economics and outcomes research has grown by a factor of 29 since 2010 and reached 852 indexed records in 2025. Under blinded independent classification, approximately half of it is about something else, and the fastest growing label is the one that can least reliably be assigned. Thirty eight of 2,476 records were randomized trials and 17 were validation studies. No regulator or health technology assessment body has yet been documented accepting or rejecting an AI derived endpoint as such.

The measured gains are concentrated where ground truth is observable, which is to say in the clerical layer, and they are absent where the quantity of interest is a counterfactual. That division is stable across every workflow reviewed here, and it is the reason a scoping review of this field has to report its own error rate before it reports anything else. Part 2 asks what the regulatory and submission record says about the same division, and what reporting would make it auditable.

## Disclosures

The author reports no conflicts of interest related to this work. No funding was received for this study. The author is affiliated with an academic institution and a health economics consultancy that conducts real-world evidence studies for pharmaceutical and life sciences clients; no client had any role in the conception, conduct, analysis, or reporting of this review, and no client reviewed the manuscript before submission.

The large language model classifier described in the Methods is a measured object of study in this review rather than an assistive writing tool. Its prompts, inputs, and outputs are archived in the replication package. No AI tool is listed as an author.

## Data Availability

All search strings, retrieved records, the classification dictionary, the blinded classifier prompts and outputs, the analysis scripts, the figure generation code, and the complete reference library are available in the public replication package^20^. No individual patient data were used.

## Author Affiliations

¹ Department of Internal Medicine, University of Michigan, Ann Arbor, Michigan

² Graduate School of Public Health and Health Policy, City University of New York, New York, New York

## Figures

**Figure 1. PRISMA-ScR flow of study identification, screening, and inclusion.** Records identified in PubMed for publication years 2010 through 2025, with duplicate removal, itemized exclusions, and the 2,476 included records. The precision-adjusted corpus estimate derived from blinded independent classification of 300 randomly sampled included records is shown for comparison.

**Figure 2. Growth and composition of the AI and HEOR literature, 2010 to 2025, against its denominators.** Panel A shows publication volume on a logarithmic scale for the included corpus, for all indexed medical AI publications, and for all indexed HEOR publications. Panel B shows the penetration of each literature into the other, that is AI containing HEOR publications as a percentage of all indexed HEOR publications, which reached 6.0% in 2025, and HEOR publications as a percentage of all indexed medical AI publications, which reached 0.86%. Panel C shows the method family composition of the included corpus as a percentage of records per year, with generative AI and large language models, pre-generative natural language processing, deep learning, classical machine learning, artificial intelligence unspecified, and records with no AI method term in the abstract.

**Figure 3. Evidence map of AI applications across HEOR tasks.** Panel A cross-tabulates the eight application domains against the six method families; cell values are counts of included records and domain labels are non-exclusive, so rows do not sum to the corpus. Panel B gives the domain total for each row, with the precision-adjusted total shown as an inner bar so that the measured and the nominal size of each literature can be read together.

**Figure 4. Validation of the term dictionary against blinded independent classification of 300 randomly sampled included records.** Panel A shows Cohen kappa for agreement on each HEOR task domain, annotated with the number of records the dictionary and the blinded classifier each assigned to that domain, and shaded by the conventional interpretive bands for fair, moderate, and substantial agreement. Panel B shows search precision overall and stratified by whether the dictionary assigned at least one domain label or none, with exact binomial 95% confidence intervals. Full agreement statistics, including prevalence-adjusted bias-adjusted kappa, precision, recall, and F1, are given in Table 2 and eTable 8.

## Tables

**Table 1.** Characteristics of the included corpus: annual output, application domains, method categories, leading journals, and indexed publication types (n = 2,476).

**Table 2.** Validation of the classification against blinded independent classification of 300 randomly sampled records: per label counts, observed agreement, Cohen kappa, PABAK, precision, recall, and F1, with search precision and the precision-adjusted corpus estimate.

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

14. Lee W, Schwartz N, Bansal A, Khor S, Hammarlund N, Basu A, et al. A Scoping Review of the Use of Machine Learning in Health Economics and Outcomes Research: Part 1: Data From Wearable Devices. Value in Health 2023;26(2):292-299. DOI: 10.1016/j.jval.2022.08.005.

15. Lee W, Schwartz N, Bansal A, Khor S, Hammarlund N, Basu A, et al. A Scoping Review of the Use of Machine Learning in Health Economics and Outcomes Research: Part 2: Data From Nonwearables. Value in Health 2022;25(12):2053-2061. DOI: 10.1016/j.jval.2022.07.011.

16. von GH, Helenius M, Hörhammer I, Moen H, Peltonen L. Scoping review on the economic aspects of machine learning applications in healthcare. International Journal of Medical Informatics 2026;205:106103. DOI: 10.1016/j.ijmedinf.2025.106103.

17. Daghash H, Kernohan A, Brownson-Smith R, Pandey R, Ananthakrishnan A, Cong C, et al. Machine Learning in Health Economic Evaluations: Protocol for a Scoping Review. JMIR Res Protoc 2025;14:e77494. DOI: 10.2196/77494.

18. Wynants L, Van CB, Collins GS, Riley RD, Heinze G, Schuit E, et al. Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal. BMJ 2020:m1328. DOI: 10.1136/bmj.m1328.

19. Andaur NCL, Damen JAA, Takada T, Nijman SWJ, Dhiman P, Ma J, et al. Risk of bias in studies on prediction models developed using supervised machine learning techniques: systematic review. BMJ 2021:n2281. DOI: 10.1136/bmj.n2281.

20. Baser O. Replication package for Artificial Intelligence in Health Economics and Outcomes Research: A Systematic Scoping Review. GitHub repository; 2026. Available at: https://github.com/obaser/ai-heor-scoping-review

21. Matsui K, Utsumi T, Aoki Y, Maruki T, Takeshima M, Takaesu Y. Human-Comparable Sensitivity of Large Language Models in Identifying Eligible Studies Through Title and Abstract Screening: 3-Layer Strategy Using GPT-3.5 and GPT-4 for Systematic Reviews. J Med Internet Res 2024;26:e52758. DOI: 10.2196/52758.

22. Tran V, Gartlehner G, Yaacoub S, Boutron I, Schwingshackl L, Stadelmaier J, et al. Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses. Ann Intern Med 2024;177(6):791-799. DOI: 10.7326/m23-3389.

23. Oami T, Okada Y, Nakada T. GPT-3.5 Turbo and GPT-4 Turbo in Title and Abstract Screening for Systematic Reviews. JMIR Med Inform 2025;13:e64682-e64682. DOI: 10.2196/64682.

24. Khraisha Q, Put S, Kappenberg J, Warraitch A, Hadfield K. Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages. Research Synthesis Methods 2024;15(4):616-626. DOI: 10.1002/jrsm.1715.

25. Nykvist B, Macura B, Xylia M, Olsson E. Testing the utility of GPT for title and abstract screening in environmental systematic evidence synthesis. Environ Evid 2025;14(1):7. DOI: 10.1186/s13750-025-00360-x.

26. Flemyng E, Noel-Storr A, Macura B, Gartlehner G, Thomas J, Meerpohl JJ, et al. Position statement on artificial intelligence (AI) use in evidence synthesis across Cochrane, the Campbell Collaboration, JBI and the Collaboration for Environmental Evidence 2025. Environ Evid 2025;14(1):20. DOI: 10.1186/s13750-025-00374-5.

27. Lee K, Paek H, Ofoegbu N, Rube S, Higashi MK, Dawoud D, et al. A4SLR: An Agentic Artificial Intelligence-Assisted Systematic Literature Review Framework to Augment Evidence Synthesis for Health Economics and Outcomes Research and Health Technology Assessment. Value in Health 2025;28(11):1655-1664. DOI: 10.1016/j.jval.2025.08.002.

28. Gartlehner G, Kahwati L, Hilscher R, Thomas I, Kugley S, Crotty K, et al. Data extraction for evidence synthesis using a large language model: A proof-of-concept study. Research Synthesis Methods 2024;15(4):576-589. DOI: 10.1002/jrsm.1710.

29. Liu J, Lai H, Zhao W, Huang J, Xia D, Liu H, et al. AI-driven evidence synthesis: data extraction of randomized controlled trials with large language models. International Journal of Surgery 2025;111(3):2722-2726. DOI: 10.1097/js9.0000000000002215.

30. Lai H, Liu J, Bai C, Liu H, Pan B, Luo X, et al. Language models for data extraction and risk of bias assessment in complementary medicine. npj Digit. Med. 2025;8(1):74. DOI: 10.1038/s41746-025-01457-w.

31. Reason T, Rawlinson W, Langham J, Gimblett A, Malcolm B, Klijn S. Artificial Intelligence to Automate Health Economic Modelling: A Case Study to Evaluate the Potential Application of Large Language Models. PharmacoEconomics Open 2024;8(2):191-203. DOI: 10.1007/s41669-024-00477-8.

32. Reason T, Benbow E, Langham J, Gimblett A, Klijn SL, Malcolm B. Artificial Intelligence to Automate Network Meta-Analyses: Four Case Studies to Evaluate the Potential Application of Large Language Models. PharmacoEconomics Open 2024;8(2):205-220. DOI: 10.1007/s41669-024-00476-9.

33. Sharp S, Lokuge K, Elvidge J, Hudson T, Dawoud D. Systematic literature review of the use of generative AI in health economic evaluation. 2025. DOI: 10.1101/2025.04.25.25326412.

34. Abogunrin S, Muir JM, Zerbini C, Sarri G. How much can we save by applying artificial intelligence in evidence synthesis? Results from a pragmatic review to quantify workload efficiencies and cost savings. Front. Pharmacol. 2025;16:1454245. DOI: 10.3389/fphar.2025.1454245.

35. Michelson M, Reuter K. The significant cost of systematic reviews and meta-analyses: A call for greater involvement of machine learning to assess the promise of clinical trials. Contemporary Clinical Trials Communications 2019;16:100443. DOI: 10.1016/j.conctc.2019.100443.

36. Schneeweiss S, Rassen JA, Glynn RJ, Avorn J, Mogun H, Brookhart MA. High-dimensional Propensity Score Adjustment in Studies of Treatment Effects Using Health Care Claims Data. Epidemiology 2009;20(4):512-522. DOI: 10.1097/ede.0b013e3181a663cc.

37. Guertin JR, Rahme E, LeLorier J. Performance of the high-dimensional propensity score in adjusting for unmeasured confounders. Eur J Clin Pharmacol 2016;72(12):1497-1505. DOI: 10.1007/s00228-016-2118-x.

38. Pang M, Schuster T, Filion KB, Eberg M, Platt RW. Targeted Maximum Likelihood Estimation for Pharmacoepidemiologic Research. Epidemiology 2016;27(4):570-577. DOI: 10.1097/ede.0000000000000487.

39. Benasseur I, Talbot D, Durand M, Holbrook A, Matteau A, Potter BJ, et al. A comparison of confounder selection and adjustment methods for estimating causal effects using large healthcare databases. Pharmacoepidemiology and Drug 2022;31(4):424-433. DOI: 10.1002/pds.5403.

40. van DLMJ, Rubin D. Targeted Maximum Likelihood Learning. The International Journal of Biostatistics 2006;2(1). DOI: 10.2202/1557-4679.1043.

41. van DLMJ, Polley EC, Hubbard AE. Super Learner. Statistical Applications in Genetics and Molecular Biology 2007;6(1). DOI: 10.2202/1544-6115.1309.

42. Wager S, Athey S. Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association 2018;113(523):1228-1242. DOI: 10.1080/01621459.2017.1319839.

43. Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, et al. Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal 2018;21(1):C1-C68. DOI: 10.1111/ectj.12097.

44. Bonander C, Svensson M. Using causal forests to assess heterogeneity in cost-effectiveness analysis. Health Economics 2021;30(8):1818-1832. DOI: 10.1002/hec.4263.

45. Zhang Y, Kreif N, GC VS, Manca A. Machine Learning Methods to Estimate Individualized Treatment Effects for Use in Health Technology Assessment. Med Decis Making 2024;44(7):756-769. DOI: 10.1177/0272989x241263356.

46. Glynn D, Giardina J, Hatamyar J, Pandya A, Soares M, Kreif N. Integrating decision modeling and machine learning to inform treatment stratification. Health Economics 2024;33(8):1772-1792. DOI: 10.1002/hec.4834.

47. Möller M, Wild E, Tan W, Schreyögg J. Estimating Heterogeneous Treatment Effects With Real-World Health Data: A Scoping Review of Machine Learning Methods. Value in Health 2026;29(5):905-913. DOI: 10.1016/j.jval.2026.01.013.

48. Manke-Reimers F, Brugger V, Bärnighausen T, Kohler S. When, why and how are estimated effects transported between populations? A scoping review of studies applying transportability methods. Eur J Epidemiol 2025;40(3):255-273. DOI: 10.1007/s10654-025-01217-w.

49. Turner AJ, Sammon C, Latimer N, Adamson B, Beal B, Subbiah V, et al. Transporting Comparative Effectiveness Evidence Between Countries: Considerations for Health Technology Assessments. PharmacoEconomics 2023;42(2):165-176. DOI: 10.1007/s40273-023-01323-1.

50. Weise A, Büchter RB, Pieper D, Mathes T. Assessing transferability in systematic reviews of health economic evaluations, a review of methodological guidance. BMC Med Res Methodol 2022;22(1):52. DOI: 10.1186/s12874-022-01536-6.

51. Wang K, Rosman LA, Lu H. Machine Learning Versus Logistic Regression for Propensity Score Estimation: A Benchmark Trial Emulation Against the PARADIGM-HF Randomized Trial. 2025. DOI: 10.1101/2025.06.16.25329708.

52. US Food and Drug Administration. Real-World Data: Assessing Electronic Health Records and Medical Claims Data To Support Regulatory Decision-Making for Drug and Biological Products. Guidance for industry. Docket FDA-2020-D-2307. July 2024. Available at: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/real-world-data-assessing-electronic-health-records-and-medical-claims-data-support-regulatory

53. Gruber S, Phillips RV, Lee H, Concato J, van DLM. Evaluating and improving real-world evidence with Targeted Learning. BMC Med Res Methodol 2023;23(1):178. DOI: 10.1186/s12874-023-01998-2.

54. Padula WV, Kreif N, Vanness DJ, Adamson B, Rueda J, Felizzi F, et al. Machine Learning Methods in Health Economics and Outcomes Research: The PALISADE Checklist: A Good Practices Report of an ISPOR Task Force. Value in Health 2022;25(7):1063-1080. DOI: 10.1016/j.jval.2022.03.022.

55. Patra BG, Sharma MM, Vekaria V, Adekkanattu P, Patterson OV, Glicksberg B, et al. Extracting social determinants of health from electronic health records using natural language processing: a systematic review. Journal of the American Medical Informatics Association 2021;28(12):2716-2727. DOI: 10.1093/jamia/ocab170.

56. Kharrazi H, Anzaldi LJ, Hernandez L, Davison A, Boyd CM, Leff B, et al. The Value of Unstructured Electronic Health Record Data in Geriatric Syndrome Case Identification. J American Geriatrics Society 2018;66(8):1499-1507. DOI: 10.1111/jgs.15411.

57. Guevara M, Chen S, Thomas S, Chaunzwa TL, Franco I, Kann BH, et al. Large language models to identify social determinants of health in electronic health records. npj Digit. Med. 2024;7(1):6. DOI: 10.1038/s41746-023-00970-0.

58. Xu W, Gu B, Lotter WE, Kehl KL. Extraction and Imputation of Eastern Cooperative Oncology Group Performance Status From Unstructured Oncology Notes Using Language Models. JCO Clin Cancer Inform 2024:e2300269. DOI: 10.1200/cci.23.00269.

59. Maghsoudi A, Sada YH, Nowakowski S, Guffey D, Zhu H, Yarlagadda SR, et al. A Multi-Institutional Natural Language Processing Pipeline to Extract Performance Status From Electronic Health Records. Cancer Control 2024;31:10732748241279518. DOI: 10.1177/10732748241279518.

60. Lin E, Zwolinski R, Wu JT, La J, Goryachev S, Huhmann L, et al. Machine learning-based natural language processing to extract PD-L1 expression levels from clinical notes. Health Informatics J 2023;29(3):14604582231198021. DOI: 10.1177/14604582231198021.

61. Kenney RC, Chen X, Shintani K, Gagnon C, Liu J, DaCosta BS, et al. Validation of Non-Small Cell Lung Cancer Clinical Insights Using a Generalized Oncology Natural Language Processing Model. JCO Clin Cancer Inform 2024:e2300099. DOI: 10.1200/cci.23.00099.

62. Abedian S, Sholle ET, Adekkanattu PM, Cusick MM, Weiner SE, Shoag JE, et al. Automated Extraction of Tumor Staging and Diagnosis Information From Surgical Pathology Reports. JCO Clinical Cancer Informatics 2021:1054-1061. DOI: 10.1200/cci.21.00065.

63. Varma G, Yenukoti RK, Kumar MP, Ashrit BS, Purushotham K, Subash C, et al. A Deep Learning-Enabled Workflow to Estimate Real-World Progression-Free Survival in Patients With Metastatic Breast Cancer: Study Using Deidentified Electronic Health Records. JMIR Cancer 2025;11:e64697-e64697. DOI: 10.2196/64697.

64. Estevez M, Singh N, Dyson L, Adamson B, Krismer K, Magee K, et al. Ensuring Reliability of Curated Electronic Health Record-Derived Data: The Validation of Accuracy for Large Language Model-/Machine Learning-Extracted Information and Data (VALID) Framework. JCO Clin Cancer Inform 2026;10(1):e2500215. DOI: 10.1200/cci-25-00215.

65. Flatiron Health. Flatiron Health publishes first peer-reviewed validation framework for AI-extracted real-world oncology data. Press release. Available at: https://resources.flatiron.com/press/flatiron-health-publishes-first-peer-reviewed-validation-framework-for-ai-extracted-real-world-oncology-data-in-journal-of-clinical-oncology

66. Ma X, Bellomo L, Magee K, Bennette CS, Tymejczyk O, Samant M, et al. Characterization of a Real-World Response Variable and Comparison with RECIST-Based Response Rates from Clinical Trials in Advanced NSCLC. Adv Ther 2021;38(4):1843-1859. DOI: 10.1007/s12325-021-01659-0.

67. Development and validation of a machine learning approach to scale real-world response in oncology. Poster presented at ISPOR. Available at: https://www.ispor.org/docs/default-source/cti-meeting-21021-documents/6f2aef20-5193-4ad1-b198-1156a7ea80f7.pdf

68. Flatiron Health. Flatiron Health research on AI-driven cancer progression extraction presented at AACR Special Conference in Cancer Research: Artificial Intelligence. Press release. Available at: https://resources.flatiron.com/press/flatiron-health-research-on-ai-driven-cancer-progression-extraction-presented-at-aacr-special-conference-in-cancer-research-artificial-intelligence

69. Riskin DJ, Monda KL, Gagne JJ, Reynolds R, Garan AR, Dreyer N, et al. Implementing Accuracy, Completeness, and Traceability for Data Reliability. JAMA Netw Open 2025;8(3):e250128. DOI: 10.1001/jamanetworkopen.2025.0128.

70. Truveta. Truveta Studio and data quality. Presentation at ISPOR Europe 2024. Available at: https://www.ispor.org/docs/default-source/euro2024/ispor-eu-2024---truveta-final.pdf

71. Pfizer. US FDA approves IBRANCE (palbociclib) for the treatment of men with HR+, HER2- metastatic breast cancer. Press release. Available at: https://www.pfizer.com/news/press-release/press-release-detail/u_s_fda_approves_ibrance_palbociclib_for_the_treatment_of_men_with_hr_her2_metastatic_breast_cancer

72. Degeling K, IJzerman MJ, Lavieri MS, Strong M, Koffijberg H. Introduction to Metamodeling for Reducing Computational Burden of Advanced Analyses with Health Economic Models: A Structured Overview of Metamodeling Methods in a 6-Step Application Process. Med Decis Making 2020;40(3):348-363. DOI: 10.1177/0272989x20912233.

73. Fleurence, R, Bian, J, Wang, X, Xu, H, Dawoud, D, Higashi, M, et al. Generative AI for Health Technology Assessment: Opportunities, Challenges, and Policy Considerations. arXiv 2024. DOI: 10.48550/arxiv.2407.11054.

74. Hasan B, Saadi S, Rajjoub NS, Hegazi M, Al-Kordi M, Fleti F, et al. Integrating large language models in systematic reviews: a framework and case study using ROBINS-I for risk of bias assessment. BMJ EBM 2024;29(6):394-398. DOI: 10.1136/bmjebm-2023-112597.

75. Qureshi R, Shaughnessy D, Gill KAR, Robinson KA, Li T, Agai E. Are ChatGPT and large language models “the answer” to bringing us closer to systematic review automation? Syst Rev 2023;12(1):72. DOI: 10.1186/s13643-023-02243-z.

76. Otten TM, Grimm SE, Ramaekers B, Joore MA. Comprehensive Review of Methods to Assess Uncertainty in Health Economic Evaluations. PharmacoEconomics 2023;41(6):619-632. DOI: 10.1007/s40273-023-01242-1.

77. Bojke L, Claxton K, Sculpher M, Palmer S. Characterizing Structural Uncertainty in Decision Analytic Models: A Review and Application of Methods. Value in Health 2009;12(5):739-749. DOI: 10.1111/j.1524-4733.2008.00502.x.

78. Fenwick E, Steuten L, Knies S, Ghabri S, Basu A, Murray JF, et al. Value of Information Analysis for Research Decisions: An Introduction: Report 1 of the ISPOR Value of Information Analysis Emerging Good Practices Task Force. Value in Health 2020;23(2):139-150. DOI: 10.1016/j.jval.2020.01.001.

79. Rothery C, Strong M, Koffijberg H, Basu A, Ghabri S, Knies S, et al. Value of Information Analytical Methods: Report 2 of the ISPOR Value of Information Analysis Emerging Good Practices Task Force. Value in Health 2020;23(3):277-286. DOI: 10.1016/j.jval.2020.01.004.

80. Sculpher M, Claxton K. Establishing the Cost-Effectiveness of New Pharmaceuticals under Conditions of Uncertainty: When Is There Sufficient Evidence? Value in Health 2005;8(4):433-446. DOI: 10.1111/j.1524-4733.2005.00033.x.

81. Fenwick E, Claxton K, Sculpher M. The Value of Implementation and the Value of Information: Combined and Uneven Development. Med Decis Making 2007;28(1):21-32. DOI: 10.1177/0272989x07308751.

82. Husereau D, Drummond M, Augustovski F, de BE, Briggs AH, Carswell C, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) Statement: Updated Reporting Guidance for Health Economic Evaluations. Value in Health 2022;25(1):3-9. DOI: 10.1016/j.jval.2021.11.1351.

83. D'Amico S, Dall’Olio D, Sala C, Dall’Olio L, Sauta E, Zampini M, et al. Synthetic Data Generation by Artificial Intelligence to Accelerate Research and Precision Medicine in Hematology. JCO Clinical Cancer Informatics 2023:e2300021. DOI: 10.1200/cci.23.00021.

84. Elvatun S, Knoors D, Brant S, Jonasson C, Nygård JF. Synthetic data as external control arms in scarce single-arm clinical trials. PLOS Digit Health 2025;4(1):e0000581. DOI: 10.1371/journal.pdig.0000581.

85. Wang D, Florian H, Lynch S, Robieson W, Zhuang R, Kusiak C, et al. Using AI-generated digital twins to boost clinical trial efficiency in Alzheimer's disease. A&D Transl Res & Clin Interv 2025;11(4):e70181. DOI: 10.1002/trc2.70181.

86. Akiya I, Ishihara T, Yamamoto K. Comparison of Synthetic Data Generation Techniques for Control Group Survival Data in Oncology Clinical Trials: Simulation Study. JMIR Med Inform 2024;12:e55118-e55118. DOI: 10.2196/55118.

87. Kaabachi B, Despraz J, Meurers T, Otte K, Halilovic M, Kulynych B, et al. A scoping review of privacy and utility metrics in medical synthetic data. npj Digit. Med. 2025;8(1):60. DOI: 10.1038/s41746-024-01359-3.

88. Kopanitsa G. Validation is not enough: Longitudinal evidence of post-deployment fragility in clinical AI systems. PLOS Digit Health 2026;5(7):e0001534. DOI: 10.1371/journal.pdig.0001534.

89. Artificial intelligence tools in health technology assessment: a scoping review. Conference proceeding OP07. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC11718724/

