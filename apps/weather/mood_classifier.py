# weather_app/mood_classifier.py

from .mood_categories import MOOD_CATEGORIES

def classify_mood(weather_data):
    # Extract the main weather condition from the weather data
    condition = weather_data.get('weather')[0].get('main')

    # Look up the mood category for the condition in the MOOD_CATEGORIES dictionary
    mood = MOOD_CATEGORIES.get(condition, 'Neutral')

    return mood
