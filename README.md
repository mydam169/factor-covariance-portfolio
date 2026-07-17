# Factor Investing: Does Factor-Based Portfolio Construction Improve Robustness and Performance?

Research question: does covariance estimation via a factor model (Fama-French
5-factor) produce more robust / better out-of-sample GMV than 
(a) sample historical covariance, 
(b) Ledoit-Wolf shrinkage,
(c) naive 1/N, under walk-forward backtesting?

## Project phases

1. **Data pipeline** — Fama-French factors, price history
   for a 48-stock universe across 4 macro/style groups (cyclical growth,
   cyclical value, defensive growth, defensive value), 10-year window.
2. **Factor regressions** — per-stock and portfolio-level time-series
   regressions (FF3 / FF5), with diagnostic checks (HAC errors,
   Ljung-Box, Breusch-Pagan, VIF, QQ plot).
3. **Covariance estimators** — historical sample, Ledoit-Wolf shrinkage,
   factor-based using $\Sigma = B \Sigma_F B' + D$.
4. **Portfolio construction** — GMV portfolios via `cvxpy`, against 1/N
   benchmark, under long-only / position-cap constraints (TBD in config).
5. **Walk-forward backtest engine** — rolling estimation window, fixed
   rebalance frequency, transaction cost model.
6. **Evaluation** — Sharpe and Sortino ratios, turnover, Herfindahl concentration, max
   drawdown, and formal significance testing (Jobson-Korkie / Memmel,
   stationary bootstrap) across methods.


## Repo layout

```
config/                  Project-wide config (universe, dates, params)
data/raw/                Raw pulled data (gitignored)
data/processed/          Cleaned / merged datasets (gitignored)
notebooks/               Exploratory notebooks only — no logic lives here
src/factor_project/
  data/                  Fetching + validating factors, macro, prices
  models/                Time-series factor regressions, diagnostics
  covariance/            Historical, shrinkage, and factor-based Sigma estimators
  portfolio/             Optimizers (GMV, 1/N) + constraints
  backtest/              Walk-forward engine + transaction cost model
  evaluation/            Performance metrics + statistical significance tests
  utils/                 Shared I/O and config helpers
tests/                   Unit tests, one file per src module
results/backtest_runs/   Raw per-method return series / weights from run_walk_forward (gitignored)
results/tables/          Method comparison tables, significance test outputs (gitignored)
reports/figures/         Output charts from the backtest / evaluation (gitignored)
scripts/                 Thin CLI entry points that call into src/
```

## Design principles for this repo

- **No logic in notebooks.** Notebooks call functions from
  `src/factor_project`; they don't redefine them. Keeps the pipeline
  testable and re-runnable.
- **Config-driven, not hardcoded.** Universe, date ranges, rolling window
  length, rebalance frequency, and transaction cost assumptions all live in
  `config/config.yaml`, not scattered through scripts.
- **Every estimator/optimizer shares an interface.** All covariance
  estimators take `(returns_df, **kwargs) -> pd.DataFrame` (an N x N Sigma).
  All portfolio constructors take `(mu, Sigma, **kwargs) -> pd.Series`
  (weights). This is what makes the walk-forward engine able to loop over
  methods generically instead of needing bespoke branches per method.
- **Tests before scale-up.** Each estimator/optimizer gets a unit test on
  a small synthetic case (e.g., a known 3-asset covariance matrix) before
  it's trusted inside the 48-stock backtest loop.

## Quickstart (once implemented)

```bash
pip install -r requirements.txt
python scripts/run_data_pipeline.py   # fetch + validate raw data
python scripts/run_backtest.py        # run walk-forward backtest across methods
```
