import streamlit as st
import pandas as pd

st.title("Trader Behavior vs Market Sentiment Dashboard")

# -----------------------------
# Load datasets
# -----------------------------
trades = pd.read_csv("historical_data.csv")
sentiment = pd.read_csv("fear_greed_index.csv")
# -----------------------------
# Convert timestamps to date
# -----------------------------
trades['date'] = pd.to_datetime(
    trades['Timestamp IST'],
    format="%d-%m-%Y %H:%M"
).dt.date

sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# -----------------------------
# Merge datasets
# -----------------------------
df = trades.merge(sentiment, on='date', how='inner')

st.write("Merged Dataset Overview")
st.write(df.head())

# -----------------------------
# Metrics
# -----------------------------
st.metric("Total Trades", len(df))

# -----------------------------
# Sentiment Filter
# -----------------------------
sentiment_option = st.selectbox(
    "Select Sentiment Category",
    df['classification'].unique()
)

filtered = df[df['classification'] == sentiment_option]

st.write("Filtered Data")
st.write(filtered.head())

st.write("Average Closed PnL:", filtered['Closed PnL'].mean())
