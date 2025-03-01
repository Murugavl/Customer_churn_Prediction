import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open("churn_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Mapping categorical values
def preprocess_input():
    contract_mapping = {"Yes": 1, "No": 0}
    payment_mapping = {"Yes": 1, "No": 0}
    internet_service_mapping = {"Yes": 1, "No": 0}

    # Get input data from Streamlit UI
    input_data = np.array([
        age, 
        tenure, 
        monthly_charges, 
        total_charges,
        contract_mapping[contract_one_year],
        contract_mapping[contract_two_year],
        payment_mapping[credit_card_payment],
        payment_mapping[electronic_check_payment],
        payment_mapping[mailed_check_payment],
        internet_service_mapping[internet_service_fiber_optic],
        internet_service_mapping[internet_service_no]
    ]).reshape(1, -1)

    return input_data

# Streamlit UI
st.set_page_config(page_title="📊 Customer Churn Prediction", page_icon=":guardsman:")
st.title("📊 Customer Churn Prediction App")
st.markdown("🔍 **Enter customer details to predict churn probability**")

# Input fields (Ensure these match the training dataset)
age = st.slider("🧑 Age", 18, 100, 30)
tenure = st.slider("📆 Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("💰 Monthly Charges ($)", 0.0, 500.0, 50.0)
total_charges = st.number_input("💳 Total Charges ($)", 0.0, 10000.0, 500.0)

contract_one_year = st.selectbox("📜 One Year Contract", ["Yes", "No"])
contract_two_year = st.selectbox("📜 Two Year Contract", ["Yes", "No"])
credit_card_payment = st.selectbox("💳 Credit Card Payment", ["Yes", "No"])
electronic_check_payment = st.selectbox("💳 Electronic Check Payment", ["Yes", "No"])
mailed_check_payment = st.selectbox("💳 Mailed Check Payment", ["Yes", "No"])
internet_service_fiber_optic = st.selectbox("🌐 Internet Service Fiber Optic", ["Yes", "No"])
internet_service_no = st.selectbox("🌐 Internet Service No", ["Yes", "No"])

# Prediction button
if st.button("🔮 Predict Churn"):
    input_data = preprocess_input()
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    if prediction == 1:
        st.error(f"🚨 This customer is **likely to churn**! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ This customer is **likely to stay**! (Probability: {1 - probability:.2f})")

st.markdown("___")
st.markdown("Made with ❤️ by MURUGAVEL V")