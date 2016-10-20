from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.Cadastro, name="Cadastro"),
]