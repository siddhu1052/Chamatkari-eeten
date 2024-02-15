from django.shortcuts import render
from .form import *
from .models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views 
def home(request):
    y=category.objects.all()
    return render(request,'bricks/home.html',{"y":y})

def land_details(request):
    if(request.method=='GET'):
        x=land_Form()
        return render(request,'bricks/land_details.html',{'form':x})
    else:
        x=land_Form(request.POST,request.FILES)
        if(x.is_valid()):
            x.save()
        return render(request,'bricks/land_details.html',{'form':x})

def built_details(request):
    if(request.method=='GET'):
        x=built_Form()
        return render(request,'bricks/built_details.html',{'form':x})
    else:
        x=built_Form(request.POST,request.FILES)
        if(x.is_valid()):
            x.save()
        return render(request,'bricks/built_details.html',{'form':x})

def properties(request):
    x=request.GET.get('category')
    obj=get_object_or_404(category, pk=x)
    print (obj)
    p=land.objects.filter(cat__cat=obj.cat)
    q=built.objects.filter(cat__cat=obj.cat)
    
    print(p.count())
    return render(request,'bricks/properties.html',{"obj":p,"obj2":q})
    