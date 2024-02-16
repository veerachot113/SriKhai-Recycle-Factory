from django.shortcuts import render ,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def logouts(request):
    logout(request)
    return redirect('home') 


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)
            if user: 

                login(request, user)
                return redirect('home')

        else:
            form = LoginForm()
    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form })