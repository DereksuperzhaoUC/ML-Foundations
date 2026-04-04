CONFIG = {
    "data": {
        "symbol": "^GSPC",
        "start": "2010-01-01"
    },
    "model": {
        "type": "linear",
        "lags": 5
    },
    "split": {
        "window": 252
    },
    "eval": {
        "metrics": ["mse"]
    }
}