# Public Repository Build Report

- Builder version: `1.0.4`
- Private project root: `<private-project-root>`
- Public repository: `axiological_matrix_repo`
- Text policy: `redacted`

## Validated counts

- `applicable`: 734
- `consensus_3class`: 395
- `consensus_5class`: 244
- `excluded`: 763
- `external_2024_hybrid_applicable`: 752
- `external_2024_linear_applicable`: 773
- `external_2024_non_portuguese`: 124
- `external_2024_records`: 989
- `external_2024_unique_hashes`: 973
- `formal_validation_applicability`: 1497
- `formal_validation_consensus_3class`: 395
- `formal_validation_consensus_5class`: 244
- `formal_validation_paired_axes`: 733
- `local_pairwise_items_different_from_canonical`: 1
- `main_total`: 1497
- `raw_conflicts`: 173

## Included artifacts

- `docs/annotation_manual_ptbr.md` — Final annotation manual (source: `repo_builder/templates/annotation_manual_ptbr.md`)
- `docs/annotation_manual_en.md` — Final annotation manual (source: `repo_builder/templates/annotation_manual_en.md`)
- `data/gold/applicability_gold_final_1497.csv` — Canonical gold artifact: app_gold (source: `final_full_consolidation_1497_REBUILT/applicability_gold_final_1497.csv`)
- `data/gold/axis_gold_consensus_3class_only.csv` — Canonical gold artifact: axis3 (source: `final_full_consolidation_1497_REBUILT/axis_gold_consensus_3class_only.csv`)
- `data/gold/axis_gold_consensus_5class_only.csv` — Canonical gold artifact: axis5 (source: `final_full_consolidation_1497_REBUILT/axis_gold_consensus_5class_only.csv`)
- `data/gold/final_app_adjudication_application_log.csv` — Canonical gold artifact: adjudication_log (source: `final_full_consolidation_1497_REBUILT/final_app_adjudication_application_log.csv`)
- `data/gold/coverage_final_1497.csv` — Canonical gold artifact: coverage (source: `final_full_consolidation_1497_REBUILT/coverage_final_1497.csv`)
- `data/gold/iaa_metrics_final_1497.csv` — Canonical gold artifact: iaa (source: `final_full_consolidation_1497_REBUILT/iaa_metrics_final_1497.csv`)
- `data/gold/final_pairwise_annotations_1497.csv` — Exact pairwise annotation snapshot used by the submitted paper, joined to locally sanitized text (source: `repo_builder/templates/canonical_pairwise_axis_snapshot.csv`)
- `results/tables/raw_applicability_agreement_with_ci.csv` — Final paper-relevant table: raw_agreement (source: `ENIAC_AUDIT_COMPLETION/tables/02_raw_applicability_agreement_with_ci.csv`)
- `results/tables/standardized_metrics_by_seed.csv` — Final paper-relevant table: metrics_by_seed (source: `ENIAC_AUDIT_COMPLETION/tables/10_standardized_metrics_by_seed.csv`)
- `results/tables/standardized_model_summary.csv` — Final paper-relevant table: model_summary (source: `ENIAC_AUDIT_COMPLETION/tables/11_standardized_model_summary_across_seeds.csv`)
- `results/tables/full_model_comparison.csv` — Final paper-relevant table: full_model_table (source: `ENIAC_AUDIT_COMPLETION/tables/12_paper_ready_full_model_table.csv`)
- `results/tables/per_class_metrics.csv` — Final paper-relevant table: per_class (source: `ENIAC_AUDIT_COMPLETION/tables/14_per_class_metrics_mean_std.csv`)
- `results/tables/normalized_confusion_mean_std.csv` — Final paper-relevant table: normalized_confusion (source: `ENIAC_AUDIT_COMPLETION/tables/16_normalized_confusion_mean_std.csv`)
- `results/tables/paired_model_comparisons.csv` — Final paper-relevant table: paired_tests (source: `ENIAC_AUDIT_COMPLETION/tables/20_paired_bootstrap_and_permutation_results.csv`)
- `results/tables/hyperparameter_inventory.csv` — Final paper-relevant table: hyperparameters (source: `ENIAC_AUDIT_COMPLETION/tables/28_complete_hyperparameter_inventory.csv`)
- `results/tables/consensus_subset_retention.csv` — Final paper-relevant table: consensus_retention (source: `ENIAC_AUDIT_EXPERIMENTAL_REVIEW/tables/10_consensus_subset_retention_summary.csv`)
- `results/tables/consensus_removed_agreement.csv` — Final paper-relevant table: consensus_removed (source: `ENIAC_AUDIT_EXPERIMENTAL_REVIEW/tables/14_consensus_retained_removed_agreement_rates.csv`)
- `results/tables/intensity_mapping_audit.csv` — Final paper-relevant table: mapping_audit (source: `ENIAC_AUDIT_EXPERIMENTAL_REVIEW/tables/15_alternative_intensity_3_mapping_audit.csv`)
- `results/tables/disagreement_aware_corrected.csv` — Final paper-relevant table: disagreement_summary (source: `ENIAC_AUDIT_PATCH_AND_2024/disagreement_aware_corrected/11_corrected_disagreement_summary.csv`)
- `results/tables/disagreement_aware_paper_table.csv` — Final paper-relevant table: disagreement_paper (source: `ENIAC_AUDIT_PATCH_AND_2024/disagreement_aware_corrected/12_corrected_disagreement_paper_table.csv`)
- `results/tables/2024_region_counts.csv` — Final paper-relevant table: region_counts (source: `ENIAC_AUDIT_PATCH_AND_2024/2024_analysis/tables/09_external_2024_region_counts.csv`)
- `results/tables/2024_pipeline_agreement.csv` — Final paper-relevant table: pipeline_agreement (source: `ENIAC_AUDIT_PATCH_AND_2024/2024_analysis/tables/10_external_2024_pipeline_agreement.csv`)
- `results/predictions/tfidf_oof_predictions.csv` — OOF predictions: tfidf_oof (source: `FINAL_ENIAC_1497_RESULTS/predictions/tfidf_shared_splits_predictions.csv`)
- `results/predictions/bertimbau_oof_predictions.csv` — OOF predictions: bert_oof (source: `FINAL_ENIAC_1497_RESULTS/predictions/bertimbau_repeated_cv_predictions.csv`)
- `results/predictions/disagreement_aware_oof_predictions.csv` — OOF predictions: disagreement_oof (source: `ENIAC_AUDIT_PATCH_AND_2024/disagreement_aware_corrected/09_corrected_disagreement_oof_predictions.csv`)
- `data/external_2024/corpus_2024.csv` — Sanitized external 2024 corpus (source: `corpus_ia_educacao_2024_final.json`)
- `data/external_2024/linear_predictions.csv` — Linear 2024 projection (source: `FINAL_ENIAC_1497_RESULTS/predictions/external_2024_linear_predictions.csv`)
- `data/external_2024/hybrid_predictions.csv` — Hybrid 2024 projection (source: `FINAL_ENIAC_1497_RESULTS/predictions/external_2024_hybrid_predictions.csv`)
- `results/tables/2024_linguistic_audit_item_level.csv` — Final 2024 linguistic audit (source: `repo_builder/templates/canonical_2024_language_assignments.csv`)
- `results/tables/2024_linguistic_audit_summary.csv` — Final 2024 linguistic audit summary (source: `repo_builder/templates/canonical_2024_language_assignments.csv`)
- `data/validation/formal_applicability_gold_1497.csv` — Primary formal applicability validation gold (source: `final_full_consolidation_1497_REBUILT/applicability_gold_final_1497.csv`)
- `data/validation/paired_axis_annotations_733.csv` — Paired A1/A2 axis labels used for human agreement analyses (source: `final_full_consolidation_1497_REBUILT/final_pairwise_annotations_1497.csv`)
- `data/validation/exact_consensus_gold_3class_395.csv` — Exact-consensus three-class human gold (source: `final_full_consolidation_1497_REBUILT/axis_gold_consensus_3class_only.csv`)
- `data/validation/exact_consensus_gold_5class_244.csv` — Exact-consensus five-class human gold (source: `final_full_consolidation_1497_REBUILT/axis_gold_consensus_5class_only.csv`)
- `results/tables/formal_gold_validation_summary.csv` — Generated summary of the formal verified/adjudicated human gold
- `data/validation/README.md` — Generated explanation of the formal human validation package
- `results/figures/human_consensus_3x3.png` — Paper-relevant figure: figure_human_3x3 (source: `FINAL_ENIAC_1497_RESULTS/figures/consensus_gold_3x3_matrix.png`)
- `results/figures/human_consensus_5x5.png` — Paper-relevant figure: figure_human_5x5 (source: `FINAL_ENIAC_1497_RESULTS/figures/consensus_gold_5x5_matrix.png`)
- `results/figures/2024_linear_3x3.png` — Paper-relevant figure: figure_linear_3x3 (source: `FINAL_ENIAC_1497_RESULTS/figures/external_2024_linear_3x3_matrix.png`)
- `results/figures/2024_hybrid_3x3.png` — Paper-relevant figure: figure_hybrid_3x3 (source: `FINAL_ENIAC_1497_RESULTS/figures/external_2024_hybrid_3x3_matrix.png`)
- `results/figures/2024_linear_5x5.png` — Paper-relevant figure: figure_linear_5x5 (source: `FINAL_ENIAC_1497_RESULTS/figures/external_2024_linear_5x5_matrix.png`)
- `results/figures/2024_hybrid_5x5.png` — Paper-relevant figure: figure_hybrid_5x5 (source: `FINAL_ENIAC_1497_RESULTS/figures/external_2024_hybrid_5x5_matrix.png`)
- `results/figures/confusion_applicability_bertimbau.png` — Paper-relevant figure: figure_conf_app (source: `ENIAC_AUDIT_COMPLETION/figures/normalized_confusion_applicability_transformer_bertimbau_weighted_raw.png`)
- `results/figures/confusion_acceptance_3_linearsvc.png` — Paper-relevant figure: figure_conf_acc3 (source: `ENIAC_AUDIT_COMPLETION/figures/normalized_confusion_acceptance_3_tfidf_tfidf_word_linearsvc_raw_raw.png`)
- `results/figures/confusion_intensity_3_bertimbau.png` — Paper-relevant figure: figure_conf_int3 (source: `ENIAC_AUDIT_COMPLETION/figures/normalized_confusion_intensity_3_transformer_bertimbau_weighted_raw.png`)
- `results/tables/human_consensus_3x3_counts.csv` — Paper-relevant matrix counts: matrix_human_3x3 (source: `FINAL_ENIAC_1497_RESULTS/tables/consensus_gold_3x3_matrix.csv`)
- `results/tables/human_consensus_5x5_counts.csv` — Paper-relevant matrix counts: matrix_human_5x5 (source: `FINAL_ENIAC_1497_RESULTS/tables/consensus_gold_5x5_matrix.csv`)
- `results/tables/2024_linear_3x3_counts.csv` — Paper-relevant matrix counts: matrix_linear_3x3 (source: `FINAL_ENIAC_1497_RESULTS/tables/external_2024_linear_3x3_matrix.csv`)
- `results/tables/2024_hybrid_3x3_counts.csv` — Paper-relevant matrix counts: matrix_hybrid_3x3 (source: `FINAL_ENIAC_1497_RESULTS/tables/external_2024_hybrid_3x3_matrix.csv`)
- `results/tables/2024_linear_5x5_counts.csv` — Paper-relevant matrix counts: matrix_linear_5x5 (source: `FINAL_ENIAC_1497_RESULTS/tables/external_2024_linear_5x5_matrix.csv`)
- `results/tables/2024_hybrid_5x5_counts.csv` — Paper-relevant matrix counts: matrix_hybrid_5x5 (source: `FINAL_ENIAC_1497_RESULTS/tables/external_2024_hybrid_5x5_matrix.csv`)
- `environment/training_environment.csv` — Environment artifact: environment_csv (source: `ENIAC_AUDIT_PATCH_AND_2024/environment/01_training_and_audit_environment.csv`)
- `environment/requirements_snapshot.txt` — Environment artifact: requirements (source: `ENIAC_AUDIT_PATCH_AND_2024/environment/requirements_snapshot.txt`)
- `environment/EXPERIMENTAL_ENVIRONMENT_PROVENANCE.md` — Environment artifact: environment_provenance (source: `ENIAC_AUDIT_PATCH_AND_2024/environment/EXPERIMENTAL_ENVIRONMENT_PROVENANCE.md`)
- `requirements.txt` — Top-level dependency snapshot (source: `ENIAC_AUDIT_PATCH_AND_2024/environment/requirements_snapshot.txt`)
- `notebooks/01_gold_agreement_and_mapping_audit.ipynb` — Generated gold and agreement verification notebook
- `notebooks/02_repeated_cv_models_and_projection.ipynb` — Cleaned final training and projection notebook (source: `eniac_final_1497_retraining_and_projection.ipynb`)
- `notebooks/03_disagreement_aware_analysis.ipynb` — Generated corrected disagreement-aware notebook
- `notebooks/04_external_2024_audit_and_matrices.ipynb` — Generated external 2024 verification notebook
- `README.md` — Generated README
- `docs/data_collection.md` — Generated data-collection documentation
- `docs/adjudication_flow.md` — Generated adjudication-flow documentation
- `docs/paper_to_artifact_map.md` — Generated paper-to-artifact map
- `ARTIFACT_GUIDE.md` — Generated artifact guide
- `DATA_AVAILABILITY.md` — Generated data-availability policy
- `LICENSE` — Generated code license
- `expected_results.json` — Generated expected-results file
- `.gitignore` — Generated Git ignore rules
- `scripts/verify_release.py` — Generated release verifier
- `BUILD_REPORT.md` — Generated build report
- `CHECKSUMS.sha256` — Generated release checksums

## Warnings

- The local pairwise working file differs from the exact paper snapshot for 1 item(s). Examples: 298. The bundled canonical snapshot was used.

## Errors

- None.

## Intentionally excluded

- duplicate bundles and ZIPs;
- `_extracted/` directories;
- checkpoints and runtime folders;
- internal review packages and prompts;
- private blind-validation model keys;
- superseded notebooks and preliminary provenance patch files;
- abandoned LLM experiments;
- OS metadata, author names, e-mails, local usernames, and absolute paths.

## Post-build reproducibility audit

The uploaded release passed all scientific count and checksum checks. A second
audit repaired two packaging defects:

- the top-level dependency file contained a non-portable full Conda snapshot;
- the cleaned full-training notebook had lost its configuration cell.

The repaired release now separates lightweight verification dependencies from
full-training dependencies and includes notebook smoke tests.
