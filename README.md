# trader-behavior-vs-market-sentiment
Trader Behavior vs Market Sentiment Analysis
Overview

Financial markets are influenced not only by fundamentals and technical indicators, but also by collective human behavior. In markets characterized by high volatility—such as cryptocurrency trading—emotions like fear and greed play a critical role in shaping trader decisions.

This project examines how trader behavior varies across different market sentiment regimes by integrating historical trading data with the Crypto Fear & Greed Index. The analysis focuses on understanding how profitability, risk exposure, trading volume, and directional bias change under varying emotional conditions in the market.

Rather than treating sentiment as a direct price predictor, this study evaluates sentiment as a behavioral and risk-regime indicator, providing insights into when traders tend to act conservatively, aggressively, or opportunistically.

Objectives

The primary goals of this analysis are to:

Examine how trader profitability (PnL) varies across sentiment regimes

Study changes in risk-taking behavior using trade size and return volatility

Analyze trading volume during periods of fear and greed

Understand directional bias through buy/sell ratios

Evaluate whether market sentiment offers predictive value or primarily reflects behavioral conditions

Key Findings

Trader profitability is most consistent during Fear regimes, rather than during Greed.

Extreme Greed produces occasional large profits, but is accompanied by significantly higher volatility and downside risk.

Buying pressure is strongest during Extreme Fear, indicating contrarian accumulation behavior.

Market sentiment shows little direct correlation with next-day PnL, but strongly influences trading behavior and risk exposure.

Overall, sentiment functions better as a behavioral and risk-context indicator than as a short-term forecasting signal.

Repository Structure
trader-behavior-vs-market-sentiment/
│
├── data/
│   ├── historical_data.csv        # Trader transaction records
│   └── fear_greed_index.csv       # Market sentiment data
│
├── notebooks/
│   └── trader_sentiment_analysis.ipynb
│
├── reports/
│   └── analysis_report.md         # Optional written analysis
│
├── requirements.txt
└── README.md

Data Description
Trader Behavior Data

The trader dataset contains transaction-level records, which are aggregated at a daily level. Key variables used include:

Timestamp (IST)

Trade size (USD)

Trade direction (Buy/Sell)

Closed profit and loss (PnL)

Transaction fees

From these, daily metrics such as total PnL, average trade size, total volume, and buy/sell ratios are derived.

Market Sentiment Data

Market sentiment is captured using the Crypto Fear & Greed Index, which classifies market mood into five regimes:

Extreme Fear

Fear

Neutral

Greed

Extreme Greed

Sentiment data is aligned with trading data on a daily basis to ensure temporal consistency.

Methodology

The analysis follows a structured exploratory workflow:

Data cleaning and preprocessing

Daily aggregation of trader behavior metrics

Alignment of trading data with sentiment regimes

Exploratory data analysis using visualizations

Distributional analysis (mean, median, volatility)

Lagged sentiment analysis and rank-based correlation testing

Statistical methods are chosen to be robust to outliers and heavy-tailed financial data.

Setup and Installation
Requirements

Python 3.8 or higher

Jupyter Notebook or Google Colab

Installation

(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Dependencies
pandas
numpy
matplotlib
seaborn
scipy

How to Run

Place the datasets in the data/ directory

Open the notebook:

jupyter notebook notebooks/trader_sentiment_analysis.ipynb


Run the notebook sequentially to reproduce the analysis and visualizations

Limitations

Sentiment indices reflect aggregate market mood, not individual trader intent

Daily aggregation may mask intraday dynamics

Results are observational and do not imply causality

Findings are specific to the dataset and market conditions studied

Future Improvements

Potential extensions of this work include:

Risk-adjusted performance metrics (Sharpe, Sortino)

Quantile-based and regime-switching models

Strategy backtesting using sentiment filters

Intraday sentiment alignment

Clustering or segmentation of trader behavior

Author

Aiyan
Data Science | Behavioral Finance | Market Analysis

Final Note

This project highlights the importance of behavioral context in trading decisions. Market sentiment does not reliably predict short-term returns, but it strongly shapes how traders allocate risk, respond to uncertainty, and behave under emotional extremes.
