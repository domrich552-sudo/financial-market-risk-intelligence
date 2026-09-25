"""Market feature engineering."""

import pandas as pd

def build_market_features(df, price_col="close", volume_col="volume"):
    out = df.copy().sort_values("date")
    out["daily_return"] = out[price_col].pct_change()
    out["rolling_5d_return"] = out[price_col].pct_change(5)
    out["volatility_20d"] = out["daily_return"].rolling(20).std()
    out["volume_zscore"] = (
        (out[volume_col] - out[volume_col].rolling(20).mean())
        / out[volume_col].rolling(20).std()
    )
    rolling_max = out[price_col].rolling(60, min_periods=1).max()
    out["drawdown"] = out[price_col] / rolling_max - 1
    out["high_low_range"] = (out["high"] - out["low"]) / out[price_col]
    return out
