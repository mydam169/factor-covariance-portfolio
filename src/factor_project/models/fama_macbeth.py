"""Fama-MacBeth two-pass regression -- ROBUSTNESS CHECK / APPENDIX ONLY.

Per project discussion: this is NOT a dependency for portfolio construction.
Pass 1 (per-stock betas) is already produced by
models/time_series_regression.py and reused directly by
covariance/factor_based.py. This module implements pass 2 only: testing
whether those betas are actually priced (i.e., whether higher factor
exposure corresponds to higher average realized return across the
cross-section), as a validity check on the factor premia -- not as an input
to the GMV/mean-variance pipeline.

Caveat to carry into any report generated from this module: with ~48 stocks
the cross-section is still thin for a reliable Fama-MacBeth estimate
(ideally hundreds of assets). Present lambda estimates with this caveat
attached, not as a definitive pricing test.
"""

from typing import Dict

import pandas as pd

from factor_project.models.time_series_regression import RegressionResult


def cross_sectional_regression(
    period_returns: pd.Series,
    betas: pd.DataFrame,
) -> pd.Series:
    """Single cross-sectional regression for one period t:
    r_i,t = lambda_0,t + lambda' beta_i + eta_i,t

    Returns the lambda vector (including intercept) for this period.

    TODO: implement via sm.OLS per period.
    """
    raise NotImplementedError


def run_fama_macbeth(
    returns: pd.DataFrame,
    pass1_results: Dict[str, RegressionResult],
) -> pd.DataFrame:
    """Run cross_sectional_regression for every period, then summarize:
    mean lambda per factor, time-series std error, t-stat.

    Returns a summary DataFrame: index=factor names (+ intercept),
    columns=[mean_lambda, se, t_stat, p_value].

    TODO: implement (loop over periods, collect lambdas, aggregate).
    """
    raise NotImplementedError
