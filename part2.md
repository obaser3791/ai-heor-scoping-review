---
title: "Faster but Not Truer, Part 2: The Regulatory Record, the Economics, and the TRACE-HEOR Reporting Standard"
subtitle: "What Is Claimed, What Is Disclosed, and What Reviewers Need"
author: "Onur Baser, Ph.D."
type: "Review"
series: "Part 2 of a two part series"
---

**Onur Baser, Ph.D.**^1,2^

^1^Department of Internal Medicine, University of Michigan, Ann Arbor, MI
^2^Graduate School of Public Health and Health Policy, City University of New York, New York, NY

The author affiliations are listed at the end of the article.

This is the second of two articles. Part 1 measured the literature on artificial intelligence in health economics and outcomes research and validated its own classification. Part 2 assembles the regulatory, health technology assessment, and industry record, examines what the economics of automation implies for this field, and proposes a reporting standard.

## Short Summary

Pharmaceutical companies report time savings of 40% to 97% from artificial intelligence in regulatory and evidence work. Three of 1,391 health technology assessment documents disclose using it. This second article of a two part series sets the claims against the record: what the Food and Drug Administration and European regulators have written, what agencies have accepted, what industry has published, and how these tools fail. It reads the gap through the productivity arithmetic of Nobel laureate Daron Acemoglu, whose distinction between tasks with observable answers and tasks without one predicts the pattern almost exactly, and it proposes TRACE-HEOR, ten reporting items whose central requirement is a decision reversal analysis.

## Abstract

**BACKGROUND**

Part 1 of this series found that measured gains from artificial intelligence (AI) in health economics and outcomes research (HEOR) concentrate in tasks with observable ground truth and disappear where the quantity of interest is a counterfactual. What regulators, health technology assessment (HTA) bodies, and sponsors have said about that division has not been assembled in one place.

**METHODS**

We assembled the primary regulatory, HTA, industry, and journal policy record through September 2026, requiring for each claim a named primary source and, where a quantity was reported, its provenance and whether the reporting party had a commercial interest. We downloaded the Food and Drug Administration (FDA) AI enabled medical device list in full, tabulated published economic evaluations of AI, and set reported industry efficiency gains against disclosed use in submissions. We then evaluated the field against the task based productivity framework of Nobel laureate Daron Acemoglu and derived a reporting standard from the documented failure modes.

**RESULTS**

The FDA has authorized 1,614 AI enabled devices, 1,230 (76.2%) in radiology, rising from 18 in 2016 to 335 in 2025, and has received more than 500 drug and biologic submissions containing AI components since 2016; its January 2025 credibility assessment guidance remains a draft and excludes discovery and operational uses. Industry reports time savings of 40% to 97% in regulatory writing and approximately 80% in payer dossier drafting, every figure single arm and reported by the deploying or selling party. Disclosed AI use is 3 of 1,391 HTA documents (0.2%) and 0.6% of one journal's submissions, against surveys reporting use between 25% and 81%. Nineteen economic evaluations of AI have been published against 1,614 authorized devices. No regulator or HTA body has been documented accepting or rejecting an AI derived endpoint as such.

**CONCLUSIONS**

Current disclosure instruments ask whether AI wrote the text. Reviewers need to know whether AI selected the evidence, defined the cohort, derived the endpoint, or generated the code, and whether the recommendation would change without it.

## Introduction

Part 1 of this series reported a systematic scoping review of 2,476 indexed studies on artificial intelligence in health economics and outcomes research published between 2010 and 2025, and measured the error rate of its own classification against a blinded independent classifier. Two findings carry forward. First, the size of this literature is not known to within a factor of two: the corpus reduces to approximately 1,271 genuinely HEOR relevant studies (95% confidence interval [CI] 1,131 to 1,410), and the fastest growing label, economic evaluation, is the one that could least reliably be assigned (Cohen kappa 0.144). Second, measured gains concentrate in tasks with an observable answer and are absent where the quantity of interest is a counterfactual^1-3^.

That division sorts the field into two layers. A clerical layer, comprising screening, extraction, code drafting, and dossier assembly, has measurable ground truth and documented gains. An inferential layer, comprising cohort definition, endpoint derivation, confounder selection, and effect estimation, has no supervised target, because no patient is observed under both the treatment and the comparator. The two layers carry different risks and should be governed differently.

This second article asks what the institutional record says about that distinction. Regulators come first, because a reimbursement dossier is a regulated document and because the FDA has written the most developed framework while becoming one of the largest users of these tools. HTA agencies come second, because they will absorb whatever the automation produces. Industry comes third, because the efficiency claims driving adoption originate there and almost none has been independently replicated. We then turn to how these systems fail, to what productivity economics predicts for a field whose central quantity is unobservable, and to what reporting would make an AI assisted submission auditable.

## Methods

The review methods, search strategy, classification dictionary, and validation procedure are reported in full in Part 1 and archived in the public replication package^4^. This article draws on the narrative evidence review conducted alongside that scoping review.

For the regulatory, HTA, industry, and journal policy record we searched agency, society, and company sources through September 2026 and required a named primary source for every claim. Where a quantity was reported we recorded its provenance, whether a peer reviewed study, a conference abstract, a regulatory document, or a company communication, and whether the reporting party had a commercial interest in the result. Conference abstracts and vendor communications are labelled rather than excluded, because in this field they carry information available nowhere else.

We downloaded the FDA AI enabled medical device list in full and tabulated authorizations by year and specialty in eTable 2. Published economic evaluations of AI in health care appear in eTable 1, industry efficiency claims with their provenance in eTable 3, journal and society policies in eTable 4, and survey estimates of use and proficiency in eTable 5. Figure 1 places the instruments on a common timeline.

## Results

### THE REGULATORY RECORD

The FDA's position is the most developed and the least finished. Table 1 summarizes the instruments now in force or in draft.

For drugs and biologics, the January 2025 draft guidance proposes a seven step credibility assessment framework in which a sponsor defines the question of interest, the context of use, and the model risk, then establishes credibility proportionate to that risk^5^. The definition of model risk is the operative sentence: "Model risk is a combination of two factors: (a) model influence... and (b) decision consequence." Two features are routinely missed. The guidance explicitly excludes AI used in drug discovery and in operational efficiencies, so most publicly announced pharmaceutical AI deployments fall outside it. And it remains a draft as of September 2026, with the comment period closed on 7 April 2025. The agency's account of the evidence behind it names an FDA sponsored workshop convened by the Duke Margolis Institute for Health Policy in December 2022, more than 800 comments from 65 entities, and experience with more than 500 submissions containing AI components since 2016^6,7^. PhRMA asked the agency to clarify which device provisions apply, how human in the loop mitigation affects the risk assessment, and how models composed of multiple models are treated^8^, a fair summary of what the framework does not yet answer.

For devices the record is quantitative. We downloaded the FDA AI enabled medical device list in full: 1,614 authorizations current as of 4 September 2026, of which 1,230 (76.2%) are in radiology, 154 (9.5%) in cardiovascular, and 73 (4.5%) in neurology, rising from 18 authorizations in 2016 to 335 in 2025 and 181 in the first eight months of 2026^9^. The January 2025 draft guidance on AI enabled device software functions asks for validation at "at least three geographically diverse US clinical sites" with two sided 95% confidence intervals^10,11^. The concentration in radiology is the number a health economist should notice: three quarters of authorized AI in American medicine operates in one specialty, so the cost effectiveness literature is being asked to generalize from a narrow deployment base.

The agency is also now a user. Elsa was deployed agency wide in June 2025 on a FedRAMP High environment, with the explicit statement that it does not train on data submitted by regulated industry^12^. A regulator that uses these tools internally will develop views about their failure modes faster than one that only reviews them.

The European position is more prescriptive on one dimension. The European Medicines Agency reflection paper states that "the use of transparent models is preferred"^13^, a preference the National Institute for Health and Care Excellence (NICE) echoes in requiring that where more explainable methods are potentially robust "those should be presented in the first instance, with supplementary use of less transparent approaches"^14^. The EU AI Act entered into force on 1 August 2024 with general purpose AI obligations applying from 2 August 2026^15^, and EFPIA has argued that AI used solely for medicines research and development is exempt under Recital 25 and Articles 2.6 and 2.8^16^. Industry association frameworks converge on similar content^17-19^.

Payer side regulation has moved faster than either. The Centers for Medicare and Medicaid Services stated in February 2024 that "algorithms or artificial intelligence alone cannot be used as the basis to deny admission" in Medicare Advantage^20^, and California enacted Senate Bill 1120 requiring physician review of medical necessity determinations^21^. World Health Organization guidance on large multi-modal models notes hallucination rates of "at least 3 percent" and "as high as 27 percent"^22,23^. The asymmetry is worth stating plainly: using AI to deny care is now regulated in US statute, while using AI to generate the evidence that determines whether care is covered at all is governed by voluntary position statements.

### THE HTA RECORD

Table 2 sets the claims against the record.

NICE published its position statement on 15 August 2024, requiring demonstrable value, a preference for explainable methods, justification of assumptions using instruments such as PALISADE, and naming algorithmic bias, cybersecurity, and reduced human oversight as the principal risks^14^. Canada's Drug Agency followed in April 2025, drawing explicitly on NICE, permitting model generated search strategies, automated screening and extraction, meta-analysis code, and synthetic data and external control arms subject to transparent reporting, and framing the whole under augmentation rather than replacement^24-27^.

The workload argument for automation is real. Regulation (EU) 2021/2282 applies from 12 January 2025 for new oncology active substances and advanced therapy medicinal products, from 13 January 2028 for orphan products, and from 13 January 2030 for all others in scope^28-30^. The HTA Coordination Group estimated approximately 50 joint clinical assessments of medicines and approximately 5 of devices for 2026, with 12 ongoing and 14 countries involved as of December 2025^31,32^. A doubling of dossier volume with no increase in HEOR headcount is the strongest business case for automation available.

And yet disclosed use remains three documents out of 1,391, at NICE technology appraisals TA1154 for AI assisted study screening, TA1071 for AI assisted searches to identify treatment effect modifiers, and TA962 for a natural language processing approach, with no explicit reporting in any Canada's Drug Agency or IQWiG dossier^33^. A separate audit reported that seven agencies are adopting AI internally, with NICE recording 49 AI initiatives across 25 appraisals^34^. Agencies are adopting faster than submitters are disclosing. Conference activity confirms both volume and concentration: of 28,184 abstracts submitted to ISPOR and ISPE between January 2020 and December 2024, 1,153 addressed AI, with 89% of applications in literature review automation and 9% in economic modeling^35-37^.

### THE INDUSTRY RECORD

For a pharmaceutical reader the question is not whether these tools work but whether the reported gains are the kind a budget can be built on. Table 2 and eTable 3 present the claims with provenance labelled.

Reported reductions in regulatory writing time span Pfizer at 40% faster first draft clinical study reports^38^, Merck at 180 hours to 80 hours per fully human reviewed first draft with errors reduced by 50%^39^, Novo Nordisk at more than ten weeks to ten minutes for clinical study documentation^40^, Takeda at a projected halving of a 20 week tabulation process^41^, and a Takeda and Weave Bio preprint at a 97% reduction, from about 100 hours to 3.7 hours for 18,870 pages across 61 source documents in one investigational new drug application^42^. Certara states the baseline these are measured against, about 120 hours of regulatory writing over four weeks and an average of 83 days from database lock to an approved clinical study report, without reporting a time saving for its own product^43^.

Every one of those figures is reported by the party deploying or selling the tool, and none has been independently replicated. The most methodologically explicit, the Weave and Takeda preprint, compares against a historical estimate with no concurrent control and an n of two. Elsewhere, Novartis reported site selection falling from four to six weeks to a two hour meeting for a 14,000 patient trial, and GSK reported approximately £8 million saved in late stage asthma studies^44-49^.

On the market access side the quantified evidence reduces to a single conference abstract. A retrieval augmented generation multi-agent pipeline ingesting 110 documents and generating sections per AMCP Format version 5.0 produced a draft reported as approximately 90% complete with approximately 80% less development time, while the authors noted repetition in all sections and subject matter experts who only somewhat agreed that responses were largely complete^50,51^. Vendor claims for payer landscape monitoring are unaudited^52,53^. For pricing, gross to net, contracting analytics, and international reference pricing we located no primary source with a measured, attributable efficiency or accuracy figure. That absence is itself a finding.

Against the efficiency claims stand the failures. DSP-1181, presented as the first AI designed drug when it entered the clinic in January 2020, was abandoned in January 2022 for failing to meet study criteria, and EXS-21546 was discontinued after modelling suggested a suitable therapeutic index would be difficult to reach, with Exscientia, BenevolentAI, and Recursion having accumulated a combined deficit above US$1.5 billion^54,55^. Independent analyses of AI discovered molecules report phase 1 success of 80% to 90% and phase 2 success of approximately 40%^56^, against historical benchmarks of 13.8% overall probability of success from phase 1 to approval and 3.4% in oncology across 406,038 trial entries^57,58^. Counts of AI discovered candidates in trials range from 31 across eight companies^59^ to 117 assets across 63 companies^60^, against a total pipeline of several thousand. Phase 2 is where efficacy is tested, and phase 2 success for AI discovered molecules sits at the historical average, judged against a cost per approved drug of US$2,558 million capitalized pre-approval in 2013 dollars^61^ or a median of US$985.3 million (95% CI 683.6 to 1,228.9) in 2018 dollars^62-64^.

### FAILURE MODES

Four failure modes are documented well enough to be expected rather than exceptional.

Bias in deployed algorithms. Obermeyer and colleagues showed that a commercial risk algorithm applied to approximately 200 million Americans, by using cost as a proxy for need, identified 17.7% of Black patients for extra help where correcting the target would have identified 46.5%^65^. The mechanism was label choice, not model class, which is why it is a HEOR problem: the outcome variable was a health economics variable.

Weak external validity. The Epic sepsis model, evaluated externally across 38,455 hospitalizations, achieved area under the curve of 0.63 (95% CI 0.62 to 0.64) against a vendor reported range of 0.76 to 0.83^66^. High risk of bias is the norm rather than the exception here^67,68^.

Post deployment decay. Rahmani and colleagues documented data drift across 112,972 encounters^69^, and Kopanitsa found across four deployed clinical AI systems that calibration degraded earlier and more consistently than discrimination^70^. For HEOR this is the crux, because a cost effectiveness result depends on calibration, not on ranking. A model that still discriminates well and no longer calibrates will keep passing the metric that is monitored and stop supporting the estimate that is used.

Human factors. Jabbour and colleagues showed in a randomized vignette study of 457 clinicians that a standard AI raised diagnostic accuracy from a baseline of 73.0% by 2.9 percentage points, while a systematically biased AI lowered it by 11.3 points, with explanations providing no significant protection^71^. Dratsch and colleagues found experienced radiologists falling from 82.3% to 45.5% accuracy when shown an incorrect AI suggestion^72-74^, and Budzyń and colleagues reported adenoma detection in non-AI-assisted colonoscopies falling by 6.0 percentage points after AI exposure, from 28.4% to 22.4% (95% CI 10.5 to 1.6 lower; p = 0.0089)^75,76^. Goh and colleagues randomized 50 physicians and found diagnostic reasoning scores of 76% with a large language model against 74% without, an adjusted difference of 2 percentage points (95% CI 4 lower to 8 higher; p = 0.60), while the model alone scored 16 points higher than physicians (95% CI 2 to 30; p = 0.03)^77^. The model beat the physician and beat the physician using the model. Any workflow that assumes a human reviewer will catch the model's errors is assuming away the best measured finding in this literature.

Fabrication is the failure mode most specific to evidence work. Chelli and colleagues assessed 471 references and found hallucination rates of 39.6% for GPT-3.5, 28.6% for GPT-4, and 91.4% for Bard^78^, and Walters and Wilder examined 636 citations and found 55% fabricated by GPT-3.5 and 18% by GPT-4^79^. This has already reached consequential documents: a US federal health policy report cited studies that do not appear to exist, with a listed first author confirming she had never written the paper attributed to her^80^, a filed expert declaration in federal court contained a citation to a nonexistent statistics article^81,82^, and one journal retracted 129 papers in the first six weeks of 2025^83^. No equivalent incident has yet been documented inside a drug regulatory or HTA submission. That is the state of the record, not a reassurance.

### THE ECONOMIC EVALUATION OF AI ITSELF

HEOR is being asked to evaluate AI and has barely done so. El Arab and colleagues found 19 economic evaluations of AI in health care published from 2020 through 2024, with CHEERS scores between 21 and 27 of 28^84^. Nineteen evaluations against 1,614 authorized AI enabled devices^9^ is the field's most direct self indictment. eTable 1 lists them.

The evaluations that exist are instructive. Mital and Nguyen estimated an incremental cost effectiveness ratio of US$23,755 per quality adjusted life year for AI versus polygenic risk scores in breast cancer risk stratification, with an AI cost threshold of US$318 per mammogram^85,86^. Against this, Vargas-Palacios and colleagues modelled AI in the UK breast screening programme and found a scenario in which no price per scan made the technology cost effective^87^. That is the result to hold onto: for a diagnostic AI, cost effectiveness is frequently determined by the downstream care pathway rather than by the price of the algorithm, so a procurement negotiated on price per scan is negotiating the wrong parameter^88-90^.

The regulatory record on external controls is more informative than the synthetic data literature acknowledges. Jahanshahi and colleagues identified 45 FDA approvals between 2000 and 2019 that accepted external control data, 36 (80%) in rare disease^91,92^, and in its qualification opinion on prognostic covariate adjustment the EMA Committee for Medicinal Products for Human Use stated that excluding dropout data "would not be acceptable for regulatory purposes"^93^. The model may be qualified, and the analysis population still has to be complete.

### TRANSPARENCY, DISCLOSURE, AND WORKFORCE

The baseline is poor before AI is introduced. In a random sample of 200 health economic evaluations, 10 (5%) mentioned access to raw data and analytic code^94^, and in healthcare discrete event simulation 47 of 564 studies (8.3%) cited an openly available model^95-98^. Replication attempts are sobering: of five economic analyses re-implemented, two were fully replicated and two were unequivocally not replicable^99^, and four obesity models rebuilt from 87 publications showed cost utility ratio deviations from 3.0% lower to 17.9% higher^100^.

Disclosure of AI use runs far below reported use. Journals and societies have converged on rules that prohibit AI authorship and require disclosure of model name, version, and dates^101-110^. eTable 4 tabulates them. Against those rules, 0.6% of Lancet submissions in February 2024 declared ChatGPT use and 1.8% declared AI as a research tool^111^, while surveys report use between 25% and 81%, including more than half of about 1,600 academics across 111 countries having used AI in peer review and 81% of 1,692 physicians aware of or using AI in 2026 against 38% in 2023^112-117^. eTable 5 gives the survey estimates.

Within HEOR the workforce is not yet equipped. Of 133 HEOR, real-world data, and medical affairs professionals surveyed in April 2026, 61% rated their AI proficiency as basic or very limited and 4% as expert^118^. Among 100 HEOR leaders at 72 companies, 69% personally use AI, 29% expect AI to replace some HEOR staff within two years, and 59% report that their team does not use AI for any listed HEOR workflow^119^. Medical affairs reports higher confidence than capability, with 49% still using full manual expert review of every AI generated output^120,121^. Competency frameworks are appearing but none is HEOR specific^122-127^, while capital has already moved: AI enabled startups took 54% of US digital health funding in 2025 against 37% in 2024^128-132^.

## Discussion

The governance finding is the sharpest contrast in this series. Adoption claims run at 40% to 97% time savings in pharmaceutical regulatory writing and approximately 80% in payer dossier drafting, while disclosed use in HTA submissions is 3 of 1,391 documents (0.2%) and declared use in journal submissions is 0.6%. There are only three explanations. Either the tools are not actually used in submission grade work, which the industry evidence makes implausible. Or they are used and not disclosed, which the survey evidence makes likely. Or the disclosure requirement is understood to apply to authorship rather than to method, so a systematic review screened by a large language model is not thought to require declaration in the way a manuscript drafted by one would be. The third explanation carries most of the weight, and it is fixable, because it is a definitional failure rather than a compliance failure. Current instruments ask whether AI wrote the text. Reviewers need to know whether AI selected the evidence, defined the cohort, extracted the parameter, or generated the code.

### WHAT ACEMOGLU'S CRITIQUE MEANS FOR THIS FIELD

Daron Acemoglu, awarded the 2024 Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel with Simon Johnson and James Robinson^133^, estimates total factor productivity gains no greater than 0.66% over ten years, roughly 0.064% annually, with gross domestic product effects near 1%. The estimate derives from a task based decomposition rather than from pessimism about model capability^134,135^. His central mechanism is the distinction between easy and hard learning tasks. A task is easy to learn when outcomes are observed, labels are abundant, and feedback is fast, and hard to learn when the correct answer is not observed. His illustration is clinical: diagnosing a persistent cough is hard because "there is no large, well-curated data set of successful diagnoses and cures."

Health economics is the limiting case of a hard learning task, for structural rather than technological reasons. The quantity of interest is a counterfactual, so no data set of correct incremental cost effectiveness ratios exists, will exist, or could exist. This is why the empirical pattern reported in Part 1 is exactly what his framework predicts: the gains disappear precisely where the label disappears.

His second mechanism is task share. Even large improvements on a small share of total task time yield small aggregate gains^136,137^. Applied to HEOR, the clerical layer is where the 40% to 97% figures live, and it is a minority of the total work and the least remunerated portion of it. The judgment layer, choosing the comparator, specifying the model structure, defending the extrapolation, negotiating the price, is unaffected. Under this arithmetic an 80% reduction in a task that is 20% of the total yields a 16% aggregate gain in the best case, before accounting for the review burden the automation creates.

The counterargument deserves fair statement, because it is empirically supported. Noy and Zhang found writing time down 40% and quality up 18% across 453 professionals with the largest gains for weaker performers^138^, Brynjolfsson and colleagues found 14% to 15% more resolutions per hour across 5,179 support agents with 34% gains for novices^139,140^, and Peng and colleagues found programmers 55.8% faster^141^. Three features are uncomfortable for HEOR. The gains concentrate in the least experienced, which compresses the junior training pathway through which HEOR expertise has been built. They are largest where output is verifiable, which HEOR output is not. And the direction reverses outside the frontier of capability: in a randomized study of 758 consultants, those using AI inside that frontier completed 12.2% more tasks 25.1% faster, while on a task outside it accuracy fell from 84.5% to 70.6% with AI and to 60.0% with AI plus an overview of its limits^142^. The overview made it worse. HEOR's hardest tasks sit outside the frontier, and its practitioners cannot yet reliably tell which side a given task is on, since 61% rate their proficiency as basic or very limited^118^.

What follows is not that AI will not matter. It is that the mechanism by which it matters will be cost structure rather than evidence quality, and that the two are separable. The realistic ten year expectation is a HEOR function producing more dossiers per analyst at similar quality, with a compressed junior tier, a widened tail of low quality submissions from parties who could not previously afford to submit at all, and a corresponding increase in the burden on reviewers. Reviewers, not producers, absorb the externality. That is the case for the reporting standard below, and it is an economic case rather than an ethical one.

### TRACE-HEOR: A REPORTING STANDARD FOR AI ASSISTED HEOR EVIDENCE

Existing instruments cover the parts of this problem that resemble clinical prediction or clinical trials: TRIPOD+AI and PROBAST+AI for prediction model reporting and bias^143,144^, CONSORT-AI and SPIRIT-AI for trials of AI interventions^145,146^, DECIDE-AI for early live clinical evaluation^147^, STARD-AI for diagnostic accuracy^148^, TRIPOD-LLM for large language model studies^149^, CANGARU for disclosure in scholarly writing^150^, CHEERS 2022 for economic evaluation reporting^151^, PALISADE for real-world data study credibility^152^, and ELEVATE-GenAI with the ISPOR taxonomy for the HEOR specific work^153-155^. None answers the question an HTA reviewer actually has, which is whether the reimbursement recommendation would change if the AI component were removed.

We propose TRACE-HEOR, for Transparent Reporting of Artificial intelligence Components in health Economics and Outcomes Research: ten items designed as an extension to CHEERS 2022 and PALISADE rather than as a replacement, and stated so that each is verifiable by a reviewer with access only to the submission. Table 3 presents them in full with the evidence supporting each.

1. Declare the function, not the tool. State, for each AI component, which of the following it performed: evidence identification or screening, data extraction, cohort or exposure definition, outcome or endpoint derivation, covariate selection, effect estimation, parameter derivation, model code generation, synthetic data or external control generation, or narrative drafting. Name the model, version, vendor, and dates of use, as JAMA already requires^105^.
2. Specify the context of use and the model risk, using the FDA's two factor definition of model influence and decision consequence^5^, and state which decision the model influences.
3. Report calibration, not only discrimination, in the deployment population and time period. Where an estimate depends on absolute risk or absolute cost, discrimination alone is insufficient^70^.
4. Report the human reference standard and its own reliability. Where AI output is validated against human abstraction, report inter-abstractor agreement for the reference^156,157^.
5. Report performance for the variables the analysis depends on, disaggregated. Aggregate F1 conceals the pattern in which stage extraction reaches 0.988 precision while histology linkage reaches 0.79 recall^158^ and T stage reaches F1 0.89 while M stage reaches 0.24^159^.
6. Report a decision reversal analysis. Re-estimate the primary result with the AI component replaced by the pre-AI alternative, or by a plausible worst case, and state whether the incremental cost effectiveness ratio crosses the relevant threshold or whether the recommendation changes. This item exists in no current instrument and is the one reviewers need most.
7. Report bias and subgroup performance for the populations the decision affects, and state the demographic composition of any training or synthetic population^65,160^.
8. For synthetic data or model based external controls, report generator family, fidelity against the real target quantity rather than against summary statistics, and a privacy evaluation. Generator choice alone moved recovery of the true median progression free survival from 6.5% to 98.1% of replicates^161,162^.
9. Report the human oversight actually performed, quantitatively: what fraction of AI output was reviewed, by whom, with what qualifications, and what the disagreement rate was^71,72,77,120^.
10. Deposit prompts, code, model versions, seeds, and intermediate outputs in a citable archive at submission. Five percent of health economic evaluations currently mention code availability^94^, and an AI assisted analysis is not auditable without the prompts.

Items 1, 2, 6, 9, and 10 are the TRACE-HEOR minimum set, and a submission reporting only those five is materially more auditable than any submission we located. If an agency were to adopt only one, it should be item 6, because decision reversal is the only item that converts a technical property of a model into the currency a reimbursement committee reasons in.

### A RESEARCH AGENDA

Five priorities follow, ordered by the ratio of decision relevance to current investment.

First, benchmark AI derived endpoints against regulatory grade human abstraction in a multi-sponsor, multi-vendor study with a pre-registered protocol, and publish the discordant cases. Current validation is vendor authored^157,163,164^, which is a conflict rather than a failing, and the remedy is independent replication.

Second, obtain a regulatory precedent. Sponsors should seek scientific advice or a qualification opinion on an AI derived endpoint, and agencies should publish the reasoning when they give it, as the EMA did on prognostic covariate adjustment^93^. One published opinion would be worth more to this field than fifty conference abstracts.

Third, establish an empirical decision reversal literature. Take completed cost effectiveness analyses and HTA submissions, substitute AI assisted components for the original ones, and measure how often the recommendation changes. The replication literature indicates the base rate of non-replication is already high before AI is introduced^99,100^, which makes the marginal question both answerable and urgent.

Fourth, run randomized trials of AI assisted HEOR workflows with quality, not speed, as the primary endpoint. Every existing industry efficiency figure is single arm and self reported, and the designs already exist in adjacent fields^2,138,142^.

Fifth, evaluate AI itself economically at a scale proportionate to its deployment, and build HEOR specific competency and audit capacity. Nineteen published economic evaluations against 1,614 authorized devices is a ratio of about one to eighty five^9,84^, the finding that no price per scan made an AI cost effective in a national screening programme should be reproduced or refuted^87,88^, and reviewer side capacity is the binding constraint because joint clinical assessment volume rises on a fixed schedule^28,32,118^.

### LIMITATIONS

The regulatory, HTA, and industry record assembled here is a narrative review rather than a systematic one, and negative results are less visible in it: a sponsor that abandoned an AI assisted approach has no reason to publish that fact. Several central quantities rest on conference abstracts and company communications, which we label rather than exclude because they are the only available source. The disclosure denominators are audits of published documents, so they measure disclosure and not use. TRACE-HEOR is a proposal derived from documented failure modes rather than a consensus instrument; it has not been through a Delphi process, and it should be treated as a starting draft for one.

## Conclusions

Regulators have written more about artificial intelligence in evidence generation than sponsors have disclosed using it. The FDA has authorized 1,614 AI enabled devices and received more than 500 drug and biologic submissions containing AI components, while its credibility framework remains a draft that excludes discovery and operational uses. Industry reports time savings of 40% to 97% in regulatory writing, none independently replicated. Three of 1,391 health technology assessment documents disclose an AI component.

The gap is not primarily a compliance problem. Disclosure instruments were built to establish who wrote a document, and the operations that matter in this field are the ones that select the evidence, define the cohort, derive the endpoint, and generate the code. Under the task based productivity arithmetic that Acemoglu applies to the wider economy, the tasks AI does well in health economics are the minority of the work and the least remunerated part of it, while the burden of checking the output falls on reviewers who did not choose the tool. TRACE-HEOR states ten items that would make an AI assisted submission auditable, and one of them, a decision reversal analysis, would tell a reimbursement committee the only thing it needs to know.

## Disclosures

The author reports no conflicts of interest related to this work. No funding was received for this study. The author is affiliated with an academic institution and a health economics consultancy that conducts real-world evidence studies for pharmaceutical and life sciences clients; no client had any role in the conception, conduct, analysis, or reporting of this review, and no client reviewed the manuscript before submission.

The large language model classifier described in Part 1 is a measured object of study in this series rather than an assistive writing tool. Its prompts, inputs, and outputs are archived in the replication package. No AI tool is listed as an author.

## Data Availability

All search strings, retrieved records, the classification dictionary, the blinded classifier prompts and outputs, the analysis scripts, the figure generation code, the regulatory and industry source tables, and the complete reference library are available in the public replication package^4^. No individual patient data were used.

## Author Affiliations

¹ Department of Internal Medicine, University of Michigan, Ann Arbor, Michigan

² Graduate School of Public Health and Health Policy, City University of New York, New York, New York

## Figures

**Figure 1. Timeline of regulatory, health technology assessment, and journal policy instruments governing artificial intelligence in evidence generation, 2019 to 2030.** Instruments are grouped by issuing domain, with drug and biologic regulation, device regulation, health technology assessment, payer regulation, and publication policy shown separately. Items in force are distinguished from drafts and from provisions with future application dates, including the staged application of Regulation (EU) 2021/2282 from 2025 through 2030 and the general purpose AI obligations of the EU AI Act from August 2026.

## Tables

**Table 1.** Regulatory and health technology assessment instruments governing artificial intelligence in evidence generation: issuing body, instrument, date, status, scope, and the operative requirement.

**Table 2.** Reported claims set against the documented record: efficiency and performance claims by domain, the primary source, the provenance of the figure, whether the reporting party had a commercial interest, and independent replication status.

**Table 3.** The TRACE-HEOR reporting standard: ten items for artificial intelligence assisted health economics and outcomes research evidence, with the rationale, the supporting evidence, and the existing instrument each item extends.

## References

1. Lai H, Liu J, Bai C, Liu H, Pan B, Luo X, et al. Language models for data extraction and risk of bias assessment in complementary medicine. npj Digit. Med. 2025;8(1):74. DOI: 10.1038/s41746-025-01457-w.

2. Lee K, Paek H, Ofoegbu N, Rube S, Higashi MK, Dawoud D, et al. A4SLR: An Agentic Artificial Intelligence-Assisted Systematic Literature Review Framework to Augment Evidence Synthesis for Health Economics and Outcomes Research and Health Technology Assessment. Value in Health 2025;28(11):1655-1664. DOI: 10.1016/j.jval.2025.08.002.

3. Reason T, Rawlinson W, Langham J, Gimblett A, Malcolm B, Klijn S. Artificial Intelligence to Automate Health Economic Modelling: A Case Study to Evaluate the Potential Application of Large Language Models. PharmacoEconomics Open 2024;8(2):191-203. DOI: 10.1007/s41669-024-00477-8.

4. Baser O. Replication package for Artificial Intelligence in Health Economics and Outcomes Research: A Systematic Scoping Review. GitHub repository; 2026. Available at: https://github.com/obaser/ai-heor-scoping-review

5. US Food and Drug Administration. Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products. Draft guidance for industry. Docket FDA-2024-D-4689. Silver Spring, MD: FDA; January 2025. Available at: https://www.fda.gov/media/184830/download

6. US Food and Drug Administration. FDA proposes framework to advance credibility of AI models used for drug and biological product submissions. Press announcement, January 6, 2025. Available at: https://www.fda.gov/news-events/press-announcements/fda-proposes-framework-advance-credibility-ai-models-used-drug-and-biological-product-submissions

7. Poddar A, Samson M, Innes GK, Liu Q, Saha A, Hanger M, et al. Leveraging Artificial Intelligence in Drug and Biological Product Development: An FDA and Clinical Trial Transformation Initiative Workshop Report. NEJM AI 2025;2(12). DOI: 10.1056/aipc2500801.

8. Pharmaceutical Research and Manufacturers of America. PhRMA comments on Docket FDA-2024-D-4689. Available at: https://cdn.aglty.io/phrma/global/resources/import/pdfs/FDA-2024-D-4689_PhRMA%20Comments.pdf

9. US Food and Drug Administration. Artificial Intelligence-Enabled Medical Devices. Device list current as of September 4, 2026. Available at: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices

10. US Food and Drug Administration. Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations. Draft guidance. Docket FDA-2024-D-4488. January 2025. Available at: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing

11. US Food and Drug Administration. Digital Health Advisory Committee Meeting: Total Product Life Cycle Considerations for Generative AI-Enabled Devices. November 20-21, 2024. Available at: https://www.fda.gov/advisory-committees/advisory-committee-calendar/digital-health-advisory-committee-meeting-november-20-21-2024

12. US Food and Drug Administration. FDA launches agency-wide AI tool to optimize performance for the American people. News release, June 2, 2025. Available at: https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people

13. European Medicines Agency. Reflection paper on the use of artificial intelligence in the lifecycle of medicines. EMA/CHMP/CVMP/83833/2023. September 9, 2024. Available at: https://www.ema.europa.eu/en/documents/scientific-guideline/reflection-paper-use-artificial-intelligence-ai-medicinal-product-lifecycle_en.pdf

14. National Institute for Health and Care Excellence. Use of AI in evidence generation: NICE position statement. ECD11. August 15, 2024. Available at: https://www.nice.org.uk/corporate/ecd11

15. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Official Journal of the European Union. Available at: https://eur-lex.europa.eu/eli/reg/2024/1689/oj

16. European Federation of Pharmaceutical Industries and Associations. EFPIA position on the use of artificial intelligence in the medicinal product lifecycle. October 2024. Available at: https://efpia.eu/media/tzeavw1t/efpia-position-on-the-use-of-artificial-intelligence-in-the-medicinal-product-lifecycle.pdf

17. International Federation of Pharmaceutical Manufacturers and Associations. IFPMA Artificial Intelligence Ethics Principles. July 2022. Available at: https://www.ifpma.org/wp-content/uploads/2023/01/i2023_IFPMA-Artificial-Intelligence-AI-Ethics-Principles.pdf

18. Novartis. Novartis commitment to the ethical and responsible use of AI systems. Available at: https://www.novartis.com/sites/novartis_com/files/novartis-responsible-use-of-ai-systems.pdf

19. Roche. Roche AI Ethics Principles. Updated April 1, 2025. Available at: https://assets.roche.com/f/176343/x/401c28049f/roche-ai-ethics-principles.pdf

20. Centers for Medicare and Medicaid Services. Coverage criteria and utilization management requirements in CMS-4201-F. Health Plan Management System memorandum, February 6, 2024. Available at: https://www.cms.gov/files/document/faq-contract-year-2024-policy-and-technical-changes-medicare-advantage-program-final-rule-utilization.pdf

21. California Senate Bill 1120, Chapter 879, Statutes of 2024 (Physicians Make Decisions Act). Available at: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1120

22. World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. Geneva: WHO; 2024. ISBN 978-92-4-008475-9.

23. World Health Organization. Ethics and governance of artificial intelligence for health: WHO guidance. Geneva: WHO; 2021. ISBN 978-92-4-002920-0.

24. Canada's Drug Agency. Position Statement on the Use of Artificial Intelligence in the Generation and Reporting of Evidence. April 2025. Available at: https://www.cda-amc.ca/sites/default/files/MG%20Methods/Position_Statement_AI_Renumbered.pdf

25. CDA-AMC. Development of an Evaluation Instrument on Artificial Intelligence Search Tools for Evidence Synthesis. cjht 2024;4(10). DOI: 10.51731/cjht.2024.1004.

26. Institute FQAEIHC. General Methods; Version 8.0. IQWiG 2026. DOI: 10.60584/general-methods_v8.0.

27. Pearson SD, Singh P, Beaudoin F, Campbell J, Schapiro L, Emond SK, et al. Institute for Clinical and Economic Review: Peterson Health Technology Institute value assessment framework for digital health technologies. J. Comp. Eff. Res. 2023;12(12):e230154. DOI: 10.57264/cer-2023-0154.

28. Regulation (EU) 2021/2282 of the European Parliament and of the Council of 15 December 2021 on health technology assessment. Official Journal of the European Union. Available at: https://eur-lex.europa.eu/eli/reg/2021/2282/oj/eng

29. European Commission. Implementation of the Regulation on health technology assessment. Available at: https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment_en

30. European Commission. Joint Clinical Assessments. Available at: https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment/joint-clinical-assessments_en

31. Barbuto V, European Commission DG SANTE. The HTA Regulation. Presentation to the 15th EMA Industry Standing Group, December 11, 2025. Available at: https://www.ema.europa.eu/en/documents/presentation/presentation-hta-regulation-v-barbuto-ec_en.pdf

32. Health Technology Assessment Coordination Group. Annual Work Programme 2026. November 28, 2025. Available at: https://health.ec.europa.eu/document/download/81db097f-a9cb-4404-837c-115b4289321d_en

33. Use of artificial intelligence and machine learning in evidence synthesis for health technology assessment submissions: a review of NICE, CDA, and IQWiG documents. Poster presented at ISPOR 2026, Philadelphia, PA, May 17-20, 2026. Available at: https://www.ispor.org/docs/default-source/cti-meeting-21463-documents/9774d614-3a98-4fba-bcf4-c1ab426db452.pdf

34. Use of artificial intelligence in health technology assessment submissions and agency practice. Poster MSR96 presented at ISPOR 2026, Philadelphia, PA. Available at: https://www.ispor.org/docs/default-source/cti-meeting-21463-documents/edf7be4a-ac97-45e7-82f1-ed3fc505aa61.pdf

35. Emerging trends in AI applications shaping pharmacoepidemiology and health technology assessments. Poster presented at ISPOR 2025. Available at: https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2025/poster-session-3/emerging-trends-in-ai-applications-shaping-pharmacoepidemiology-and-health-technology-assessments

36. Assessing the use of artificial intelligence in publication-grade research: a literature review of applications in HEOR. Poster SA14 presented at ISPOR Europe 2025. Available at: https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-europe-2025/poster-session-1-2/assessing-the-use-of-artificial-intelligence-in-publication-grade-research-a-literature-review-of-applications-in-heor

37. Artificial intelligence tools in health technology assessment: a scoping review. Conference proceeding OP07. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC11718724/

38. Pfizer. How AI is already reshaping cancer care. Available at: https://www.pfizer.com/news/articles/how_ai_is_already_reshaping_cancer_care

39. Merck and Co. Merck expands innovative internal generative AI solutions, helping to deliver medicines to patients faster. Press release, June 25, 2025. Available at: https://www.merck.com/news/merck-expands-innovative-internal-generative-ai-solutions-helping-to-deliver-medicines-to-patients-faster/

40. Anthropic. Novo Nordisk transforms clinical documentation with Claude. Customer story. Available at: https://claude.com/customers/novo-nordisk

41. Takeda. Aiming to enhance regulatory submissions with GenAI. December 12, 2024. Available at: https://www.takeda.com/our-impact/our-stories/aiming-to-enhance-regulatory-submissions-with-genai/

42. Automated generation of investigational new drug applications with large language models. arXiv preprint 2509.09738. Available at: https://arxiv.org/pdf/2509.09738

43. Certara. CoAuthor and GPTs: transforming regulatory writing. White paper, November 2024. Available at: https://www.certara.com/wp-content/uploads/2024/11/2024-11-08-White-Paper-CoAuthor-and-GPTs.pdf

44. Reuters. Drugmakers turn to AI to speed trials, regulatory submissions. January 26, 2026. Available at: https://www.reuters.com/legal/litigation/drugmakers-turn-ai-speed-trials-regulatory-submissions-2026-01-26/

45. Merck and Co. Merck and Google Cloud partner to accelerate agentic AI enterprise transformation. Press release, April 22, 2026. Available at: https://www.merck.com/news/merck-and-google-cloud-partner-to-accelerate-agentic-ai-enterprise-transformation/

46. Eli Lilly and Company. Lilly partners with NVIDIA to build industry's most powerful AI supercomputer owned and operated by a pharmaceutical company. October 28, 2025. Available at: https://investor.lilly.com/news-releases/news-release-details/lilly-partners-nvidia-build-industrys-most-powerful-ai

47. Tempus AI. Tempus signs expanded strategic agreements with AstraZeneca and Pathos AI. April 23, 2025. Available at: https://investors.tempus.com/news-releases/news-release-details/tempus-signs-expanded-strategic-agreements-astrazeneca-and/

48. OpenAI. Moderna: advancing mRNA medicine with generative AI. Customer story. Available at: https://openai.com/index/moderna/

49. Sanofi. Sanofi to become the first pharma company powered by artificial intelligence at scale. Press release, June 13, 2023. Available at: https://www.sanofi.com/en/media-room/press-releases/2023/2023-06-13-12-00-00-2687072

50. Automated AMCP dossier development using a retrieval-augmented generation (RAG) based multi-agent approach. Abstract MSR207. Value Health 2026;29(S6). Available at: https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2026/poster-session-5-3/automated-amcp-dossier-development-using-a-retrieval-augmented-generation-rag-based-multi-agent-approach

51. Academy of Managed Care Pharmacy. AMCP Format for Formulary Submissions. Available at: https://www.amcp.org/resource/amcp-format-formulary-submissions-guidance

52. Norstella. Norstella AI: principles and product capabilities. Available at: https://ai.norstella.com/

53. IQVIA. Market Access Insights. Fact sheet, November 7, 2023. Available at: https://www.iqvia.com/library/fact-sheets/market-access-insights

54. Endpoints News. The first AI-designed drugs fall short in the clinic following years of hype. Available at: https://endpoints.news/first-ai-designed-drugs-fall-short-in-the-clinic-following-years-of-hype/

55. Fierce Biotech. Several months after Exscientia merger, AI outfit Recursion reworks pipeline. Available at: https://www.fiercebiotech.com/biotech/several-months-after-exscientia-merge-ai-outfit-recursion-reworks-pipeline

56. KP JM, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. Drug Discovery Today 2024;29(6):104009. DOI: 10.1016/j.drudis.2024.104009.

57. Wong CH, Siah KW, Lo AW. Estimation of clinical trial success rates and related parameters. Biostatistics 2018;20(2):273-286. DOI: 10.1093/biostatistics/kxx069.

58. Wong CH, Siah KW, Lo AW. Corrigendum: Estimation of clinical trial success rates and related parameters. Biostatistics 2018;20(2):366-366. DOI: 10.1093/biostatistics/kxy072.

59. Wilczok D, Zhavoronkov A. Progress, Pitfalls, and Impact of AI-Driven Clinical Trials. Clin Pharma and Therapeutics 2024;117(4):887-890. DOI: 10.1002/cpt.3542.

60. Haque W, Sai-Palm K, Kasparcova MZ, Rana I, Verlingue L, Garassino MC, et al. Clinical-stage AI-enabled therapeutic assets: An industry-wide analysis of scale, clinical progression, and company characteristics. J Clin Oncol 2026;44(16_suppl):11072-11072. DOI: 10.1200/jco.2026.44.16_suppl.11072.

61. DiMasi JA, Grabowski HG, Hansen RW. Innovation in the pharmaceutical industry: New estimates of R&D costs. Journal of Health Economics 2016;47:20-33. DOI: 10.1016/j.jhealeco.2016.01.012.

62. Wouters OJ, McKee M, Luyten J. Estimated Research and Development Investment Needed to Bring a New Medicine to Market, 2009-2018. JAMA 2020;323(9):844. DOI: 10.1001/jama.2020.1166.

63. Wouters OJ, McKee M, Luyten J. Errors in Source Data for Study of Drug Development Costs. JAMA 2022;328(11):1110. DOI: 10.1001/jama.2022.14317.

64. Error in Data in Study of Estimated Cost of Bringing a Drug to Market. JAMA 2022;328(11):1111. DOI: 10.1001/jama.2022.14733.

65. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. Dissecting racial bias in an algorithm used to manage the health of populations. Science 2019;366(6464):447-453. DOI: 10.1126/science.aax2342.

66. Wong A, Otles E, Donnelly JP, Krumm A, McCullough J, DeTroyer-Cooley O, et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Intern Med 2021;181(8):1065. DOI: 10.1001/jamainternmed.2021.2626.

67. Wynants L, Van CB, Collins GS, Riley RD, Heinze G, Schuit E, et al. Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal. BMJ 2020:m1328. DOI: 10.1136/bmj.m1328.

68. Andaur NCL, Damen JAA, Takada T, Nijman SWJ, Dhiman P, Ma J, et al. Risk of bias in studies on prediction models developed using supervised machine learning techniques: systematic review. BMJ 2021:n2281. DOI: 10.1136/bmj.n2281.

69. Rahmani K, Thapa R, Tsou P, Chetty SC, Barnes G, Lam C, et al. Assessing the effects of data drift on the performance of machine learning models used in clinical sepsis prediction. 2022. DOI: 10.1101/2022.06.06.22276062.

70. Kopanitsa G. Validation is not enough: Longitudinal evidence of post-deployment fragility in clinical AI systems. PLOS Digit Health 2026;5(7):e0001534. DOI: 10.1371/journal.pdig.0001534.

71. Jabbour S, Fouhey D, Shepard S, Valley TS, Kazerooni EA, Banovic N, et al. Measuring the Impact of AI in the Diagnosis of Hospitalized Patients. JAMA 2023;330(23):2275. DOI: 10.1001/jama.2023.22295.

72. Dratsch T, Chen X, Rezazade MM, Kloeckner R, Mähringer-Kunz A, Püsken M, et al. Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance. Radiology 2023;307(4):e222176. DOI: 10.1148/radiol.222176.

73. Wang D, Ding J, Sun A, Liu S, Jiang D, Li N, et al. Artificial intelligence suppression as a strategy to mitigate artificial intelligence automation bias. Journal of the American Medical Informatics Association 2023;30(10):1684-1692. DOI: 10.1093/jamia/ocad118.

74. Sakamoto T, Harada Y, Shimizu T. Facilitating Trust Calibration in Artificial Intelligence-Driven Diagnostic Decision Support Systems for Determining Physicians’ Diagnostic Accuracy: Quasi-Experimental Study. JMIR Form Res 2024;8:e58666-e58666. DOI: 10.2196/58666.

75. Budzyń K, Romańczyk M, Kitala D, Kołodziej P, Bugajski M, Adami HO, et al. Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. The Lancet Gastroenterology & Hepatology 2025;10(10):896-903. DOI: 10.1016/s2468-1253(25)00133-5.

76. Budzyń K, Romańczyk M, Mori Y. Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: Authors' reply. The Lancet Gastroenterology & Hepatology 2025;10(12):1062. DOI: 10.1016/s2468-1253(25)00324-3.

77. Goh E, Gallo R, Hom J, Strong E, Weng Y, Kerman H, et al. Large Language Model Influence on Diagnostic Reasoning. JAMA Netw Open 2024;7(10):e2440969. DOI: 10.1001/jamanetworkopen.2024.40969.

78. Chelli M, Descamps J, Lavoué V, Trojani C, Azar M, Deckert M, et al. Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis. J Med Internet Res 2024;26:e53164. DOI: 10.2196/53164.

79. Walters WH, Wilder EI. Fabrication and errors in the bibliographic citations generated by ChatGPT. Sci Rep 2023;13(1):14045. DOI: 10.1038/s41598-023-41032-5.

80. Science. Trump officials downplay fake citations in high-profile report on children's health. Available at: https://www.science.org/content/article/trump-officials-downplay-fake-citations-high-profile-report-children-s-health

81. Reuters. Anthropic expert accused of using AI-fabricated source in copyright case. May 13, 2025. Available at: https://www.reuters.com/legal/litigation/anthropic-expert-accused-using-ai-fabricated-source-copyright-case-2025-05-13/

82. Washington State Bar Association. Federal court excludes expert for AI-hallucinated citations. NWSidebar, August 31, 2026. Available at: https://nwsidebar.wsba.org/2026/08/31/federal-court-excludes-expert-for-ai-hallucinated-citations/

83. Retraction Watch. As Springer Nature journal clears AI papers, one university's retractions rise drastically. February 10, 2025. Available at: https://retractionwatch.com/2025/02/10/as-springer-nature-journal-clears-ai-papers-one-universitys-retractions-rise-drastically/

84. El ARA, Al MOA. Systematic review of cost effectiveness and budget impact of artificial intelligence in healthcare. npj Digit. Med. 2025;8(1):548. DOI: 10.1038/s41746-025-01722-y.

85. Mital S, Nguyen HV. Cost-effectiveness of using artificial intelligence versus polygenic risk score to guide breast cancer screening. BMC Cancer 2022;22(1):501. DOI: 10.1186/s12885-022-09613-1.

86. Yala A, Mikhael PG, Lehman C, Lin G, Strand F, Wan Y, et al. Optimizing risk-based breast cancer screening policies with reinforcement learning. Nat Med 2022;28(1):136-143. DOI: 10.1038/s41591-021-01599-w.

87. Vargas-Palacios A, Sharma N, Sagoo GS. Cost-effectiveness requirements for implementing artificial intelligence technology in the Women’s UK Breast Cancer Screening service. Nat Commun 2023;14(1):6110. DOI: 10.1038/s41467-023-41754-0.

88. Hendrix N, Veenstra DL, Cheng M, Anderson NC, Verguet S. Assessing the Economic Value of Clinical Artificial Intelligence: Challenges and Opportunities. Value in Health 2022;25(3):331-339. DOI: 10.1016/j.jval.2021.08.015.

89. Huang X, Yang B, Zheng W, Liu Q, Xiao F, Ouyang P, et al. Cost-effectiveness of artificial intelligence screening for diabetic retinopathy in rural China. BMC Health Serv Res 2022;22(1):260. DOI: 10.1186/s12913-022-07655-6.

90. Kalavadekar PN, Khandarkar KR, Dhotre DR, Chincholkar A, Swarnkar SK, Joshi HJ. Reinforcement learning to optimize tuberculosis screening strategies in resource-limited settings. Indian Journal of Tuberculosis 2025;72:S159-S167. DOI: 10.1016/j.ijtb.2025.11.019.

91. Jahanshahi M, Gregg K, Davis G, Ndu A, Miller V, Vockley J, et al. The Use of External Controls in FDA Regulatory Decision Making. Ther Innov Regul Sci 2021;55(5):1019-1035. DOI: 10.1007/s43441-021-00302-y.

92. Yin X, Mishra-Kalyan PS, Sridhara R, Stewart MD, Stuart EA, Davi RC. Exploring the Potential of External Control Arms created from Patient Level Data: A case study in non-small cell lung cancer. Journal of Biopharmaceutical Statistics 2022;32(1):204-218. DOI: 10.1080/10543406.2021.2011901.

93. European Medicines Agency. Qualification opinion for Prognostic Covariate Adjustment (PROCOVA). Committee for Medicinal Products for Human Use. Available at: https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/qualification-opinion-prognostic-covariate-adjustment-procovatm_en.pdf

94. Catalá-López F, Ridao M, Tejedor-Romero L, Caulley L, Hutton B, Husereau D, et al. Transparency, openness, and reproducible research practices are frequently underused in health economic evaluations. Journal of Clinical Epidemiology 2024;165:111208. DOI: 10.1016/j.jclinepi.2023.10.024.

95. Monks T, Harper A. Computer model and code sharing practices in healthcare discrete-event simulation: a systematic scoping review. Journal of Simulation 2023;19(1):108-123. DOI: 10.1080/17477778.2023.2260772.

96. Henderson RH, Sampson C, Pouwels XG, Harvard S, Handels R, Feenstra T, et al. Mapping the Landscape of Open Source Health Economic Models: A Systematic Database Review and Analysis: An ISPOR Special Interest Group Report. Value in Health 2025;28(6):813-820. DOI: 10.1016/j.jval.2025.01.019.

97. Zavalis EA, Ioannidis JPA. A meta-epidemiological assessment of transparency indicators of infectious disease models. PLoS ONE 2022;17(10):e0275380. DOI: 10.1371/journal.pone.0275380.

98. Naudet F, Sakarovitch C, Janiaud P, Cristea I, Fanelli D, Moher D, et al. Data sharing and reanalysis of randomized controlled trials in leading biomedical journals with a full data sharing policy: survey of studies published in The BMJ and PLOS Medicine. BMJ 2018:k400. DOI: 10.1136/bmj.k400.

99. Bermejo I, Tappenden P, Youn J. Replicating Health Economic Models: Firm Foundations or a House of Cards? PharmacoEconomics 2017;35(11):1113-1121. DOI: 10.1007/s40273-017-0553-x.

100. Schwander B, Nuijten M, Evers S, Hiligsmann M. Replication of Published Health Economic Obesity Models: Assessment of Facilitators, Hurdles and Reproduction Success. PharmacoEconomics 2021;39(4):433-446. DOI: 10.1007/s40273-021-01008-7.

101. International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals: Artificial intelligence use by authors. Available at: https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html

102. Committee on Publication Ethics. Authorship and AI tools. COPE position statement. Available at: https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools

103. NEJM AI. Editorial policies. Available at: https://ai.nejm.org/about/editorial-policies

104. NEJM AI. About NEJM AI. Available at: https://ai.nejm.org/about

105. JAMA. Instructions for Authors. Available at: https://jamanetwork.com/journals/jama/pages/instructions-for-authors

106. Health Affairs. New article requirements. Available at: https://www.healthaffairs.org/help-for-authors/journal/new-article-requirements

107. Elsevier. Generative AI policies for journals. Available at: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals

108. Springer Nature. Artificial intelligence: editorial policies. Available at: https://www.nature.com/nature-portfolio/editorial-policies/ai

109. International Society for Pharmacoeconomics and Outcomes Research. ISPOR Artificial Intelligence Policy. Available at: https://www.ispor.org/ai-policy

110. Value in Health. Guide for authors. Available at: https://www.sciencedirect.com/journal/value-in-health/publish/guide-for-authors

111. The Lancet Infectious Diseases. The use of artificial intelligence in scientific publishing. Editorial. Lancet Infect Dis 2024. Available at: https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(24)00160-9/fulltext

112. Kwon D. Is it OK for AI to write science papers? Nature survey shows researchers are split. Nature 2025;641(8063):574-578. DOI: 10.1038/d41586-025-01463-8.

113. Naddaf M. More than half of researchers now use AI for peer review, often against guidance. Nature 2025;649(8096):273-274. DOI: 10.1038/d41586-025-04066-5.

114. American Medical Association. Augmented Intelligence Research: Physician Sentiments Around the Use of AI in Health Care. Chicago, IL: AMA; 2026. Available at: https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf

115. American Medical Association. AI usage among doctors doubles, confidence in technology grows. Press release, 2026. Available at: https://www.ama-assn.org/press-center/ama-press-releases/ama-ai-usage-among-doctors-doubles-confidence-technology-grows

116. McKinsey and Company. Generative AI in healthcare: current trends and future outlook. 2026. Available at: https://www.mckinsey.com/industries/healthcare/our-insights/generative-ai-in-healthcare-current-trends-and-future-outlook

117. HIMSS and Medscape. AI Adoption by Health Systems Report 2024. Available at: https://www.himss.org/news-center/himss-and-medscape-unveil-groundbreaking-report-ai-adoption-health-systems/

118. Polygon Health Analytics. AI in HEOR, RWD and medical affairs: what 133 professionals told us. April 2026. Available at: https://polygonhealthanalytics.com/ai-in-heor-rwd-medical-affairs-what-133-professionals-told-us-and-what-it-means-for-the-industry/

119. Center for the Evaluation of Value and Risk in Health, Tufts Medical Center. HEOR trends: results of a survey of HEOR leaders. Poster presented at ISPOR 2026, April 7, 2026. Available at: https://cevr.tuftsmedicalcenter.org/assets/images/2026_04_07_ISPOR_Poster_HEOR_Trends.pdf

120. Medical Affairs Professional Society. Workflows, not chatbots: findings from the 2026 AI in Medical Affairs Industry Benchmark Survey. Available at: https://medicalaffairs.org/solution-provider-perspective/workflows-not-chatbots/

121. ZS Associates. Medical Affairs Outlook Report 2025. Available at: https://www.zs.com/content/dam/global/master/pdfs/zs-medical-affairs-outlook-report-2025.pdf

122. Cai C, Zhu G, Zhou S, Ng O, Duell J, Ho WK, et al. A Competency Framework for Medical AI Education: Mixed Methods Study. JMIR Med Educ 2026;12:e91116-e91116. DOI: 10.2196/91116.

123. Acosta JA. Perspective: advancing public health education by embedding AI literacy. Front. Digit. Health 2025;7:1584883. DOI: 10.3389/fdgth.2025.1584883.

124. Semi MMA, Das S, Utsho MR, Hossain A, Kamal MB, Sizan AA, et al. Artificial Intelligence in Public Health Education: A Scoping Review of Workforce Competency Development. Health Science Reports 2026;9(3):e72066. DOI: 10.1002/hsr2.72066.

125. Wolthusen RPF, El-tohami M, Hendler RA, Riordan PA, Stoklosa JB. A Framework for Artificial Intelligence in Medical Education: Could I, Would I, Should I? Journal of Graduate Medical Education 2025;17(4):430-433. DOI: 10.4300/jgme-d-25-00009.1.

126. Gordon M, Daniel M, Ajiboye A, Uraiby H, Xu NY, Bartlett R, et al. A scoping review of artificial intelligence in medical education: BEME Guide No. 84. Medical Teacher 2024;46(4):446-470. DOI: 10.1080/0142159x.2024.2314198.

127. Pizzi LT, Onukwugha E, Corey R, Albarmawi H, Murray J. Competencies for Professionals in Health Economics and Outcomes Research: The ISPOR Health Economics and Outcomes Research Competencies Framework. Value in Health 2020;23(9):1120-1127. DOI: 10.1016/j.jval.2020.04.1834.

128. Rock Health. 2025 year-end digital health funding overview: a tale of two markets. Available at: https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/

129. Rock Health. 2024 year-end market overview: Davids and Goliaths. Available at: https://rockhealth.com/insights/2024-year-end-market-overview-davids-and-goliaths/

130. White and Case and Mergermarket. Life Sciences and AI Report. January 2026. Available at: https://www.whitecase.com/sites/default/files/2026-01/W%26C_Life%20Sciences%20%26%20AI%20Report_January%202026.pdf

131. McKinsey and Company. AI budgets grow in life sciences. Week in Charts, 2025. Available at: https://www.mckinsey.com/featured-insights/week-in-charts/ai-budgets-grow-in-life-sciences

132. Grand View Research. Artificial intelligence in healthcare market size, share and trends analysis report. Available at: https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market

133. The Royal Swedish Academy of Sciences. The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2024: Daron Acemoglu, Simon Johnson and James A. Robinson, for studies of how institutions are formed and affect prosperity. Stockholm: NobelPrize.org; 2024. Available from: https://www.nobelprize.org/prizes/economic-sciences/2024/summary/

134. Acemoglu D. The simple macroeconomics of AI. Economic Policy 2024;40(121):13-58. DOI: 10.1093/epolic/eiae042.

135. Acemoglu D. The Simple Macroeconomics of AI. 2024. DOI: 10.3386/w32487.

136. Acemoglu D, Restrepo P. Automation and New Tasks: How Technology Displaces and Reinstates Labor. Journal of Economic Perspectives 2019;33(2):3-30. DOI: 10.1257/jep.33.2.3.

137. Acemoglu D, Restrepo P. The Race between Man and Machine: Implications of Technology for Growth, Factor Shares, and Employment. American Economic Review 2018;108(6):1488-1542. DOI: 10.1257/aer.20160696.

138. Noy S, Zhang W. Experimental evidence on the productivity effects of generative artificial intelligence. Science 2023;381(6654):187-192. DOI: 10.1126/science.adh2586.

139. Brynjolfsson E, Li D, Raymond L. Generative AI at Work. The Quarterly Journal of Economics 2025;140(2):889-942. DOI: 10.1093/qje/qjae044.

140. Brynjolfsson E, Li D, Raymond L. Generative AI at Work. 2023. DOI: 10.3386/w31161.

141. Peng, S, Kalliamvakou, E, Cihon, P, Demirer, M. The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. arXiv 2023. DOI: 10.48550/arxiv.2302.06590.

142. Dell’Acqua F, McFowland E, Mollick E, Lifshitz H, Kellogg KC, Rajendran S, et al. Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. Organization Science 2026;37(2):403-423. DOI: 10.1287/orsc.2025.21838.

143. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van CB, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ 2024;385:e078378. DOI: 10.1136/bmj-2023-078378.

144. Moons KGM, Damen JAA, Kaul T, Hooft L, Andaur NC, Dhiman P, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ 2025;388:e082505. DOI: 10.1136/bmj-2024-082505.

145. Liu X, Cruz RS, Moher D, Calvert MJ, Denniston AK, The SACWG, et al. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nat Med 2020;26(9):1364-1374. DOI: 10.1038/s41591-020-1034-x.

146. Cruz RS, Liu X, Chan A, Denniston AK, Calvert MJ, The SACWG, et al. Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. Nat Med 2020;26(9):1351-1363. DOI: 10.1038/s41591-020-1037-7.

147. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. Nat Med 2022;28(5):924-933. DOI: 10.1038/s41591-022-01772-9.

148. Sounderajah V, Ashrafian H, Golub RM, Shetty S, De FJ, Hooft L, et al. Developing a reporting guideline for artificial intelligence-centred diagnostic test accuracy studies: the STARD-AI protocol. BMJ Open 2021;11(6):e047709. DOI: 10.1136/bmjopen-2020-047709.

149. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med 2025;31(1):60-69. DOI: 10.1038/s41591-024-03425-5.

150. Cacciamani, GE, Eppler, MB, Ganjavi, C, Pekan, A, Biedermann, B, Collins, GS, et al. Development of the ChatGPT, Generative Artificial Intelligence and Natural Large Language Models for Accountable Reporting and Use (CANGARU) Guidelines. arXiv 2023. DOI: 10.48550/arxiv.2307.08974.

151. Husereau D, Drummond M, Augustovski F, de BE, Briggs AH, Carswell C, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) Statement: Updated Reporting Guidance for Health Economic Evaluations. Value in Health 2022;25(1):3-9. DOI: 10.1016/j.jval.2021.11.1351.

152. Padula WV, Kreif N, Vanness DJ, Adamson B, Rueda J, Felizzi F, et al. Machine Learning Methods in Health Economics and Outcomes Research: The PALISADE Checklist: A Good Practices Report of an ISPOR Task Force. Value in Health 2022;25(7):1063-1080. DOI: 10.1016/j.jval.2022.03.022.

153. Fleurence RL, Dawoud D, Bian J, Higashi MK, Wang X, Xu H, et al. ELEVATE-GenAI: Reporting Guidelines for the Use of Large Language Models in Health Economics and Outcomes Research: An ISPOR Working Group Report. Value in Health 2025;28(11):1611-1625. DOI: 10.1016/j.jval.2025.06.018.

154. Fleurence RL, Wang X, Bian J, Higashi MK, Ayer T, Xu H, et al. A Taxonomy of Generative Artificial Intelligence in Health Economics and Outcomes Research: An ISPOR Working Group Report. Value in Health 2025;28(11):1601-1610. DOI: 10.1016/j.jval.2025.04.2167.

155. Fleurence RL, Bian J, Wang X, Xu H, Dawoud D, Higashi M, et al. Generative Artificial Intelligence for Health Technology Assessment: Opportunities, Challenges, and Policy Considerations: An ISPOR Working Group Report. Value in Health 2025;28(2):175-183. DOI: 10.1016/j.jval.2024.10.3846.

156. Ma X, Bellomo L, Magee K, Bennette CS, Tymejczyk O, Samant M, et al. Characterization of a Real-World Response Variable and Comparison with RECIST-Based Response Rates from Clinical Trials in Advanced NSCLC. Adv Ther 2021;38(4):1843-1859. DOI: 10.1007/s12325-021-01659-0.

157. Estevez M, Singh N, Dyson L, Adamson B, Krismer K, Magee K, et al. Ensuring Reliability of Curated Electronic Health Record-Derived Data: The Validation of Accuracy for Large Language Model-/Machine Learning-Extracted Information and Data (VALID) Framework. JCO Clin Cancer Inform 2026;10(1):e2500215. DOI: 10.1200/cci-25-00215.

158. Kenney RC, Chen X, Shintani K, Gagnon C, Liu J, DaCosta BS, et al. Validation of Non-Small Cell Lung Cancer Clinical Insights Using a Generalized Oncology Natural Language Processing Model. JCO Clin Cancer Inform 2024:e2300099. DOI: 10.1200/cci.23.00099.

159. Abedian S, Sholle ET, Adekkanattu PM, Cusick MM, Weiner SE, Shoag JE, et al. Automated Extraction of Tumor Staging and Diagnosis Information From Surgical Pathology Reports. JCO Clinical Cancer Informatics 2021:1054-1061. DOI: 10.1200/cci.21.00065.

160. Wang D, Florian H, Lynch S, Robieson W, Zhuang R, Kusiak C, et al. Using AI-generated digital twins to boost clinical trial efficiency in Alzheimer's disease. A&D Transl Res & Clin Interv 2025;11(4):e70181. DOI: 10.1002/trc2.70181.

161. Akiya I, Ishihara T, Yamamoto K. Comparison of Synthetic Data Generation Techniques for Control Group Survival Data in Oncology Clinical Trials: Simulation Study. JMIR Med Inform 2024;12:e55118-e55118. DOI: 10.2196/55118.

162. Kaabachi B, Despraz J, Meurers T, Otte K, Halilovic M, Kulynych B, et al. A scoping review of privacy and utility metrics in medical synthetic data. npj Digit. Med. 2025;8(1):60. DOI: 10.1038/s41746-024-01359-3.

163. Riskin DJ, Monda KL, Gagne JJ, Reynolds R, Garan AR, Dreyer N, et al. Implementing Accuracy, Completeness, and Traceability for Data Reliability. JAMA Netw Open 2025;8(3):e250128. DOI: 10.1001/jamanetworkopen.2025.0128.

164. Varma G, Yenukoti RK, Kumar MP, Ashrit BS, Purushotham K, Subash C, et al. A Deep Learning-Enabled Workflow to Estimate Real-World Progression-Free Survival in Patients With Metastatic Breast Cancer: Study Using Deidentified Electronic Health Records. JMIR Cancer 2025;11:e64697-e64697. DOI: 10.2196/64697.

