# 🏭 Factory Reallocation & Shipping Optimization

### Interactive Recommendation & Analytics Dashboard

A data-driven dashboard designed to analyze factory performance and recommend suitable factory allocations based on shipping performance, lead time, expected profit, risk level, and other operational factors.

---

## 📌 Problem Statement

Static factory assignments can result in inefficient shipping distances, higher lead times, increased operational costs, and reduced profit margins.

This project analyzes order and factory data to identify better factory allocation opportunities and support data-driven decision making.

---

## 🎯 Objective

The main objectives of this project are:

- Analyze factory and order performance
- Identify inefficient factory allocations
- Compare current and suggested factory assignments
- Analyze shipping speed and lead time
- Estimate expected profit
- Identify orders recommended for reallocation
- Provide an interactive dashboard for business insights

---

## 📊 Dataset

The project uses an order-level dataset containing information related to:

- Factory
- Product
- Region
- Division
- Sales
- Units
- Gross Profit
- Lead Time
- Shipping Speed
- Recommendation Status
- Risk Level
- Suggested Factory
- Expected Profit
- Predicted Lead Time

The dataset was cleaned and transformed before analysis and modeling.

---

## ⚙️ Methodology

The project follows these major steps:

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Exploratory Data Analysis (EDA)
5. Machine Learning
6. Factory Recommendation
7. Expected Profit Analysis
8. Interactive Dashboard Development

---

## 🤖 Machine Learning Models

Multiple machine learning models were evaluated for predicting lead time:

- Linear Regression
- Random Forest
- Gradient Boosting

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 181.06 | 181.97 | 0.535 |
| Random Forest | 180.97 | 184.19 | 0.524 |
| Gradient Boosting | 181.00 | 182.60 | 0.532 |

---

## 🎯 Recommendation System

The recommendation system evaluates factory allocation and classifies orders into:

- **Keep Current Factory**
- **Reallocate**

The recommendation considers factors such as:

- Lead Time
- Expected Profit
- Shipping Performance
- Risk Level
- Factory suitability

The system identified opportunities where reallocating an order could potentially improve operational performance.

---

## 📈 Dashboard Features

The Streamlit dashboard provides:

- KPI cards
- Sales by Factory
- Gross Profit by Factory
- Sales by Region
- Sales by Division
- Orders by Factory
- Units Sold by Factory
- Recommendation Status
- Risk Level Distribution
- Lead Time Analysis
- Shipping Speed Analysis
- Monthly Sales Trend
- Suggested Factory Analysis
- Current vs Suggested Factory comparison
- Expected Profit by Suggested Factory
- Predicted Lead Time Analysis
- Interactive filters
- Filtered dataset view

---

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- Scikit-learn
- Microsoft Excel
- Machine Learning

---

## 📊 Key Results

The analysis produced the following key outcomes:

- **8,549 orders** analyzed
- **4,608 orders** identified for reallocation
- **3,941 orders** recommended to keep at the current factory
- Multiple factory allocation opportunities identified through the recommendation system
- Interactive dashboard developed for analyzing operational and financial performance

---

## ▶️ How to Run the Dashboard

### 1. Install the required libraries

```bash
pip install streamlit pandas plotly scikit-learn openpyxl
### 2. Keep the project files in the same folder

Factory-Reallocation-Shipping-Optimization/
│
├── app.py
├── Final_Dataset.xlsx
└── README.md

### 3. Run the Streamlit application

```bash
python -m streamlit run app.py
