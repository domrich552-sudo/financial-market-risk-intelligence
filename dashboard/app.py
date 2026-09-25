import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Financial Market Risk Intelligence",
    page_icon="💹",
    layout="wide"
)

st.title("💹 Financial Market Risk Intelligence")
st.caption(
    "An explainable monitoring framework combining market behaviour, "
    "fundamentals, macroeconomic context and news sentiment."
)

st.sidebar.header("Controls")
ticker = st.sidebar.selectbox("Company", ["AAPL", "MSFT", "NVDA", "JPM", "XOM"])

c1, c2, c3, c4 = st.columns(4)
c1.metric("Market status", "Monitoring")
c2.metric("Anomalies", "—")
c3.metric("News sentiment", "—")
c4.metric("Volatility", "—")

tab1, tab2, tab3 = st.tabs(["Overview", "Company Intelligence", "Methodology"])

with tab1:
    st.subheader("Market overview")
    st.info(
        "Connect the dashboard to the processed Alpha Vantage tables to "
        "populate live analytical metrics."
    )

with tab2:
    st.subheader(f"{ticker} intelligence")
    st.write("Price, volatility, volume, sentiment and financial-health analytics will appear here.")

with tab3:
    st.subheader("How the system works")
    st.markdown(
        "The system uses chronological validation and multivariate anomaly "
        "detection rather than attempting to predict individual stock prices."
    )
