"""Evaluation metrics and validation helpers."""
import numpy as np

def evaluate(y, preds):
    mse = np.mean((y - preds)**2)
    print("MSE:", mse)