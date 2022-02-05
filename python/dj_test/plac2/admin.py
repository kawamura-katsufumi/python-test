from django.contrib import admin
from .models import Test
from django.contrib.admin import ModelAdmin

class All(ModelAdmin):
    list_display=["id","hinban","zaiko","koshin"]
    list_display_links=["id","hinban"]

admin.site.register(Test,All)
