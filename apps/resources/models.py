from django.db import models
from apps.mood.models import Mood

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    music_link = models.URLField()

    def __str__(self):
        return self.title

class MoodMusicAssociation(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mood} - {self.music}"