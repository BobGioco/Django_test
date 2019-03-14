from django.contrib import admin
from django.urls import path, include
from Project_app import views

#Template urls
app_name='Project_app'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
]
