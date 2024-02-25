from .models import *
from django.forms import ModelForm

class land_Form(ModelForm):
    class Meta:
        model = land
        fields = '__all__'
        exclude = ('p_type','owner_mail',)

class built_Form(ModelForm):
    class Meta:
        model = built
        # fields = ["area", "floors", "status", "faces", "furnished_status","type_of_ownership","age","address", "images"]
        fields = '__all__'
        exclude = ('p_type','owner_mail',)

