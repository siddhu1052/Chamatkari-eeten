from django.shortcuts import render
from .form import *

# Create your views 
def home(request):
    return render(request,'bricks/home.html')

def land_details(request):
    if(request.method=='GET'):
        x=land_Form()
        return render(request,'bricks/land_details.html',{'form':x})
    else:
        x=land_Form(request.POST)
        if(x.is_valid()):
            x.save()
        return render(request,'bricks/land_details.html',{'form':x})

def built_details(request):
    if(request.method=='GET'):
        x=built_Form()
        return render(request,'bricks/built_details.html',{'form':x})
    else:
        x=built_Form(request.POST)
        if(x.is_valid()):
            x.save()
        return render(request,'bricks/built_details.html',{'form':x})