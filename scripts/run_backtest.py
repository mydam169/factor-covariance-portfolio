"""Entry point: run the walk-forward backtest across all covariance x
portfolio method combinations, then evaluate and report.

Thin script -- all logic lives in src/factor_project/{covariance,portfolio,
backtest,evaluation}/. This just wires config -> method registry -> engine
-> evaluation -> report.
"""

from factor_project.utils.io import load_config, load_processed, save_backtest_run, save_results_table
from factor_project.covariance import historical, shrinkage, factor_based
from factor_project.portfolio import optimizers
from factor_project.backtest.engine import run_walk_forward
from factor_project.evaluation.performance import summarize_method
from factor_project.evaluation.statistical_tests import jobson_korkie_memmel


# Registry mapping config method names -> actual functions.
# Adding a new method later should only require adding an entry here + config.yaml.
COVARIANCE_ESTIMATORS = {
    "historical": historical.estimate,
    "shrinkage": shrinkage.estimate,
    "factor_based": factor_based.estimate,
}

PORTFOLIO_CONSTRUCTORS = {
    "gmv": optimizers.gmv,
    "mean_variance": optimizers.mean_variance,
    "equal_weight": optimizers.equal_weight,
}


def main():
    config = load_config()

    prices = load_processed("prices")
    returns = prices.pct_change().dropna()  # TODO: confirm this belongs here vs. a dedicated returns module

    active_cov_methods = {
        k: v for k, v in COVARIANCE_ESTIMATORS.items()
        if k in config["covariance_methods"]
    }
    active_port_methods = {
        k: v for k, v in PORTFOLIO_CONSTRUCTORS.items()
        if k in config["portfolio_methods"]
    }

    results = run_walk_forward(
        returns=returns,
        covariance_estimators=active_cov_methods,
        portfolio_constructors=active_port_methods,
        estimation_window_days=config["backtest"]["estimation_window_days"],
        rebalance_frequency=config["backtest"]["rebalance_frequency"],
        transaction_cost_bps=config["backtest"]["transaction_cost_bps"],
    )

    # Persist raw per-method output immediately -- the walk-forward loop is
    # the expensive step; everything downstream (evaluation, significance
    # tests, plots) should be re-runnable from this saved data without
    # re-running run_walk_forward.
    save_backtest_run(results, run_name="baseline_run")

    # TODO: loop over `results`, call summarize_method per method, build
    # comparison table (-> save_results_table), run jobson_korkie_memmel
    # pairwise (-> save_results_table), save figures to reports/figures/.


if __name__ == "__main__":
    main()
