# 🚀 Startup Burnout & Failure Prediction System

An end-to-end Machine Learning project that predicts **Founder Burnout Risk** and **Startup Failure Risk** using startup-related business and founder information.

The project follows a two-stage prediction pipeline:

1. Predict the founder's burnout risk.
2. Use the predicted burnout result along with business metrics to estimate startup failure risk.

---

## 📌 Project Overview

Startup success depends on many factors such as founder experience, funding, product-market fit, runway, work-life balance, and market conditions.

This project uses Machine Learning to analyze these factors and provide:

- 🔥 Founder Burnout Prediction
- 🚨 Startup Failure Prediction

The burnout prediction is used as an additional input feature for the startup failure model.

---

## 🧠 Workflow

```text
User Inputs
      │
      ▼
Founder Burnout Model
(Logistic Regression)
      │
      ▼
Founder_Burnout_Flag
      │
      ▼
Startup Failure Model
(XGBoost)
      │
      ▼
Final Predictions
```

---

# 📊 Features Used

## Founder Burnout Prediction

- Economic Climate
- Founder Age
- Founder Experience
- Industry
- Funding Stage
- Work Mode
- Team Size
- Startup Age
- Weekly Work Hours
- Monthly Revenue Growth
- Runway Remaining
- Product Market Fit Score
- Employee Turnover
- Work-Life Balance
- Mental Health Support

---

## Startup Failure Prediction

All the above features plus:

- Founder Type
- Founder Burnout Prediction

---

# ⚙️ Machine Learning Pipeline

The project uses Scikit-Learn Pipelines for automated preprocessing and prediction.

### Data Preprocessing

- One Hot Encoding
- Standard Scaling
- Column Transformer
- Pipeline Automation

---

# 🤖 Algorithms Compared

The following algorithms were evaluated before selecting the final models.

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- AdaBoost
- Bagging
- Voting Classifier
- Gradient Boosting
- XGBoost

---

# ✅ Final Models

## Founder Burnout Prediction

**Algorithm**

- Logistic Regression

### Performance

| Metric | Score |
|---------|--------|
| Accuracy | **95.24%** |
| Weighted F1 Score | **95.16%** |

---

## Startup Failure Prediction

**Algorithm**

- XGBoost Classifier

### Performance

| Metric | Score |
|---------|--------|
| Accuracy | **88.32%** |
| Weighted F1 Score | **88.13%** |

---

# 📈 Feature Importance

The most influential features for startup failure prediction include:

- Work-Life Balance Score
- Founder Burnout Flag
- Runway Remaining
- Product Market Fit Score
- Economic Climate
- Employee Turnover
- Founder Experience

---

# 💻 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

# 📂 Project Structure

```
Startup-Failure-Prediction/
│
├── app.py
├── burnout_pipe.pkl
├── failure_pipe.pkl
├── dataset.csv
├── requirements.txt
├── Startup Project.ipynb
└── README.md
```

---

# 🚀 Running the Project

### Clone the repository

```bash
git clone https://github.com/dawareashwini/Startup-Failure_prediction.git
```

### Move into the project

```bash
cd Startup-Failure_prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📷 Application

The Streamlit application allows users to enter startup information and receive:

- Founder Burnout Risk
- Startup Failure Risk
- Prediction Probability

---

# 📚 What I Learned

During this project I gained practical experience with:

- Data preprocessing
- Feature Engineering
- One-Hot Encoding
- Feature Scaling
- Pipeline Creation
- Model Evaluation
- Classification Metrics
- Model Serialization using Joblib
- Streamlit Application Development

---

# 🔮 Future Improvements

- Use real-world startup datasets
- Hyperparameter tuning
- Probability calibration
- Explainable AI using SHAP
- Cloud deployment
- Larger dataset for improved generalization
