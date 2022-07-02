from django.urls import path
from .views import index,upload


app_name="plac9"
urlpatterns = [
    path('index/', index, name="index"),
    path('upload/', upload, name="upload"),
]