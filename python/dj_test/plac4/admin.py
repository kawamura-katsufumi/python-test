from django.contrib import admin
from .models import Photo,Category
from django.contrib.admin import ModelAdmin

class CategoryAdmin(ModelAdmin):
    list_display=["id","title"]
    list_display_links=["id","title"]

class PhotoAdmin(ModelAdmin):
    list_display=["id","title"]
    list_display_links=["id","title"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Photo,PhotoAdmin)
