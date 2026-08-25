import pandas as pd

from src.predict import predict_student


df = pd.read_csv(
    "data/raw/student-mat.csv",
    sep=";"
)

sample_student = (
    df.drop(columns=["G3"])
    .iloc[0]
    .to_dict()
)

actual_grade = df.iloc[0]["G3"]

predicted_grade = predict_student(
    sample_student
)

print(
    f"Actual grade: {actual_grade}"
)

print(
    f"Predicted grade: {predicted_grade:.2f}"
)