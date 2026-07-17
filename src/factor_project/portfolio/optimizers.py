"""Portfolio construction methods sharing a common interface:
    construct(mu: pd.Series | None, Sigma: pd.DataFrame, **kwargs) -> pd.Series (weights)

mu is None for GMV and equal_weight (covariance-only methods, per project
decision to sidestep mean-estimation error for now). Keep the signature
uniform anyway so the backtest engine can call all three methods the same
way without branching.
"""

import pandas as pd


def gmv(Sigma: pd.DataFrame, long_only: bool = True, max_weight: float = 0.15) -> pd.Series:
    """Global minimum variance portfolio: min w' Sigma w s.t. sum(w)=1 [, w>=0, w<=max_weight].

    TODO: implement via cvxpy (needed once long-only / max-weight
    constraints are active -- closed-form GMV only holds unconstrained).
    """
    raise NotImplementedError


def mean_variance(
    mu: pd.Series,
    Sigma: pd.DataFrame,
    risk_aversion: float = 1.0,
    long_only: bool = True,
    max_weight: float = 0.15,
) -> pd.Series:
    """Mean-variance optimal portfolio: max w'mu - risk_aversion/2 * w'Sigma w.

    TODO: implement via cvxpy. Confirm what `mu` is sourced from before
    implementing (historical mean vs. factor-implied) -- see project
    discussion on holding mu fixed across Sigma methods to isolate the
    Sigma-estimator effect.
    """
    raise NotImplementedError


def equal_weight(assets: list) -> pd.Series:
    """Naive 1/N benchmark. Do not remove -- see DeMiguel et al. 2009.

    TODO: implement (trivial).
    """
    raise NotImplementedError
