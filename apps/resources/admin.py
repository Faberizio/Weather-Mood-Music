from django.contrib import admin
'''from apps.resources import models

admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.Review)
'''

# Register your models here.
# apps/resources/admin.py
from django.contrib import admin
from .models import Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
    search_fields = ('title', 'artist')