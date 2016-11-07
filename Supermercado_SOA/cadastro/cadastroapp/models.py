from __future__ import unicode_literals

from django.db import models
from mongoengine import *

from django.contrib.auth.models import User
from django.utils import timezone

#connect(
#    name='admin',
#     username='admin',
#     password='admin123',
#     host='mongodb://admin:qwerty@localhost/27017'
#)
# Create your models here.

class Usuario(Document):
    idusuario = StringField()
    nome = StringField(max_length=200)
    email = EmailField(max_length=200)
    cpf = IntField()
    senha = StringField(max_length=15)

    def getNome(self):
        return self.nome
    def getEmail(self):
        return self.email
    def getSenha(self):
        return self.senha
    def setNome(self, nome):
        nome = nome
    def setEmail(self, email):
        email = email
    def setSenha(self, senha):
        senha = senha
