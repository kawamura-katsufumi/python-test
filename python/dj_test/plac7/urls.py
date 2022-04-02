from django.urls import path
from .views import index,ajax_number,selenium_test

app_name="plac7"
urlpatterns = [
    path('index/', index, name="index"),
    path('ajax_number/', ajax_number ,name="ajax_number"),
    path('selenium_test/', selenium_test ,name="selenium_test"),
]