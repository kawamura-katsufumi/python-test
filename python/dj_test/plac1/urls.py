from django.urls import path
from .views import index

#接続用
urlpatterns = [
    path('', index,name="index"),
]
