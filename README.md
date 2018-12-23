# AplicacaoWeb

Parte de aplicação web do aplicativo para supermercado

## ATENÇÃO: PARA TESTAR TUDO, É BOM TER O MONGODB INSTALADO PARA TESTAR O BANCO DE DADOS LOCAL. Se não tiver, quando der runserver, vai ter erro de conexão com o BD.

### Como subir a aplicação utilizando o Django:

Abra a pasta que se deseja inicializar (por exemplo, login) e utilize:

```python manage.py runserver```

### Requerimentos:
<sup>OBS: Em alguns sistemas é necessário utilizar o comando "pip" com sudo</sup>

* Python 3.6

* Para instalar o MongoDB no Windows

https://code.msdn.microsoft.com/Mongo-Database-setup-on-6963f46f

* Para instalar o MongoDB no Ubuntu 16.04

https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04

<sup>Obs: Ao instalar utilizando o apt-get ao invés de apontar o pacote "mongodb-org", use apenas "mongodb"</sup>

<sup>Obs2: Em alguns computadores, o "mongodb-org" funciona. Não sei porquê. Mas vamos usar todos o "mongodb" pra não correr riscos</sup>

* Executando o MongoDB (Ubuntu)

```

cd /usr

./bin/mongo

```

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

* Instalando os pacotes utilizados:

```pip install -r requirements.txt```
