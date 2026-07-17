"""Factor-based covariance estimator: Sigma = B Sigma_F B' + D.

Same interface as historical.estimate: (returns_df) -> Sigma (N x N).

Inputs needed (produced by models/time_series_regression.py):
- B: N x K matrix of factor loadings (betas) per stock
- Sigma_F: K x K covariance matrix of the factors themselves
- D: N x N diagonal matrix of idiosyncratic (residual) variances per stock

This is the estimator this whole project's research question is about, so
it's the one most worth unit-testing carefully against a small synthetic
example before trusting it inside the 48-stock walk-forward loop.
"""

import pandas as pd

from factor_project.models.time_series_regression import fit_all_assets


def estimate(
    returns: pd.DataFrame,
    factor_returns: pd.DataFrame,
    hac_maxlags: int = 5,
) -> pd.DataFrame:
    """Estimate Sigma via the factor-model decomposition.

    Steps (TODO: implement):
    1. results = fit_all_assets(returns, factor_returns, hac_maxlags)
    2. B = stack betas per asset into an N x K DataFrame
    3. Sigma_F = factor_returns.cov()
    4. D = diag of resid_variance per asset (N x N)
    5. Sigma = B @ Sigma_F @ B.T + D
    """
    raise NotImplementedError
