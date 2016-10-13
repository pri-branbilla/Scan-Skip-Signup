# AplicacaoWeb

Parte de aplicação web do aplicativo para supermercado

### Como subir a aplicação utilizando o Django:

Abra a pasta que se deseja inicializar (por exemplo, login) e utilize:

```python manage.py runserver```

### Trabalhando em branches separadas:

* Criando uma branch nova e mudando para ela (o nome ficará no estilo "seunome/nomebranch"):

```git branch -m seunome/nomebranch```

* Dando o primeiro push nessa branch

```git push --set-upstream origin seunome/nomebranch```

* Para ver em qual branch se está nesse momento:

```git branch```

* Para mudar de branch:

```git checkout branch-que-deseja-ir```

* Depois de terminar o trabalho na sua branch (ter feito os commits e os pushs), para fazer um merge colocando o seu novo conteúdo na master:

```git checkout master``` 

```git merge seunome/nomebranch```

```git push origin master```

* Se você quiser fazer um merge do conteúdo da master na sua branch, é só fazer:

```git checkout seunome/nomebranch``` 

```git merge master```

```git push origin seunome/nomebranch```

### Requerimentos:
<sup>OBS: Em alguns sistemas é necessário utilizar o comando "pip" com sudo</sup>

* Python 2.7

* Django (https://www.djangoproject.com/download/):

```pip install Django```

* Mongoengine (http://docs.mongoengine.org/):

```pip install mongoengine==0.9```

* Django REST Framework (http://www.django-rest-framework.org/):

```
pip install djangorestframework
pip install markdown
pip install django-filter
```

* Blinker (https://pythonhosted.org/blinker/):

```pip install blinker```

* Django Rest Framework Mongoengine (https://github.com/umutbozkurt/django-rest-framework-mongoengine):

```pip install django-rest-framework-mongoengine```

* Para instalar o MongoDB no Ubuntu 16.04

https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04

<sup>Obs: Ao instalar utilizando o apt-get ao invés de apontar o pacote "mongodb-org", use apenas "mongodb"</sup>