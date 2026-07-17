"""Fetch and validate daily adjusted close prices for the universe via yfinance.

Known gotchas to handle here (see project discussion log):
- yf.download() default period is '1mo' if start/end are both None -- always
  pass explicit start/end, never rely on defaults.
- Some tickers (GM, TMUS, MDLZ, LVMUY) may not have data going back the full
  requested window due to IPO / spinoff / merger history. Do not silently
  truncate the universe -- log and surface these to the user.
- LVMUY is a thin OTC ADR; check liquidity/null counts before trusting it.
"""

from typing import List

import pandas as pd


def fetch_price_history(
    tickers: List[str],
    start_date: str,
    end_date: str,
    price_field: str = "Close",
) -> pd.DataFrame:
    """Download daily prices for all tickers over [start_date, end_date).

    Returns a wide DataFrame: index=Date, columns=tickers.

    TODO: implement via yf.download(tickers, start=start_date, end=end_date).
    Must NOT rely on default start/end/period.
    """
    raise NotImplementedError


def validate_price_history(
    prices: pd.DataFrame,
    expected_start: str,
    expected_end: str,
) -> pd.DataFrame:
    """Return a per-ticker validation report.

    Columns should include: earliest_date, latest_date, n_obs, n_nulls,
    starts_late (bool: earliest_date > expected_start + some tolerance).

    This is the check we agreed to run BEFORE finalizing the universe --
    don't skip it even though it feels like boilerplate.

    TODO: implement.
    """
    raise NotImplementedError
