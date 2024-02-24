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
    types = models.CharField(max_length=20, choices=TYPES_CHOICES)

    def __str__(self):
        return f"Recycle Purchase - {self.types}"
