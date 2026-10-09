
import streamlit as st
import pandas as pd
import joblib

# =====================
# Load Models
# =====================
burnout_pipe = joblib.load("burnout_pipe.pkl")
failure_pipe = joblib.load("failure_pipe.pkl")

# =====================
# Title
# =====================
st.title("🚀 Startup Burnout & Failure Predictor")

# =====================
# Inputs
# =====================

founder_type = st.selectbox(
    "Founder Type",
    [
        "Serial Entrepreneur",
        "Calm Operator",
        "Burned-Out Operator",
        "Chaotic Innovator",
        "Growth Obsessed Founder",
        "Visionary CEO",
        "Technical Builder",
        "Solo Hustler"
    ]
)

economic_climate = st.selectbox(
    "Economic Climate",
    [
        "Bull Market",
        "Stable Economy",
        "Recession",
        "Funding Winter"
    ]
)

founder_age = st.number_input(
    "Founder Age",
    min_value=18,
    max_value=80,
    value=30
)

founder_experience_years = st.number_input(
    "Founder Experience Years",
    min_value=0,
    max_value=50,
    value=5
)

industry = st.selectbox(
    "Industry",
    [
        "AI",
        "SaaS",
        "FinTech",
        "E-commerce",
        "HealthTech",
        "EdTech"
    ]
)

funding_stage = st.selectbox(
    "Funding Stage",
    [
        "Bootstrapped",
        "Seed",
        "Series A",
        "Series B",
        "Series C"
    ]
)

# Fixed here: Office instead of On-site
work_mode = st.selectbox(
    "Work Mode",
    [
        "Remote",
        "Hybrid",
        "Office"
    ]
)

team_size = st.number_input(
    "Team Size",
    min_value=1,
    max_value=1000,
    value=10
)

startup_age_months = st.number_input(
    "Startup Age (Months)",
    min_value=1,
    max_value=240,
    value=24
)

weekly_work_hours = st.number_input(
    "Weekly Work Hours",
    min_value=20,
    max_value=120,
    value=60
)

monthly_revenue_growth_percent = st.number_input(
    "Monthly Revenue Growth %",
    value=10.0
)

runway_months_remaining = st.number_input(
    "Runway Months Remaining",
    value=12.0
)

product_market_fit_score = st.slider(
    "Product Market Fit Score",
    0.0,
    10.0,
    7.0
)

employee_turnover_percent = st.slider(
    "Employee Turnover %",
    0.0,
    100.0,
    15.0
)

work_life_balance_score = st.slider(
    "Work-Life Balance Score",
    0.0,
    10.0,
    6.0
)

mental_health_support = st.selectbox(
    "Seeks Mental Health Support",
    ["Yes", "No"]
)

# =====================
# Prediction
# =====================

if st.button("Predict"):

    # -------- Burnout Model Input --------
    burnout_input = pd.DataFrame({
        "Economic_Climate": [economic_climate],
        "Founder_Age": [founder_age],
        "Founder_Experience_Years": [founder_experience_years],
        "Industry": [industry],
        "Funding_Stage": [funding_stage],
        "Work_Mode": [work_mode],
        "Team_Size": [team_size],
        "Startup_Age_Months": [startup_age_months],
        "Weekly_Work_Hours": [weekly_work_hours],
        "Monthly_Revenue_Growth_Percent": [monthly_revenue_growth_percent],
        "Runway_Months_Remaining": [runway_months_remaining],
        "Product_Market_Fit_Score": [product_market_fit_score],
        "Employee_Turnover_Percent": [employee_turnover_percent],
        "Work_Life_Balance_Score": [work_life_balance_score],
        "Seeks_Mental_Health_Support": [mental_health_support]
    })

    # Burnout Prediction
    burnout_pred = burnout_pipe.predict(burnout_input)[0]
    burnout_prob = burnout_pipe.predict_proba(burnout_input)[0][1]

    # -------- Failure Model Input --------
    failure_input = pd.DataFrame({
        "Founder_Type": [founder_type],
        "Economic_Climate": [economic_climate],
        "Founder_Age": [founder_age],
        "Founder_Experience_Years": [founder_experience_years],
        "Industry": [industry],
        "Funding_Stage": [funding_stage],
        "Work_Mode": [work_mode],
        "Team_Size": [team_size],
        "Startup_Age_Months": [startup_age_months],
        "Weekly_Work_Hours": [weekly_work_hours],
        "Founder_Burnout_Flag": [burnout_pred],
        "Monthly_Revenue_Growth_Percent": [monthly_revenue_growth_percent],
        "Runway_Months_Remaining": [runway_months_remaining],
        "Product_Market_Fit_Score": [product_market_fit_score],
        "Employee_Turnover_Percent": [employee_turnover_percent],
        "Work_Life_Balance_Score": [work_life_balance_score],
        "Seeks_Mental_Health_Support": [mental_health_support]
    })

    # Failure Prediction
    failure_pred = failure_pipe.predict(failure_input)[0]
    failure_prob = failure_pipe.predict_proba(failure_input)[0][1]

    # =====================
    # Results
    # =====================

    st.header("Prediction Results")

    st.write(f"🔥 Founder Burnout Probability : {burnout_prob*100:.2f}%")
    st.write(f"🚨 Startup Failure Probability : {failure_prob*100:.2f}%")

    if burnout_pred == 1:
        st.error("⚠ Founder Burnout Risk : HIGH")
    else:
        st.success("✅ Founder Burnout Risk : LOW")

    if failure_pred == 1:
        st.error("⚠ Startup Failure Risk : HIGH")
    else:
        st.success("✅ Startup Failure Risk : LOW")

