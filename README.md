📘 README –Telecom Churn Prediction & Retention Intelligence

📌 Project Title
Telecom Customer Churn Prediction & Retention Strategy

🚀 Business Problem
Customer churn is one of the biggest revenue leakages in telecom.

Acquiring a new customer costs 5–10× more than retaining an existing one.
The company needs an intelligent system to:
✔ identify high-risk customers
✔ understand churn drivers
✔ take proactive retention actions

🎯 Objective
Build an end-to-end ML pipeline that:
integrates customer, usage, complaint & billing data
predicts churn probability
highlights key churn factors
enables business teams to act early

🧱 Solution Architecture
Raw CSVs → ETL (Python/Pandas) → Master Dataset
        → ML Model (Sklearn)
        → Predictions
        → Streamlit App / Power BI Dashboard

🛠 Tech Stack
Python
Pandas & NumPy
Scikit-learn
MySQL
Streamlit
Power BI

📂 Dataset
Multiple tables were combined:
customers → profile, region, plan
usage_data → consumption & revenue
complaints → issues & resolution
billing → tenure, contract, churn

⚙️ Project Workflow
1️⃣ Data Engineering
Cleaned missing values & duplicates
Standardized categories
Aggregated complaints
Merged into single analytical table
Output → telecom_master.csv

2️⃣ Exploratory Analysis
Key observations:
📌 higher churn in month-to-month contracts
📌 customers with low tenure more likely to churn
📌 repeated complaints strongly linked to churn
📌 certain regions show elevated risk

3️⃣ Modeling
Models trained:
Logistic Regression
Decision Tree
Used:
One-Hot Encoding
Standard Scaling
Stratified Train/Test split
Evaluation metrics:
Accuracy
Precisio
Recall
F1 Score
Confusion Matrix
Best model saved as:
model.pkl

4️⃣ Predictions
Generated:
churn probability
churn label
Output → predictions.csv

5️⃣ Streamlit Application
Interactive app where users can:
✔ simulate customer data
✔ view churn probability
✔ receive retention suggestions

Run locally:
streamlit run app.py

6️⃣ Power BI Dashboard
Visual storytelling of:
churn by region
churn by contract type
ARPU vs churn
complaint impact
