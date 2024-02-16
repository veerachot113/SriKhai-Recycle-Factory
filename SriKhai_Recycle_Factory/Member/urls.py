from django.contrib import admin
from django.urls import path,include
from .views import*
urlpatterns = [
    path('identity/',identity,name='identity'),
    path('home/',home,name='home_member'),
    path('delete_pf/',delete_pf,name='delete_pf'),
    
]