from .models import *
from django.forms import ModelForm

class land_Form(ModelForm):
    class Meta:
        model = built
        fields = "__all__"

class built_Form(ModelForm):
    class Meta:
        model = land
        fields = "__all__"

