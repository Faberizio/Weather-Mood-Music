# apps/weather/admin.py
from django.contrib import admin
from .models import Weather

@admin.register(Weather)
class WeatherStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
