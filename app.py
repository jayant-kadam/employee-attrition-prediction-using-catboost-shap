import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Predictor",
    layout="wide"
)

st.title("Employee Attrition Prediction System")

st.markdown("""
### Features

- Bulk Employee Prediction
- Single Employee Prediction
- SHAP Explainability
- Risk Scoring
- Retention Recommendations
- Download Results
""")