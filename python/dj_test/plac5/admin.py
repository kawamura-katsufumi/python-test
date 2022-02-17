from django.contrib import admin
from .models import Session
from django.contrib.admin import ModelAdmin

class All(ModelAdmin):
    list_display = ["hinban","hinmei","color","size"]

admin.site.register(Session,All)
