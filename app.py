# =========================================
# Loan Approval Prediction System - Full Working Code
# =========================================

import streamlit as st
import pandas as pd
import joblib
import os

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Loan Approval Prediction System",
    page_icon="🏦",
    layout="wide"
)

# =========================================
# LOAD MODEL FUNCTION
# =========================================

def load_model():
    paths = [
        "model.pkl",
        "model (2).pkl",
        "./model.pkl",
        "models/model.pkl",
        "artifacts/model.pkl"
    ]

    for path in paths:
        if os.path.exists(path):
            return joblib.load(path), path

    return None, None

model, model_path = load_model()

# =========================================
# SIDEBAR NAVIGATION
# =========================================

st.sidebar.title("⚙️ Navigation")
menu = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "🔍 Loan Prediction",
        "📂 Batch Prediction",
        "📊 Model Information"
    ]
)

# =========================================
# HOME PAGE
# =========================================

if menu == "🏠 Home":

    st.title("🏦 Loan Approval Prediction System")
    st.markdown("---")

    st.write("""
    This application predicts whether a loan will be **Approved** or **Rejected** based on applicant details.

    ### Features:
    - Single Loan Prediction
    - Batch Prediction using CSV
    - Professional UI
    - Automatic Model Detection
    """)

# =========================================
# LOAN PREDICTION PAGE
# =========================================

elif menu == "🔍 Loan Prediction":

    st.title("🏦 Loan Approval Prediction System")
    st.subheader("Enter Applicant Details")

    if model is None:
        st.error("❌ Model file not found.")
        st.stop()

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        married = st.selectbox(
            "Married",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["0", "1", "2", "3+"]
        )

        education = st.selectbox(
            "Education",
            ["Graduate", "Not Graduate"]
        )

    with col2:
        self_employed = st.selectbox(
            "Self Employed",
            ["Yes", "No"]
        )

        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0
        )

        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0
        )

        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0
        )

    with col3:
        loan_term = st.number_input(
            "Loan Amount Term",
            min_value=0
        )

        credit_history = st.selectbox(
            "Credit History",
            [1, 0]
        )

        property_area = st.selectbox(
            "Property Area",
            ["Urban", "Semiurban", "Rural"]
        )

    # =========================================
    # PREDICTION BUTTON
    # =========================================

    if st.button("🚀 Predict Loan Status"):

        try:

            
            input_data = pd.DataFrame({
                'Gender': [gender],
                'Married': [married],
                'Dependents': [dependents],
                'Education': [education],
                'Self_Employed': [self_employed],
                'ApplicantIncome': [applicant_income],
                'CoapplicantIncome': [coapplicant_income],
                'LoanAmount': [loan_amount],
                'Loan_Amount_Term': [loan_term],
                'Credit_History': [credit_history],
                'Property_Area': [property_area],
                            })

            # ENCODING

            input_data['Gender'] = input_data['Gender'].map({
                'Male': 1,
                'Female': 0
            })

            input_data['Married'] = input_data['Married'].map({
                'Yes': 1,
                'No': 0
            })

            input_data['Education'] = input_data['Education'].map({
                'Graduate': 1,
                'Not Graduate': 0
            })

            input_data['Self_Employed'] = input_data['Self_Employed'].map({
                'Yes': 1,
                'No': 0
            })

            input_data['Property_Area'] = input_data['Property_Area'].map({
                'Urban': 2,
                'Semiurban': 1,
                'Rural': 0
            })

            input_data['Dependents'] = input_data['Dependents'].replace({
                '3+': 3
            }).astype(int)

            prediction = model.predict(input_data)[0]

            if prediction == 1:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

        except Exception as e:
            st.error(f"Error: {e}")

# =========================================
# BATCH PREDICTION
# =========================================

elif menu == "📂 Batch Prediction":

    st.title("📂 Batch Prediction")

    if model is None:
        st.error("❌ Model file not found.")
        st.stop()

    file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)

        st.write("Preview:")
        st.dataframe(df.head())

        try:

            predictions = model.predict(df)

            df['Prediction'] = predictions

            st.success("Batch prediction completed")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')

            st.download_button(
                "Download Results",
                csv,
                "predictions.csv",
                "text/csv"
            )

        except Exception as e:
            st.error(e)

# =========================================
# MODEL INFORMATION
# =========================================

elif menu == "📊 Model Information":

    st.title("📊 Model Information")

    if model is None:
        st.error("❌ Model not loaded")

    else:
        st.success("Model Loaded Successfully")

        st.write("Model Path:")
        st.code(model_path)

        st.write("Model Type:")
        st.code(type(model))
