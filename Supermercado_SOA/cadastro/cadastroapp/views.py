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

from .models import Usuario


def Sobre(request):
    #user = Usuario(nome="x3231", email="bla@bla3.com", senha="x1233")
    #user.save()
    #return HttpResponseRedirect('http://143.107.102.52:8000/carrinho/id=3894728582/nome=blablabla')
    return render(request, 'cadastroapp/sobre.html', {})



def Cadastro(request):
    registrado = False
    if request.method == 'POST':
        user_form = UsuarioForm(data=request.POST)
        if user_form.is_valid():
            if user_form.senha1 == user_form.senha2:
                Usuario = user_form.save()
                registrado = True
        else:
            print(user_form.errors)
    else:
        user_form = UsuarioForm()
    return render(request,
                  'cadastroapp/Cadastro.html', {'user_form': user_form, 'registrado': registrado})


def cadastro(request):
    registrado = False
    erroSenha = False
    erroEmail = False
    erroUsuario = False
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        if nome=="":
            erroUsuario = True
        else:
            erroUsuario = False
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        try:
            user = Usuario.objects.get(nome=nome, email=email)
            registrado = True
        except:
            registrado = False
        if senha1 == senha2:
            erroSenha = False
        else:
            erroSenha = True
        if '@' in email and '.' in email:
            erroEmail = False
        else:
            erroEmail = True
        if not erroUsuario and not erroEmail and not erroSenha:
            #U.create_user(username=usuario, password=senha1, email=email)
            cliente = Usuario(nome=nome, email=email, senha=senha1)
            cliente.save()
            registrado = True
            return HttpResponseRedirect('/cadastro/login')
    else:
        usuario = ''
        nome = ''
        email = ''

    return render(request,
                  'cadastroapp/Cadastro.html',
                  {'erroSenha' : erroSenha, 'registrado' : registrado, 'erroEmail' : erroEmail, 'erroUsuario' : erroUsuario})


def login(request):
    desativada = False
    errado = False
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try: #se usuario e senha corretos
                user = Usuario.objects.get(email=email, senha=senha)
                id = str(user._id)
                nome = str(user.nome)
                return HttpResponseRedirect('http://192.168.1.12:5555/carrinho/id=' + id + '/nome=' + nome)
        except:
                errado = True
    return render(request, 'cadastroapp/login.html', {'errado': errado})


class UsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    senha2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    def __init__(self, *args, **kwargs):
		self.instance = kwargs.pop('instance', None)
		super(UsuarioForm, self).__init__(*args, **kwargs)

# Create your views here.
