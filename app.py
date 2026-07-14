import streamlit as st
import joblib
import numpy as np
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AQI Predictor",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("air_quality_model.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("👩‍💻 Developer")

st.sidebar.write("**Sukhjeevan Kaur**")
st.sidebar.write("B.Tech AIML Student")

st.sidebar.markdown("---")

st.sidebar.subheader("🤖 Model")
st.sidebar.write("Linear Regression")

st.sidebar.subheader("🛠 Technologies")
st.sidebar.write("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
""")

st.sidebar.markdown("---")
st.sidebar.info(
    "This application predicts the Air Quality Index (AQI) "
    "using a Machine Learning model."
)

# -----------------------------
# Main Heading
# -----------------------------
st.title("🌍 Air Quality Index (AQI) Predictor")

st.markdown("""
Predict the **Air Quality Index (AQI)** using environmental
and pollutant parameters.

Fill in the values below and click **Predict AQI**.
""")

st.divider()
col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input("Latitude", value=28.58)
    longitude = st.number_input("Longitude", value=77.19)
    temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0)
    humidity = st.slider("Humidity (%)", 0, 100, 60)
    wind_speed = st.slider("Wind Speed (km/h)", 0.0, 100.0, 15.0)

with col2:
    pollutant_min = st.number_input("Pollutant Minimum", value=10.01)
    pollutant_max = st.number_input("Pollutant Maximum", value=50.02)
    pollutant_avg = st.number_input("Pollutant Average", value=29.99)
    year = st.selectbox("Year", [2022, 2023, 2024, 2025])
    month = st.selectbox("Month", list(range(1,13)))
    day = st.slider("Day",1,31,1)
    hour = st.slider("Hour",0,23,12)
    import pandas as pd

st.markdown("---")

if st.button("🔍 Predict AQI", use_container_width=True):

    input_data = pd.DataFrame({
        "latitude": [latitude],
        "longitude": [longitude],
        "pollutant_min": [pollutant_min],
        "pollutant_max": [pollutant_max],
        "pollutant_avg": [pollutant_avg],
        "Temperature_C": [temperature],
        "Humidity_%": [humidity],
        "Wind_Speed_kmh": [wind_speed],
        "Year": [year],
        "Month": [month],
        "Day": [day],
        "Hour": [hour]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("✅ Prediction Result")

    st.metric(
        label="Predicted AQI",
        value=f"{prediction:.2f}"
    )

    if prediction <= 50:
        st.success("🟢 Air Quality: Good")
    elif prediction <= 100:
        st.info("🟡 Air Quality: Moderate")
    elif prediction <= 150:
        st.warning("🟠 Air Quality: Unhealthy for Sensitive Groups")
    elif prediction <= 200:
        st.error("🔴 Air Quality: Unhealthy")
    elif prediction <= 300:
        st.error("🟣 Air Quality: Very Unhealthy")
    else:
        st.error("⚫ Air Quality: Hazardous")

    with st.expander("📋 View Input Summary"):
        st.write(f"Latitude: {latitude}")
        st.write(f"Longitude: {longitude}")
        st.write(f"Pollutant Minimum: {pollutant_min}")
        st.write(f"Pollutant Maximum: {pollutant_max}")
        st.write(f"Pollutant Average: {pollutant_avg}")
        st.write(f"Temperature: {temperature} °C")
        st.write(f"Humidity: {humidity} %")
        st.write(f"Wind Speed: {wind_speed} km/h")
        st.write(f"Date: {day}/{month}/{year}")
        st.write(f"Hour: {hour}:00")

st.markdown("---")
st.caption("👩‍💻 Developed by Sukhjeevan Kaur | B.Tech AIML Student")