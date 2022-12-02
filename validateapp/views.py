from django.shortcuts import render
from django.http import HttpResponse
from validateapp.forms import libraryform
# Create your views here.


def libraryview(request):
    form=libraryform()
    if request.method=='POST':
        form=libraryform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data has been stored')
    return render(request,'library.html',{'form':form})