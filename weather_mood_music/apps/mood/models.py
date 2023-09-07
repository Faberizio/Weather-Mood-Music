from django.db import models

class Mood(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='mood_icons/')
    description = models.TextField()

    def __str__(self):
        return self.name
