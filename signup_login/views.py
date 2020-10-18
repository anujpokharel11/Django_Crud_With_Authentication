from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def sign_up(request):
    if not request.user.is_authenticated: #if user logged in then block signup from url
        if request.method =='POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                form = SignUpForm()

        else:
            form = SignUpForm()
        return render(request,'signup_login/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/admin/')

def user_login(request):
    #Get method 
    if not request.user.is_authenticated:  #if user is logged in then block user from login from url
        log = AuthenticationForm()

        if request.method == 'POST':
            log = AuthenticationForm(request=request,data=request.POST)
            if log.is_valid():
                uname = log.cleaned_data['username']
                upass = log.cleaned_data['password']
    
                user = authenticate( request, username=uname,password=upass)
    
    
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/admin/')
                    

        
        return render(request,'signup_login/login.html',{'log':log})

    else:
        return HttpResponseRedirect('/admin/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')