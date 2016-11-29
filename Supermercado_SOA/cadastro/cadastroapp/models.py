from __future__ import unicode_literals

from mongoengine import *
from django.utils import timezone

class Usuario(Document):
    idusuario = StringField()
    nome = StringField(max_length=200)
    email = EmailField(max_length=200)
    cpf = StringField(max_length=14)
    senha = StringField(max_length=15)
    ativado = BooleanField()
    tokenEmail = StringField()
    tentativas = IntField()

    def getNome(self):
        return self.nome
    def getEmail(self):
        return self.email
    def getSenha(self):
        return self.senha
