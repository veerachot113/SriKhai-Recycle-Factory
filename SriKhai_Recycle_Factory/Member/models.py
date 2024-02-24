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

# Factory/models.py
from django.db import models

class RecyclePurchase(models.Model):
    TYPES_CHOICES = [
        ('Bottle', 'ขวด'),
        ('Bag', 'ถุง'),
        ('Crate', 'ลัง'),
        ('Glass bottle', 'ขวดแก้ว'),
        ('Paper', 'กระดาษ'),
        ('Can', 'กระป๋อง'),
    ]
    
    image = models.ImageField(upload_to='recycle_purchase_images/')
    address = models.TextField()
    location_pin = models.CharField(max_length=100)
    types = models.ManyToManyField('GarbageType', related_name='recycle_purchases')

    def __str__(self):
        return f"Recycle Purchase - {self.types}"

class GarbageType(models.Model):
    name = models.CharField(max_length=20, choices=RecyclePurchase.TYPES_CHOICES)

    def __str__(self):
        return self.name
