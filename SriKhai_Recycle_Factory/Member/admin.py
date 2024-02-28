#Member/admin.py
from django.contrib import admin

from .models import *
admin.site.register(Profile)
admin.site.register(RecyclePurchase)


