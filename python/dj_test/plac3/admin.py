from django.contrib import admin
from .models import Omote,Ura
from django.contrib.admin import ModelAdmin

class A(ModelAdmin):
    list_display=["club","name2"]
    list_display_links=["name2"]

admin.site.register(Omote)
admin.site.register(Ura,A)
