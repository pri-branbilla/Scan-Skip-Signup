from .models import *
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer


class ClienteSerializer(DocumentSerializer):
    class Meta:
        model = Cliente


class ProdutoSerializer(DocumentSerializer):
    class Meta:
        model = Produto


class FilaSerializer(DocumentSerializer):
    class Meta:
        model = Fila


class LojaSerializer(DocumentSerializer):
    class Meta:
        model = Loja
