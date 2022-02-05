from django.urls import path
from .views import list,detail

urlpatterns = [
    path('list/',list,name="list"),
    path('detail/<int:pk>/',detail,name="detail"),
]
