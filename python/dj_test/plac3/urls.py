from django.urls import path
from .views import omote,name,club

urlpatterns = [
    path('omote/',omote,name="omote"),
    path('omote/<int:num>/',omote,name="omote"),
    path('name/',name,name="name"),
    path('club/',club,name="club"),
]
