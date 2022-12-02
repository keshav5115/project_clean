from django.shortcuts import render,redirect
from django.http import HttpResponse

from appmedia.forms import Blogform
from appmedia.models import Blog
# Create your views here.

def Blogview(request):
    form=Blogform()
    if request.method =='POST' and request.FILES:
        print(request.POST)
        print(request.FILES)
        form=Blogform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/media/blogall/')
    return render(request,'blog.html',{'form':form})

def Blogget(request):
    data=Blog.objects.all()
    return render(request,'blogget.html',{'data':data})


def Blogread(request,pk):
    data=Blog.objects.get(id=pk)
    return render(request,'blogread.html',{'data':data})

def Blogupdate(request,pk):
    data=Blog.objects.get(id=pk)
    if request.method=='POST' and request.FILES:
        form=Blogform(request.POST,request.FILES,instance=data)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            redirect('/media/blogall/')
    return render(request,'blogupdate.html',{'data':data})

def Blogdelete(request,pk):
    data=Blog.objects.get(id=pk).delete()
    return redirect('/media/blogall/')
