# Independent (blinded) LLM classification audit — summary

Input: `/home/user/workspace/data/sample_for_llm_audit.jsonl` (300 records)
Output: `/home/user/workspace/data/llm_audit_labels.json` (300 keys, validated, key set identical to input pmids)
Partials retained: `llm_audit_partial_0.json` … `llm_audit_partial_11.json` (25 records each)
Blinding respected: no dictionary labels, eligible.csv, screened.jsonl, or bibliometrics scripts were opened. All labels made by reading each title/abstract; no keyword script used.

## Records classified
300 / 300

## Domain counts (multi-label; 91 records had no domain)
| domain | n |
|---|---|
| rwd_causal | 75 |
| economic_evaluation | 69 |
| governance_reporting | 68 |
| outcome_prediction | 50 |
| evidence_synthesis | 46 |
| decision_modeling | 30 |
| hta_access | 25 |
| pro_preferences | 22 |

## Method counts (single label)
| method | n |
|---|---|
| ai_general | 74 |
| classical_ml | 73 |
| deep_learning | 63 |
| none | 61 |
| nlp | 17 |
| generative_llm | 12 |

## HEOR relevance
- true: 154
- false: 146

## Conventions applied (for interpreting disagreement with the dictionary)
- Incidental "cost-effective(ness)" wording in non-economic abstracts (devices, imaging, lab assays, engineering, agriculture, energy) did NOT earn `economic_evaluation`; only formal costing/CEA/CUA/CBA/budget-impact work did. Non-health cost-benefit analyses received `economic_evaluation` but `heor_relevant: false`.
- Claims/EHR/registry/administrative/surveillance data and causal-inference designs (propensity score, HTE, target trial) → `rwd_causal`.
- Formal quality/risk-of-bias tools (PROBAST, ROBINS-I, CHEC, QUADAS-2), reporting standards, regulation, ethics, equity, bias/fairness, explainability-as-focus → `governance_reporting`.
- Markov / decision tree / microsimulation / PSA / in-silico or scenario simulation → `decision_modeling`.
- Method mapping: BERT-style text classifiers and rule-based/NLP pipelines → `nlp`; GPT/RAG/agentic LLM → `generative_llm`; neural nets (incl. MLP, SOM, CNN, GAN/CTGAN) on non-language tasks → `deep_learning`; tree ensembles, SVM, LASSO, clustering, RL, generic "ML" → `classical_ml`; narrative AI reviews without an identifiable family → `ai_general`; no AI at all → `none`.
- `heor_relevant: false` for purely clinical/diagnostic-accuracy, bench, veterinary, educational, and non-health engineering work, even when a cost figure appears.
