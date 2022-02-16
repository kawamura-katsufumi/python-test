from django.urls import path
from .views import index,users_detail,signup,photos_new,photos_detail,photos_delete,photos_category
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/',index,name="index"),
    path('users/<int:pk>/',users_detail,name="users_detail"),
    path('login/',auth_views.LoginView.as_view(template_name="plac4/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',signup,name="signup"),
    path('photos_new/',photos_new,name="photos_new"),
    path('photos/<int:pk>/',photos_detail,name="photos_detail"),
    path('photos/<int:pk>/delete/',photos_delete,name="photos_delete"),
    path('photos/<str:category>/',photos_category,name="photos_category"),
]
