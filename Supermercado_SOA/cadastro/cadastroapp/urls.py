from . import views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    url(r'^cadastro/', views.cadastro, name="cadastro"),
    url(r'^sobre/', views.Sobre, name="Sobre"),
    url(r'^perfil/', views.perfil, name="perfil"),
    url(r'^editarcadastro/', views.alterar_dados, name="alterar dados"),
    url(r'^editarsenha/', views.alterar_senha, name="alterar senha"),
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^$', views.Home, name="Home"),
    url(r'^ativa/token=(?P<token>[-\w ]+)', views.Ativa, name="Ativa"),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#?senha=(?P<senha>[-\w ]+)&email=(?P<email>\w+)/$
#site_media = os.path.join(os.path.dirname(__file__), ',,/', 'cadastroapp', 'static', 'cadastro')