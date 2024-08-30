import streamlit as st
import requests
from datetime import datetime

# Center-aligned style for headers and titles
header_style = """
<style>
.centered-header {
    text-align: center;
}
.centered-header-orange {
    text-align: center;
    color: orange;
}
.stButton>button {
    width: 100%;
    font-size: 20px;
    background-color: orange;
    color: white;
}
</style>
"""
st.markdown(header_style, unsafe_allow_html=True)

# Title of the app (centered)
st.markdown('<h1 class="centered-header">Taxi Fare Prediction</h1>', unsafe_allow_html=True)

st.markdown('''
This Taxi Fare Prediction app, built as part of a data science bootcamp, uses a machine
learning model we developed to estimate taxi fares in New York City. Enter ride details to get an instant fare prediction!
''')

# Section for Date and Time input
st.markdown('<h3 class="centered-header">Ride Date and Time</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    date = st.date_input("Date", datetime.now())
with col2:
    time = st.time_input("Time", datetime.now().time(), key="time_wheel")

pickup_datetime = f"{date} {time}"

# Section for Pickup Location
st.markdown('<h3 class="centered-header">Pickup Location</h3>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    pickup_longitude = st.number_input('Longitude', value=-73.985428, format="%.6f", key='pickup_longitude')
with col4:
    pickup_latitude = st.number_input('Latitude', value=40.748817, format="%.6f", key='pickup_latitude')

# Section for Dropoff Location
st.markdown('<h3 class="centered-header">Dropoff Location</h3>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    dropoff_longitude = st.number_input('Longitude', value=-73.985428, format="%.6f", key='dropoff_longitude')
with col6:
    dropoff_latitude = st.number_input('Latitude', value=40.748817, format="%.6f", key='dropoff_latitude')

# Section for Passenger Count
st.markdown('<h3 class="centered-header">Number of Passengers</h3>', unsafe_allow_html=True)
passenger_count = st.number_input('Passengers', min_value=1, max_value=8, value=1)

# Centered and styled 'Get Fare Prediction' button
if st.markdown('<div style="text-align: center;">', unsafe_allow_html=True):
    if st.button('Get Fare Prediction'):
        params = {
            'pickup_datetime': pickup_datetime,
            'pickup_longitude': pickup_longitude,
            'pickup_latitude': pickup_latitude,
            'dropoff_longitude': dropoff_longitude,
            'dropoff_latitude': dropoff_latitude,
            'passenger_count': passenger_count
        }

        # Make API request
        url = 'https://taxifare.lewagon.ai/predict'
        response = requests.get(url, params=params)
        if response.status_code == 200:
            prediction = response.json()['fare']
            st.markdown('<h3 class="centered-header">Prediction Fare:</h3>', unsafe_allow_html=True)
            st.markdown(f'<h1 class="centered-header-orange">${prediction:.2f}</h1>', unsafe_allow_html=True)
            # st.write(f"Predicted Fare: ${prediction:.2f}")
        else:
            st.write("Error in API request. Please try again.")
    st.markdown('</div>', unsafe_allow_html=True)
