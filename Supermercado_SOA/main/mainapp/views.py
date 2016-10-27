from django.shortcuts import render
from mongoengine import *
from .models import Cliente

import json


def login(request, usuario, senha, logado):
    try:
        user = User.objects.get(username=usuario)
        if user.check_password(senha):
            user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            request.session.set_expiry(60 * 60 * 1)  # 1 hour timeout
            logado = True
        else:
            pass # Senha errada
    except DoesNotExist:
        pass    # Nome de usuario nao existe
    return request, logado


def index(request):
    logado = False
    if request.method == 'POST':
        username = request.POST.get('E-mail')
        senha = request.POST.get('Senha')
        request, logado = login(request, username, senha, logado)
        if logado:
            return render(request, 'Interfaces/fila.html', {})
    else:
        username = ''
        senha = ''
    return render(request, 'Interfaces/login.html', {'logado': logado, 'username': username, 'senha': senha})


def Cadastro(request):
    registrado = False
    if request.method == 'POST':
        usuario = request.POST.get('username')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        if User.objects(username=usuario).count() > 0 or User.objects(email=email).count() > 0:
            erroUsuario = True
        else:
            erroUsuario = False
        cpf = request.POST.get('cpf')
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
            cliente = Cliente(nome=nome, cpf=cpf)
            cliente.save()
            registrado = True
    else:
        usuario = ''
        nome = ''
        email = ''
        cpf = ''

    return render(request,
            'Interfaces/cadastro.html',
            {'registrado': registrado, 'usuario': usuario, 'nome': nome, 'email': email, 'cpf': cpf} )


def Fila(request):
    if request.method == 'POST':
        naFila = True
        posicao = json.dumps()
    else:
        posicao = json.dumps(0)
        naFila = False

    return render(request, 'Interfaces/fila.html', {'naFila': naFila, 'posicao': posicao})
