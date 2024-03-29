#Factory/views.py
from django.shortcuts import render,HttpResponse,redirect
from Member.models import*
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def cfidentity(request):
    cancel = Profile.objects.filter(cancel=True)
    firm = Profile.objects.filter(status=True,cancel=False)
    nofirm = Profile.objects.filter(status=False,cancel=False)
    return render(request,'factory/cfidentity.html',{'firm':firm,'nofirm':nofirm,'cancel':cancel})
@login_required 
def editestate(request,id):
    nfn = Profile.objects.get(pk=id)
    ed = EditStatus()
    if request.method == 'POST':
        ed = EditStatus(request.POST,instance=nfn)
        if ed.is_valid():
            ed.save()
            return redirect('cfidentity')
        else:
            ed = EditStatus(instance=nfn)
    else:
        ed = EditStatus(instance=nfn)

    return render(request,'factory/editstate.html',{'form':ed,'nfn':nfn})




