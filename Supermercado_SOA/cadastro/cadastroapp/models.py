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
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    senha = models.CharField(max_length=15)

    #def __str__(self):
    #   return self.email
    def getNome(self):
        return self.nome
    def getEmail(self):
        return self.email
    def getSenha(self):
        return self.senha
    def setNome(nome):
        nome = nome
    def setEmail(email):
        email = email
    def setSenha(senha):
        senha = senha
