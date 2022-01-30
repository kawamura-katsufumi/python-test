from django.urls import path
from .views import index

#接続用あああいいい５５５
urlpatterns = [
    path('', index,name="index"),
]
