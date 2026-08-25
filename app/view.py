import streamlit as st

from app.controller import (
    EDUCATION_MAPPING,
    JOB_MAPPING,
    SCHOOL_MAPPING,
    SCHOOL_REASON_MAPPING,
    TRAVEL_TIME_MAPPING,
    STUDY_TIME_MAPPING,
    RELATIONSHIP_MAPPING,
    generate_prediction
)


def render_header():
    st.title("🎓 Student Performance Prediction")

    st.write(
        """
        This application uses a trained **Random Forest machine-learning model**
        to estimate a student's final academic performance using academic
        history, study behavior, educational background, family information,
        and selected lifestyle factors.

        Enter the student's information below to receive an estimated
        **final grade on a 0–100 scale**.
        """
    )

    st.info(
        """
        **How does the prediction work?**

        The original Student Performance dataset records grades from
        **0 to 20**.

        This application uses the more familiar **0–100 scale** for easier
        interpretation. Grades entered here are automatically converted to
        the original 0–20 scale before being passed to the model, and the
        resulting prediction is converted back to 0–100 for display.
        """
    )

    st.caption(
        "The prediction is an estimate generated from patterns learned "
        "from historical data and is not a guaranteed academic outcome."
    )


def render_academic_section():
    st.subheader("📚 Academic Information")

    st.write(
        """
        **G1 — First-period grade** represents performance during the
        first assessment period.

        **G2 — Second-period grade** represents performance during the
        second assessment period, closer to the student's final assessment.

        Both grades are entered on a **0–100 scale**.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        G1 = st.slider(
            "First-period grade (G1)",
            0,
            100,
            50,
            help=(
                "Student's grade during the first assessment period."
            )
        )

        st.caption(
            "**0 = lowest performance · 100 = highest performance**"
        )

    with col2:
        G2 = st.slider(
            "Second-period grade (G2)",
            0,
            100,
            50,
            help=(
                "Student's grade during the second assessment period."
            )
        )

        st.caption(
            "**0 = lowest performance · 100 = highest performance**"
        )

    with col3:
        absences = st.number_input(
            "Number of absences",
            min_value=0,
            max_value=100,
            value=4,
            step=1,
            help="Total recorded school absences."
        )

        st.caption(
            "Total recorded absences during the course."
        )

    return {
        "G1": G1,
        "G2": G2,
        "absences": absences
    }


def render_student_section():
    st.subheader("👤 Student Information")

    st.write(
        "Provide general demographic, family, and educational information."
    )

    col1, col2, col3 = st.columns(3)

    form_data = {}

    with col1:
        form_data["school"] = st.selectbox(
            "School",
            list(SCHOOL_MAPPING.keys()),
            help=(
                "GP = Gabriel Pereira. "
                "MS = Mousinho da Silveira."
            )
        )

        form_data["sex"] = st.selectbox(
            "Sex",
            [
                "Female",
                "Male"
            ]
        )

        form_data["age"] = st.slider(
            "Age",
            15,
            22,
            17
        )

        form_data["address"] = st.selectbox(
            "Home location",
            [
                "Urban",
                "Rural"
            ]
        )

        form_data["family_size"] = st.selectbox(
            "Family size",
            [
                "3 or fewer people",
                "More than 3 people"
            ]
        )

        form_data["parent_status"] = st.selectbox(
            "Parents' living arrangement",
            [
                "Living together",
                "Living apart"
            ]
        )

    with col2:
        form_data["mother_education"] = st.selectbox(
            "Mother's education",
            list(EDUCATION_MAPPING.keys()),
            index=2
        )

        st.caption(
            "From no formal education through higher education."
        )

        form_data["father_education"] = st.selectbox(
            "Father's education",
            list(EDUCATION_MAPPING.keys()),
            index=2
        )

        form_data["mother_job"] = st.selectbox(
            "Mother's occupation",
            list(JOB_MAPPING.keys())
        )

        form_data["father_job"] = st.selectbox(
            "Father's occupation",
            list(JOB_MAPPING.keys())
        )

        form_data["reason"] = st.selectbox(
            "Primary reason for choosing the school",
            list(SCHOOL_REASON_MAPPING.keys())
        )

        form_data["guardian"] = st.selectbox(
            "Primary guardian",
            [
                "Mother",
                "Father",
                "Other"
            ]
        )

    with col3:
        form_data["travel_time"] = st.selectbox(
            "Travel time to school",
            list(TRAVEL_TIME_MAPPING.keys())
        )

        form_data["study_time"] = st.selectbox(
            "Weekly study time",
            list(STUDY_TIME_MAPPING.keys()),
            index=1
        )

        form_data["failures"] = st.slider(
            "Previous class failures",
            0,
            3,
            0
        )

        st.caption(
            "**0 = none · 1 = one · 2 = two · 3 = three or more**"
        )

        form_data["family_relationship"] = st.slider(
            "Family relationship quality",
            1,
            5,
            4
        )

        st.caption(
            "**1 = very poor · 2 = poor · 3 = average · "
            "4 = good · 5 = excellent**"
        )

        form_data["free_time"] = st.slider(
            "Free time after school",
            1,
            5,
            3
        )

        st.caption(
            "**1 = very little · 2 = little · 3 = moderate · "
            "4 = high · 5 = very high**"
        )

        form_data["going_out"] = st.slider(
            "Frequency of going out with friends",
            1,
            5,
            3
        )

        st.caption(
            "**1 = very rarely · 2 = rarely · 3 = sometimes · "
            "4 = often · 5 = very often**"
        )

    return form_data


def render_lifestyle_section():
    st.subheader("🌱 Support and Lifestyle")

    st.write(
        """
        These variables describe educational support, extracurricular
        activities, future educational intentions, and selected lifestyle
        characteristics.
        """
    )

    col1, col2, col3 = st.columns(3)

    form_data = {}

    with col1:
        form_data["school_support"] = st.selectbox(
            "Receives extra educational support",
            ["no", "yes"]
        )

        form_data["family_support"] = st.selectbox(
            "Receives family educational support",
            ["no", "yes"]
        )

        form_data["paid_classes"] = st.selectbox(
            "Takes paid extra classes",
            ["no", "yes"]
        )

        form_data["activities"] = st.selectbox(
            "Participates in extracurricular activities",
            ["no", "yes"]
        )

    with col2:
        form_data["nursery"] = st.selectbox(
            "Attended nursery school",
            ["yes", "no"]
        )

        form_data["higher_education"] = st.selectbox(
            "Plans to pursue higher education",
            ["yes", "no"]
        )

        form_data["internet"] = st.selectbox(
            "Has internet access at home",
            ["yes", "no"]
        )

        form_data["relationship_status"] = st.selectbox(
            "Relationship status",
            list(RELATIONSHIP_MAPPING.keys()),
            help=(
                "Indicates whether the student reported being "
                "in a romantic relationship."
            )
        )

    with col3:
        form_data["weekday_alcohol"] = st.slider(
            "Weekday alcohol consumption",
            1,
            5,
            1
        )

        st.caption(
            "**1 = very low · 2 = low · 3 = moderate · "
            "4 = high · 5 = very high**"
        )

        form_data["weekend_alcohol"] = st.slider(
            "Weekend alcohol consumption",
            1,
            5,
            1
        )

        st.caption(
            "**1 = very low · 2 = low · 3 = moderate · "
            "4 = high · 5 = very high**"
        )

        form_data["health"] = st.slider(
            "Current health status",
            1,
            5,
            3
        )

        st.caption(
            "**1 = very poor · 2 = poor · 3 = average · "
            "4 = good · 5 = excellent**"
        )

    return form_data


def render_prediction_result(result):
    st.subheader("Prediction Result")

    prediction_percent = result[
        "percentage_grade"
    ]

    prediction_original = result[
        "original_grade"
    ]

    col1, col2, col3 = st.columns(
        [1, 1, 2]
    )

    with col1:
        st.metric(
            "Estimated Final Grade",
            f"{prediction_percent:.1f} / 100"
        )

    with col2:
        st.metric(
            "Original Dataset Scale",
            f"{prediction_original:.2f} / 20"
        )

    with col3:
        st.progress(
            int(prediction_percent)
        )

        st.caption(
            f"Estimated academic performance: "
            f"{prediction_percent:.1f}%"
        )

    if prediction_percent >= 50:
        st.success(
            "The model predicts a final grade of "
            "50% or higher."
        )
    else:
        st.warning(
            "The model predicts a final grade below "
            "the 50% reference threshold."
        )


def render_prediction_section(form_data):
    st.divider()

    st.subheader("🔮 Generate Prediction")

    st.write(
        "Select the button below after entering the student's "
        "information to generate the estimated final grade."
    )

    if st.button(
        "Predict Final Grade",
        type="primary",
        use_container_width=True
    ):
        result = generate_prediction(
            form_data
        )

        render_prediction_result(
            result
        )


def render_footer():
    st.divider()

    st.caption(
        "Educational demonstration only. This system estimates academic "
        "performance from patterns learned from the training dataset. "
        "Predictions should not be used as the sole basis for academic, "
        "admission, disciplinary, or other high-impact decisions."
    )


def render_app():
    render_header()

    academic_data = (
        render_academic_section()
    )

    student_data = (
        render_student_section()
    )

    lifestyle_data = (
        render_lifestyle_section()
    )

    form_data = {
        **academic_data,
        **student_data,
        **lifestyle_data
    }

    render_prediction_section(
        form_data
    )

    render_footer()