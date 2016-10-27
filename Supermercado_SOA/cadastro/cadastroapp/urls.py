from . import views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    url(r'^$', views.Cadastro, name="Cadastro"),
    url(r'^sobre/', views.Sobre, name="Sobre"),
    url(r'^login/', views.login, name="login")
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#site_media = os.path.join(os.path.dirname(__file__), ',,/', 'cadastroapp', 'static', 'cadastro')