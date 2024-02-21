from django.shortcuts import render
from .form import *
from .models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login ,logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views

def home(request):
    y=category.objects.all()
    p=land.objects.all()
    q=built.objects.all()
    return render(request,'bricks/home.html',{"obj":p,"obj2":q,"y":y})

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
    # print (obj)
    p=land.objects.filter(cat__cat=obj.cat)
    q=built.objects.filter(cat__cat=obj.cat)
    y=category.objects.all()
    print(p.count())
    return render(request,'bricks/properties.html',{"obj":p,"obj2":q,"y":y,"current_cat":obj.cat})
    
def property_details(request,property_id):
    # property_id=request.GET.get('property_id')
    p_type=request.GET.get('p_type')
    is_land = True
    if p_type == "Built" :
        # print("Built")
        is_land=False
        obj=built.objects.filter(pk=property_id)
    else: 
        # print ("Unknown property")
        obj=land.objects.filter(pk=property_id)
    
    return render(request,'bricks/property_details.html',{"obj":obj[0],"is_land":is_land})

def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        Name=request.POST['username']
        username = request.POST['username']
        
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            #messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            return render(request, 'bricks/login.html',{'Alert':"Username or password sahi se toh dal"})
            #messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'bricks/login.html') 

def signup(request):
    if request.method== 'GET':
        return render(request, 'bricks/signup.html',{'frm':UserCreationForm()});
    else:
        print ('hello')
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if b==c:
            if(User.objects.filter(username =a)):
                return render(request,'bricks/signup.html',{'frm':UserCreationForm(),'error':'username already exists'})
            else:
                user=User.objects.create_user(username=a, password=b);
                user.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'bricks/signup.html',{'frm':UserCreationForm(),'error':'password mismatch'})