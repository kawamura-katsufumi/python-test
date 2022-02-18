from django.urls import path
from .views import index,add,delete

urlpatterns = [
    path('index/', index, name="index"),
    path('add/<int:pk>', add, name="add"),
    path('delete/', delete, name="delete"),
]
