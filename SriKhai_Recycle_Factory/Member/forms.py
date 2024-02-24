# Factory/forms.py
# forms.py

from django import forms
from .models import RecyclePurchase

class RecyclePurchaseForm(forms.ModelForm):
    class Meta:
        model = RecyclePurchase
        fields = ['image', 'address', 'map_pin', 'has_bottle', 'has_bag', 'has_can', 'has_glass_bottle', 'has_paper', 'has_can']
        widgets = {
            'has_bottle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_bag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_can': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_glass_bottle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_paper': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_can': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
