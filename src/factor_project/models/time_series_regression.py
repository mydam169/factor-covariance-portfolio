"""Time-series factor regressions (FF3 / FF5), per-stock and portfolio-level.

This is Fama-MacBeth "pass 1" when reused for that purpose, but the primary
use here is direct: estimating betas (B) and idiosyncratic residual
variances (D) per stock, which feed the factor-based covariance estimator
in covariance/factor_based.py.

Design decision from project discussion: use HAC (Newey-West) standard
errors, not HC3 -- residual autocorrelation was detected via ACF/Ljung-Box
in the original notebook, and HC3 only corrects for heteroskedasticity.
"""

from typing import Dict, NamedTuple

import pandas as pd


class RegressionResult(NamedTuple):
    """Container for a single stock's (or portfolio's) factor regression."""
    alpha: float
    betas: pd.Series          # index: factor names
    resid_variance: float     # idiosyncratic variance, feeds D in Sigma = B Sigma_F B' + D
    r_squared: float
    fitted_model: object      # raw statsmodels result, kept for diagnostics.py


def fit_factor_regression(
    asset_returns: pd.Series,
    factor_returns: pd.DataFrame,
    hac_maxlags: int = 5,
) -> RegressionResult:
    """Fit r_i = alpha + B' f + eps via OLS with HAC standard errors.

    TODO: implement via sm.OLS(...).fit(cov_type='HAC', cov_kwds={'maxlags': hac_maxlags}).
    """
    raise NotImplementedError


def fit_all_assets(
    returns: pd.DataFrame,
    factor_returns: pd.DataFrame,
    hac_maxlags: int = 5,
) -> Dict[str, RegressionResult]:
    """Run fit_factor_regression for every column (asset) in `returns`.

    Returns {ticker: RegressionResult}. This is the per-stock pass-1 step
    discussed for both the factor-covariance construction and (optionally)
    Fama-MacBeth pass 2.

    TODO: implement (loop + fit_factor_regression).
    """
    raise NotImplementedError
