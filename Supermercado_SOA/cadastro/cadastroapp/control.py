from models import *
import re

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



__all__ = ['validar_cpf']

def validar_cpf(cpf):

    cpf = ''.join(re.findall('\d', str(cpf)))

    if (not cpf) or (len(cpf) < 11):
        return False

    hifen = cpf.count('-')
    pontos = cpf.count('.')
    if(hifen!=1 or pontos!=3):
        return False
    inteiros = map(int, cpf)
    novo = inteiros[:9]

    while len(novo) < 11:
        r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)


    if novo == inteiros:
        return cpf
    return False

if __name__ == "__main__":
    import doctest, sys
    result = doctest.testmod() #verbose=True)
    if result[0] == 0:
        print "OK!"
    else:
        print result