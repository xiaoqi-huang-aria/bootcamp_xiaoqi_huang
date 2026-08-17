# Stakeholder Brief — API-Driven Multi-Asset Portfolio Risk Monitor

**Audience:** Portfolio Manager / Risk Manager  
**Cadence:** Daily after market close and after material portfolio changes  
**Decision Supported:** Risk-limit review, concentration alert, and escalation for further analysis

## Context

Portfolio risk depends on position size, diversification, changing correlations, and extreme market events—not only the volatility of individual assets. Portfolio and Risk Managers need a consistent daily view of potential loss, tail risk, concentrated exposures, and model performance before deciding whether current risk is acceptable or requires further investigation.

## What You'll Receive

- A daily dashboard and downloadable risk report after market close.
- 95% and 99% one-day Historical and Parametric Value at Risk (VaR).
- Historical Expected Shortfall showing average loss beyond the VaR threshold.
- Portfolio volatility, maximum drawdown, and rolling correlation measures.
- Asset-level risk contributions identifying concentrated exposures.
- Portfolio losses under historical and hypothetical stress scenarios.
- VaR backtesting exceptions showing when realized losses exceeded estimated VaR.
- Data-freshness, missing-data, input-validation, and model-performance warnings.
- A plain-language summary of the main risk drivers, assumptions, and limitations.

## Decision Workflow

1. Review total VaR, Expected Shortfall, and any internal risk-limit warning.
2. Identify the assets contributing the most portfolio risk.
3. Examine changes in volatility, correlation, and drawdown.
4. Review historical and hypothetical stress losses.
5. Check data-quality warnings and VaR backtesting exceptions.
6. Decide whether to accept the current exposure, request deeper analysis, escalate a potential limit breach, or consider reducing risk.

## Assumptions & Constraints

- The MVP covers four to six liquid, USD-denominated stocks or ETFs.
- Risk is calculated from adjusted daily closing prices, not intraday data.
- Portfolio symbols, market value, and weights supplied by the user are accurate.
- Portfolio weights remain constant within each daily risk calculation.
- Historical VaR assumes past returns provide a useful risk reference but does not predict future losses.
- Parametric VaR assumes approximately normal short-horizon returns and may understate fat-tail risk.
- Expected Shortfall is estimated from the historical observations beyond the VaR threshold.
- Results exclude transaction costs, bid-ask spreads, taxes, liquidity effects, and market impact.
- Options, structured products, foreign-exchange conversion, and other nonlinear risks are outside the MVP scope.
- Free API services may impose request limits or restrict historical data availability; responses will therefore be cached.
- The report supports educational or internal risk analysis, not regulatory capital calculation or automatic trade recommendations.
- VaR is not the maximum possible loss. Users should interpret it together with Expected Shortfall, stress losses, and backtesting results.

## Escalation Triggers

- VaR or Expected Shortfall exceeds an internal risk limit.
- One asset contributes a disproportionate share of total portfolio risk.
- Rolling correlations rise materially and reduce diversification.
- Stress-test loss exceeds the desk's tolerance.
- VaR exceptions occur more frequently than expected for the selected confidence level.
- Market data are stale, incomplete, or affected by an unresolved price anomaly.

## Owner and Users

- **Decision owner:** Portfolio Manager or Risk Manager.
- **Primary users:** Risk Analyst, Portfolio Analyst, and Trader.
- **Risk Analyst responsibility:** Validate inputs, review exceptions, and explain model limitations.
- **Portfolio Analyst responsibility:** Maintain portfolio inputs and analyze concentration and diversification.
- **Trader responsibility:** Use the report to understand risk implications of proposed position changes; the tool does not recommend or execute trades.
