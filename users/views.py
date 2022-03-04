from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from .forms import renew,person
from django.core.mail import send_mail
import os
from django.conf import settings

# Create your views here.
def register(request):
    if request.method =='POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
              messages.info(request,'username taken')
              return redirect('register')
            elif  User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                store =User.objects.create_user(username=username,email=email,password=password1)
                store.save()
                messages.success(request,'Registered successfully,you can log in')
                return redirect('login')
        else:
            messages.error(request,'incorrect password,try again')
            return redirect('register')
    return render(request,'users/register.html')




def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            messages.success(request,'You are logged in already')
            return redirect('home')
        else:
            messages.error(request,'you are not registered yet,kindly register')
            return redirect('register')
    else:
        return render(request,'users/login.html')


def logout(request):
    users=request.user
    auth.logout(request)
    messages.success(request,'you have been logged out')
    return redirect('login')

def profiles(request):
    if request.method == 'POST':
        u_form = renew(request.POST, instance=request.user)
        p_form = person(request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Updated successful')
            return redirect('profile')
    else:
        u_form = renew()
        p_form = person()
    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})
