📌 Customer Churn Prediction System
------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Project Overview

Built a machine learning model to predict whether a telecom customer will churn or not. Implemented using Logistic Regression for binary classification. 
Developed an interactive web application using Streamlit. Users can input customer details and get real-time churn probability.
Designed to simulate a real-world telecom customer retention analytics system.

🎯 Problem Statement

Customer churn refers to customers who stop using a company's product or service within a given period.

High churn rates can:
  Reduce revenue
  Increase customer acquisition costs
  Affect long-term business growth
  
This project aims to:
  Analyze customer data
  Identify churn patterns
  Build a predictive classification model
  Evaluate performance using standard ML metrics

📊 Dataset Information

Dataset Used: Telco Customer Churn Dataset Type: Supervised Binary Classification Target Variable: Churn (Yes / No)

🔹 Key Features: Tenure (months) MonthlyCharges TotalCharges Contract Type Internet Service Type Payment Method Online Security Paperless Billing Other telecom-related service features

🔹 Data Preprocessing:

Handled missing and inconsistent values Converted categorical variables using One-Hot Encoding Converted target variable (Yes/No) into binary format (1/0) Scaled numerical features
where required Ensured feature alignment between training and prediction data


🤖 Model & Approach 

🔹 Model Used: Logistic Regression

🔹 Why Logistic Regression? Best suited for binary classification problems Outputs churn probability (0–100%) Provides interpretable feature coefficients
    Computationally efficient and fast

🔹 Training Process: Split dataset into training and testing sets Trained Logistic Regression model on training data Evaluated performance using test data Saved trained model using 
    Pickle Integrated model into Streamlit for deployment

🎯 Model Performance

Accuracy: (Insert your actual accuracy here, e.g., 81%) Evaluation Metrics Used:

Accuracy Score Precision F1-Score Model outputs churn probability using the sigmoid function.

🛠️ Technologies & Libraries Used

Python ,Pandas ,NumPy, Scikit-learn  ,Matplotlib , Streamlit Pickle

💡 Future Improvements

Implement advanced models (Random Forest, XGBoost) Deploy using cloud services Add feature importance visualization Improve UI/UX for better user experience Add input validation for realistic data ranges
