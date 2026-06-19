<h1 align="center">📊 Employee Attrition Prediction System</h1>

<p align="center">
Employee Attrition Prediction System using <b>CatBoost</b>, <b>SHAP</b>, and <b>Streamlit</b>. Predicts employee attrition, calculates risk scores, identifies key contributing factors, and generates retention recommendations. Includes bulk and single employee prediction modules with interactive HR analytics dashboards.</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
Employee attrition is a major challenge for organizations. This project helps HR teams identify employees who are at risk of leaving the company by leveraging Machine Learning and Explainable AI.
</p>

<p>
The application predicts employee attrition, calculates risk scores, identifies key contributing factors using SHAP, and provides personalized retention recommendations.
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
<li>Predict employee attrition using CatBoost Classifier</li>
<li>Bulk employee attrition prediction via CSV upload</li>
<li>Single employee attrition prediction through an interactive form</li>
<li>Employee Risk Score calculation</li>
<li>SHAP-based explainability</li>
<li>Top contributing factors for each prediction</li>
<li>Personalized retention recommendations</li>
<li>Interactive HR analytics dashboard</li>
<li>CSV download functionality</li>
</ul>

<hr>

<h2>🧠 Machine Learning Model</h2>

<ul>
<li>Algorithm: CatBoost Classifier</li>
<li>Target Variable: Attrition (Stayed / Left)</li>
<li>Explainability: SHAP (SHapley Additive exPlanations)</li>
<li>Prediction Output:
    <ul>
        <li>Attrition Prediction</li>
        <li>Risk Score (%)</li>
        <li>Top Contributing Factors</li>
        <li>Retention Recommendations</li>
    </ul>
</li>
</ul>

<hr>

<h2>📊 Dashboard Features</h2>

<ul>
<li>Total Employees</li>
<li>Employees At Risk</li>
<li>Employees Likely To Stay</li>
<li>Average Risk Score</li>
<li>Attrition Distribution Pie Chart</li>
<li>Risk Score Distribution Histogram</li>
<li>Feature Importance Visualization</li>
</ul>

<hr>

<h2>🖥️ Streamlit Application Pages</h2>

<h3>🏠 Home Page</h3>

<ul>
<li>Project overview</li>
<li>Application description</li>
<li>Navigation menu</li>
</ul>

<h3>📁 Bulk Employee Prediction</h3>

<ul>
<li>Upload employee CSV file</li>
<li>Predict attrition for all employees</li>
<li>Generate risk scores</li>
<li>Identify top contributing factors</li>
<li>Generate retention recommendations</li>
<li>Download prediction results as CSV</li>
</ul>

<h3>👤 Single Employee Prediction</h3>

<ul>
<li>Interactive employee details form</li>
<li>Predict attrition for an individual employee</li>
<li>Generate risk score</li>
<li>Display SHAP-based contributing factors</li>
<li>Generate retention recommendations</li>
<li>Download employee report</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Employee_Attrition_App/

│
├── app.py
├── Data/
│   ├── Test.csv
│   └── Train.csv  
│
├── pages/
│   ├── 1_Bulk_Prediction.py
│   └── 2_Single_Prediction.py
│
├── model/
│   ├── categorical_columns_catboost.pkl
│   ├── employee_attrition_catboost.pkl
│   └── feature_columns_catboost.pkl
│
├── utils.py
├── requirements.txt
├── employee-attrition-catboost.ipynb
├── employee-attrition-EDA.ipynb
├── kaggle link.txt
└── README.md
</pre>

<hr>

<h2>🛠️ Technologies Used</h2>

<ul>
<li>Python</li>
<li>Pandas</li>
<li>NumPy</li>
<li>CatBoost</li>
<li>SHAP</li>
<li>Scikit-Learn</li>
<li>Plotly</li>
<li>Streamlit</li>
<li>Joblib</li>
</ul>

<hr>

<h2>⚙️ Installation</h2>

<ol>

<li>
        Download all files from the GitHub repository:
        <br>
        <a href="https://github.com/jayant-kadam/employee-attrition-prediction-using-catboost-shap">
            GitHub Repository
        </a>
</li>

<li>Create a project folder and copy-paste all downloaded files into it.</li>

<li>Run the <strong>app.py</strong> file using your preferred IDE.</li>

<li>
In Bulk Upload the <strong>test</strong> CSV file and the model will predict attrition,  Risk Score (%), Top Contributing Factors, Retention Recommendations and generate an interactive dashboard. Click Download Results button to download all data as csv.
</li>

<li>Input data must be provided in <strong>.csv</strong> format for bulk upload.</li>

<li>
        The input CSV file must contain the following columns: Employee ID,	Age,	Gender,	Years at Company,	Job Role,	Monthly Income,	Work-Life Balance,	Job Satisfaction,	Performance Rating,	Number of Promotions,	Overtime,	Distance from Home,	Education Level,	Marital Status,	Number of Dependents,	Job Level,	Company Size,	Company Tenure,	Remote Work,	Leadership Opportunities,	Innovation Opportunities,	Company Reputation,	Employee Recognition.

</li>

<li>In Single Employee Attrition, enter all details and the model will predict attrition,  Risk Score (%), Top Contributing Factors, Retention Recommendations. Click Download Employee Report button to download all data as csv.</li>

</ol>

<hr>

<h2>📈 Business Benefits</h2>

<ul>
<li>Early identification of employees at risk of leaving</li>
<li>Improved employee retention strategies</li>
<li>Data-driven HR decision making</li>
<li>Enhanced workforce planning</li>
<li>Explainable AI insights for HR teams</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>
This project is intended for educational, research, and portfolio purposes.
</p>

<hr>

<h2>🧑‍💻 Author</h2>

<p>
<strong>Jayant Kadam</strong><br>
Data Analyst<br>
https://www.linkedin.com/in/jayantkadam/
</p>

<hr>

<p align="center">
⭐ If you found this project useful, consider giving it a star on GitHub.
</p>
