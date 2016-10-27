from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from mongoengine import *
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import mongoengine.django.auth
#from mongoengine.django.auth import User


from .models import Usuario

def Sobre(request):
    return render(request, 'cadastroapp/sobre.html', {})

def Cadastro(request):
    registrado = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            Usuario = user_form.save()
            print(user_form)
            Usuario.set_password(Usuario.senha)
            Usuario.save()
            registrado = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,
                  'cadastroapp/Cadastro.html', {'user_form': user_form, 'registrado': registrado})

def cadastro(request):
    registrado = False
    if request.method == 'POST':
        usuario = request.POST.get('username')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        if User.objects(username=usuario).count() > 0 or User.objects(email=email).count() > 0:
            erroUsuario = True
        else:
            erroUsuario = False
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        if senha1 == senha2:
            erroSenha = False
        else:
            erroSenha = True
        if '@' in email and '.' in email:
            erroEmail = False
        else:
            erroEmail = True
        if not erroUsuario and not erroEmail and not erroSenha:
            User.create_user(username=usuario, password=senha1, email=email)
            cliente = Usuario(nome=nome, email=email, senha=senha1)
            cliente.save()
            registrado = True
    else:
        usuario = ''
        nome = ''
        email = ''


    return render(request,
            'cadastroapp/Cadastro.html',
            {'registrado': registrado, 'usuario': usuario, 'nome': nome, 'email': email} )



def login(request):
    desativada = False
    errado = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/cadastro/sobre/')
            else:
                desativada = True
        else:
            errado = True
    return render(request, 'cadastroapp/login.html', {'desativada': desativada, 'errado': errado})


class UserForm(forms.Form):
    nome = forms.CharField(label='Nome completo')
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
# Create your views here.
