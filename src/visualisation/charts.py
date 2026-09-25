"""Reusable Plotly charts."""

import plotly.express as px

def price_chart(df, x="date", y="close", title="Price"):
    return px.line(df, x=x, y=y, title=title)

def sentiment_chart(df, x="date", y="sentiment", title="News Sentiment"):
    return px.line(df, x=x, y=y, title=title)
