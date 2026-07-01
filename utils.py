import pandas as pd
# Used to create and manipulate tables (DataFrames).

import joblib
# Used to load saved files.

import shap
# Loads SHAP.

model = joblib.load(
    "model/employee_attrition_catboost.pkl"
)
# Loads your trained CatBoost model.

feature_names = joblib.load(
    "model/feature_columns_catboost.pkl"
)
# Loads list of columns used during training.

explainer = shap.TreeExplainer(model)
# Creates SHAP explanation object.


# --------------------------------------------------
# Risk Score
# --------------------------------------------------

# def get_risk_score(df):
#     prob = model.predict_proba(df)
#     return (prob[:,1] * 100).round(2)

def get_risk_score(df):

    probabilities = model.predict_proba(df)
    # Gets probabilities.

    risk_scores = probabilities[:, 1] * 100
    # Take only second column.

    return risk_scores.round(2)
    # Rounds to 2 decimal places.


# --------------------------------------------------
# Attrition
# --------------------------------------------------
# Converts model output into human-readable labels.

def get_attrition(df):

    predictions = model.predict(df)

    attrition = []

    for pred in predictions:

        if pred == 1:

            attrition.append("Leave")

        else:

            attrition.append("Stay")

    return attrition


# --------------------------------------------------
# Top Contributing Factors
# --------------------------------------------------
# Finds top 3 reasons behind each prediction.

def get_top_factors(df):

    shap_values = explainer.shap_values(df)

    factors = []

    for i in range(len(df)):

        temp = pd.DataFrame(
            {
                "Feature": df.columns,
                "Value": abs(shap_values[i])
            }
        )

        temp = temp.sort_values(
            "Value",
            ascending=False
        )

        factors.append(
            ", ".join(
                temp.head(3)["Feature"]
            )
        )

    return factors


# --------------------------------------------------
# Generate Retention Recommendations
# --------------------------------------------------
# Rule-based HR recommendations.

def generate_recommendation(row):

    recs = []

    if row["Work-Life Balance"] == "Poor":

        recs.append(
            "Improve work-life balance"
        )

    if row["Job Satisfaction"] == "Low":

        recs.append(
            "Career counselling"
        )

    if row["Monthly Income"] < 4000:

        recs.append(
            "Compensation review"
        )

    if row["Overtime"] == "Yes":

        recs.append(
            "Reduce overtime"
        )

    if len(recs) == 0:

        recs.append(
            "Monitor employee"
        )

    return "; ".join(recs)


# --------------------------------------------------
# Feature Importance
# --------------------------------------------------
# Returns feature importance table for Streamlit charts.

def get_feature_importance():

    importance_df = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": model.get_feature_importance()
        }
    )

    importance_df = importance_df.sort_values(
        "Importance",
        ascending=False
    )

    return importance_df


# --------------------------------------------------
# Feature Names
# --------------------------------------------------
# Used to validate uploaded CSV columns.

def get_feature_names():

    return feature_names