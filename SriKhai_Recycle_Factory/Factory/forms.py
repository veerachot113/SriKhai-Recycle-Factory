# Factory/forms.py
from Member.models import *
from django import forms
from .models import RecyclePurchase

class EditStatus(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['status','cancel']

        labels = {
            'status':'อนุมัติ',
            'cancel':'ไม่ผ่าน',
        }


