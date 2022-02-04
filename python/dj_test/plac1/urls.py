from django.urls import path
from .views import index,about,moto

urlpatterns = [
    path('',moto,name="moto"),
    path('plac1/index/', index,name="index"),
    path('plac1/about/', about,name="about"),
]
