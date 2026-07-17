"""Walk-forward backtest engine.

Loops over rebalance dates; at each date, for each (covariance_method,
portfolio_method) pair:
  1. Slice the trailing `estimation_window_days` of returns (ROLLING window,
     not expanding -- see stationarity discussion in project log).
  2. Estimate Sigma via the given covariance method.
  3. Construct weights via the given portfolio method.
  4. Hold those weights until the next rebalance date; apply transaction
     costs on the turnover from the previous weights.

Design note: this engine should NOT know the internals of any specific
covariance or portfolio method -- it only calls the shared interfaces
defined in covariance/*.py and portfolio/optimizers.py. Adding a new method
later should require zero changes here, only a registration in config.yaml
and a new function following the shared signature.
"""

from typing import Callable, Dict

import pandas as pd


def run_walk_forward(
    returns: pd.DataFrame,
    covariance_estimators: Dict[str, Callable],
    portfolio_constructors: Dict[str, Callable],
    estimation_window_days: int,
    rebalance_frequency: str,
    transaction_cost_bps: float,
) -> Dict[str, pd.DataFrame]:
    """Run the full walk-forward loop for every (cov_method, port_method) combo.

    Returns {method_label: DataFrame} where each DataFrame has columns
    [date, portfolio_return_gross, portfolio_return_net, turnover, weights...]
    or similar -- exact schema TBD when we implement, but must include
    enough to compute all evaluation/performance.py metrics without
    re-running the backtest.

    TODO: implement. This is the centerpiece of the project -- build and
    unit-test on a tiny synthetic returns panel (e.g., 3 assets, 20 periods)
    before running on the full 48-stock, 10-year panel.
    """
    raise NotImplementedError
