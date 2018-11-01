from .models import * 

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username =  forms.CharField(
        max_length=20,
        required=True
    )
    
    first_name = forms.CharField(
        max_length=50,
        required=True
    )
    last_name = forms.CharField(
        max_length=50,
        required=True
    )
    email = forms.EmailField(
        required=True
    )
    

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'error_messages'
        )


class InvernaderoForm(forms.ModelForm):

    class Meta:
        model = Invernadero
        fields = (
            'id_invernadero',
            'id_dispositivo',
            'id_usuario',
            'id_cultivo',
            'nombre_invernadero',
            'ubicacion'
            )