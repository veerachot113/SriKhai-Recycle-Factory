#Member/urls.py
from django.urls import path,include
from .views import*
urlpatterns = [
    path('identity/',identity,name='identity'),
    path('home/',home,name='home_member'),
    path('delete_pf/',delete_pf,name='delete_pf'),
    path('purchase/', purchase_recycle, name='purchase_recycle'),
    path('purchase/success/', purchase_success, name='purchase_success'),
    
]