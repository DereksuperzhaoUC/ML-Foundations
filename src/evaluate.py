"""Evaluation metrics and validation helpers."""
import numpy as np

def mse(y, y_hat):
    return np.mean((y - y_hat)**2)

def summarize(results):
    import numpy as np
    mse_vals = [r["mse"] for r in results]
    print("Mean MSE:", np.mean(mse_vals))