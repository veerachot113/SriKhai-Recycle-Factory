#Factory/urls.py
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',cfidentity,name='cfidentity'),
    path('editestate/<int:id>/',editestate,name='editestate')
]