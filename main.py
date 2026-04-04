"""Main entry point for the ML pipeline."""
from src.data_loader import load_data
from src.features import make_features
from src.models import train_model
from src.evaluate import evaluate

def main() -> None:
    """Run the project pipeline."""
    
    df = load_data()
    X, y = make_features(df)

    preds = train_model(X, y)
    evaluate(y, preds)


if __name__ == "__main__":
    main()