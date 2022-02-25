from django.urls import path
from .views import index,master

urlpatterns = [
    path('index/', index, name="index"),
    path('master/', master, name="master"),
]
