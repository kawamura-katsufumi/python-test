from django.urls import path
from .views import list,detail,create,delete

urlpatterns = [
    path('list/',list,name="list"),
    path('detail/<int:pk>/',detail,name="detail"),
    path('create/',create,name="create"),
    path('delete/<int:pk>/',delete,name="delete"),
]
