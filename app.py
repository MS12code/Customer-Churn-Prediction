import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# LOAD MODEL + TRAINING COLUMNS
# -----------------------------
model = pickle.load(open("churn_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Customer Churn App", layout="centered")

st.title("📊 Customer Churn Prediction App")
st.write("Enter customer details to predict whether they will churn:")

# -----------------------------
# INPUT FIELDS
# -----------------------------

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=0)

phone = st.selectbox("Phone Service", ["Yes", "No"])
multiline = st.selectbox("Multiple Lines", ["Yes", "No phone service", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox("Payment Method", 
                       ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

monthly = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total = st.number_input("Total Charges", min_value=0.0, value=100.0)

# -----------------------------
# PREDICTION BUTTON
# -----------------------------

if st.button("Predict Churn"):
    # Create input dictionary
    input_dict = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiline,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    # Convert to DataFrame
    df = pd.DataFrame([input_dict])

    # One-hot encode
    df = pd.get_dummies(df)

    # Align with training columns
    df = df.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(df)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ This customer is likely to **CHURN**.")
    else:
        st.success("🎉 This customer is likely to **STAY**.")

