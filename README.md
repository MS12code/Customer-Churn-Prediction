
# 📊 Customer Churn Prediction

This project predicts whether a telecom customer is likely to **churn** (leave the service) using a machine learning model trained on the Telco Customer Churn dataset.
It includes full data preprocessing, model training, evaluation, and an interactive **Streamlit web application** to make predictions.

---

## 🚀 Project Overview

Customer churn impacts revenue and retention strategies.
This project helps businesses:

* Identify customers at high risk of churning
* Understand factors contributing to churn
* Take proactive retention actions
* Visualize churn predictions through a GUI

The Streamlit app allows users to input customer details and instantly get a churn prediction.

---

## 🧠 Machine Learning Pipeline

### **1️⃣ Data Preprocessing**

* Loaded CSV dataset
* Handled missing and incorrect values
* Converted `TotalCharges` to numeric
* Removed irrelevant columns like `customerID`
* One-hot encoded categorical features
* Saved feature columns into `model_columns.pkl`

### **2️⃣ Model Training**

Model used: **Logistic Regression**

Why?

* Fast & lightweight
* Works well for binary classification
* Easy to interpret
* Stable baseline model

**Accuracy achieved: ~82%**

### **3️⃣ Model Saving**

Two files are generated:

| File                | Purpose                                           |
| ------------------- | ------------------------------------------------- |
| `churn_model.pkl`   | Stores trained ML model                           |
| `model_columns.pkl` | Stores feature columns for proper input alignment |

### **4️⃣ Streamlit Application**

The app collects user inputs for:

* Demographics details
* Account info
* Services subscribed
* Charges

Outputs provided:

* **Churn or Stay prediction**
* **Color-coded result message**
* (Optional upgrades): probability score & feature importance

---

## 📁 Project Structure

```
📁 Customer-Churn-Prediction/
│── app.py
│── churn_model.pkl
│── model_columns.pkl
│── data/
│     └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│── README.md
```

---

## 💻 How to Run This Project

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/MS12code/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### **2️⃣ Install required packages**

If you don't have a `requirements.txt`, install manually:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

### **3️⃣ Run the Streamlit app**

```bash
streamlit run app.py
```

Your browser will open:

```
http://localhost:8501
```

---

## 📈 Future Enhancements

* Add probability scores in UI
* Add feature importance visualization
* Try advanced models (RandomForest, XGBoost)
* Deploy using Streamlit Cloud
* Add database/real-time API integration
* Implement SHAP explainability

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Git & GitHub

---

## 📬 Contact

Feel free to reach out if you want improvements or deployment guidance.

---

