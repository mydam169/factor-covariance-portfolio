"""Entry point: fetch + validate all raw data (prices, factors, macro).

Thin script -- all logic lives in src/factor_project/data/. This just wires
config -> fetch functions -> validation report -> save to data/processed.
"""

from factor_project.utils.io import load_config, save_processed
from factor_project.data.universe import load_universe, flatten_universe
from factor_project.data.fetch_prices import fetch_price_history, validate_price_history
from factor_project.data.fetch_factors import fetch_ff_factors
from factor_project.data.fetch_macro import fetch_macro_series


def main():
    config = load_config()

    universe = load_universe()
    tickers = flatten_universe(universe)

    prices = fetch_price_history(
        tickers,
        start_date=config["data"]["start_date"],
        end_date=config["data"]["end_date"],
        price_field=config["data"]["price_field"],
    )
    validation_report = validate_price_history(
        prices,
        expected_start=config["data"]["start_date"],
        expected_end=config["data"]["end_date"],
    )
    print(validation_report)  # TODO: replace with proper logging + save to reports/

    ff_factors = fetch_ff_factors(config["data"]["fama_french_url"])
    macro = fetch_macro_series(
        config["data"]["fred_series"],
        start_date=config["data"]["start_date"],
        end_date=config["data"]["end_date"],
    )

    save_processed(prices, "prices")
    save_processed(ff_factors, "ff_factors")
    save_processed(macro, "macro")


if __name__ == "__main__":
    main()
