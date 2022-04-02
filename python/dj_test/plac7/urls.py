from django.urls import path
from .views import index,ajax_number
from .tests import LoginTest

app_name="plac7"
urlpatterns = [
    path('index/', index, name="index"),
    path('ajax_number/', ajax_number ,name="ajax_number"),
    path('LoginTest/', LoginTest,name="ajax_number"),
]