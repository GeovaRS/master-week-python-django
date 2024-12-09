# Django do Zero

## Requisitos

* Python 3 ou superior - Conferir a versão:

```bash
python --version
```

* PIP - Conferir a versão:

```bash
pip --version
```

* Pasta de Trabalho - Criar Pasta:

```bash
mkdir master-week
cd master-week

mkdir django-do-zero
cd django-do-zero
```

* Virtual Environment - Criar Ambiente Virtual:

```bash
python -m venv venv
```

* Virtual Environment - Ativar Ambiente Virtual:

```bash
source venv/bin/activate
```

* PIP - Conferir a versão:

```bash
pip --version
```

* Django - Instalar o Django em Ambiente Virtual (Recomendado):

```bash
pip install django
```

* Django 5 ou superior - Conferir a versão:

```bash
django-admin --version
```

Criar o projeto com Django.

```bash
django-admin startproject admin .
```

* Alterar Linguagem e TimeZone do Django para Português do Brasil

```bash
code admin/settings.py

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True
```

Executar as migrations para criar as tabelas.

```bash
python manage.py migrate
```

Criar o super usuário.

```bash
python manage.py createsuperuser

Username (leave blank to use 'cesar'): admin
Email address: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Rodar o projeto.

```bash
python manage.py runserver
```

Acessar a página padrão criada com Django.

```bash
http://127.0.0.1:8000
```

Acessar o sistema administrativo padrão do Django.

```bash
http://127.0.0.1:8000/admin

Usuário: admin
Senha: 123456A#
```

```bash
pip freeze > requirements.txt

pip install -r requirements.txt
```

* Virtual Environment - Desativar Ambiente Virtual:

```bash
deactivate
```

* MySQL 8 ou superior - Conferir a versão:

```bash
mysql --version
```

## Como rodar o projeto baixado

* MySQLClient - Instalar o Cliente MySQL:

```bash
pip install mysqlclient
```

Alterar no arquivo "settings.py" as credenciais do banco de dados.

```bash
# DATABASES = {
#  'default': {
#   'ENGINE': 'django.db.backends.sqlite3',
#   'NAME': BASE_DIR / 'db.sqlite3',
#  }
# }

DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.mysql',
  'HOST': '127.0.0.1',
  'NAME': 'nome-do-banco-de-dados',
  'USER': 'usuario-do-banco-de-dados',
  'PASSWORD': 'senha-do-usuario-do-banco-de-dados',
  'PORT': '3306',
 }
}
```

Executar as migrations para criar as tabelas.

```bash
python manage.py migrate
```

Rodar o projeto.

```bash
python manage.py runserver
```

Acessar a página padrão criada com Django.

```bash
http://127.0.0.1:8000
```

Criar o super usuário.

```bash
python manage.py createsuperuser

Username (leave blank to use 'cesar'): admin
Email address: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo padrão do Django.

```bash
http://127.0.0.1:8000/admin

Usuário: admin
Senha: 123456A#
```

## Sequencia para criar o projeto

Instalar o Django.

```bash
pip install Django
```

Criar o projeto com Django.

```bash

django-admin startproject admin .
```

Rodar o projeto.

```bash
python manage.py runserver
```

Acessar a página padrão criada com Django.

```bash
http://127.0.0.1:8000
```

Instalar o conector MySQL.

```bash
pip install mysqlclient
```

Criar a base de dados.

```bash
CREATE DATABASE celke CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

GRANT ALL PRIVILEGES ON `celke`.* TO 'celke'@'%'; ALTER USER 'celke'@'%' ;
```

Alterar no arquivo "settings.py" as credenciais do banco de dados.

```bash
code admin/settings/py

# DATABASES = {
#  'default': {
#   'ENGINE': 'django.db.backends.sqlite3',
#   'NAME': BASE_DIR / 'db.sqlite3',
#  }
# }

'ENGINE': 'django.db.backends.mysql',
'HOST': '127.0.0.1',
'PORT': '3306'
'NAME': 'celke',
'USER': 'celke',
'PASSWORD': '123456A#',
```

Executar as migrations para criar as tabelas.

```bash
python manage.py migrate
```

Criar o super usuário.

```bash
python manage.py createsuperuser

Username (leave blank to use 'cesar'): admin
Email address: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo padrão do Django.

```bash
http://127.0.0.1:8000/admin
```

## Como usar o GitHub

Inicializar um novo repositorio GIT.

```bash
git init
```

Adicionar todos os arquivos modificados na área de preparação.

```bash
git add .
```

Commit registra alterações nos arquivos adicionados na área de preparação.

```bash

git commit -m "Base do projeto"
```

Verificar em qual branch está.

```bash
git branch
```

Renomear a branch atual no GIT para main.

```bash
git branch -M main
```

Adicionar um repositório remoto ao repositório local.

```bash
git remote add origin https://github.com/celkecursos/master-week-python-e-django.git
```

Enviar os commits locais para um repositório remoto.

```bash
git push -u origin main
```

Remover o arquivo do cache do GIT.

```bash
git rm --cached db.sqlite3
```

Remover o diretório do cache do GIT e venv.

```bash
git rm --cached -r admin/__pycache__/

git rm --cached -r venv/
```

Criar Novo App

```bash
python manage.py startapp travelpackages
```

Incluir App no arquivo admin/settings.py

```bash
code admin/settings.py

# Application definition

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'travelpackages',
]
```

Instalar Biblioteca para Trabalhar com ImageField

```bash
pip install pillow
```

Editar arquivo travelpackages/models.py

```bash
code travelpackages/models.py

from django.db import models
import os

# Create your models here.

class TravelPackage(models.Model):
 name = models.CharField(max_length=255, verbose_name="Nome")
 original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Original")
 discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço com Desconto")
 image = models.ImageField(upload_to="travelpackages", verbose_name="Imagem")
 created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
 updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado em")

 # Sobrescrever o Método save no Modelo
 def save(self, *args, **kwargs):
  # Verificar se o objeto já existe no banco de dados
  if self.pk:
   # Buscar o objeto atual no banco de dados
   old_image = TravelPackage.objects.get(pk=self.pk).image

   # Comparar se a imagem foi alterada
   if old_image and old_image != self.image:
    # Remover a imagem antiga do sistema de arquivos
     if os.path.isfile(old_image.path):
      os.remove(old_image.path)

  # Salvar novo registro
  super().save(*args, **kwargs)

 # Sobrescrever o Método delete do Django para Remover a Imagem
 def delete(self, *args, **kwargs):
  # Remover a imagem associada ao objeto
  if self.image and os.path.isfile(self.image.path):
   os.remove(self.image.path)

  # Excluir o registro
  super().delete(*args, **kwargs)

 def __str__(self):
  return self.name

 class Meta:
  db_table = "travelpackages"
  verbose_name = "pacote de viagem"
  verbose_name_plural = "pacotes de viagens"
```

Editar arquivo admin/settings.py

```bash
code admin/settings.py

from pathlib import Path
import os

...

# Diretório base para arquivos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Criar Migrações do Aplicativo

```bash
python manage.py makemigrations travelpackages --name travelpackages

Migrations for 'travelpackages':
  travelpackages/migrations/0001_travelpackages.py
    + Create model TravelPackage
```

Executar as migrations para criar as tabelas.

```bash
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, travelpackages
Running migrations:
  Applying travelpackages.0001_travelpackages... OK
```

Registrar o models do App TravelPackage

```bash
code travelpackages/admin.py

from django.contrib import admin
from .models import TravelPackage

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'original_price', 'discounted_price')
```

Registrar o models do App TravelPackage

```bash
code travelpackages/apps.py

from django.apps import AppConfig


class TravelpackagesConfig(AppConfig):
 default_auto_field = 'django.db.models.BigAutoField'
 name = 'travelpackages'
 verbose_name = 'pacote de viagem'
```

Alterar Django para acessar Mídias em modo Desenvolvimento (DEBUG=True)

```bash
code travelpackages/urls.py

"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views.
For more information please see:
 https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
 1. Add an import:
 from my_app import views
 2. Add a URL to urlpatterns:
 path('', views.home, name='home')
Class-based views
 1. Add an import:
 from other_app.views import Home
 2. Add a URL to urlpatterns:
 path('', Home.as_view(), name='home')
Including another URLconf
 1. Import the include() function:
 from django.urls import include, path
 2. Add a URL to urlpatterns:
 path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('admin/', admin.site.urls),
]

# Adicionar suporte para servir arquivos de mídia durante modo desenvolvimento
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
