"""Formal tests for whether Sharpe ratio differences across methods are
statistically significant, rather than eyeballing point estimates.

Per project discussion: with a limited number of effectively independent
out-of-sample rebalancing periods (even with 10 years of daily data,
monthly rebalancing gives only ~120 periods), point-estimate Sharpe
comparisons across 4+ methods will be noisy. Use one or both of:
- Jobson-Korkie test with Memmel's correction (pairwise Sharpe comparison)
- Stationary bootstrap over realized return paths
"""

import pandas as pd


def jobson_korkie_memmel(returns_a: pd.Series, returns_b: pd.Series) -> dict:
    """Test whether Sharpe(returns_a) - Sharpe(returns_b) is significant.

    Returns {'sharpe_diff', 'z_stat', 'p_value'}.

    TODO: implement (Jobson & Korkie 1981, Memmel 2003 correction).
    """
    raise NotImplementedError


def stationary_bootstrap_sharpe_ci(
    returns: pd.Series,
    n_boot: int = 1000,
    block_size_expected: int = 10,
) -> dict:
    """Bootstrap confidence interval on the Sharpe ratio of a single return series.

    Returns {'sharpe', 'ci_lower', 'ci_upper'}.

    TODO: implement, likely via `arch.bootstrap.StationaryBootstrap`
    (confirm this is the right tool once we get here -- flagged as
    unconfirmed in requirements.txt).
    """
    raise NotImplementedError
