#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"

def execute_notebook(path: Path, cells=None, env=None):
    notebook = nbformat.read(path, as_version=4)
    if cells is not None:
        notebook.cells = [notebook.cells[index] for index in cells]
    old_env = os.environ.copy()
    try:
        if env:
            os.environ.update(env)
        old_cwd = Path.cwd()
        os.chdir(ROOT)
        try:
            client = NotebookClient(
                notebook,
                timeout=600,
                kernel_name="python3",
                allow_errors=False,
            )
            client.execute()
        finally:
            os.chdir(old_cwd)
    finally:
        os.environ.clear()
        os.environ.update(old_env)

def main():
    for name in [
        "01_gold_agreement_and_mapping_audit.ipynb",
        "03_disagreement_aware_analysis.ipynb",
        "04_external_2024_audit_and_matrices.ipynb",
    ]:
        print(f"Executing {name}...")
        execute_notebook(NOTEBOOK_DIR / name)

    # Execute only configuration, utility, and input-audit cells from the full
    # retraining notebook. This validates imports and repository-relative paths
    # without starting model training.
    with tempfile.TemporaryDirectory() as temp_dir:
        print("Executing setup/input audit from notebook 02...")
        execute_notebook(
            NOTEBOOK_DIR / "02_repeated_cv_models_and_projection.ipynb",
            cells=[0, 1, 2, 3],
            env={"AXIOLOGICAL_RESULTS_DIR": temp_dir},
        )

    print("Notebook smoke tests passed.")

if __name__ == "__main__":
    main()
