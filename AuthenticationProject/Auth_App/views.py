from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth




# Create your views here.

def home(request):
    return render(request,"Auth_App/home.html")


def user_registration(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username Taken!")
                return redirect("Auth_App:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken!")
                return redirect("Auth_App:register")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save()
                return redirect('Auth_App:login')
        else:
            return redirect("Auth_App:register")
        return redirect('Auth_App:home')
    else:
        return render(request, 'Auth_App/user_registration.html')
    

def login(request):
    if request.method=='POST':
        user_name=request.POST.get("user_name")
        password=request.POST.get("password")
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("Auth_App:home")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect ("Auth_App:login")
    else:
        return render(request, 'Auth_App/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect("Auth_App:home")



                
