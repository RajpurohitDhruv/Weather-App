import streamlit as st
import requests
from datetime import datetime

# Set the title and layout of the app
st.set_page_config(page_title="Weather App", page_icon="🌦️", layout="wide")

# API Key for WeatherAPI
API_KEY = "08d46110d611489ba8f114450240712"  # Replace with your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json?"

# Function to get weather data
def get_weather(city):
    complete_url = f"{BASE_URL}key={API_KEY}&q={city}&aqi=no"
    response = requests.get(complete_url)
    data = response.json()

    if "error" not in data:
        current = data["current"]
        location = data["location"]
        return current, location
    else:
        return None, None

# Title and description
st.title("Weather Dashboard 🌦️")
st.markdown("""
    Enter a city to get the weather information. The app provides temperature, weather conditions, 
    humidity, wind speed, and more. Enjoy the weather forecast!
""")

# Input for city name
city = st.text_input("Enter City Name", "London")

# Fetch weather data when a city is entered
if city:
    current, location = get_weather(city)

    if current:
        st.subheader(f"Weather in **{city}** ({location['region']}, {location['country']})")

        # Show temperature, weather description, and icon
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(f"http:{current['condition']['icon']}", width=100)
        with col2:
            st.write(f"**Temperature:** {current['temp_c']}°C")
            st.write(f"**Weather:** {current['condition']['text'].capitalize()}")
            st.write(f"**Humidity:** {current['humidity']}%")
            st.write(f"**Wind Speed:** {current['wind_kph']} km/h")

        # Show additional data like feels like, pressure, and visibility
        st.write(f"**Feels Like:** {current['feelslike_c']}°C")
        st.write(f"**Pressure:** {current['pressure_mb']} hPa")
        st.write(f"**Visibility:** {current['vis_km']} km")

        # Show date and time of the weather update
        st.write(f"**Last Updated:** {current['last_updated']}")

    else:
        st.error("City not found. Please check the name and try again.")

# Customize theme
st.markdown("""
    <style>
        .css-1d391kg {
            background-color: #222222;
        }
        .css-1d391kg h1 {
            color: #fff;
        }
        .stButton>button {
            background-color: #FF6347;
            color: white;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)
