# Student Performance Prediction System

An end-to-end machine learning application for predicting student academic performance using academic, behavioral, demographic, and educational features.

The project explores student performance data, compares multiple regression approaches, evaluates early and progressive prediction scenarios, tunes the strongest models using cross-validation, and deploys the final Random Forest model through an interactive Streamlit application.

## Overview

The objective of this project is to investigate whether student academic performance can be predicted from information available during a course.

Two prediction scenarios were evaluated:

### Early Prediction

Predicts the final grade without using previous course grades (`G1` and `G2`).

This scenario explores whether demographic, behavioral, family, educational, and lifestyle information alone can provide useful early indications of academic performance.

### Progressive Prediction

Predicts the final grade using all available features, including:

- `G1` — first-period grade
- `G2` — second-period grade

This scenario evaluates how prediction improves once previous academic performance becomes available.

The comparison showed that prior academic performance provides substantial predictive information.

---

## Machine Learning Results

The models were evaluated using **Mean Absolute Error (MAE)** and **R²** on a held-out test set.

| Model | Scenario | MAE | R² |
|---|---|---:|---:|
| Baseline | Baseline | 3.646 | -0.010 |
| Decision Tree | Early | 3.595 | -0.116 |
| Random Forest | Early | 2.966 | 0.313 |
| Decision Tree | Progressive | 1.278 | 0.733 |
| Random Forest | Progressive | 1.178 | 0.805 |
| Tuned Decision Tree | Progressive | 1.341 | 0.718 |
| **Tuned Random Forest** | **Progressive** | **1.172** | **0.809** |

The **Tuned Progressive Random Forest** was selected as the final model.

### Final Model

- **Test MAE:** 1.172 grade points
- **Test R²:** 0.809
- **Algorithm:** Random Forest Regression
- **Hyperparameter selection:** Grid Search with 5-fold cross-validation

The Progressive Random Forest reduced MAE by approximately **60%** compared with the Early Random Forest, demonstrating the predictive value of previous academic performance.

---

## Model Development

The machine learning workflow includes:

1. Exploratory data analysis
2. Data-quality analysis
3. Numerical and categorical feature analysis
4. Train/test splitting
5. One-hot encoding of categorical variables
6. Baseline regression
7. Decision Tree Regression
8. Random Forest Regression
9. Training/test overfitting analysis
10. Five-fold cross-validation
11. Hyperparameter tuning with GridSearchCV
12. Feature-importance analysis
13. Residual and prediction-error analysis
14. Final model serialization with Joblib

The complete preprocessing and Random Forest model are stored together in a scikit-learn `Pipeline`, ensuring that the same preprocessing operations are automatically applied during future predictions.

---

## Dataset

This project uses the **Student Performance dataset** from the UCI Machine Learning Repository.

The mathematics dataset contains:

- **395 student observations**
- **33 variables**
- Academic information
- Demographic characteristics
- Family and educational background
- Study behavior
- Lifestyle characteristics
- Previous and final grades

The prediction target is:

`G3` — final academic grade

The original dataset represents grades on a **0–20 scale**.

For easier interpretation in the deployed application, users enter and receive grades on a **0–100 scale**. The application converts these values internally to and from the original dataset scale before and after prediction.

---

## Exploratory Analysis

Exploratory data analysis showed that previous academic performance is strongly associated with final performance.

In particular:

- `G2` showed the strongest relationship with the final grade.
- `G1` also showed a strong relationship with final performance.
- Previous failures showed a negative relationship with final grades.
- Study behavior, absences, family characteristics, and other variables were also investigated.

The analysis motivated the comparison between Early and Progressive prediction scenarios.

---

## Application

The trained model is integrated into an interactive **Streamlit web application**.

Users can provide information including:

- First-period and second-period grades
- Study time
- Previous failures
- Absences
- Educational support
- Family and educational background
- Extracurricular activities
- Health and selected lifestyle factors

The application converts the user inputs into the original feature representation expected by the trained model and returns an estimated final grade on a **0–100 scale**.

### Application Architecture

The application uses an MVC-inspired structure:

```text
User
  ↓
View
  ↓
Controller
  ↓
Model
  ↓
Prediction Service
  ↓
Saved ML Pipeline
```

- **View** — Streamlit interface and result presentation
- **Controller** — input mapping, validation, and coordination
- **Model** — application-level prediction interface
- **Prediction service** — loads and executes the trained ML pipeline
- **Training pipeline** — reproduces model training and serialization

---

## Project Structure

```text
student-performance-prediction/
│
├── app/
│   ├── __init__.py
│   ├── controller.py
│   ├── model.py
│   └── view.py
│
├── data/
│   └── raw/
│       └── student-mat.csv
│
├── models/
│   └── student_performance_random_forest.joblib
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   └── 02_model_development.ipynb
│
├── src/
│   ├── __init__.py
│   ├── predict.py
│   └── train.py
│
├── streamlit_app.py
├── test_prediction.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies

### Machine Learning

- Python
- scikit-learn
- Pandas
- NumPy
- Decision Tree Regression
- Random Forest Regression
- GridSearchCV
- OneHotEncoder
- scikit-learn Pipelines
- Joblib

### Data Analysis

- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

### Application

- Streamlit
- MVC-inspired application architecture

### Development

- Git
- GitHub
- VS Code
- Python virtual environments

---

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd student-performance-prediction
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run streamlit_app.py
```

### 5. Retrain the model

The final training pipeline can be reproduced with:

```bash
python src/train.py
```

The trained pipeline will be saved to:

```text
models/student_performance_random_forest.joblib
```

### 6. Test prediction

```bash
python test_prediction.py
```

---

## Model Limitations

This project uses a relatively small dataset containing students from two schools. The model therefore should not be interpreted as universally representative of students across different educational systems, institutions, populations, or grading structures.

The Progressive model also relies heavily on previous academic performance, particularly later course grades. Its strong predictive performance should therefore not be interpreted as evidence that demographic, behavioral, or lifestyle characteristics independently determine academic outcomes.

Feature importance indicates predictive contribution within the trained model and does **not** establish causation.

This application is intended as a machine-learning and software-engineering demonstration. Predictions should not be used as the sole basis for academic, admission, disciplinary, or other high-impact decisions.

---

## Future Improvements

Potential extensions include:

- Deploying separate Early and Progressive prediction models
- Comparing additional regression algorithms
- Expanding the dataset
- Adding model explainability techniques
- Improving prediction uncertainty estimates
- Adding automated tests
- Containerizing the application with Docker
- Adding continuous integration
- Expanding the application dashboard with model-performance visualizations

---

## Author

**Murali Karthik Ganji**

Computer Science  
University of Arizona

Portfolio: https://murali-karthik-ganji.vercel.app/
LinkedIn: https://www.linkedin.com/in/murali-karthik-ganji

---

## Acknowledgments

Dataset: **Student Performance — UCI Machine Learning Repository**

The dataset was originally developed for research into student achievement in secondary education.