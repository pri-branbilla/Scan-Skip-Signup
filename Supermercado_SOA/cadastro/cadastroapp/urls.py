from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^cadastro/', views.cadastro, name="cadastro"),
    url(r'^sobre/', views.Sobre, name="Sobre"),
    url(r'^perfil/', views.perfil, name="perfil"),
    url(r'^editarcadastro/', views.alterar_dados, name="alterardados"),
    url(r'^editarsenha/', views.alterar_senha, name="alterarsenha"),
    url(r'^login/$', views.login, name="login"),
    url(r'^login/(?P<tk>[-\w ]+)', views.loginEMailConfirmado, name="loginEMailConfirmado"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^mapa/', views.mapa, name="mapa"),
    url(r'^$', views.Home, name="Home"),
    url(r'^ativa/token=(?P<token>[-\w ]+)', views.Ativa, name="Ativa"),
    url(r'^recuperar-senha/', views.recuperarsenha, name="recuperarsenha"),
    url(r'^novasenha/(?P<idusuario>[-\w ]+)', views.novasenha, name="novasenha"),
    url(r'^confirmacao-email/', views.confirmacaoemail, name="confirmacaoemail"),
]