from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Music

def music_list(request):
    music = Music.objects.all()
    return render(request, 'resources/music_list.html', {'music': music})