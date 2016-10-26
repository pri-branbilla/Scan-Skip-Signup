from __future__ import unicode_literals

from mongoengine import *

#connect(
#    name='test',
#     username='user',
#     password='12345',
#     host='mongodb://admin:qwerty@localhost/production'
#)


class Cliente(Document):
    nome = StringField(max_length=200, required=True)
    cpf = IntField(required=True)


class Produto(Document):
    lojaID = ObjectIdField(required=True)
    nome = StringField(unique_with='lojaID', required=True)
    categoria = StringField(required=True)
    marca = StringField(required=True)
    preco = IntField(required=True)


class Caixa(EmbeddedDocument):
    lojaID = ObjectIdField(required=True)
    numero = IntField(unique_with='lojaID', required=True)


class FilaCliente(EmbeddedDocument):
    cliente = ReferenceField(Cliente)
    senha = IntField(unique=True, required=True)


class Fila(Document):
    clientes = EmbeddedDocumentListField(FilaCliente)


class Loja(Document):
    nome = StringField(unique=True, required=True)
    fila = ReferenceField(Fila)
    listaCaixas = EmbeddedDocumentListField(Caixa)

