from django.urls import path
from .views import index,top,left,right,upload,right1


app_name="plac8"
urlpatterns = [
    path('index/', index, name="index"),
    path('top/', top, name="top"),
    path('left/', left, name="left"),
    path('right/', right, name="right"),
    path('right/<int:pk>/', right1, name="right1"),
    path('upload/', upload, name="upload"),
]