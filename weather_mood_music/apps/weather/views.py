# weather_app/views.py

from django.shortcuts import render
from .weather_data import get_weather_data

def weather_view(request):
    # Fetch weather data using the get_weather_data function
    weather_data = get_weather_data('New York')  # Replace 'New York' with the user's location

    return render(request, 'weather_app/weather.html', {'weather_data': weather_data})


# weather_app/views.py

from django.shortcuts import render
from .mood_classifier import classify_mood

def mood_view(request):
    # Fetch weather data using the get_weather_data function
    weather_data = get_weather_data('New York')  # Replace 'New York' with the user's location

    # Classify the mood based on weather conditions
    mood = classify_mood(weather_data)

    return render(request, 'weather_app/mood.html', {'mood': mood})
