"""
URL configuration for BGWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

import main.views
import user.views

urlpatterns = [
    path("api/user/register", user.views.user_register),
    path("api/user/login", user.views.user_login),
    path("api/user/current", user.views.current_user),
    path("api/postBasicInfo", main.views.post_basic_info),
    path("api/postDetails", main.views.post_detail),
    path("api/postPhoto", main.views.post_photo),
    path("api/postVideo", main.views.post_video),
    path("api/postOver", main.views.post_over),
    path("api/getBasicInfo", main.views.get_basic_info),
    path("api/user/getMyInfo", main.views.get_my_info),
    path("api/user/GetImage", main.views.get_file),
    path('admin/', admin.site.urls),
]
