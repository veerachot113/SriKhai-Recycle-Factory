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
    path('add_weight/<int:order_id>/', add_weight, name='add_weight'),
    path('order/<int:order_id>/upload_slip/', views.upload_slip, name='upload_slip'),
    path('slip/<int:order_id>/', slip_detail, name='slip_detail'),
      




    
    # เพิ่ม URL pattern สำหรับแสดงหน้ารายละเอียดของออเดอร์
    # เพิ่ม URL pattern สำหรับแสดงรายการออเดอร์ทั้งหมด
    
]