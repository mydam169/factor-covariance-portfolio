"""Fetch macro series from FRED (rates, inflation, unemployment).

Note from project discussion: in the original notebook this data was pulled
but never used, which was flagged as a dead end. Decide explicitly, before
implementing downstream models, whether this feeds into:
  (a) a macro-conditioned regime indicator for the rolling window /
      shrinkage intensity (lightweight regime-awareness, see Phase 3 notes
      in config.yaml deferred_scope), or
  (b) nothing, in which case cut this module rather than leave it dangling.
"""

from typing import List

import pandas as pd


def fetch_macro_series(
    series_ids: List[str],
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """Fetch one or more FRED series via pandas_datareader.

    TODO: implement via web.DataReader(series_ids, 'fred', start, end).
    """
    raise NotImplementedError
