#Member/models.py
from django.db import models
from django.contrib.auth.models import *
# Create your models hermodee.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.TextField()
    bank = models.CharField(max_length=150)
    bank_accounts = models.CharField(max_length=350)
    bank_number = models.CharField(max_length=20)
    pass_bookQR = models.ImageField(upload_to = 'ImagePassBook/')
    status = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)


# models.py

from django.db import models

from django.db import models

class RecyclePurchase(models.Model):
    image = models.ImageField(upload_to='recycle_images/')
    address = models.TextField(max_length=200)
    map_pin = models.CharField(max_length=100)
    has_bottle = models.BooleanField(default=False)
    has_bag = models.BooleanField(default=False)
    has_can = models.BooleanField(default=False)
    has_glass_bottle = models.BooleanField(default=False)
    has_paper = models.BooleanField(default=False)
    has_can = models.BooleanField(default=False)
    TYPES_CHOICES = [
        ('กำลังดำเนินการ', 'กำลังดำเนินการ'),
        ('กำลังเข้ารับ', 'กำลังเข้ารับ'),
        ('รับแล้ว', 'รับแล้ว'),
        ('ตรวจสอบขยะ', 'ตรวจสอบขยะ'),
        ('รอชำระเงิน', 'รอชำระเงิน'),
        ('เสร็จสิ้น', 'เสร็จสิ้น'),
        ('ยกเลิก', 'ยกเลิก'),

    ]
    status = models.CharField(max_length=200, choices=TYPES_CHOICES,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # เพิ่มฟิลด์สำหรับเก็บวันที่และเวลาที่สร้างข้อมูล
    id = models.AutoField(primary_key=True)  # เพิ่มฟิลด์สำหรับเก็บลำดับที่

    def __str__(self):
        return f'Recycle Purchase: {self.address}'

