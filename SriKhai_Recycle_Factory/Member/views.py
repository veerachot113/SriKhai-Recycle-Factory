#Member/views.py
from audioop import reverse
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import*
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required
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
            phone = request.FILES.get('phone')


            profile = Profile.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                address=address,
                bank=bank,
                bank_accounts=bank_accounts,
                bank_number=bank_number,
                pass_bookQR=pass_bookQR,
                phone=phone,
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
            profile.phone = request.FILES.get('phone')
            profile.save()

        return redirect('home_member')

    return render(request, 'member/identity.html', {'profile': profile})


def home(request):
    pf = Profile.objects.filter(user=request.user)
    return render(request,'member/member_home.html',{'pf':pf.first()})
@login_required
def delete_pf(request):
    pf = Profile.objects.filter(user=request.user).delete()
    return redirect('identity')

@login_required
def recycle_purchase(request):
    if request.method == 'POST':
        form = RecyclePurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            # ดึงข้อมูลโปรไฟล์ของผู้ใช้งานปัจจุบัน
            profile = Profile.objects.get(user=request.user)
            # บันทึกข้อมูลการรับรถโดยเชื่อมโยงกับโปรไฟล์
            form.instance.profile = profile
            form.save()
            return redirect('home')  # หรือไปยัง URL ที่คุณต้องการหลังจากบันทึกข้อมูลแล้ว
    else:
        form = RecyclePurchaseForm()
    
    return render(request, 'member/recycle_purchase.html', {'form': form})



@login_required
def list_order(request):
    # ตรวจสอบว่าผู้ใช้เป็น superuser หรือไม่
    if request.user.is_superuser:
        # ถ้าเป็น superuser ให้ดึงรายการรับรถทั้งหมด
        list_orders = RecyclePurchase.objects.all()
    else:
        # ถ้าไม่ใช่ superuser ให้ดึงรายการรับรถของผู้ใช้นั้นๆ เท่านั้น
        list_orders = RecyclePurchase.objects.filter(profile__user=request.user)

    return render(request, 'list_order.html', {'list_orders': list_orders})
    
def order_detail(request, order_id):
    # ดึงข้อมูลออเดอร์จากฐานข้อมูล
    order = get_object_or_404(RecyclePurchase, pk=order_id)
    return render(request, 'detail_purchase.html', {'order': order})

def update_order_status(request, order_id):
    order = RecyclePurchase.objects.get(id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('order_detail', order_id=order_id)
    return render(request, 'detail_purchase.html', {'order': order})
@login_required
def add_weight(request, order_id):
    if request.method == 'POST':
        # รับข้อมูลน้ำหนักขยะจาก POST request
        weight_has_bottle = request.POST.get('weight_has_bottle')
        weight_has_can = request.POST.get('weight_has_can')
        weight_has_glass_bottle = request.POST.get('weight_has_glass_bottle')
        weight_has_paper = request.POST.get('weight_has_paper')

        # ค้นหาการสั่งซื้อที่ต้องการจะเพิ่มข้อมูลน้ำหนักขยะ
        order = RecyclePurchase.objects.get(id=order_id)

        # บันทึกข้อมูลน้ำหนักขยะลงในฐานข้อมูล
        order.weight_has_bottle = weight_has_bottle
        order.weight_has_can = weight_has_can
        order.weight_has_glass_bottle = weight_has_glass_bottle
        order.weight_has_paper = weight_has_paper
        order.save()


        return redirect('order_detail', order_id=order_id)
    else:
        # หากไม่ใช่ POST request ให้ redirect กลับไปยังหน้าแรกหรือหน้าที่เหมาะสม
        return redirect('home')  
    
def upload_slip(request, order_id):
    order = RecyclePurchase.objects.get(id=order_id)
    if request.method == 'POST' and request.FILES.get('slip_image'):
        slip_image = request.FILES['slip_image']
        # Save the uploaded image
        order.slip_image = slip_image
        order.save()
        # You can optionally save the image to a specific location if needed
        # with default_storage.open('path/to/save/slip_image.jpg', 'wb+') as destination:
        #     for chunk in slip_image.chunks():
        #         destination.write(chunk)
        return redirect('order_detail', order_id=order_id)
    return render(request, 'detail_purchase.html', {'order': order})
@login_required
def slip_detail(request, order_id):
    # ดึงข้อมูลรายละเอียดการจองโดยใช้ ID
    order = get_object_or_404(RecyclePurchase, pk=order_id)
    return render(request, 'member/slip_detail.html', {'order': order})
