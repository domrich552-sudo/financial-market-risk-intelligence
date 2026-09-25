# 💹 Financial Market Risk Intelligence

> An explainable financial-market intelligence platform that combines market behaviour, company fundamentals, macroeconomic indicators and financial-news sentiment to detect unusual market conditions.

## Problem

Financial analysts often need to distinguish ordinary market movement from genuinely unusual conditions. This project builds an evidence-driven monitoring system rather than a stock-price prediction tool.

It answers:

- What has changed?
- How unusual is the change?
- Which variables are associated with the event?
- Is the signal company-specific or broader?
- How reliable is the detection model?
- Can the result be explained?

## Architecture

```
Alpha Vantage API
      ↓
Data ingestion
      ↓
Quality checks
      ↓
Feature engineering
      ↓
Market + fundamentals + macro + news
      ↓
Statistical analysis
      ↓
Anomaly detection
      ↓
Time-aware validation
      ↓
Explainability
      ↓
Streamlit dashboard
```

## Data

The pipeline is designed around Alpha Vantage data families including:

- Daily market prices and volume
- Company overview and financial statements
- News and sentiment
- GDP
- CPI
- Federal funds rate
- FX data
- Technical indicators

See the official Alpha Vantage documentation before running the pipeline because endpoint availability and API limits depend on the account plan.

## Analytical features

### Market
- Daily and rolling returns
- Rolling volatility
- Volume change and z-scores
- Drawdown
- High-low range

### Fundamentals
- Revenue growth
- Earnings growth
- Profit margin
- Debt-to-equity
- Current ratio
- ROE
- Free-cash-flow trends

### News
- Article count
- Average sentiment
- Positive/negative article ratio
- Sentiment change
- News attention

### Macro
- GDP
- CPI
- Interest rates
- FX movement

## Machine learning

The first modelling layer uses **Isolation Forest** to identify multivariate observations that differ from the recent baseline.

A second layer can classify market regimes such as:

- NORMAL
- ELEVATED_RISK
- HIGH_VOLATILITY

Validation is chronological rather than random to reduce future-information leakage.

## Dashboard

The Streamlit dashboard is designed around six pages:

1. Market Overview
2. Company Intelligence
3. Market Events
4. News Intelligence
5. Financial Health
6. Model Explainability

## Repository structure

```
financial-market-risk-intelligence/
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── database/
│   └── schema.sql
├── src/
│   ├── ingestion/
│   ├── cleaning/
│   ├── features/
│   ├── modelling/
│   └── visualisation/
├── notebooks/
├── dashboard/
├── tests/
├── reports/
├── .github/workflows/
├── .env.example
├── requirements.txt
└── README.md
```

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
streamlit run dashboard/app.py
```

Do not commit your API key.

## Example research questions

1. Are unusual market movements associated with changes in news sentiment?
2. Does abnormal trading volume coincide with elevated volatility?
3. How much does macroeconomic context explain changes in market behaviour?
4. Does multivariate anomaly detection identify events that simple thresholds miss?
5. How stable are model findings under chronological validation?

## Interpretation

The project deliberately treats relationships between sentiment and returns as **associations**, not proof of causation. It is an analytical monitoring system, not financial advice or an investment recommendation.

## Portfolio value

This project demonstrates:

**API ingestion → data engineering → feature engineering → statistics → time-series analysis → anomaly detection → model validation → explainability → dashboard development.**

## Author

**Richard Dominic**  
GitHub: https://github.com/domrich552-sudo
