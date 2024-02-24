#Member/views.py
from django.shortcuts import render,redirect
from .models import*
from .forms import *

def identity(request):
    try:
        # ตรวจสอบว่าโปรไฟล์สำหรับผู้ใช้งานนั้นมีอยู่หรือไม่
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    # ตรวจสอบว่าผู้ใช้งานเป็น staff หรือไม่
    if request.user.is_staff:
        # หากเป็น staff ให้เรียกใช้หน้าหลักของร้านค้า
        return redirect('home')

    if request.method == 'POST':
        # ดำเนินการเฉพาะหากโปรไฟล์ยังไม่มีอยู่
        if not profile:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            address = request.POST.get('address')
            bank = request.POST.get('bank')
            bank_accounts = request.POST.get('bank_accounts')
            bank_number = request.POST.get('bank_number')
            pass_bookQR = request.FILES.get('pass_bookQR')

            profile = Profile.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                address=address,
                bank=bank,
                bank_accounts=bank_accounts,
                bank_number=bank_number,
                pass_bookQR=pass_bookQR
            )
        else:
            # หากโปรไฟล์มีอยู่แล้วให้อัปเดตข้อมูล
            profile.first_name = request.POST.get('first_name')
            profile.last_name = request.POST.get('last_name')
            profile.address = request.POST.get('address')
            profile.bank = request.POST.get('bank')
            profile.bank_accounts = request.POST.get('bank_accounts')
            profile.bank_number = request.POST.get('bank_number')
            profile.pass_bookQR = request.FILES.get('pass_bookQR')
            profile.save()

        return redirect('home_member')

    return render(request, 'member/identity.html', {'profile': profile})


def home(request):
    pf = Profile.objects.filter(user=request.user)
    return render(request,'member/member_home.html',{'pf':pf.first()})

def delete_pf(request):
    pf = Profile.objects.filter(user=request.user).delete()
    return redirect('identity')


def purchase_recycle(request):
    if request.method == 'POST':
        form = RecyclePurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # หรือไปยังหน้าอื่นที่ต้องการ
    else:
        form = RecyclePurchaseForm()
    return render(request, 'member/purchase_recycle.html', {'form': form})

def purchase_success(request):
    return render(request, 'member/purchase_success.html')
