import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("air_quality_model.pkl")

# Page Configuration
st.set_page_config(page_title="AQI Predictor", page_icon="🌍")

st.title("🌍 Air Quality Index (AQI) Predictor")
st.write("Enter the environmental details below to predict the AQI.")

# User Inputs
latitude = st.number_input("Latitude", value=28.6139)
longitude = st.number_input("Longitude", value=77.2090)
pollutant_min = st.number_input("Pollutant Minimum", value=10.0)
pollutant_max = st.number_input("Pollutant Maximum", value=50.0)
pollutant_avg = st.number_input("Pollutant Average", value=30.0)
temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.number_input("Humidity (%)", value=60.0)
wind_speed = st.number_input("Wind Speed (km/h)", value=12.0)

year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
day = st.number_input("Day", min_value=1, max_value=31, value=1)
hour = st.number_input("Hour", min_value=0, max_value=23, value=12)

# Prediction Button
if st.button("Predict AQI"):

    input_data = pd.DataFrame({
        "latitude":[latitude],
        "longitude":[longitude],
        "pollutant_min":[pollutant_min],
        "pollutant_max":[pollutant_max],
        "pollutant_avg":[pollutant_avg],
        "Temperature_C":[temperature],
        "Humidity_%":[humidity],
        "Wind_Speed_kmh":[wind_speed],
        "Year":[year],
        "Month":[month],
        "Day":[day],
        "Hour":[hour]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted AQI: {prediction[0]:.2f}")

    if prediction[0] <= 50:
        st.success("🟢 Air Quality: Good")
    elif prediction[0] <= 100:
        st.info("🟡 Air Quality: Moderate")
    elif prediction[0] <= 150:
        st.warning("🟠 Air Quality: Unhealthy for Sensitive Groups")
    elif prediction[0] <= 200:
        st.warning("🔴 Air Quality: Unhealthy")
    elif prediction[0] <= 300:
        st.error("🟣 Air Quality: Very Unhealthy")
    else:
        st.error("⚫ Air Quality: Hazardous")