"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include

from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),
    path('profile/<str:username>', user_view.profile, name='profile'),
    path('', include("my_blog.urls")),
    path('tinymce/', include('tinymce.urls')),
    
]
