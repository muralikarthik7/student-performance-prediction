from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score


RANDOM_STATE = 42

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "student-mat.csv"
)

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "student_performance_random_forest.joblib"
)


def load_data():
    """Load the student performance dataset."""
    return pd.read_csv(
        DATA_PATH,
        sep=";"
    )


def prepare_data(df):
    """Create features and target for progressive prediction."""
    X = df.drop(columns=["G3"])
    y = df["G3"]

    return X, y


def build_pipeline(X):
    """Create the preprocessing and Random Forest pipeline."""
    numerical_features = (
        X.select_dtypes(
            include=np.number
        )
        .columns
        .tolist()
    )

    categorical_features = (
        X.select_dtypes(
            exclude=np.number
        )
        .columns
        .tolist()
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical_features
            ),
            (
                "numerical",
                "passthrough",
                numerical_features
            )
        ]
    )

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=8,
        max_features=1.0,
        min_samples_leaf=1,
        min_samples_split=2,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )

    return pipeline


def train_model():
    """Train, evaluate, and save the final model."""
    df = load_data()

    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=RANDOM_STATE
        )
    )

    pipeline = build_pipeline(X)

    pipeline.fit(
        X_train,
        y_train
    )

    predictions = pipeline.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(
        pipeline,
        MODEL_PATH
    )

    print("Training complete.")
    print(f"Test MAE: {mae:.3f}")
    print(f"Test R²: {r2:.3f}")
    print(f"Model saved to: {MODEL_PATH}")


def main():
    train_model()

main()