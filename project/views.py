from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistrationForm
from . models import User

# Create your views here.
def add_show(request):
    if request.user.is_authenticated: #if authenticated then give acess from url try to access admin then redirect to login 
        if request.method =="POST":
            form = StudentRegistrationForm(request.POST)   #data aaucha yesma form ko 
            if form.is_valid():
                namee = form.cleaned_data['name']
                emaill = form.cleaned_data['email']
                passwordd = form.cleaned_data['password']
                register = User(name=namee,email=emaill,password=passwordd)
                register.save()
                form = StudentRegistrationForm()
        else:
            form = StudentRegistrationForm()

        show = User.objects.all()
        context = {'show':show,'form':form,'name':request.user}

        return render (request,'project/add_show.html',context)

    else: #else redirect to login
       return HttpResponseRedirect('/login/') 



def delete(request,id):
    if request.method == 'POST':
        remove = User.objects.get(pk=id)
        remove.delete()
        return HttpResponseRedirect('/admin')

def update(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        form = StudentRegistrationForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin')
    else:
       data = User.objects.get(pk=id)  #at first when edit clicked hen id is taken ani from bata data aaucha
       form = StudentRegistrationForm(instance=data) 
    return render(request,'project/edit.html',{'form':form})    