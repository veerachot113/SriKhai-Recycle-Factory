from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home, name = 'home'),
    path('register/',register, name = 'register'),
    path('login/',sign_in, name = 'login'),
    path('logout/',logouts, name = 'logout'),


    
]