#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = json.loads((ROOT / "expected_results.json").read_text(encoding="utf-8"))
errors = []
required = [
    "README.md", "REPRODUCIBILITY.md", "ARTIFACT_GUIDE.md", "DATA_AVAILABILITY.md",
    "SOURCE_MANIFEST.csv", "CHECKSUMS.sha256", "requirements-training.txt",
    "docs/annotation_manual_ptbr.md", "docs/annotation_manual_en.md",
    "data/gold/applicability_gold_final_1497.csv",
    "data/gold/axis_gold_consensus_3class_only.csv",
    "data/gold/axis_gold_consensus_5class_only.csv",
    "data/gold/final_pairwise_annotations_1497.csv",
    "data/validation/formal_applicability_gold_1497.csv",
    "data/validation/paired_axis_annotations_733.csv",
    "data/validation/exact_consensus_gold_3class_395.csv",
    "data/validation/exact_consensus_gold_5class_244.csv",
    "results/tables/formal_gold_validation_summary.csv",
    "results/tables/standardized_model_summary.csv",
    "results/tables/paired_model_comparisons.csv",
    "results/tables/disagreement_aware_corrected.csv",
    "data/external_2024/corpus_2024.csv",
    "data/external_2024/linear_predictions.csv",
    "data/external_2024/hybrid_predictions.csv",
]
for relative in required:
    if not (ROOT / relative).exists():
        errors.append(f"Missing required file: {relative}")
for path in ROOT.rglob("*"):
    if any(token in str(path) for token in ["_extracted", "runtime_no_checkpoints", "transformer_runtime_no_checkpoints", "review_packages_split", "manual_validation_2024_50_model_key_DO_NOT_SHOW.csv", "Zone.Identifier"]):
        errors.append(f"Forbidden release path: {path.relative_to(ROOT)}")
patterns = [r"/home/[^/\s]+", r"[A-Za-z]:\\Users\\[^\\\s]+", r"\bbryan\b", r"\bbkhelios\b", r"@gmail\.com"]
for path in ROOT.rglob("*"):
    if path.resolve() == Path(__file__).resolve():
        continue
    if not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".py", ".json", ".csv", ".ipynb"}:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for pattern in patterns:
        if re.search(pattern, text, flags=re.I):
            errors.append(f"Potential identifying content in {path.relative_to(ROOT)}: {pattern}")
app = pd.read_csv(ROOT / "data/gold/applicability_gold_final_1497.csv")
app_col = next(column for column in app.columns if "applicability" in column.lower() and "a1" not in column.lower() and "a2" not in column.lower())
checks = {
    "main_total": len(app),
    "applicable": int((app[app_col] == 1).sum()),
    "excluded": int((app[app_col] == 0).sum()),
    "consensus_3class": len(pd.read_csv(ROOT / "data/gold/axis_gold_consensus_3class_only.csv")),
    "consensus_5class": len(pd.read_csv(ROOT / "data/gold/axis_gold_consensus_5class_only.csv")),
}
for key, actual in checks.items():
    expected = EXPECTED["corpus"][key]
    if actual != expected:
        errors.append(f"Count mismatch {key}: expected {expected}, got {actual}")
validation_checks = {
    "formal_applicability_gold_1497.csv": 1497,
    "paired_axis_annotations_733.csv": 733,
    "exact_consensus_gold_3class_395.csv": 395,
    "exact_consensus_gold_5class_244.csv": 244,
}
for filename, expected_rows in validation_checks.items():
    frame = pd.read_csv(ROOT / "data/validation" / filename)
    actual_rows = len(frame)
    if actual_rows != expected_rows:
        errors.append(
            f"Validation row-count mismatch {filename}: "
            f"expected {expected_rows}, got {actual_rows}"
        )

paired = pd.read_csv(
    ROOT / "data/validation/paired_axis_annotations_733.csv"
)
paired_allowed = {
    "a1_acceptance_5": {-2, -1, 0, 1, 2},
    "a1_intensity_5": {1, 2, 3, 4, 5},
    "a2_acceptance_5": {-2, -1, 0, 1, 2},
    "a2_intensity_5": {1, 2, 3, 4, 5},
    "a1_acceptance_3": {-1, 0, 1},
    "a1_intensity_3": {0, 1, 2},
    "a2_acceptance_3": {-1, 0, 1},
    "a2_intensity_3": {0, 1, 2},
}
for column, allowed in paired_allowed.items():
    values = pd.to_numeric(paired[column], errors="coerce")
    if values.isna().any():
        errors.append(f"Missing or non-numeric paired label in {column}")
    invalid = sorted(set(values.dropna()) - allowed)
    if invalid:
        errors.append(f"Invalid paired labels in {column}: {invalid}")

# Top-level requirements must be installable and must not contain local Conda
# build paths or private-only packages.
requirements_text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
if "file:///" in requirements_text:
    errors.append("Top-level requirements.txt contains non-portable file URLs")
if "ace_tools" in requirements_text:
    errors.append("Top-level requirements.txt contains private-only ace_tools")

# Notebook code must be syntactically valid. The full training notebook must
# include the configuration that defines all path and experiment constants.
for notebook_path in sorted((ROOT / "notebooks").glob("*.ipynb")):
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    code = "\n\n".join(
        "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    )
    try:
        compile(code, str(notebook_path), "exec")
    except SyntaxError as exc:
        errors.append(f"Notebook syntax error in {notebook_path.name}: {exc}")

training_notebook = json.loads(
    (ROOT / "notebooks/02_repeated_cv_models_and_projection.ipynb")
    .read_text(encoding="utf-8")
)
training_code = "\n".join(
    "".join(cell.get("source", []))
    for cell in training_notebook.get("cells", [])
    if cell.get("cell_type") == "code"
)
for required_symbol in [
    "REPO_ROOT",
    "RESULTS_DIR",
    "INPUT_SEARCH_DIRS",
    "APP_FILE_NAME",
    "AXIS3_FILE_NAME",
    "AXIS5_FILE_NAME",
]:
    if required_symbol not in training_code:
        errors.append(
            f"Training notebook is missing required configuration: {required_symbol}"
        )

external = pd.read_csv(ROOT / "data/external_2024/corpus_2024.csv")
if len(external) != EXPECTED["external_2024"]["external_2024_records"]:
    errors.append("External 2024 row-count mismatch")
if external["text_hash"].nunique() != EXPECTED["external_2024"]["external_2024_unique_hashes"]:
    errors.append("External 2024 unique-hash mismatch")
if errors:
    print("Release verification failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print("Release verification passed.")
print(json.dumps(EXPECTED, indent=2))
