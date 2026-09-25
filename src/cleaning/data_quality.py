"""Data-quality checks for market datasets."""

import pandas as pd

def validate_prices(df):
    required = {"date", "close", "volume"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    result = df.copy()
    result["date"] = pd.to_datetime(result["date"], errors="coerce")
    result["close"] = pd.to_numeric(result["close"], errors="coerce")
    result["volume"] = pd.to_numeric(result["volume"], errors="coerce")

    return result.dropna(subset=["date", "close"]).sort_values("date")
