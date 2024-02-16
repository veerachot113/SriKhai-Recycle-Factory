from django.shortcuts import render,redirect
from .models import*

def identity(request):

    pf = Profile.objects.filter(user=request.user)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        bank = request.POST.get('bank')
        bank_accounts = request.POST.get('bank_accounts')
        bank_number = request.POST.get('bank_number')
        pass_bookQR = request.FILES.get('pass_bookQR')

        profile = Profile.objects.create(
        user=request.user,  # ใส่ค่าที่เหมาะสมสำหรับ user ในกรณีที่มีการใช้ OneToOneField หรือแก้ไขตามที่ต้องการ
        first_name=first_name,
        last_name=last_name,
        address=address,
        bank=bank,
        bank_accounts=bank_accounts,
        bank_number=bank_number,
        pass_bookQR=pass_bookQR,  # ต้องใส่ที่อยู่ที่เหมาะสมของรูปภาพที่อัปโหลด

        )
        profile.save()

        return redirect('home_member')


    return render(request,'member/identity.html',{'profile':pf})


def home(request):
    pf = Profile.objects.filter(user=request.user)
    return render(request,'member/member_home.html',{'pf':pf.first()})

def delete_pf(request):
    pf = Profile.objects.filter(user=request.user).delete()
    return redirect('identity')