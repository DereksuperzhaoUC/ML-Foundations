"""Feature engineering helpers for the ML pipeline."""
def make_features(df):
    for lag in range(1, 6):
        df[f"lag_{lag}"] = df["ret"].shift(lag)
    df = df.dropna()

    X = df[[f"lag_{i}" for i in range(1, 6)]]
    y = df["ret"]
    return X, y