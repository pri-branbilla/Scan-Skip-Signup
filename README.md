# AplicacaoWeb

Parte de aplicação web do aplicativo para supermercado

## ATENÇÃO: PARA TESTAR TUDO, É BOM TER O MONGODB INSTALADO PARA TESTAR O BANCO DE DADOS LOCAL. Se não tiver, quando der runserver, vai ter erro de conexão com o BD.

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

* Fazendo downgrade no PyMongo para funcionar direito:

```pip uninstall pymongo```

```pip install pymongo==2.8```

* Para instalar o MongoDB no Windows

https://code.msdn.microsoft.com/Mongo-Database-setup-on-6963f46f

* Para instalar o MongoDB no Ubuntu 16.04

https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04

<sup>Obs: Ao instalar utilizando o apt-get ao invés de apontar o pacote "mongodb-org", use apenas "mongodb"</sup>

<sup>Obs2: Em alguns computadores, o "mongodb-org" funciona. Não sei porquê. Mas vamos usar todos o "mongodb" pra não correr riscos</sup>

* Executando o MongoDB (Ubuntu)

``` cd /usr 
 ./bin/mongo```

ou

```mongo ```

* Criando banco de dados no MongoDB

```use <nome>```

(Serve tanto para criar quanto para selecionar este BD - nome padrão utilizado: supermercado)

* Inserindo dados

https://docs.mongodb.com/getting-started/shell/insert/

Para mais informações, seguir o mesmo tutorial (selecionar dados, etc).

* Criando o usuário admin:

https://docs.mongodb.com/v2.6/tutorial/add-user-administrator/

Sigam o item 2, e criem da seguinte forma (caso usem o banco de dados local para testes):

```usuário: admin ```
```senha: admin123 ```

Façam assim para que o django consiga conectar no bd, já que os arquivos foram configurados dessa forma.