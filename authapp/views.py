from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.
# Create your views here.
def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('password2')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')

    return render(request, 'registration/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('users')
        else:
            messages.info(request, 'please provide correct details')
            return redirect('login')

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('profile')

def profile_page(request):

    return render(request, 'profile_page.html')