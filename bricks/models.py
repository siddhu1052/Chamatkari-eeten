from django.db import models

choice = (
    ('rent','Rent'),
    ('sale','Sale'),
    ('pg','PG'),
    ('on_lease', 'On Lease'),
)

l_b = (
    ('land','Land'),
    ('built','Built'),
)
# Create your models here.

st=(
    ('uc','Under Construction'),
    ('rtm',"Reasy to move"),
)
direction = (
    ('E','east'),
    ('NE','North-East'),
    ('N','north'),
    ('NW','North-West'),
    ('W','west'),
    ('SW','South-West'),
    ('S','south'),
    ('SE','South-East'),
)
state = (
    ('F','Furnished'),
    ('uf','Furnished'),
)

too=(
    ('ind','Independent'),
    ('wo','With Owner'),
)

class built(models.Model):
    type = models.CharField(max_length=50,choices=choice,null=True, default=None)
    
    area=models.IntegerField()
    floors=models.IntegerField()
    images=models.ImageField(upload_to='media/', unique=True, blank=False, null=False)
    status=models.CharField(max_length=50,choices=st)
    faces=models.CharField(choices=direction, max_length=50, blank=False)
    p_type=models.CharField(max_length=10, default="Built")
    fs=models.CharField(max_length=50,choices=state, blank=False)
    type_of_ownership=models.CharField(max_length=50,choices=too)
    Age=models.IntegerField()
    rent=models.FloatField()
    address=models.CharField(max_length=200, blank= False, default=None, null=False, unique=True)
    def __str__(self): 
        return self.address

t_l = (
    ('agg','Aggrecultural') ,
    ('res','Residential') ,
)

class land(models.Model):
    type = models.CharField(max_length=50,choices=choice,null=True, default=None)
    # category=models.ForeignKey("category", null=True , on_delete=models.CASCADE, default=None)
    images=models.ImageField(upload_to='media/', unique=True)
    land_type=models.CharField(choices=t_l, max_length=10, default= None, null=True)
    price=models.FloatField(default=0)
    area=models.IntegerField(default=0)
    p_type=models.CharField(max_length=10, default="Land")
    EMI=models.BooleanField(blank=False, null=False, default=False)
    EMI_rate=models.IntegerField(blank=True,null=True, default=None)
    address=models.CharField(max_length=200, blank= False, default=None, null=False, unique=True)

    def __str__(self): 
        return self.address
    
