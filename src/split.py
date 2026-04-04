def rolling_split(X, y, window):
    for t in range(window, len(X)):
        X_train = X.iloc[t-window:t]
        y_train = y.iloc[t-window:t]

        X_test = X.iloc[t:t+1]
        y_test = y.iloc[t:t+1]

        yield X_train, y_train, X_test, y_test