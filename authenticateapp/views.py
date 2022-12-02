from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import Autheregform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def Authregview(request):
    form=Autheregform()
    if request.method=='POST':
        form=Autheregform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data has stored')
    return render(request,'authereg.html',{'form':form})


def login_view(request):
    form=AuthenticationForm()
    if request.method == "POST":
        form=AuthenticationForm(request,request.POST)
        
        
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            #authenticate function return  username if username and password matches otherwise 
            #it will return None
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponse('SUCCESSFULLY LOGIN')
                 
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return HttpResponse('loged out')


