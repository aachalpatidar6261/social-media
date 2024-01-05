from django.shortcuts import render,redirect
from .models import UserActivity # chat 
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random

from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request,'index.html')



def validate_signup(request):
    email=request.GET.get('email')
    data={
        'is_taken':User.objects.filter(email__iexact=email).exists()
         }
    return JsonResponse(data)


def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Register"
            return render(request,'signup.html',{'msg':msg})
        
        except:
            if request.POST['password']==" " and request.POST['cpassword']==" ":
                msg="Empty Password is Not Acceptable. Please Enter Password and Confirm Password"
                return render(request,'login.html',{'msg':msg})
            elif request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    
                    profile_pic=request.FILES['profile_pic']
                    
                )                
                return render(request,'login.html')
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
    
def login(request):
    if request.method=='POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                    request.session['email']=user.email
                    request.session['fname']=user.fname
                    request.session['profile_pic']=user.profile_pic.url
                    return render(request,'index.html')
                
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except Exception as e:
            msg="Email Not Register"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')

def department(request):
    return render(request,'departments.html')


def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=='POST':        
        if user.password==request.POST['oldpassword']:
            if request.POST['newpassword']==request.POST['cnewpassword']:
                user.password=request.POST['newpassword']
                user.save()
                return redirect('logout')
            else:
                msg="New password & Confirm New Password Does Not Matched"
                
        else:
            msg="Incorrect Old Password"
            if user.usertype=="patient":
                    return render(request,"change-password.html",{'msg':msg})
            else:
                return render(request,"doctor-change-password.html",{'msg':msg})
    else:
        return render(request,"change-password.html")
       

    
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        user.address=request.POST['address']
        try:
            user.profile_pic=request.FILES('profile_pic')
        except:
            pass
        user.save()
        msg="Profile Updated Successfully"
        return render(request,'profile.html',{'msg':msg})  #  {'user':user}
        
    else:
        return render(request,'profile.html',{'user':user})  #  {'user':user}
        

def forgot_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject = 'OTP For Forgot Password'
            message = 'Hello '+user.fname+' Your OTP For Forget Password Is : '+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'otp.html',{'email':user.email,'otp':otp})
        except:
            msg="Email Not Register"
            return render(request,'forgot-password.html',{'msg':msg})
    else:
        return render(request,'forgot-password.html')
    

def verify_otp(request):
    email=request.POST['email']
    otp=request.POST['otp']
    uotp=request.POST['uotp']

    if otp==uotp:
        return render(request,'new-password.html',{'email':email})
    else:
        msg="Incorrect OTP"
        return render(request,'otp.html',{'msg':msg,'email':email,'otp':otp})
    
def new_password(request):
    email=request.POST['email']
    np=request.POST['newpassword']
    cnp=request.POST['cnewpassword']

    if np==cnp:
        user=User.objects.get(email=email)
        user.password=np
        user.save()
        return render(request,'login.html')
    else:
        msg="New Password And Confirm New Password Does Not MAtched"
        return render(request,'new-password.html',{'email':email,'msg':msg})

# chat /*
def dashboard(request):
    activities = UserActivity.objects.filter(user=request.user)    
    return render(request, 'dashboard/dashboard.html', {'activities': activities})   # */