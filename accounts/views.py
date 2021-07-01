from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login





# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user_obj=auth.authenticate(username=username,password=password)
        if user_obj is None: 
            messages.success(request,'Invalid username/password')
            return redirect("login")
        profile_obj=Profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'Profile is not verified check your mail.')
            return redirect('/login')
        user=auth.authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password')
            return redirect('login')
        auth.login(request,user)
        return redirect('/')


    else:
        return render(request,'login.html')


def register(request):

    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']
        if password==re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('login')
            else:
                user_obj=User.objects.create_user(username=username,email=email,password=password)
                """user.save()"""
                user_obj.save()
                auth_token=str(uuid.uuid4())
                profile_obj=Profile.objects.create(user=user_obj,auth_token=auth_token)
                profile_obj.save()
                send_mail_after_registration(email,auth_token)
                print('user created')
                return redirect("/accounts/token")
        else:
            messages.info(request,"password not matching")
            return redirect('login')
        return redirect("/")
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
def success(request):
    return render(request,'success.html')
def token_send(request):
    return render(request,'token_send.html')

def verify(request,auth_token):
    try:
        profile_obj=Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request,'your account already verified please login by scrolling down the page')
                return redirect("login")
            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request,'your account has been verified please login by scrolling down the page')
            return redirect("login")
        else:
            return redirect('accounts/error')
    except Exception as e:
        print(e)

def error_page(request):
    return render(request,'error.html')


def send_mail_after_registration(email,token):
    subject="Your account need to be verified"
    message=f'hi click on the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list )