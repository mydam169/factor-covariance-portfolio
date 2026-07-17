"""Baseline sample (historical) covariance estimator.

Shared interface used by every estimator in this package:
    estimate(returns_df: pd.DataFrame, **kwargs) -> pd.DataFrame  (N x N)

This shared signature is what lets backtest/engine.py loop over methods
generically -- do not deviate from it in the other estimators.
"""

import pandas as pd


def estimate(returns: pd.DataFrame) -> pd.DataFrame:
    """Plain sample covariance matrix over the given return window.

    TODO: implement via returns.cov(). Trivial, but keep it as its own
    function so the walk-forward engine treats it identically to the
    other (more complex) estimators.
    """
    raise NotImplementedError
