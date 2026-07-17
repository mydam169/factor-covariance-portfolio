"""Stock universe loading and lookup utilities.

The universe is defined in config/config.yaml, organized as:
    group -> sub_sector -> [tickers]

This module flattens that structure for use elsewhere (e.g., a single
yf.download call) and provides a reverse lookup for tagging returns /
weights by group and sub-sector during evaluation.
"""

from pathlib import Path
from typing import Dict, List, Tuple

import yaml


def load_universe(config_path: str = "config/config.yaml") -> Dict[str, Dict[str, List[str]]]:
    """Load the nested group -> sub_sector -> tickers structure from config.

    TODO: implement. Just a yaml.safe_load + return config['universe'].
    """
    raise NotImplementedError


def flatten_universe(universe: Dict[str, Dict[str, List[str]]]) -> List[str]:
    """Return a flat, deduplicated list of all tickers across all groups.

    TODO: implement.
    """
    raise NotImplementedError


def build_ticker_map(
    universe: Dict[str, Dict[str, List[str]]]
) -> Dict[str, Tuple[str, str]]:
    """Return {ticker: (group, sub_sector)} for tagging results downstream.

    TODO: implement.
    """
    raise NotImplementedError
