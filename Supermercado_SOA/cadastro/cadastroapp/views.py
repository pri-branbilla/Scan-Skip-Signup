from __future__ import print_function
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.conf import settings
import string
from cadastroapp.control import verificaUsuario, pegaUsuario
from control import *
import random
from .models import Usuario
from tests import *

# Link do carrinho: 'https://scan-skip-carrinho.herokuapp.com/id=' + id1 + '/nome=' + nome

def Sobre(request):
    return render(request, 'cadastroapp/sobre.html', {})

def Home(request):
    return render(request, 'cadastroapp/home.html', {})

def cadastro(request):
    registrado = False
    erroSenha = False
    erroEmail = False
    erroCPF = False
    erroUsuario = False
    chars = string.letters + string.digits
    siz = 25
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
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
        if not erroUsuario and not erroEmail and not erroSenha and not erroCPF:
            #U.create_user(username=usuario, password=senha1, email=email)
            tokenEmail = ''.join(random.choice(chars) for x in range(siz))
            cliente = Usuario(idusuario=str(random.randint(0,100000)), nome=nome, email=email, cpf=cpf, senha=senha1, ativado=False, tokenEmail = tokenEmail)
            cliente.save()
            subject = '[Sem Resposta]'
            message = 'Acesse o link para confirmar seu e-mail /n http://localhost:8000/cadastro/ativa/token=' + tokenEmail
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
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

def Ativa(request, token):
    user=Usuario.objects.get(tokenEmail = token)
    user.ativado = True
    user.save()
    return redirect('/perfil')

def alterar_dados(request):
    logado = verificaUsuario(request)
    erroEmail = False

    if logado:
        usuario = pegaUsuario(request.session['idusuario'], request.session['nome'])
        nome = usuario.nome
        email = usuario.email
        CPF = usuario.cpf

        document.getElementsByName("nome")[0].value="";
        document.getElementsByName("nome")[0].placeholder=nome;
        document.getElementsByName("email")[0].value="";
        document.getElementsByName("email")[0].placeholder=email;
        document.getElementsByName("CPF")[0].value="";
        document.getElementsByName("CPF")[0].placeholder=CPF;

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
                usuario.setNome(nome)
                usuario.setEmail(email)   
                usuario.save()
            
            #cliente = Usuario(idusuario=str(random.randint(0,100000)), nome=nome, email=email, cpf=cpf, senha=senha1, ativado=False, tokenEmail = tokenEmail)
            cliente.save()
            
        else:
            usuario = ''
            nome = ''
            email = ''

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

        if request.method == 'POST':
            senha_atual = request.POST.get('atual')
            senha_nova = request.POST.get('nova')
            senha_confirma = request.POST.get('confirma')

            if (senha_salva == senha_atual): # se senha correta
                if (senha_nova == senha_confirma):
                    usuario.setSenha(senha_nova)
                    usuario.save()
                    return perfil(request)

                else:
                    naoConfirma = True
            else:
                atualErrada = True

        return render(request, 'cadastroapp/alterar-dados.html', {'atualErrada': atualErrada, 'naoConfirma' : naoConfirma})
    
    else:
        return render(request, 'cadastroapp/home.html', {})

    

