import streamlit as st
#To load streamlit. Used for: Buttons, Tables, Charts, File upload.

import pandas as pd
#Used to create and manipulate tables (DataFrames).

import plotly.express as px
#Used for interactive charts.

#import Functions from utils.py
from utils import (
    get_attrition,
    get_risk_score,
    get_top_factors,
    generate_recommendation,
    get_feature_importance,
    get_feature_names
)

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

# Check If File Uploaded
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # ------------------------------------------------
    # Validate Employee ID Column
    # ------------------------------------------------

    if "Employee ID" not in df.columns:

        st.error(
            "The uploaded CSV must contain an 'Employee ID' column."
        )

        st.stop()

    original_df = df.copy()

    prediction_df = df.copy()

    # ------------------------------------------------
    # Drop Columns Not Used By Model
    # ------------------------------------------------

    prediction_df.drop(
        ["Employee ID", "Attrition"],
        axis=1,
        inplace=True,
        errors="ignore"
    )

    # ------------------------------------------------
    # Validate Uploaded CSV Columns
    # ------------------------------------------------

    expected_columns = get_feature_names()

    uploaded_columns = prediction_df.columns.tolist()

    if uploaded_columns != expected_columns:

        missing_columns = [
            col for col in expected_columns
            if col not in uploaded_columns
        ]

        extra_columns = [
            col for col in uploaded_columns
            if col not in expected_columns
        ]

        st.error(
            "Uploaded CSV columns do not match the columns used during model training."
        )

        if missing_columns:

            st.write("### Missing Columns")

            st.write(missing_columns)

        if extra_columns:

            st.write("### Extra Columns")

            st.write(extra_columns)

        st.stop()

    # ------------------------------------------------
    # Predict Attrition
    # ------------------------------------------------

    attrition = get_attrition(
        prediction_df
    )

    risk_score = get_risk_score(
        prediction_df
    )

    factors = get_top_factors(
        prediction_df
    )

    recommendations = []

    for _, row in prediction_df.iterrows():

        recommendations.append(
            generate_recommendation(row)
        )

    # ------------------------------------------------
    # Merge Results
    # ------------------------------------------------

    original_df["Attrition"] = attrition
    original_df["Risk Score"] = risk_score
    original_df["Top Contributing Factors"] = factors
    original_df["Retention Recommendations"] = recommendations



    # Display 5 Employees

    st.dataframe(
        original_df[
            [
                "Employee ID",
                "Attrition",
                "Risk Score",
                "Top Contributing Factors",
                "Retention Recommendations"
            ]
        ].head()
    )

    # Dashboard

    # KPIs

    total_employees = len(original_df)

    leave_count = (
        original_df["Attrition"] == "Leave"
    ).sum()

    stay_count = (
        original_df["Attrition"] == "Stay"
    ).sum()

    avg_risk = original_df[
        "Risk Score"
    ].mean()

    col1, col2, col3, col4 = st.columns(4)
    #Creates 4 side-by-side columns.

    col1.metric(
        "Total Employees",
        total_employees
    )

    col2.metric(
        "Employees At Risk",
        leave_count
    )

    col3.metric(
        "Employees Likely To Stay",
        stay_count
    )

    col4.metric(
        "Average Risk Score",
        round(avg_risk, 2)
    )

    # Visuals - Row 1

    #Creates 2 columns.
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        fig = px.pie(
            original_df,
            names="Attrition",
            title="Attrition Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart_col2:

        fig2 = px.histogram(
            original_df,
            x="Risk Score",
            title="Risk Score Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # Visuals - Row 2

    feature_importance_df = (
        get_feature_importance()
        .head(10)
    )

    fig5 = px.bar(
        feature_importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top 10 Most Important Features"
    )

    fig5.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    #Convert Results To CSV and Download Button

    csv = original_df.to_csv(
        index=False
    )

    st.download_button(
        "Download Results",
        csv,
        "attrition_predictions.csv",
        "text/csv"
    )