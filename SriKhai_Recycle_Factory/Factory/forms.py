from Member.models import *
from django import forms

class EditStatus(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['status','cancel']

        labels = {
            'status':'อนุมัติ',
            'cancel':'ไม่ผ่าน',
        }
