from django.urls import path
from .views import index,add,delete,send,send_delete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', index, name="index"),
    path('add/<int:pk>', add, name="add"),
    path('delete/', delete, name="delete"),
    path('send/', send, name="send"),
    path('send_delete/<int:pk>/', send_delete, name="send_delete"),
    path('login/',auth_views.LoginView.as_view(template_name="plac5/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
]
