from pathlib import Path
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

app_name = 'users'
urlpatterns = [
    path('index/register', views.register, name= 'register'),
    path('index/login', authentication_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('index/logout', authentication_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout')
] 