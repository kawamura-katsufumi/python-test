from django.urls import path
from .views import index,upload,koshin,delete,hyouji_all,hyouji_inoue,hyouji_furukawa,hyouji_mashimo


app_name="plac9"
urlpatterns = [
    path('index/', index, name="index"),
    path('upload/', upload, name="upload"),
    path('koshin/<int:pk>/', koshin, name="koshin"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('hyouji_all/', hyouji_all, name="hyouji_all"),
    path('hyouji_inoue/', hyouji_inoue, name="hyouji_inoue"),
    path('hyouji_furukawa/', hyouji_furukawa, name="hyouji_furukawa"),
    path('hyouji_mashimo/', hyouji_mashimo, name="hyouji_mashimo"),
]