# Employee Retention Intelligence System 
###  Project Overview
High employee turnover increases hiring costs and lowers team morale. This project analyzes HR data from Salifort Motors to identify the key factors driving attrition and builds a predictive model to flag at-risk employees.

**Business Impact:** The final model achieves **96% accuracy** and identifies "Overwork" (Monthly Hours > 250) as the #1 predictor of turnover, enabling HR to intervene early.

## Live Application

Try the interactive employee attrition predictor:

[https://your-streamlit-link.streamlit.app](https://employee-retention-intelligence.streamlit.app/)

###  Key Findings
* **Overwork is the Killer:** Employees working 250+ hours/month are 3x more likely to leave.
* **The "Satisfaction" Trap:** Employees with *high* evaluation scores but *low* satisfaction are the highest flight risk.
* **Tenure Risk:** Employees at the 4-year mark are most vulnerable to turnover.

## 📄 Project Deliverables
* **[View Executive Summary (PDF)](docs/Executive_Summary.pdf):** A one-page business presentation summarizing the key findings for stakeholders.

###  Tech Stack
* **Python** (Pandas, NumPy)
* **Machine Learning:** Random Forest Classifier, XGBoost
* **Visualization:** Matplotlib, Seaborn
* **Deployment:** Streamlit

###  Model Performance
| Model | Accuracy | Precision | Recall | F1 Score |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | **96.2%** | **95.8%** | **94.5%** | **95.1%** |
| XGBoost | 94.1% | 93.0% | 92.0% | 92.5% |
