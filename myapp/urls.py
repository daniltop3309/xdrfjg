"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

posts_pattern = [
    path('populars/', views.pop_posts),
    path('lasts/', views.las_posts),
    path('all/', views.all_posts),
    path('<int:post>/likes', views.get_likes),
    path('<int:post>/comments', views.get_comments),
]

redirect_pattern = [
    path('temp/', views.temp_redirect),
    path('const/', views.const_redirect),
]

cookie_pattern = [
    path('set/<str:key>/<str:value>/', views.set_cook),
    path('get/<str:key>/', views.get_cook)
]

urlpatterns = [
    path('posts/', include(posts_pattern)),
    path('redirect/', include(redirect_pattern)),
    path('cookie/', include(cookie_pattern)),
    path('login/<str:login>/<str:password>/', views.get_login),
    path('access/<str:login>/<str:password>/', views.get_access),
    path('json/', views.req_json),
    path('404/', views.not_found)
]
