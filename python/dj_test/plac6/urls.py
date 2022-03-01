from django.urls import path
from .views import index,master,csv_import

urlpatterns = [
    path('index/', index, name="index"),
    path('master/', master, name="master"),
    path('csv_import/', csv_import, name="csv_import"),
]
