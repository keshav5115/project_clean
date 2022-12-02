from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.core.mail import send_mail
from django.conf import settings
from .models import newusermodel

# Create your views here.
from .forms import newuserform
@permission_required(perm='newapp.add_newusermodel',login_url='/new/login/')
def newuserview(request):
    form=newuserform()
    if request.method=='POST' and request.FILES:
        form=newuserform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            
            password=form.cleaned_data['password']
            print(username,password)
            subject='welcome to django application'
            message=f'hi {username} thank u for registering in django application and your password is {password}'
            from_email=settings.EMAIL_HOST_USER
            recipient_list=[form.cleaned_data['email']]
            send_mail(subject,message,from_email,recipient_list)
            return HttpResponse('data stored')
    return render(request,'newuser.html',{'form':form})

def newlogin_view(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            
            user=authenticate(username=username,password=password)
            # data=newusermodel.objects.get(username=username)

            if user is not None:
                login(request,user)
                # subject='login alert'
                # message=f'{username} successfully login to django app'
                # from_email=settings.EMAIL_HOST_USER
                # recipient_list=[data.email]
                # send_mail(subject,message,from_email,recipient_list)
                return redirect('/new/home/')
    return render(request,'newlogin.html',{'form':form})

@login_required(login_url='/new/login/')
def newlogout_view(request):
    logout(request)
    return HttpResponse('successfully loged out')

@login_required(login_url='/new/login/')
def home(request):
    return render(request,'newhome.html')