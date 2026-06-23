# Reproducibility

## Lightweight verification

The lightweight environment verifies released counts, agreement values,
prediction-derived metrics, matrices, and the three compact notebooks.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/verify_release.py
python scripts/smoke_test_notebooks.py
```

## Full model retraining

```bash
pip install -r requirements-training.txt
jupyter lab
```

Run:

```text
notebooks/02_repeated_cv_models_and_projection.ipynb
```

The notebook writes to `reproduced_results/`. It does not overwrite the released
paper-facing artifacts in `results/`.

BERTimbau retraining requires network access to download
`neuralmind/bert-base-portuguese-cased`, unless it is already cached. A
CUDA-capable GPU is strongly recommended.

## Environment snapshot

`environment/requirements_snapshot.txt` is the full historical environment
snapshot. It contains platform-specific package references and is retained only
for provenance. It is not intended for direct installation.
