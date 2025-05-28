# House Rent Prediction Web Application
This project is a **machine learning-powered web application** that predicts house rent prices across major Indian metropolitan cities. It demonstrates the complete lifecycle of a data science project — from data cleaning and model building to deployment using **Flask**.
---
🔗 Check it out:
👉 https://metropolitan-cities-house-rent-prediction.onrender.com
---
## Overview
The goal of this project is to help users estimate monthly rent prices based on key features like **city**, **locality**, **BHK**, **size**, and **furnishing status**. It’s built with the intention of learning how to deploy a regression model in a real-world web application setting.

---

## Features
- Predicts house rent based on user input
- Trained using city-wise Indian rental data
- Fully integrated **web interface with dynamic dropdowns** (city → locality)
- End-to-end data pipeline: cleaning, feature engineering, scaling, modeling
- **Flask-based deployment** of the trained model

---

## Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Web Framework:** Flask  
- **Frontend:** HTML (basic interface), Jinja2 templates  
- **Model Deployment:** Pickle serialization  
- **Version Control:** Git, GitHub

---

## Project Structure
├── templates/
│ └── index.html # Frontend form for input
├── model/
│ └── lr_model.pkl # Trained Linear Regression model
├── app.py # Flask application
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── data/ # Processed/cleaned dataset (not included due to size)


---

## Machine Learning Pipeline

1. **Data Cleaning:** Missing values, incorrect types, duplicates  
2. **Feature Engineering:** Categorical encoding, numerical scaling  
3. **Model:** Linear Regression  
4. **Evaluation Metrics:** R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE)  
5. **Deployment:** Serialized model using Pickle and served with Flask

---
