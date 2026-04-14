# 🏦 Loan Approval Prediction System

A **Machine Learning Web Application** built with **Streamlit** that predicts whether a loan application will be **Approved** or **Rejected** based on applicant details.

This project demonstrates an end-to-end ML workflow including model training, deployment, and an interactive user interface.

---

# 🌐 Live Demo

👉 **Click here to use the app:**
https://loanstatuslogesticmodel-tkc445l4nbywcbhnvqwfxi.streamlit.app/                     
 
---

# 📸 Application Screenshot

![Loan Prediction App Screenshot](app_screenshot.png)
<img width="1888" height="825" alt="Screenshot 2026-04-13 122052" src="https://github.com/user-attachments/assets/ccacfe54-d151-432b-af04-3bfa0270241e" />


**How to add your image:**

1. Take a screenshot of your app
2. Save it as:

```bash
app_screenshot.png
```

3. Upload it to your GitHub repository
4. The image will automatically display in README

---

# 🚀 Features

* Single Loan Prediction
* Batch Prediction using CSV
* Clean and Professional UI
* Dropdown-based inputs
* Model auto-loading
* Error handling
* Download prediction results
* Ready for deployment

---

# 🧠 Machine Learning Model

**Algorithm Used:**

* Logistic Regression

**Problem Type:**

* Binary Classification

**Target Variable:**

* Loan Status (Approved / Rejected)

---

# 📂 Project Structure

```bash
Loan_Predict_Logistic_Reg/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── app_screenshot.png
│
└── data/
    └── loan_data.csv
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/loan-prediction-app.git
```

Move into the project folder:

```bash
cd loan-prediction-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
joblib
```

---

# 📊 Input Features Used

* Gender
* Married
* Dependents
* Education
* Self Employed
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area

---

# 📁 Batch Prediction

Upload a CSV file with the same feature columns to get predictions for multiple records.

You can also download the prediction results as a new CSV file.

---

# 🛠 Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

# 👨‍💻 Author

**Atish Kushwaha**

GitHub:
https://github.com/Atishkushwaha2004

---

# ⭐ If you like this project

Please give it a **Star** on GitHub!

It helps others discover the project and supports the developer.
