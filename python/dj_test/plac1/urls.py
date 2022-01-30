from django.urls import path
from .views import index

#接続用あああ
urlpatterns = [
    path('', index,name="index"),
]
