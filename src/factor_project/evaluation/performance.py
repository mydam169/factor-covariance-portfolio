"""Performance metrics computed on backtest output.

Per project discussion, turnover and concentration matter as much as Sharpe
here -- shrinkage/factor methods are expected to show their advantage in
stability (lower turnover, lower concentration) even where raw Sharpe
differences are statistically weak given limited effective sample size.
"""

import pandas as pd


def sharpe_ratio(returns: pd.Series, periods_per_year: int = 252) -> float:
    """TODO: implement. Annualized mean / annualized std."""
    raise NotImplementedError


def max_drawdown(returns: pd.Series) -> float:
    """TODO: implement via cumulative product of (1+returns)."""
    raise NotImplementedError


def herfindahl_index(weights: pd.Series) -> float:
    """Concentration metric: sum(w_i^2). TODO: implement."""
    raise NotImplementedError


def summarize_method(
    returns: pd.Series,
    weights_history: pd.DataFrame,
    turnover_history: pd.Series,
) -> dict:
    """Package all metrics above (+ annualized return/vol) into one dict,
    for building the final method-comparison table.

    TODO: implement.
    """
    raise NotImplementedError
