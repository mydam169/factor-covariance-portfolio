"""Shared config loading and data I/O helpers used across the pipeline."""

from typing import Any, Dict

import pandas as pd
import yaml


def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """Load the project config.yaml into a plain dict.

    TODO: implement via yaml.safe_load(open(config_path)).
    """
    raise NotImplementedError


def save_processed(df: pd.DataFrame, name: str, processed_dir: str = "data/processed") -> None:
    """Save a processed DataFrame to data/processed/{name}.parquet.

    TODO: implement. Use parquet, not csv, to preserve dtypes for the
    walk-forward engine.
    """
    raise NotImplementedError


def load_processed(name: str, processed_dir: str = "data/processed") -> pd.DataFrame:
    """Load a previously-saved processed DataFrame.

    TODO: implement.
    """
    raise NotImplementedError


def save_backtest_run(
    results: Dict[str, pd.DataFrame],
    run_name: str,
    results_dir: str = "results/backtest_runs",
) -> None:
    """Persist raw per-method output from backtest/engine.run_walk_forward.

    One parquet file per method under results/backtest_runs/{run_name}/,
    so a given walk-forward run can be reloaded for evaluation without
    re-running the (expensive) engine loop.

    TODO: implement (mkdir results_dir/run_name, loop over `results` dict,
    save each DataFrame as {method_label}.parquet).
    """
    raise NotImplementedError


def save_results_table(df: pd.DataFrame, name: str, results_dir: str = "results/tables") -> None:
    """Save a summary/comparison table (e.g., method comparison, significance
    test outputs) as CSV under results/tables/ -- CSV here rather than
    parquet since these are meant to be human-read/diffed, not reloaded
    programmatically at scale.

    TODO: implement.
    """
    raise NotImplementedError
