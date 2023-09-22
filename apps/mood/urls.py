# apps/mood/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mood/', views.mood_list, name='mood_list'),
]

# apps/resources/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.music_list, name='music_list'),
]
