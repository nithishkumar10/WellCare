from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('user-dashboard/', views.user_dashboard, name="user-dashboard"),
    path('register/', views.register_user, name="register"),
    path('result', views.user_dashboard, name='result'),
    path('contact', views.contact_us, name="contact")
]