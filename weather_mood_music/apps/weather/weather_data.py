# weather_app/weather_data.py

import requests
from django.conf import settings

def get_weather_data(location):
    api_key = settings.WEATHER_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',  # Use Celsius for temperature
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

