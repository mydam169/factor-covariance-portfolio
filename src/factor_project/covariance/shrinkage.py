"""Ledoit-Wolf shrinkage covariance estimator.

Same interface as historical.estimate: (returns_df) -> Sigma (N x N).

Worth remembering for the writeup (per project discussion): this and
factor_based.estimate are conceptually the same idea -- shrinking the noisy
sample covariance toward a structured target. Ledoit-Wolf shrinks toward a
generic target (e.g., constant correlation or single-index); the factor
estimator shrinks toward a specific, economically motivated FF5 structure.
The interesting comparison is "generic shrinkage vs. structured shrinkage",
not "shrinkage vs. something unrelated".
"""

import pandas as pd


def estimate(returns: pd.DataFrame) -> pd.DataFrame:
    """Ledoit-Wolf shrinkage estimate of the covariance matrix.

    TODO: implement via sklearn.covariance.LedoitWolf().fit(returns).covariance_,
    wrapped back into a labeled DataFrame (index/columns = returns.columns).
    """
    raise NotImplementedError
