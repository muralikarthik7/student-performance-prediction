from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "student_performance_random_forest.joblib"
)


def load_model():
    """Load the trained student performance prediction pipeline."""
    return joblib.load(MODEL_PATH)


def predict_student(student_data):
    """
    Predict a student's final grade.

    Parameters
    ----------
    student_data : dict
        Dictionary containing the model's required input features.

    Returns
    -------
    float
        Predicted final grade.
    """
    model = load_model()

    student_df = pd.DataFrame([student_data])

    prediction = model.predict(student_df)[0]

    return float(prediction)