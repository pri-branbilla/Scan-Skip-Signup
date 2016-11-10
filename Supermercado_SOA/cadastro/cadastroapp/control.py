from models import *

def verificaUsuario(request):
    try:
        logado = request.session['logado']
    except KeyError:
        request.session['logado'] = False
        logado = False
    return logado

def pegaUsuario(idusuario, nome):
    if nome == None:
        usuario = Usuario.objects.get(idusuario=idusuario)
    else:
        try:
            usuario = Usuario.objects.get(idusuario=idusuario)
        except:
            usuario = Usuario(idusuario=idusuario, nome=nome)
            usuario.save()
    return usuario
