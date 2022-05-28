from django.urls import path
from .views import index,top,left,right


app_name="plac8"
urlpatterns = [
    path('index/', index, name="index"),
    path('top/', top, name="top"),
    path('left/', left, name="left"),
    path('right/', right, name="right"),
]