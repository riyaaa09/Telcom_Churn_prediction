import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load model using a path relative to this file so wrapper/root runs work
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "outputs" / "model.pkl"

if not MODEL_PATH.exists():
    st.title("📉 Telecom Churn Prediction")
    st.error(f"Model file not found: {MODEL_PATH}.\nPlease ensure 'outputs/model.pkl' is present.")
    st.write("If your model file is located elsewhere, update the path in capstone/app.py.")
    st.stop()

model = joblib.load(MODEL_PATH)

st.title("📉 Telecom Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

# ===== User Inputs =====
tenure = st.slider("Tenure (months)", 1, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 100.0, 10000.0, 500.0)
data_used_gb = st.number_input("Data Used (GB)", 0.0, 500.0, 10.0)
calls_made = st.number_input("Calls Made", 0, 1000, 100)
revenue_inr = st.number_input("Revenue (INR)", 0.0, 20000.0, 1000.0)
complaints_total = st.number_input("Total Complaints", 0, 50, 0)
complaints_open = st.number_input("Open Complaints", 0, 20, 0)

contract_type = st.selectbox("Contract Type", ["Month-to-Month","One Year","Two Year"])
plan_type = st.selectbox("Plan Type", ["Prepaid","Postpaid"])
region = st.selectbox("Region", ["North","South","East","West"])

# ===== Create dataframe =====
input_df = pd.DataFrame([{
    "tenure": tenure,
    "monthly_charges": monthly_charges,
    "data_used_gb": data_used_gb,
    "calls_made": calls_made,
    "revenue_inr": revenue_inr,
    "complaints_total": complaints_total,
    "complaints_open": complaints_open,
    "contract_type": contract_type,
    "plan_type": plan_type,
    "region": region
}])

# ===== Prediction =====
if st.button("Predict Churn"):
    prob = model.predict_proba(input_df)[0][1]
    pred = int(prob >= 0.5)

    st.subheader(f"Churn Probability: {prob:.2%}")

    if pred == 1:
        st.error("⚠️ High Risk Customer")
        st.write("👉 Offer discount / priority support / contract upgrade.")
    else:
        st.success("✅ Customer Likely to Stay")

