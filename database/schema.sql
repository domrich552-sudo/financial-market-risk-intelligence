CREATE TABLE IF NOT EXISTS companies (
    ticker VARCHAR PRIMARY KEY,
    name VARCHAR,
    sector VARCHAR,
    industry VARCHAR
);

CREATE TABLE IF NOT EXISTS prices (
    ticker VARCHAR,
    date DATE,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT
);

CREATE TABLE IF NOT EXISTS fundamentals (
    ticker VARCHAR,
    report_date DATE,
    revenue DOUBLE,
    net_income DOUBLE,
    total_assets DOUBLE,
    total_liabilities DOUBLE,
    operating_cashflow DOUBLE
);

CREATE TABLE IF NOT EXISTS news (
    article_id VARCHAR,
    ticker VARCHAR,
    published_at TIMESTAMP,
    title VARCHAR,
    sentiment DOUBLE,
    relevance DOUBLE
);

CREATE TABLE IF NOT EXISTS macro (
    date DATE,
    gdp DOUBLE,
    cpi DOUBLE,
    interest_rate DOUBLE,
    fx_rate DOUBLE
);

CREATE TABLE IF NOT EXISTS features (
    ticker VARCHAR,
    date DATE,
    daily_return DOUBLE,
    volatility_20d DOUBLE,
    volume_zscore DOUBLE,
    drawdown DOUBLE,
    sentiment DOUBLE,
    news_count INTEGER
);
