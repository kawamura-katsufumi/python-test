from django.urls import path
from .views import index,upload,koshin


app_name="plac9"
urlpatterns = [
    path('index/', index, name="index"),
    path('upload/', upload, name="upload"),
    path('koshin/<int:pk>/', koshin, name="koshin"),
]