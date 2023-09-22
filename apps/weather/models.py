from django.db import models
from mood.models import Mood
from weather.models import Weather

class Weather(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='weather_icons/')
    description = models.TextField()

    def __str__(self):
        return self.name

class MoodWeatherAssociation(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mood} - {self.weather}"