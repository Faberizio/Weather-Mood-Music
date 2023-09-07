# apps/mood/admin.py
from django.contrib import admin
from .models import Mood

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

