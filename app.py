import streamlit as st
import pandas as pd
import pickle

st.title("Customer Churn Prediction App")

# Load model files safely
try:
    model = pickle.load(open("churn_model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    model_columns = pickle.load(open("model_columns.pkl", "rb"))
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.write("Enter customer details below:")

# --- User Inputs ---
tenure = st.number_input("Tenure (months)", min_value=0)
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", 
                             ["Electronic check", 
                              "Bank transfer (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges")

# --- Convert Input to DataFrame ---
input_dict = {
    "tenure": tenure,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
}

input_df = pd.DataFrame([input_dict])

# One-hot encoding
input_df = pd.get_dummies(input_df)

# Align with training columns
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# Scale
input_scaled = scaler.transform(input_df)

# --- Prediction ---
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1] * 100

    if prediction == 1:
        st.error(f"Customer is likely to Churn      \n Churn Probability: {probability:.2f}%")
    else:
        st.success(f"Customer is NOT likely to Churn      \n Churn Probability: {probability:.2f}%")
