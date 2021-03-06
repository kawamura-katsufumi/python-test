"""dj_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings # 追加
from django.conf.urls.static import static # 追加
from django.views.static import serve  #追加
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("plac1.urls")),
    path('plac2/',include("plac2.urls")),
    path('plac3/',include("plac3.urls")),
    path('plac4/',include("plac4.urls")),
    path('plac5/',include("plac5.urls")),
    path('plac6/',include("plac6.urls")),
    path('plac7/',include("plac7.urls")),
    path('plac8/',include("plac8.urls")),
    path('plac9/',include("plac9.urls")),
]

urlpatterns += static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
