"""Transaction cost model applied at each rebalance in the walk-forward engine.

Kept separate from engine.py so the cost model can be swapped (flat bps vs.
e.g. a size-dependent impact model) without touching the loop logic.
"""

import pandas as pd


def compute_turnover(old_weights: pd.Series, new_weights: pd.Series) -> float:
    """Sum of absolute weight changes at a rebalance date.

    TODO: implement: (new_weights - old_weights).abs().sum(), handling
    assets that enter/exit the weight vector (treat missing as 0).
    """
    raise NotImplementedError


def apply_transaction_costs(gross_return: float, turnover: float, cost_bps: float) -> float:
    """Deduct turnover * cost_bps (in bps, e.g. 10 = 0.10%) from gross_return.

    TODO: implement.
    """
    raise NotImplementedError
