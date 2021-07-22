# finnhub-python

- API documentation: https://finnhub.io/docs/api
- API version: 1.0.0
- Package version: 2.3.0

## Installation

Install package

```sh
pip install finnhub-python
```

## Getting Started

Refer to [CHANGELOG](https://github.com/Finnhub-Stock-API/finnhub-python/blob/master/CHANGELOG.md) If you are coming from version 1

```python
import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key="YOUR API KEY")

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)

#Convert to Pandas Dataframe
import pandas as pd
print(pd.DataFrame(res))

# Aggregate Indicators
print(finnhub_client.aggregate_indicator('AAPL', 'D'))

# Basic financials
print(finnhub_client.company_basic_financials('AAPL', 'margin'))

# Earnings surprises
print(finnhub_client.company_earnings('TSLA', limit=5))

# EPS estimates
print(finnhub_client.company_eps_estimates('AMZN', freq='quarterly'))

# Company Executives
print(finnhub_client.company_executive('AAPL'))

# Company News
# Need to use _from instead of from to avoid conflict
print(finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))

# Company Peers
print(finnhub_client.company_peers('AAPL'))

# Company Profile
print(finnhub_client.company_profile(symbol='AAPL'))
print(finnhub_client.company_profile(isin='US0378331005'))
print(finnhub_client.company_profile(cusip='037833100'))

# Company Profile 2
print(finnhub_client.company_profile2(symbol='AAPL'))

# Revenue Estimates
print(finnhub_client.company_revenue_estimates('TSLA', freq='quarterly'))

# List country
print(finnhub_client.country())

# Crypto Exchange
print(finnhub_client.crypto_exchanges())

# Crypto symbols
print(finnhub_client.crypto_symbols('BINANCE'))

# Economic data
print(finnhub_client.economic_data('MA-USA-656880'))

# Filings
print(finnhub_client.filings(symbol='AAPL', _from="2020-01-01", to="2020-06-11"))

# Financials
print(finnhub_client.financials('AAPL', 'bs', 'annual'))

# Financials as reported
print(finnhub_client.financials_reported(symbol='AAPL', freq='annual'))

# Forex exchanges
print(finnhub_client.forex_exchanges())

# Forex all pairs
print(finnhub_client.forex_rates(base='USD'))

# Forex symbols
print(finnhub_client.forex_symbols('OANDA'))

# Fund Ownership
print(finnhub_client.fund_ownership('AMZN', limit=5))

# General news
print(finnhub_client.general_news('forex', min_id=0))

# Investors ownership
print(finnhub_client.ownership('AAPL', limit=5))

# IPO calendar
print(finnhub_client.ipo_calendar(_from="2020-05-01", to="2020-06-01"))

# Major developments
print(finnhub_client.press_releases('AAPL', _from="2020-01-01", to="2020-12-31"))

# News sentiment
print(finnhub_client.news_sentiment('AAPL'))

# Pattern recognition
print(finnhub_client.pattern_recognition('AAPL', 'D'))

# Price target
print(finnhub_client.price_target('AAPL'))

# Quote
print(finnhub_client.quote('AAPL'))

# Recommendation trends
print(finnhub_client.recommendation_trends('AAPL'))

# Stock dividends
print(finnhub_client.stock_dividends('KO', _from='2019-01-01', to='2020-01-01'))

# Stock symbols
print(finnhub_client.stock_symbols('US')[0:5])

# Transcripts
print(finnhub_client.transcripts('AAPL_162777'))

# Transcripts list
print(finnhub_client.transcripts_list('AAPL'))

# Earnings Calendar
print(finnhub_client.earnings_calendar(_from="2020-06-10", to="2020-06-30", symbol="", international=False))

# Covid-19
print(finnhub_client.covid19())

# Upgrade downgrade
print(finnhub_client.upgrade_downgrade(symbol='AAPL', _from='2020-01-01', to='2020-06-30'))

# Economic code
print(finnhub_client.economic_code()[0:5])

# Support resistance
print(finnhub_client.support_resistance('AAPL', 'D'))

# Technical Indicator
print(finnhub_client.technical_indicator(symbol="AAPL", resolution='D', _from=1583098857, to=1584308457, indicator='rsi', indicator_fields={"timeperiod": 3}))

# Stock splits
print(finnhub_client.stock_splits('AAPL', _from='2000-01-01', to='2020-01-01'))

# Forex candles
print(finnhub_client.forex_candles('OANDA:EUR_USD', 'D', 1590988249, 1591852249))

# Crypto Candles
print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))

# Tick Data
print(finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0))


# Indices Constituents
print(finnhub_client.indices_const(symbol = "^GSPC"))

# Indices Historical Constituents
print(finnhub_client.indices_hist_const(symbol = "^GSPC"))

# ETFs Profile
print(finnhub_client.etfs_profile('SPY'))

# ETFs Holdings
print(finnhub_client.etfs_holdings('SPY'))

# ETFs Sector Exposure
print(finnhub_client.etfs_sector_exp('SPY'))

# ETFs Country Exposure
print(finnhub_client.etfs_country_exp('SPY'))

# International Filings
print(finnhub_client.international_filings('RY.TO'))
print(finnhub_client.international_filings(country='GB'))

# SEC Sentiment Analysis
print(finnhub_client.sec_sentiment_analysis('0000320193-20-000052'))

# SEC similarity index
print(finnhub_client.sec_similarity_index('AAPL'))

# Bid Ask
print(finnhub_client.last_bid_ask('AAPL'))

# FDA Calendar
print(finnhub_client.fda_calendar())

# Symbol lookup
print(finnhub_client.symbol_lookup('apple'))

# Insider transactions
print(finnhub_client.stock_insider_transactions('AAPL', '2021-01-01', '2021-03-01'))

# Mutual Funds Profile
print(finnhub_client.mutual_fund_profile("VTSAX"))

# Mutual Funds Holdings
print(finnhub_client.mutual_fund_holdings("VTSAX"))

# Mutual Funds Sector Exposure
print(finnhub_client.mutual_fund_sector_exp("VTSAX"))

# Mutual Funds Country Exposure
print(finnhub_client.mutual_fund_country_exp("VTSAX"))

# Revenue breakdown
print(finnhub_client.stock_revenue_breakdown('AAPL'))

# Social sentiment
print(finnhub_client.stock_social_sentiment('GME'))

# Investment Themes
print(finnhub_client.stock_investment_theme('financialExchangesData'))

# Supply chain
print(finnhub_client.stock_supply_chain('AAPL'))

```

## License

Apache License
