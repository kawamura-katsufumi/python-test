from django.urls import path
from .views import omote,name,club,omote_test,delete

urlpatterns = [
    path('omote/',omote,name="omote"),
    path('omote/<int:num>/',omote,name="omote"),
    path('name/',name,name="name"),
    path('club/',club,name="club"),
    path('omote_test/',omote_test,name="omote_test"),
    path('delete/<int:pk>/',delete,name="delete"),
]
