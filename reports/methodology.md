# Methodology

## Design

The project follows an end-to-end quantitative workflow:

1. Acquire data through Alpha Vantage.
2. Preserve raw observations.
3. Validate schemas, dates and numeric fields.
4. Engineer market, fundamental, sentiment and macro features.
5. Explore relationships statistically.
6. Detect unusual observations using Isolation Forest.
7. Validate predictive components chronologically.
8. Explain model outputs with feature importance/SHAP where appropriate.
9. Surface results through Streamlit.

## Validation

Financial time series have temporal ordering. Random train/test splitting can allow information from later periods to influence earlier-period evaluation. The project therefore uses chronological splits.

## Limitations

News sentiment may reflect rather than cause market movement. Fundamental data is reported periodically rather than daily. API coverage and historical depth depend on the Alpha Vantage plan. Anomaly scores identify statistical unusualness; they do not establish financial loss or investment risk by themselves.

## Responsible interpretation

The system is designed for analytical monitoring and research. It does not generate buy/sell recommendations or personalised financial advice.
