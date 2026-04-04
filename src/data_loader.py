"""Utilities for loading raw and processed datasets."""
import pandas as pd
import yfinance as yf

def load_data():
    df = yf.download("^GSPC", start="2010-01-01")
    df["ret"] = df["Close"].pct_change()
    return df.dropna()