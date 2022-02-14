from django.urls import path
from .views import index,users_detail

urlpatterns = [
    path('index/',index,name="index"),
    path('users/<int:pk>/',users_detail,name="users_detail"),
]
