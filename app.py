import streamlit as st
import requests
from datetime import datetime

# Title of the app
st.title('Taxi Fare Prediction')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# Input parameters
st.header('Select the ride parameters')

# Date and Time input
date = st.date_input("Select date of the ride", datetime.now())
time = st.time_input("Select time of the ride", datetime.now().time())

# Pickup and Dropoff location input
pickup_longitude = st.number_input('Pickup Longitude', value=-73.985428, format="%.6f")
pickup_latitude = st.number_input('Pickup Latitude', value=40.748817, format="%.6f")
dropoff_longitude = st.number_input('Dropoff Longitude', value=-73.985428, format="%.6f")
dropoff_latitude = st.number_input('Dropoff Latitude', value=40.748817, format="%.6f")

# Passenger count input
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, value=1)

# Combine date and time into a single datetime string
pickup_datetime = f"{date} {time}"

# Call API
url = 'https://taxifare.lewagon.ai/predict'

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
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()['fare']
        st.write(f"Predicted Fare: ${prediction:.2f}")
    else:
        st.write("Error in API request. Please try again.")
