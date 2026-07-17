"""Fetch Fama-French factor returns (FF3 / FF5, daily) from Dartmouth."""

import pandas as pd


def fetch_ff_factors(url: str, cache_path: str = "data/raw/ff_factors.csv") -> pd.DataFrame:
    """Download and parse the Fama-French factors zip/csv.

    Returns a DataFrame indexed by date with columns:
    ['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA', 'RF'], values in percent
    (caller is responsible for dividing by 100 before use in regressions --
    keep raw units here, convert at the point of use, not here, to avoid
    silent double-conversion bugs).

    TODO: implement (urllib download, pd.read_csv skiprows=3, drop
    copyright footer row, parse index as datetime).
    """
    raise NotImplementedError
