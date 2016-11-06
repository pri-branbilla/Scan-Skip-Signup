from . import views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    url(r'^cadastro/', views.cadastro, name="cadastro"),
    url(r'^sobre/', views.Sobre, name="Sobre"),
    url(r'^login/', views.login, name="login"),
    url(r'^header/', views.header, name="header"),
    url(r'^$', views.Home, name="Home"),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#?senha=(?P<senha>[-\w ]+)&email=(?P<email>\w+)/$
#site_media = os.path.join(os.path.dirname(__file__), ',,/', 'cadastroapp', 'static', 'cadastro')