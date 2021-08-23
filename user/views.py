from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def signin(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("signin")
    else:
        return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        name=request.POST['username']
        emailid=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=emailid).exists():
                print("email already exists")
                messages.info(request,"email already taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=name,email=emailid,password=password)
                user.save()
        else:
            messages.info(request,"password not matching")
            return redirect("signup")
        return redirect('/')
    else:
        return render(request,'register.html')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')