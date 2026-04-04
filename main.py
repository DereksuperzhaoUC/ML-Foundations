"""Main entry point for the ML pipeline."""
from src.data_loader import load_data
from src.features import make_features
from src.models import LinearModel
from src.split import rolling_split
from src.evaluate import mse, summarize
from src.logger import log_results
from src.config import CONFIG

def main():
    df = load_data()
    X, y = make_features(df)

    window = CONFIG["split"]["window"]

    model = LinearModel()
    results = []

    for X_train, y_train, X_test, y_test in rolling_split(X, y, window):
        model.fit(X_train, y_train)
        pred = model.predict(X_test)

        error = mse(y_test.values, pred)
        results.append({"mse": error})

    log_results(results)
    summarize(results)

if __name__ == "__main__":
    main()