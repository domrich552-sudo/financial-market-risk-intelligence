"""Small Alpha Vantage client used by the project."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.alphavantage.co/query"

class AlphaVantageClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("ALPHAVANTAGE_API_KEY")
        if not self.api_key:
            raise ValueError("Set ALPHAVANTAGE_API_KEY in your environment.")

    def query(self, function, **params):
        payload = {"function": function, "apikey": self.api_key, **params}
        response = requests.get(BASE_URL, params=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        if "Error Message" in data:
            raise RuntimeError(data["Error Message"])
        if "Note" in data:
            raise RuntimeError(data["Note"])
        return data

    def daily_prices(self, symbol, outputsize="compact"):
        return self.query("TIME_SERIES_DAILY", symbol=symbol, outputsize=outputsize)

    def overview(self, symbol):
        return self.query("OVERVIEW", symbol=symbol)

    def news_sentiment(self, tickers):
        return self.query("NEWS_SENTIMENT", tickers=tickers)
