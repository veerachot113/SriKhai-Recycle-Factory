#Member/models.py
from django.db import models
from django.contrib.auth.models import *
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.TextField()
    bank = models.CharField(max_length=150)
    bank_accounts = models.CharField(max_length=350)
    bank_number = models.CharField(max_length=20)
    pass_bookQR = models.ImageField(upload_to='ImagePassBook/')
    status = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

class RecyclePurchase(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='recycle_images/')
    address = models.TextField()
    map_pin = models.CharField(max_length=100)
    has_bottle = models.BooleanField(default=False)
    has_bag = models.BooleanField(default=False)
    has_can = models.BooleanField(default=False)
    has_glass_bottle = models.BooleanField(default=False)
    has_paper = models.BooleanField(default=False)
    weight_has_bottle = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_has_bag = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_has_can = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_has_glass_bottle = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_has_paper = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    TYPES_CHOICES = [
        ('กำลังดำเนินการ', 'กำลังดำเนินการ'),
        ('กำลังเข้ารับ', 'กำลังเข้ารับ'),
        ('รับแล้ว', 'รับแล้ว'),
        ('ตรวจสอบขยะ', 'ตรวจสอบขยะ'),
        ('รอชำระเงิน', 'รอชำระเงิน'),
        ('เสร็จสิ้น', 'เสร็จสิ้น'),
        ('ยกเลิก', 'ยกเลิก'),
    ]
    status = models.CharField(max_length=200, choices=TYPES_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Recycle Purchase: {self.address}'