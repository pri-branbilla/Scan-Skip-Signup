from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from mongoengine import *
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from control import *
from tests import *
import random
from .models import Usuario

# Link do carrinho: 'https://scan-skip-carrinho.herokuapp.com/id=' + id1 + '/nome=' + nome

def Sobre(request):
    return render(request, 'cadastroapp/sobre.html', {})

def Home(request):
    return render(request, 'cadastroapp/home.html', {})

def cadastro(request):
    registrado = False
    erroSenha = False
    erroCPF = False
    erroEmail = False
    erroUsuario = False
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        if nome=="":
            erroUsuario = True
        else:
            erroUsuario = False
        valido = validar_cpf(cpf)
        if not valido:
            erroCPF=True
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
        if not erroUsuario and not erroEmail and not erroSenha and not erroCPF:
            #U.create_user(username=usuario, password=senha1, email=email)
            cliente = Usuario(idusuario=str(random.randint(0,100000)), nome=nome, email=email, cpf=cpf, senha=senha1)
            cliente.save()
            registrado = True
            return HttpResponseRedirect('/login')
    else:
        usuario = ''
        nome = ''
        email = ''

    return render(request,
                  'cadastroapp/Cadastro.html',
                  {'erroSenha' : erroSenha, 'registrado' : registrado, 'erroEmail' : erroEmail, 'erroUsuario' : erroUsuario, 'erroCPF' : erroCPF})


def login(request):
    desativada = False
    errado = False

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        permanece = request.POST.get('permanece')
        try:  # se usuario e senha corretos
            user = Usuario.objects.get(email=email, senha=senha)
            id1 = str(user.idusuario)
            nome = str(user.nome)

            if (permanece == "on"):
                request.session.set_expiry(1000000000)
            else:
                request.session.set_expiry(10000)
            request.session['logado'] = True
            request.session['nome'] = nome
            request.session['idusuario'] = id1
            return perfil(request)
        except:
            errado = True

    return render(request, 'cadastroapp/login.html', {'errado': errado})


def logout(request):
    logado = verificaUsuario(request)
    if logado:
        request.session.set_expiry(1)
        del request.session['logado']
        del request.session['nome']
        del request.session['idusuario']
    return render(request, 'cadastroapp/home.html', {})


def perfil(request):
    logado = verificaUsuario(request)
    if logado:
        usuario = pegaUsuario(request.session['idusuario'], request.session['nome'])
        email = usuario.email
        CPF = usuario.cpf
        return render(request, 'cadastroapp/perfil.html', {'email': email, 'CPF': CPF})
    else:
        return render(request, 'cadastroapp/home.html', {})


# Create your views here.
