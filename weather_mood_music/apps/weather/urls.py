# weather_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_view, name='weather'),
    path('mood/', views.mood_view, name='mood'),
    path('weather-status/', views.weather_status_list, name='weather_status_list'),
]
