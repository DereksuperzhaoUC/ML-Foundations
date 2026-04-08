"""Main entry point for the ML pipeline."""


def _load_pipeline_modules():
    try:
        from src.config import CONFIG
        from src.data_loader import load_data
        from src.evaluate import mse, summarize
        from src.features import make_features
        from src.logger import log_results
        from src.models import LinearModel
        from src.split import rolling_split
    except ModuleNotFoundError as exc:
        missing_module = exc.name or "a required dependency"
        raise SystemExit(
            "Missing Python dependency: "
            f"{missing_module}. Activate the project's micromamba environment "
            "with `micromamba activate vol` or run `micromamba run -n vol python main.py`."
        ) from exc

    return {
        "CONFIG": CONFIG,
        "LinearModel": LinearModel,
        "load_data": load_data,
        "log_results": log_results,
        "make_features": make_features,
        "mse": mse,
        "rolling_split": rolling_split,
        "summarize": summarize,
    }

def main():
    modules = _load_pipeline_modules()
    config = modules["CONFIG"]

    df = modules["load_data"](
        symbol=config["data"]["symbol"],
        start=config["data"]["start"],
    )
    X, y = modules["make_features"](df)

    window = config["split"]["window"]

    model = modules["LinearModel"]()
    results = []

    for X_train, y_train, X_test, y_test in modules["rolling_split"](X, y, window):
        model.fit(X_train, y_train)
        pred = model.predict(X_test)

        error = modules["mse"](y_test.values, pred)
        results.append({"mse": error})

    modules["log_results"](results)
    modules["summarize"](results)

if __name__ == "__main__":
    main()
