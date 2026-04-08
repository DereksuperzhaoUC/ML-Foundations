"""Utilities for loading raw and processed datasets."""
import pandas as pd
import yfinance as yf


def load_data(symbol="^GSPC", start="2010-01-01"):
    df = yf.download(symbol, start=start, progress=False, auto_adjust=True)

    if df.empty:
        raise RuntimeError(
            "No market data was downloaded from Yahoo Finance for "
            f"{symbol} starting {start}. This usually means the request was "
            "rate limited or the network is unavailable. Retry later or switch "
            "to a local cached dataset."
        )

    close_col = "Close"
    if close_col not in df.columns:
        raise RuntimeError(
            f"Downloaded data for {symbol} is missing the '{close_col}' column."
        )

    df["ret"] = df[close_col].pct_change()
    df = df.dropna()
    if df.empty:
        raise RuntimeError(
            f"Downloaded data for {symbol} did not contain enough rows to build returns."
        )

    return df
