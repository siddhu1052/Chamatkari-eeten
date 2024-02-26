from .models import *
from django.forms import ModelForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
