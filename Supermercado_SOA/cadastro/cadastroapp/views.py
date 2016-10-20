from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from .models import Usuario

def Cadastro(request):
    registrado = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            Usuario = user_form.save()
            Usuario.set_password(Usuario.senha)
            Usuario.save()
            registrado = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,
                  'cadastroapp/Cadastro.html',
                  {'user_form': user_form, 'registrado': registrado})


class UserForm(forms.Form):
    nome = forms.CharField(label='Nome completo')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
# Create your views here.
