from django.db import models

# Create your models hermodee.
class Profile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.TextField()
    bank = models.CharField(max_length=150)
    bank_accounts = models.CharField(max_length=350)
    bank_number = models.CharField(max_length=20)
    pass_bookQR = models.ImageField(upload_to = 'ImagePassBook/')
    status = models.BooleanField(default=False)

