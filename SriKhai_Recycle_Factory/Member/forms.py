# Factory/forms.py
from Member.models import *
from django import forms
from .models import RecyclePurchase

class RecyclePurchaseForm(forms.ModelForm):
    class Meta:
        model = RecyclePurchase
        fields = ['image', 'address', 'location_pin', 'types']
