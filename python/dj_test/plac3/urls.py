from django.urls import path
from .views import omote

urlpatterns = [
    path('omote/',omote,name="omote"),
    path('omote/<int:num>/',omote,name="omote"),
]
