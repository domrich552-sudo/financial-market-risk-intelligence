import pandas as pd
from src.features.market_features import build_market_features

def test_market_features():
    df = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=25),
        "close": range(100, 125),
        "high": range(101, 126),
        "low": range(99, 124),
        "volume": [1000] * 25
    })
    out = build_market_features(df)
    assert "daily_return" in out.columns
    assert "volatility_20d" in out.columns
    assert len(out) == 25
