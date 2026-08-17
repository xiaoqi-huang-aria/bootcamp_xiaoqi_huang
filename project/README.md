# API-Driven Multi-Asset Portfolio Risk Monitor

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Portfolio managers and risk analysts need a consistent way to measure daily portfolio risk, identify concentrated exposures, and estimate potential losses under normal and stressed market conditions. Individual asset volatility is insufficient because total risk also depends on portfolio weights, diversification, changing correlations, and extreme events.

This project will use API data for a portfolio of liquid stocks or ETFs to calculate Value at Risk (VaR), Expected Shortfall (ES), volatility, drawdown, correlation, and asset-level risk contributions. An interactive dashboard and reproducible daily report will show current risk, stress losses, and model warnings.

## Stakeholder & User

- **Decision owner:** Portfolio Manager or Risk Manager.
- **Primary users:** Risk Analyst, Portfolio Analyst, and Trader.
- **Timing:** After each market close and whenever portfolio positions or weights change.
- **Workflow:** The user enters portfolio value, symbols, and weights. The system retrieves and validates market data, calculates risk metrics and stress losses, and displays limits, concentrations, exceptions, and warnings for review.

## Useful Answer & Decision

- **Answer type:** Descriptive and risk-estimation focused.
- **Core metrics:** 95% and 99% one-day VaR, Expected Shortfall, portfolio volatility, maximum drawdown, correlations, component risk contributions, stress losses, and VaR backtesting exceptions.
- **Decision supported:** Whether portfolio risk is within an acceptable range, whether risk is concentrated in one asset or common exposure, and whether additional investigation or risk reduction is needed.
- **Artifact:** An interactive Streamlit dashboard and downloadable daily risk report with risk metrics, stress tests, backtesting, and data/model-quality warnings.

## Assumptions & Constraints

- The MVP covers four to six liquid, USD-denominated stocks or ETFs.
- It uses daily adjusted closing prices and does not measure intraday risk.
- Portfolio weights remain constant within each risk calculation day.
- Historical VaR assumes past returns provide a useful reference for near-term risk.
- Parametric VaR assumes short-horizon portfolio returns are approximately normal.
- Historical Expected Shortfall estimates loss severity from observed tail returns.
- The system excludes transaction costs, bid-ask spreads, taxes, liquidity impact, and market impact.
- It does not support options, structured products, or other nonlinear positions.
- API responses will be cached because free access may have history and rate limits.
- API keys and restricted raw data will not be committed to GitHub.
- The tool supports educational or internal analysis, not regulatory capital reporting or automatic trading decisions.
- Risk estimates are not maximum possible losses.

## Known Unknowns / Risks

- **API availability:** Confirm accessible history and rate limits; cache responses and retain the most recent valid dataset.
- **Missing observations:** Align assets on common trading dates and report all removed or filled records.
- **Corporate actions:** Prefer adjusted prices and flag unusually large returns for review.
- **Window sensitivity:** Compare results across at least 250-day and 500-day estimation windows.
- **Normality assumption:** Compare parametric VaR with historical VaR and Expected Shortfall to reveal fat-tail underestimation.
- **Correlation instability:** Monitor rolling correlations and include a scenario in which cross-asset correlations rise sharply.
- **Model exceptions:** Backtest VaR against realized portfolio losses and warn when exceptions are too frequent.
- **Weight quality:** Validate symbols, weights, portfolio value, missing inputs, and whether weights sum to 100%.
- **Survivorship bias:** Document that a portfolio of currently traded ETFs may not represent the historical investment universe.
- **Risk interpretation:** Display ES, worst historical loss, assumptions, and plain-language VaR explanations to prevent VaR from being read as a maximum loss.

## Lifecycle Mapping

Goal → Stage → Deliverable

- Define the risk decision, stakeholder, horizon, scope, and limitations → Problem Framing & Scoping → Scoping README, stakeholder persona, and risk register.
- Establish a reproducible workspace → Tooling Setup → Repository dependencies and configuration.
- Retrieve market prices → Data Acquisition → Reusable market-data API client and cached raw responses.
- Preserve raw and analysis-ready data → Data Storage → Raw files, processed Parquet datasets, and DuckDB tables.
- Align prices and calculate returns → Data Preprocessing → Validated price and return tables.
- Detect missing data and unusual returns → Outlier Analysis → Data-quality report and review flags.
- Analyze volatility, correlation, and drawdown → Exploratory Data Analysis → Risk-analysis notebook and figures.
- Build portfolio returns and rolling statistics → Feature Engineering → Risk-ready portfolio dataset.
- Estimate VaR, ES, contribution, and stress loss → Modeling → Portfolio risk engine and scenario library.
- Test whether VaR understates realized losses → Evaluation → Backtesting exception report.
- Explain assumptions and tail-risk limitations → Risk Communication → Model-risk documentation and dashboard warnings.
- Deliver daily results to users → Reporting → Streamlit dashboard and downloadable daily report.
- Convert analysis into reusable modules → Productization → Tested Python modules and repeatable run command.
- Make the system usable outside notebooks → Deployment → Deployable Streamlit application.
- Detect stale data or model weakness → Monitoring → Freshness, exception, correlation, and estimation-window warnings.
- Automate the daily workflow → Orchestration → Scheduled data-to-report pipeline.

## Repo Plan

```text
project/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── notebooks/
└── docs/
    └── persona.md
```