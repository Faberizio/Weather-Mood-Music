from django.shortcuts import render
from .models import Mood

def mood_list(request):
    moods = Mood.objects.all()
    return render(request, 'mood/mood_list.html', {'moods': moods})