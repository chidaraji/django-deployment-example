from django.contrib import admin
from django.urls import path
from appFive import views

#Template URLS!
app_name = 'appFive'

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.user_login,name='user_login'),
]