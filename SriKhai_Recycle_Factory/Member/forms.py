# Factory/forms.py

from django import forms
from .models import RecyclePurchase

class RecyclePurchaseForm(forms.ModelForm):
    class Meta:
        model = RecyclePurchase
        fields = ['image', 'address', 'map_pin', 'has_bottle', 'weight_has_bottle', 'has_can', 'weight_has_can', 'has_glass_bottle', 'weight_has_glass_bottle', 'has_paper', 'weight_has_paper', 'slip_image']  # เพิ่ม slip_image ที่นี่
        widgets = {
            'has_bottle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'weight_has_bottle': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_can': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'weight_has_can': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_glass_bottle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'weight_has_glass_bottle': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_paper': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'weight_has_paper': forms.NumberInput(attrs={'class': 'form-control'}),
            'slip_image': forms.FileInput(attrs={'class': 'form-control-file'}),  # เพิ่ม widget สำหรับ slip_image ที่นี่
           
        }

