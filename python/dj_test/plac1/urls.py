from django.urls import path
from .views import index

#接続用あああいいい
urlpatterns = [
    path('', index,name="index"),
]
