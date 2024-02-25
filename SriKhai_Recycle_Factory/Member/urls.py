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
    path('list_order/', list_order, name='list_order'), 
    path('order/<int:order_id>/',order_detail, name='order_detail'),
    path('order/<int:order_id>/update_status/', update_order_status, name='update_order_status'),
    
    # เพิ่ม URL pattern สำหรับแสดงหน้ารายละเอียดของออเดอร์
    # เพิ่ม URL pattern สำหรับแสดงรายการออเดอร์ทั้งหมด
    
    
]