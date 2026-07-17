"""Formal diagnostic tests for factor regressions.

Replaces the "eyeball the ACF/QQ plot" approach from the original notebook
with actual test statistics and p-values, per project discussion:
- Ljung-Box: residual autocorrelation (was imported but never called originally)
- Breusch-Pagan / White: heteroskedasticity
- Jarque-Bera: normality (QQ plot showed fat tails -- quantify it)
- VIF: multicollinearity among FF5 factors (SMB/HML/RMW/CMA are correlated
  by construction)
"""

import pandas as pd


def ljung_box_test(residuals: pd.Series, lags: int = 20) -> pd.DataFrame:
    """TODO: implement via statsmodels.stats.diagnostic.acorr_ljungbox."""
    raise NotImplementedError


def breusch_pagan_test(residuals: pd.Series, exog: pd.DataFrame) -> dict:
    """TODO: implement via statsmodels.stats.diagnostic.het_breuschpagan."""
    raise NotImplementedError


def jarque_bera_test(residuals: pd.Series) -> dict:
    """TODO: implement via statsmodels.stats.stattools.jarque_bera."""
    raise NotImplementedError


def variance_inflation_factors(factor_returns: pd.DataFrame) -> pd.Series:
    """TODO: implement via statsmodels.stats.outliers_influence.variance_inflation_factor,
    looped over columns of factor_returns (with constant added)."""
    raise NotImplementedError


def run_full_diagnostic_suite(
    residuals: pd.Series,
    exog: pd.DataFrame,
) -> dict:
    """Convenience wrapper running all of the above and returning a single
    dict/report, to be logged per asset in fit_all_assets output.

    TODO: implement (call the four functions above, package results).
    """
    raise NotImplementedError
