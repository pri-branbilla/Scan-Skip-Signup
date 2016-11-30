# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.conf import settings
from mongoengine.django.sessions import MongoSession
import string
from cadastroapp.control import verificaUsuario, pegaUsuario
from control import *
import random
from .models import Usuario
from tests import *

siteCarrinho = 'https://scan-skip-carrinho-teste.herokuapp.com/'

def Sobre(request):
    return render(request, 'cadastroapp/sobre.html', {})

def Home(request):
    return render(request, 'cadastroapp/home.html', {})

def cadastro(request):

    registrado = False
    erroSenha = False
    erroEmail = False
    erroCPF = False
    erroCPFexistente = False
    erroUsuario = False
    chars = string.letters + string.digits
    siz = 25
    cpf = ""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = str(request.POST.get('cpf'))
        try:
            user2 = Usuario.objects.get(cpf=cpf)
            erroCPFexistente = True

        except:
            erroCPFexistente = False
        if nome=="":
            erroUsuario = True
        else:
            erroUsuario = False
        veif = validar_cpf(cpf)
        if not veif:
            erroCPF = True
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
        if not erroUsuario and not erroEmail and not erroSenha and not erroCPF and not erroCPFexistente:
            tokenEmail = ''.join(random.choice(chars) for x in range(siz))
            cliente = Usuario(idusuario=str(random.randint(0, 100000)), nome=nome, email=email, cpf=cpf, senha=senha1, ativado=False, tokenEmail=tokenEmail, tentativas=0)
            cliente.save()
            subject = '[Sem Resposta]'
            message = 'Acesse o link para confirmar seu e-mail /n https://scan-skip-teste.herokuapp.com/ativa/token=' + tokenEmail
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            registrado = True
            return HttpResponseRedirect('https://scan-skip-teste.herokuapp.com/login')
    else:
        usuario = ''
        nome = ''
        email = ''

    return render(request,
                  'cadastroapp/Cadastro.html',
                  {'nome': nome, 'cpf': cpf, 'email': email, 'erroSenha' : erroSenha, 'erroCPFexistente' : erroCPFexistente, 'registrado' : registrado, 'erroEmail' : erroEmail, 'erroUsuario' : erroUsuario, 'erroCPF' : erroCPF})

def loginEMailConfirmado(request, tk):
    desativada = False
    Usererrado = False
    SenhaErrada = False
    EmailConfirmado = ""
    if(tk=="confirma"):
        EmailConfirmado = "Conta confirmada com sucesso"
    elif(tk=="notfound"):
        EmailConfirmado = "Conta não encontrada"
    tent = 0
    tokenC = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        permanece = request.POST.get('permanece')
        try:  # se usuario e senha corretos
            user = Usuario.objects.get(email=email, senha=senha)
            id1 = str(user.idusuario)
            nome = str(user.nome)

            if (permanece == "on"):
                tempo = 1000000000
            else:
                tempo = 10000
            request.session.set_expiry(tempo)
            request.session['logado'] = True
            request.session['nome'] = nome
            request.session['idusuario'] = id1
            user.tentativas = 0
            user.save()
            return HttpResponseRedirect(siteCarrinho + 'id=' + id1 + '/nome=' + nome)
        except:
            try:
                user2 = Usuario.objects.get(email=email)
                SenhaErrada = True
                tent = user2.tentativas
                if (tent < 3):
                    tent = tent + 1
                    user2.tentativas = tent
                    user2.save()

            except:
                Usererrado = True

    return render(request, 'cadastroapp/login.html',
                  {'EmailConfirmado': EmailConfirmado, 'Usererrado': Usererrado, 'tent': tent,
                   'SenhaErrada': SenhaErrada})


def login(request):
    desativada = False
    Usererrado = False
    SenhaErrada = False
    EmailConfirmado = ""
    tent = 0
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        permanece = request.POST.get('permanece')
        try:  # se usuario e senha corretos
            user = Usuario.objects.get(email=email, senha=senha)
            id1 = str(user.idusuario)
            nome = str(user.nome)

            if (permanece == "on"):
                tempo = 1000000000
            else:
                tempo = 10000
            request.session.set_expiry(tempo)
            request.session['logado'] = True
            request.session['nome'] = nome
            request.session['idusuario'] = id1
            user.tentativas=0
            user.save()
            return HttpResponseRedirect(siteCarrinho + 'id=' + id1 + '/nome=' + nome)
        except:
            try:
                user2 = Usuario.objects.get(email=email)
                SenhaErrada = True
                tent = user2.tentativas
                if(tent<3):
                    tent = tent+1
                    user2.tentativas=tent
                    user2.save()

            except:
                Usererrado = True

    return render(request, 'cadastroapp/login.html', {'EmailConfirmado': EmailConfirmado, 'Usererrado': Usererrado, 'tent': tent, 'SenhaErrada': SenhaErrada})

def mapa(request):
    return render(request, 'cadastroapp/mapa.html', {})


def logout(request):
    logado = verificaUsuario(request)
    if logado:
        del request.session['logado']
        del request.session['nome']
        del request.session['idusuario']
        MongoSession.objects.get(session_key=request.session.session_key).delete()
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


def Ativa(request, token):
    try:
        user=Usuario.objects.get(tokenEmail=token)
        user.ativado = True
        user.save()
        return redirect('/login/confirma')
    except:
        return redirect('/login/notfound')




def alterar_dados(request):
    logado = verificaUsuario(request)
    erroEmail = False

    if logado:
        usuario = pegaUsuario(request.session['idusuario'], request.session['nome'])
        nome = usuario.nome
        email = usuario.email
        CPF = usuario.cpf
        senha = usuario.senha

        if request.method == 'POST':
            nome = request.POST['nome']
            email = request.POST['email']
            if nome=="":
                nome = usuario.nome
                
            if email=="":
                email = usuario.email
            elif '@' in email and '.' in email:
                erroEmail = False
            else:
                erroEmail = True
        
            if not erroEmail:
                usuario.nome=nome
                request.session['nome']=nome
                usuario.email=email  
                usuario.save()
            return perfil(request)

        return render(request, 'cadastroapp/alterar-dados.html', {'nome': nome, 'email': email, 'CPF': CPF, 'erroEmail' : erroEmail})

    else:
        return render(request, 'cadastroapp/home.html', {})


def alterar_senha(request):
    atualErrada = False
    naoConfirma = False
    logado = verificaUsuario(request)

    if logado:
        usuario = pegaUsuario(request.session['idusuario'], request.session['nome'])
        senha_salva = usuario.senha

        senha_atual = ""
        senha_nova = ""
        senha_confirma = ""

        if request.method == 'POST':
            senha_atual = request.POST.get('senha_atual')
            senha_nova = request.POST.get('senha_nova')
            senha_confirma = request.POST.get('senha_confirma')

            if (senha_salva == senha_atual): # se senha correta
                if (senha_nova == senha_confirma):
                    usuario.senha=senha_nova
                    usuario.save()
                    return perfil(request)
                else:
                    naoConfirma = True
            else:
                atualErrada = True
            

        return render(request, 'cadastroapp/alterar-senha.html', {'atualErrada': atualErrada, 'naoConfirma' : naoConfirma})
    
    else:
        return render(request, 'cadastroapp/home.html', {})


def recuperarsenha(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = 'Recuperar senha'
        usuario = Usuario.objects.get(email=email)
        idusuario=usuario.idusuario
        message = 'Foi detectado uma nova solicitacao para recuperacao de senha. Para confirmar clique no link a seguir: \n https://scan-skip-teste.herokuapp.com/novasenha/'+idusuario+ '\nCaso nao tenha solicitado a recuperacao de senha ignore esse e-mail. \n\nAtt. Scan&Skip'
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return login(request)
    return render(request, 'cadastroapp/recuperar-senha.html', {})


def novasenha(request, idusuario):

    chars = string.letters + string.digits
    siz = 8
    senhanova = ''.join(random.choice(chars) for x in range(siz))
    usuario = Usuario.objects.get(idusuario=idusuario)
    usuario.senha = senhanova
    usuario.save()
    email= usuario.email
    subject = 'Nova Senha'
    message = 'Sua nova senha é: ' +senhanova
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    return redirect('https://scan-skip-teste.herokuapp.com/confirmacao-email/')


def confirmacaoemail(request):
    return render(request, 'cadastroapp/confirmacao-email.html', {})
