from django.urls import path
from .views import index,ajax_number


app_name="plac7"
urlpatterns = [
    path('index/', index, name="index"),
    path('ajax_number/', ajax_number ,name="ajax_number"),
]