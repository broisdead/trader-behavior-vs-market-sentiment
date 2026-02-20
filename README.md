Trader Behavior vs Market Sentiment Analysis
Project Overview

This project analyzes how trader behavior and performance vary across different market sentiment regimes using the Fear & Greed Index. The objective is to determine whether sentiment impacts trader profitability, risk-taking behavior, and trading patterns.

Part A — Data Preparation
1. Dataset Loading and Inspection

Two datasets were used:

historical_data.csv → Individual trade-level data

fear_greed_index.csv → Daily sentiment index

Dataset Dimensions

Trades dataset: 211,224 rows, 16 columns

Sentiment dataset: 2,644 rows, 4 columns

Data Cleaning

Missing values checked → None found

Duplicate rows checked → Removed if present

Timestamps converted using:

%d-%m-%Y %H:%M

Daily-level alignment performed using date column

Inner merge used to align trade data with sentiment data

Merged dataset size: 211,218 rows

2. Feature Engineering

The following key metrics were created:

Daily PnL per Trader

Aggregated Closed PnL per account per day

Win Rate

Trade considered a win if Closed PnL > 0

Win rate computed per trader

Average Trade Size

Mean of Size USD

Computed overall, per trader, and per day

Leverage Proxy

Since leverage was not directly available, Size USD was used as a risk exposure proxy.

Higher position size implies greater capital exposure and effective leverage behavior.

Number of Trades per Day

Count of trades grouped by date

Long/Short Ratio

BUY vs SELL counts per day

Long/Short ratio computed accordingly

Part B — Analysis
1. Sentiment Categorization

Sentiment index was categorized into:

Fear (0–40)

Neutral (40–60)

Greed (60–100)

2. Performance Comparison Across Sentiment
Average PnL by Sentiment

Average Closed PnL computed for each sentiment category.

Win Rate by Sentiment

Win rate calculated as proportion of profitable trades within each regime.

Risk Proxy (Drawdown Approximation)

Standard deviation of Closed PnL used as volatility proxy.

This captures risk and variability in trader performance.

3. Behavioral Changes Across Sentiment

The following behavioral metrics were compared across regimes:

Trade Frequency

Number of trades executed in Fear, Neutral, and Greed periods.

Position Size (Risk Proxy)

Average Size USD compared across sentiment.

Long/Short Bias

Distribution of BUY vs SELL trades by sentiment category.

4. Trader Segmentation

Three behavioral segments were identified:

1. High vs Low Exposure Traders

Based on median split of Size USD

2. Frequent vs Infrequent Traders

Based on median trade count per account

3. Consistent vs Inconsistent Traders

Based on standard deviation of Closed PnL

Low volatility → Consistent

High volatility → Inconsistent

Cluster performance comparisons were computed for each segment.

Key Insights

Performance differs significantly across sentiment regimes. Fear periods show lower average PnL and higher volatility, indicating elevated downside risk.

Traders exhibit increased trade frequency and larger position sizes during Greed periods, suggesting higher risk-taking behavior under optimistic conditions.

Frequent and high-exposure traders generate higher average returns but experience greater volatility. Consistent traders demonstrate more stable returns with lower variance.

Part C — Actionable Strategy Recommendations

Based on the findings, the following strategy rules are proposed:

During Fear regimes, reduce exposure and avoid high leverage positions to mitigate elevated volatility and downside risk.

During Greed regimes, allow increased trade frequency but implement risk controls (position size caps) to prevent overconfidence-driven losses.

Prefer consistent traders during uncertain sentiment periods, as they exhibit lower return volatility.

Bonus Section
1. Predictive Model

A logistic regression model was built to predict next-day profitability bucket using:

Average position size

Win rate

Sentiment index

Target:

1 → Next-day positive PnL

0 → Next-day negative PnL

Model evaluation included accuracy and classification metrics.

2. Trader Clustering

K-Means clustering was applied using:

Average PnL

Trade frequency

Average position size

Win rate

Three behavioral archetypes were identified:

Conservative Traders

Aggressive High-Exposure Traders

High-Frequency Speculators

Cluster summary statistics were analyzed to interpret behavioral patterns.

3. Streamlit Dashboard

A lightweight Streamlit dashboard was implemented featuring:

Sentiment filter

Total trade count

Average Closed PnL display

Interactive data exploration

This provides an intuitive interface for analyzing trader behavior across sentiment regimes.

Conclusion

This project demonstrates that market sentiment significantly influences trader performance and behavior.

Key findings indicate:

Fear regimes increase volatility and downside risk

Greed regimes increase trade frequency and risk exposure

Behavioral segmentation reveals substantial differences in risk-adjusted performance

These insights can inform adaptive trading strategies aligned with market sentiment.

Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

Streamlit
