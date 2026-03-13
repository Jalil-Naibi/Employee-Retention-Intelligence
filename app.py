import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- 1. SETUP & MODEL LOADING ---
st.set_page_config(page_title="Salifort Motors Retention Tool", page_icon="🚗")

@st.cache_resource
def load_model():
    # Ensure this path matches your folder structure!
    with open('models/hr_rf_grid_search.pickle', 'rb') as f:
        return pickle.load(f)

model = load_model()

# These must match the order in your notebook's X_train.columns
expected_cols = [
    'satisfaction_level', 'last_evaluation', 'number_project',
    'average_monthly_hours', 'tenure', 'work_accident', 
    'promotion_last_5years', 'salary', 'department_IT', 'department_RandD', 
    'department_accounting', 'department_hr', 'department_management', 
    'department_marketing', 'department_product_mng', 'department_sales', 
    'department_support', 'department_technical'
]

# --- 2. USER INTERFACE ---
st.title("📈 Employee Retention Intelligence")
st.write("Predict attrition risk for Salifort Motors employees.")

col1, col2 = st.columns(2)

with col1:
    satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
    last_eval = st.slider("Last Evaluation Score", 0.0, 1.0, 0.5)
    tenure = st.slider("Tenure (Years)", 2, 10, 3)
    salary = st.selectbox("Salary Level", ["low", "medium", "high"])

with col2:
    projects = st.number_input("Number of Projects", 2, 7, 3)
    hours = st.number_input("Average Monthly Hours", 90, 315, 200)
    dept = st.selectbox("Department", ["sales", "technical", "support", "IT", "product_mng", "marketing", "RandD", "accounting", "hr", "management"])
    
    # Binary selections
    accident = st.checkbox("Work Accident")
    promotion = st.checkbox("Promotion (Last 5 Years)")

# --- 3. PREDICTION LOGIC ---
if st.button("Calculate Risk Score", type="primary"):
    # Create a template dataframe with all zeros
    input_df = pd.DataFrame(0, index=[0], columns=expected_cols)
    
    # Fill numerical/binary data
    input_df['satisfaction_level'] = satisfaction
    input_df['last_evaluation'] = last_eval
    input_df['number_project'] = projects
    input_df['average_monthly_hours'] = hours
    input_df['tenure'] = tenure
    input_df['work_accident'] = 1 if accident else 0
    input_df['promotion_last_5years'] = 1 if promotion else 0

    # Map salary to numerical value
    salary_mapping = {"low": 0, "medium": 1, "high": 2}
    input_df['salary'] = salary_mapping[salary]

    # Fill categorical dummies for department (Only if they exist in expected_cols)
    if f'department_{dept}' in expected_cols:
        input_df[f'department_{dept}'] = 1

    # Get Prediction
    risk_proba = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    # --- 4. DISPLAY RESULTS ---
    st.divider()
    if prediction == 1:
        st.error(f"### ⚠️ High Attrition Risk: {risk_proba:.1%}")
        st.write("This employee shows patterns similar to those who have left.")
    else:
        st.success(f"### ✅ Low Attrition Risk: {risk_proba:.1%}")
        st.write("This employee is likely to stay based on current metrics.")