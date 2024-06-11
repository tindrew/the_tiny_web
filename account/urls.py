from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('discover/', views.discover, name='discover'),
    path('user-login/', views.user_login, name='user-login'),
    path('user-logout/', views.user_logout, name='user-logout'),
]