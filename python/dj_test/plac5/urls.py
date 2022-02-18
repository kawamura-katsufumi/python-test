from django.urls import path
from .views import index,add,delete,send

urlpatterns = [
    path('index/', index, name="index"),
    path('add/<int:pk>', add, name="add"),
    path('delete/', delete, name="delete"),
    path('send/', send, name="send"),
]
