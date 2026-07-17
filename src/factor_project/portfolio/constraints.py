"""Shared constraint definitions for cvxpy-based optimizers.

Kept separate from optimizers.py so long-only / max-weight / (future)
sector-neutrality constraints can be composed and reused identically across
gmv() and mean_variance() without duplicating cvxpy constraint code.
"""

import cvxpy as cp


def budget_constraint(w: cp.Variable) -> list:
    """sum(w) == 1. TODO: implement."""
    raise NotImplementedError


def long_only_constraint(w: cp.Variable) -> list:
    """w >= 0. TODO: implement."""
    raise NotImplementedError


def max_weight_constraint(w: cp.Variable, max_weight: float) -> list:
    """w <= max_weight (elementwise). TODO: implement."""
    raise NotImplementedError
