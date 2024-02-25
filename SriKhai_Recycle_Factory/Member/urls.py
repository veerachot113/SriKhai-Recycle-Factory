#Member/urls.py
from django.urls import path,include
from .views import*
from django.urls import path
from . import views

urlpatterns = [
    path('identity/',identity,name='identity'),
    path('home/',home,name='home_member'),
    path('delete_pf/',delete_pf,name='delete_pf'),
    path('recycle_purchase/', recycle_purchase, name='recycle_purchase'),
    # path('recycle-list/', recycle_list, name='recycle_list'),
    path('list_order/', list_order, name='list_order'),
    
     path('purchase/<int:purchase_id>/', detail_purchase, name='detail_purchase'),
    # เพิ่ม URL pattern สำหรับหน้ารายละเอียดการจอง
    # ในกรณีที่มีการอัปเดตสถานะของการจองโดยแอดมิน
  

    
    
    
]