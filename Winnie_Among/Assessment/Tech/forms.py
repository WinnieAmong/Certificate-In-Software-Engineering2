from django.forms import ModelForm
from.models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
           
        