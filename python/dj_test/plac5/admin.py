from django.contrib import admin
from .models import Session,Send,Sample,Shozoku
from django.contrib.admin import ModelAdmin

class All(ModelAdmin):
    list_display = ["hinban","hinmei","color","size"]

class All2(ModelAdmin):
    list_display = ["id","sample_number","busho","name","send_name","send_tel"]

class All3(ModelAdmin):
    list_display = ["id","sample_number","hinban","hinmei","color","size"]

class All4(ModelAdmin):
    list_display = ["name","busho"]

admin.site.register(Session,All)
admin.site.register(Send,All2)
admin.site.register(Sample,All3)
admin.site.register(Shozoku,All4)
