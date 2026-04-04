import pandas as pd
import os

def log_results(results):
    os.makedirs("results", exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv("results/metrics.csv", index=False)