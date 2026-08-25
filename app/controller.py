from app.model import predict_final_grade


SCHOOL_MAPPING = {
    "Gabriel Pereira (GP)": "GP",
    "Mousinho da Silveira (MS)": "MS"
}


SEX_MAPPING = {
    "Female": "F",
    "Male": "M"
}


ADDRESS_MAPPING = {
    "Urban": "U",
    "Rural": "R"
}


FAMILY_SIZE_MAPPING = {
    "3 or fewer people": "LE3",
    "More than 3 people": "GT3"
}


PARENT_STATUS_MAPPING = {
    "Living together": "T",
    "Living apart": "A"
}


EDUCATION_MAPPING = {
    "No formal education": 0,
    "Primary education": 1,
    "Middle school": 2,
    "Secondary school": 3,
    "Higher education": 4
}


JOB_MAPPING = {
    "Teacher": "teacher",
    "Healthcare": "health",
    "Services": "services",
    "At home": "at_home",
    "Other": "other"
}


SCHOOL_REASON_MAPPING = {
    "Close to home": "home",
    "School reputation": "reputation",
    "Course preference": "course",
    "Other reason": "other"
}


TRAVEL_TIME_MAPPING = {
    "Less than 15 minutes": 1,
    "15–30 minutes": 2,
    "30–60 minutes": 3,
    "More than 60 minutes": 4
}


STUDY_TIME_MAPPING = {
    "Less than 2 hours/week": 1,
    "2–5 hours/week": 2,
    "5–10 hours/week": 3,
    "More than 10 hours/week": 4
}


RELATIONSHIP_MAPPING = {
    "Not currently in a relationship": "no",
    "Currently in a relationship": "yes"
}


def convert_percentage_to_original_grade(percentage):
    """Convert 0–100 UI grade into the dataset's 0–20 scale."""

    return percentage / 5


def prepare_student_data(form_data):
    """
    Convert user-facing form selections into the feature values
    expected by the trained machine-learning pipeline.
    """

    return {
        "school": SCHOOL_MAPPING[
            form_data["school"]
        ],

        "sex": SEX_MAPPING[
            form_data["sex"]
        ],

        "age": form_data["age"],

        "address": ADDRESS_MAPPING[
            form_data["address"]
        ],

        "famsize": FAMILY_SIZE_MAPPING[
            form_data["family_size"]
        ],

        "Pstatus": PARENT_STATUS_MAPPING[
            form_data["parent_status"]
        ],

        "Medu": EDUCATION_MAPPING[
            form_data["mother_education"]
        ],

        "Fedu": EDUCATION_MAPPING[
            form_data["father_education"]
        ],

        "Mjob": JOB_MAPPING[
            form_data["mother_job"]
        ],

        "Fjob": JOB_MAPPING[
            form_data["father_job"]
        ],

        "reason": SCHOOL_REASON_MAPPING[
            form_data["reason"]
        ],

        "guardian": (
            form_data["guardian"].lower()
        ),

        "traveltime": TRAVEL_TIME_MAPPING[
            form_data["travel_time"]
        ],

        "studytime": STUDY_TIME_MAPPING[
            form_data["study_time"]
        ],

        "failures": form_data["failures"],

        "schoolsup": form_data["school_support"],

        "famsup": form_data["family_support"],

        "paid": form_data["paid_classes"],

        "activities": form_data["activities"],

        "nursery": form_data["nursery"],

        "higher": form_data["higher_education"],

        "internet": form_data["internet"],

        "romantic": RELATIONSHIP_MAPPING[
            form_data["relationship_status"]
        ],

        "famrel": form_data["family_relationship"],

        "freetime": form_data["free_time"],

        "goout": form_data["going_out"],

        "Dalc": form_data["weekday_alcohol"],

        "Walc": form_data["weekend_alcohol"],

        "health": form_data["health"],

        "absences": form_data["absences"],

        "G1": convert_percentage_to_original_grade(
            form_data["G1"]
        ),

        "G2": convert_percentage_to_original_grade(
            form_data["G2"]
        )
    }


def generate_prediction(form_data):
    """Prepare form data and generate the final model prediction."""

    student_data = prepare_student_data(
        form_data
    )

    return predict_final_grade(
        student_data
    )