from django.db import models
from django.contrib.auth import authenticate , login ,logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
choice = (
    ('Rent','Rent'),
    ('Sale','Sale'),
    ('PG','PG'),
    ('On lease', 'On Lease'),
)

l_b = (
    ('Land','Land'),
    ('Built','Built'),
)
# Create your models here.

st=(
    ('Under Construction','Under Construction'),
    ('Ready To Move',"Reasy to move"),
)
direction = (
    ('East','east'),
    ('North-East','North-East'),
    ('North','north'),
    ('North-West','North-West'),
    ('West','west'),
    ('South-West','South-West'),
    ('South','south'),
    ('South-East','South-East'),
)
state = (
    ('Furnished','Furnished'),
    ('Un-Furnished','Un-Furnished'),
)

too=(
    ('Independent','Independent'),
    ('With Owner','With Owner'),
)

class category(models.Model):
    cat=models.CharField(max_length=50)
    def __str__(self) :
        return self.cat

class built(models.Model):
    
    name=models.CharField(max_length=500,blank=False,null=True,default=None)
    owner_phone=models.IntegerField(null=True, blank=False)
    owner_name=models.CharField(max_length=500,blank=False,null=True,default=None)
    owner_mail=models.EmailField(max_length=500,blank=False,null=True)
    cat=models.ForeignKey("category", null=True , on_delete=models.CASCADE, default=None)
    area=models.IntegerField()
    floors=models.IntegerField()
    status=models.CharField(max_length=50,choices=st)
    faces=models.CharField(choices=direction, max_length=50, blank=False)
    p_type=models.CharField(max_length=10, default="Built")
    furnished_status=models.CharField(max_length=50,choices=state, blank=False, null=True)
    type_of_ownership=models.CharField(max_length=50,choices=too)
    price=models.FloatField(default=0,null=True)
    age=models.IntegerField()
    address=models.CharField(max_length=200, blank= False, default=None, null=True, unique=True)
    image=models.ImageField(upload_to='images/')
    def __str__(self): 
        return self.address

t_l = (
    ('Aggricultural','Aggrecultural') ,
    ('Residential','Residential') ,
)

class land(models.Model):
    name=models.CharField(max_length=500,blank=False,null=True,default=None)
    cat=models.ForeignKey("category", null=True , on_delete=models.CASCADE, default=None)
    owner_phone=models.IntegerField(null=True, blank=False)
    owner_name=models.CharField(max_length=500,blank=False,null=True,default=None)
    owner_mail=models.EmailField(max_length=500,blank=False,null=True)
    area=models.IntegerField(default=0)
    land_type=models.CharField(choices=t_l, max_length=50, default= None, null=True)
    price=models.FloatField(default=0)
    p_type=models.CharField(max_length=10, default="Land")
    # EMI=models.BooleanField(blank=False, null=False, default=False)
    # EMI_rate=models.IntegerField(blank=True,null=True, default=None)
    address=models.CharField(max_length=200, blank= False, default=None, null=False, unique=True)
    image=models.ImageField(upload_to='images/')
    def __str__(self): 
        return self.address
    
