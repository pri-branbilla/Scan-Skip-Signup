from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="Login"),
    url(r'^Cadastro', views.Cadastro, name="Cadastro"),
    url(r'^Fila', views.Fila, name="Fila"),
]