from src.predict import predict_student


ORIGINAL_GRADE_MAX = 20
DISPLAY_GRADE_MAX = 100
GRADE_CONVERSION_FACTOR = 5


def predict_final_grade(student_data):
    """
    Generate the student's predicted final grade.

    Returns both:
    - original dataset scale: 0–20
    - user-facing percentage scale: 0–100
    """

    prediction = predict_student(student_data)

    prediction_original = max(
        0,
        min(ORIGINAL_GRADE_MAX, prediction)
    )

    prediction_percent = (
        prediction_original * GRADE_CONVERSION_FACTOR
    )

    return {
        "original_grade": prediction_original,
        "percentage_grade": prediction_percent
    }