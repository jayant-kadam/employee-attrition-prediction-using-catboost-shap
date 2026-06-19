import streamlit as st
import pandas as pd
import plotly.express as px

from utils import (
    get_attrition,
    get_risk_score,
    get_top_factors,
    generate_recommendation,
    get_feature_importance
)

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    original_df = df.copy()

    prediction_df = df.copy()

    prediction_df.drop(
        "Employee ID",
        axis=1,
        inplace=True
    )

    # Predict

    attrition = get_attrition(
        prediction_df
    )

    risk_score = get_risk_score(
        prediction_df
    )

    factors = get_top_factors(
        prediction_df
    )

    # Recommendations

    recommendations = []

    for i, row in prediction_df.iterrows():

        recommendations.append(
            generate_recommendation(row)
        )

    # Merge

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

    # Download Button

    csv = original_df.to_csv(
        index=False
    )

    st.download_button(
        "Download Results",
        csv,
        "attrition_predictions.csv",
        "text/csv"
    )