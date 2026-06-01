# Time Series Sales Forecasting

## Project Overview

This project focuses on forecasting future sales using historical sales data and Machine Learning techniques. The objective is to analyze sales trends, create time-based features, and predict future sales values using a Random Forest Regressor.

The project demonstrates the complete Time Series Forecasting workflow, including data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit.

---

## Dataset

The project uses the Superstore Sales Dataset containing:

* Order Date
* Customer Information
* Product Information
* Sales

The sales data was aggregated into daily sales records for forecasting purposes.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

## Project Workflow

### 1. Data Preprocessing

* Loaded sales dataset
* Converted Order Date to datetime format
* Set Order Date as index
* Aggregated sales by day

### 2. Exploratory Data Analysis

* Daily Sales Analysis
* Monthly Sales Analysis
* Yearly Sales Analysis
* Trend Visualization

### 3. Feature Engineering

Created lag features:

* Lag_1 (Previous Day Sales)
* Lag_7 (Previous Week Sales)
* Lag_30 (Previous Month Sales)

Created date features:

* Day
* Month
* Year
* DayOfWeek

### 4. Model Training

Model Used:

* Random Forest Regressor

### 5. Hyperparameter Tuning

Best Parameters:

```python
{
    'max_depth': 5,
    'min_samples_split': 5,
    'n_estimators': 100
}
```

### 6. Model Evaluation

Before Tuning:

* MAE: 1608.24
* RMSE: 2404.54

After Tuning:

* MAE: 1587.33
* RMSE: 2415.36

### 7. Feature Importance

Top Features:

1. Lag_7
2. Lag_1
3. Lag_30
4. Month
5. Day

This indicates that historical sales patterns are the most important factors in forecasting future sales.

---

## Project Structure

```text
TimeSeries_sales_forecasting/
│
├── Data/
├── Notebook/
│   └── sales_forecasting.ipynb
│
├── Screenshots/
│
├── sales_forecasting_model.pkl
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## Streamlit Application

The Streamlit application allows users to:

* Enter lag feature values
* Enter date-related features
* Predict future sales instantly

Run locally using:

```bash
streamlit run app.py
```

---

## Results

The forecasting model successfully captures historical sales patterns and demonstrates how lag-based feature engineering can be used for time series forecasting.

---

## Author

**Aravindh Nuka**
