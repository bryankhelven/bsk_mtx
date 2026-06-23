# Artifact Guide

## Paper-to-artifact navigation

| Paper component | Canonical artifact |
|---|---|
| Corpus composition | `data/gold/coverage_final_1497.csv` |
| Raw applicability agreement | `results/tables/raw_applicability_agreement_with_ci.csv` |
| Axis agreement | `data/gold/iaa_metrics_final_1497.csv` |
| Consensus selection effect | `results/tables/consensus_subset_retention.csv` |
| Human 3×3 and 5×5 matrices | `results/figures/human_consensus_3x3.png`, `results/figures/human_consensus_5x5.png` |
| Complete model comparison | `results/tables/full_model_comparison.csv` |
| Selected model summaries | `results/tables/standardized_model_summary.csv` |
| Paired statistical tests | `results/tables/paired_model_comparisons.csv` |
| Per-class results | `results/tables/per_class_metrics.csv` |
| Disagreement-aware experiment | `results/tables/disagreement_aware_corrected.csv` |
| 2024 gate comparison | `results/tables/2024_pipeline_agreement.csv` |
| 2024 regions | `results/tables/2024_region_counts.csv` |
| 2024 matrices | `results/figures/2024_*.png` |
| Linguistic audit | `results/tables/2024_linguistic_audit_summary.csv` |

## Verification levels

### Level 1: released-artifact verification

Use `requirements.txt`, `scripts/verify_release.py`, and
`scripts/smoke_test_notebooks.py`. This checks the released data and compact
verification notebooks without retraining BERTimbau.

### Level 2: complete retraining

Use `requirements-training.txt` and
`notebooks/02_repeated_cv_models_and_projection.ipynb`. New outputs are written
to `reproduced_results/`.

The historical environment snapshot under `environment/` is provenance, not an
installable requirements file.
