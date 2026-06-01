import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("sales_forecasting_model.pkl")

# Title
st.title("📈 Time Series Sales Forecasting")
st.write("Predict Future Sales using Random Forest Model")

st.header("Enter Input Features")

# Inputs
lag_1 = st.number_input("Lag_1 (Yesterday Sales)", min_value=0.0, value=1000.0)

lag_7 = st.number_input("Lag_7 (Sales 7 Days Ago)", min_value=0.0, value=1200.0)

lag_30 = st.number_input("Lag_30 (Sales 30 Days Ago)", min_value=0.0, value=1500.0)

day = st.slider("Day", 1, 31, 15)

month = st.slider("Month", 1, 12, 6)

year = st.number_input("Year", min_value=2015, max_value=2035, value=2019)

dayofweek = st.slider(
    "Day Of Week (Monday=0, Sunday=6)",
    0,
    6,
    0
)

# Prediction Button
if st.button("Predict Sales"):

    input_data = pd.DataFrame({
        "Lag_1": [lag_1],
        "Lag_7": [lag_7],
        "Lag_30": [lag_30],
        "Day": [day],
        "Month": [month],
        "Year": [year],
        "DayOfWeek": [dayofweek]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Sales: {prediction[0]:.2f}"
    )

    st.balloons()