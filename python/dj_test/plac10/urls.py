from django.urls import path
from .views import index

urlpatterns = [
    path('index/',index,name="index"),
    path('auth/', auth, name='zoom_auth'),
    path('auth/complete', index, name='zoom_auth_complete'),
]
