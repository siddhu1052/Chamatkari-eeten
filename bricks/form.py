from .models import *
from django.forms import ModelForm

class land_Form(ModelForm):
    class Meta:
        model = land
        fields = ['area',"land_type","price","address","images"]

class built_Form(ModelForm):
    class Meta:
        model = built
        fields = ["area", "floors", "status", "faces", "furnished_status","type_of_ownership","age","address", "images"]

