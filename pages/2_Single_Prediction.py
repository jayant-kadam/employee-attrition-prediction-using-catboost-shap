import streamlit as st
import pandas as pd
import plotly.express as px

from utils import (
    get_attrition,
    get_risk_score,
    get_top_factors,
    generate_recommendation
)

col1,col2,col3 = st.columns(3)

#Column 1

with col1:

    emp_id = st.text_input(
        "Employee ID"
    )

    age = st.selectbox(
        "Age",
        list(range(18, 61))
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    years_at_company = st.selectbox(
        "Years at Company",
        list(range(1, 36))
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Education",
            "Finance",
            "Healthcare",
            "Media",
            "Technology"
        ]
    )

    monthly_income = st.text_input(
        "Monthly Income"
    )

    work_life_balance = st.selectbox(
        "Work-Life Balance",
        [
            "Excellent",
            "Fair",
            "Good",
            "Poor"
        ]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [
            "High",
            "Low",
            "Medium",
            "Very High"
        ]
    )

#Column 2

with col2:

    performance_rating = st.selectbox(
        "Performance Rating",
        [
            "Average",
            "Below Average",
            "High",
            "Low"
        ]
    )

    number_of_promotions = st.text_input(
        "Number of Promotions"
    )

    overtime = st.selectbox(
        "Overtime",
        [
            "Yes",
            "No"
        ]
    )

    distance_from_home = st.text_input(
        "Distance from Home"
    )

    education_level = st.selectbox(
        "Education Level",
        [
            "Associate Degree",
            "Bachelor Degree",
            "High School",
            "Master Degree",
            "PhD"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Divorced",
            "Married",
            "Single"
        ]
    )

    number_of_dependents = st.text_input(
        "Number of Dependents"
    )

    job_level = st.selectbox(
        "Job Level",
        [
            "Entry",
            "Mid",
            "Senior"
        ]
    )

#Column 3

with col3:

    company_size = st.selectbox(
        "Company Size",
        [
            "Large",
            "Medium",
            "Small"
        ]
    )

    company_tenure = st.text_input(
        "Company Tenure"
    )

    remote_work = st.selectbox(
        "Remote Work",
        [
            "Yes",
            "No"
        ]
    )

    leadership_opportunities = st.selectbox(
        "Leadership Opportunities",
        [
            "Yes",
            "No"
        ]
    )

    innovation_opportunities = st.selectbox(
        "Innovation Opportunities",
        [
            "Yes",
            "No"
        ]
    )

    company_reputation = st.selectbox(
        "Company Reputation",
        [
            "Excellent",
            "Fair",
            "Good",
            "Poor"
        ]
    )

    employee_recognition = st.selectbox(
        "Employee Recognition",
        [
            "High",
            "Low",
            "Medium",
            "Very High"
        ]
    )

if st.button(
    "Predict Attrition"
):

    df1 = pd.DataFrame({
        "Employee ID": [emp_id],
        "Age": [age],
        "Gender": [gender],
        "Years at Company": [years_at_company],
        "Job Role": [job_role],
        "Monthly Income": [float(monthly_income)],
        "Work-Life Balance": [work_life_balance],
        "Job Satisfaction": [job_satisfaction],
        "Performance Rating": [performance_rating],
        "Number of Promotions": [int(number_of_promotions)],
        "Overtime": [overtime],
        "Distance from Home": [float(distance_from_home)],
        "Education Level": [education_level],
        "Marital Status": [marital_status],
        "Number of Dependents": [int(number_of_dependents)],
        "Job Level": [job_level],
        "Company Size": [company_size],
        "Company Tenure": [float(company_tenure)],
        "Remote Work": [remote_work],
        "Leadership Opportunities": [leadership_opportunities],
        "Innovation Opportunities": [innovation_opportunities],
        "Company Reputation": [company_reputation],
        "Employee Recognition": [employee_recognition]
    })

    original_df = df1.copy()

    prediction_df = df1.copy()

    prediction_df.drop(
        "Employee ID",
        axis=1,
        inplace=True
    )

    # Predict

    attrition = get_attrition(
        prediction_df
    )[0]

    risk = get_risk_score(
        prediction_df
    )[0]

    factor = get_top_factors(
        prediction_df
    )[0]

    # Recommendation

    rec = generate_recommendation(
            prediction_df.iloc[0])

    # Display

    st.success(
        f"Prediction : {attrition}"
    )

    st.metric(
        "Risk Score",
        f"{risk}%"
    )

    st.write("Top Contributing Factors : ",
        factor
    )

    st.write("Retention Recommendations : ",
        rec
    )

    # Download Single Employee Result

    original_df["Attrition"] = attrition
    original_df["Risk Score"] = risk
    original_df["Top Contributing Factors"] = factor
    original_df["Retention Recommendations"] = rec

    csv = original_df.to_csv(
        index=False
    )

    st.download_button(
        "Download Employee Report",
        csv,
        "employee_report.csv",
        "text/csv"
    )