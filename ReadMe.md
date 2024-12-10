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

Alterar Django para acessar view home

```bash
mkdir travelpackages/templates
mkdir travelpackages/templates/travelpackages

code travelpackages/templates/travelpackages/home.html

<!DOCTYPE html>
<html lang="pt-BR">
 <head>
  <title>Celke</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 </head>
 <body>
  <h3>Home</h3>
 </body>
</html>


code admin/urls.py

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include('travelpackages.urls')),
]

# Adicionar suporte para servir arquivos de mídia durante desenvolvimento
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


code travelpackages/urls.py

from django.urls import path
from . import views


urlpatterns = [
 path('', views.home, name='home')
]


code travelpackages/views.py

from django.shortcuts import render
from .models import TravelPackage


# Create your views here.

def home(request):
 packages = TravelPackage.objects.all()
 return render(request, 'travelpackages/home.html', {'packages': packages})
```

Instalar FrameWork CSS Bootstrap diretamente no projeto Django

```bash
pip install django-bootstrap-v5

Installing collected packages: soupsieve, django, beautifulsoup4, django-bootstrap-v5
  Attempting uninstall: django
    Found existing installation: Django 5.1.4
    Uninstalling Django-5.1.4:
      Successfully uninstalled Django-5.1.4
Successfully installed beautifulsoup4-4.12.3 django-4.2.17 django-bootstrap-v5-1.0.11 soupsieve-2.6


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
 'bootstrap5',
]


code travelpackages/templates/travelpackages/base.html

{# load the tag library #}
{% load bootstrap5 %}
<!DOCTYPE html>
<html lang="pt-BR">
 <head>
  <title>Celke</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {# load Bootstrap CSS #}
  {% bootstrap_css %}
 </head>
 <body>
  {% block content %}
  {% endblock content %}

  {# load Bootstrap JS #}
  {% bootstrap_javascript %}
 </body>
</html>


code travelpackages/templates/travelpackages/home.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <h4>Pacotes de Viagens</h4>
  </div>
{% endblock content %}
```

Criar/Editar arquivos Templates para carregar/utilizar FrameWork CSS Bootstrap

```bash
code travelpackages/templates/travelpackages/base.html

{# load the tag library #}
{% load bootstrap5 %}
<!DOCTYPE html>
<html lang="pt-BR">
 <head>
  <title>Celke</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {# load Bootstrap CSS #}
  {% bootstrap_css %}
 </head>
 <body>
  {% block content %}
  {% endblock content %}

  {# load Bootstrap JS #}
  {% bootstrap_javascript %}
 </body>
</html>


code travelpackages/templates/travelpackages/home.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <h4>Pacotes de Viagens</h4>

   <div class="row">
    {% for package in packages %}
    <div class="col-md-4 mb-4">
     <div class="card mb-4 shadow">
      {% if package.image %}
      <img
       src="{{ package.image.url }}"
       alt="{{ package.name }}"
       class="card-img-top"
      />
      {% endif %}
     </div>
    </div>
    {% endfor %}
   </div>
  </div>
{% endblock content %}
```

Criar Página Black Friday e Refatorar Templates

```bash
code travelpackages/urls.py

from django.urls import path
from . import views


urlpatterns = [
 path('', views.home, name='home'),
 path('black-friday', views.black_friday, name='black_friday'),
]


code travelpackages/views.py

from django.shortcuts import render
from .models import TravelPackage


# Create your views here.

def home(request):
 packages = TravelPackage.objects.all().order_by('-id')
 return render(request, 'travelpackages/home.html', {'packages': packages})

def black_friday(request):
 packages = TravelPackage.objects.all().order_by('discounted_price')
 return render(request, 'travelpackages/black_friday.html', {'packages': packages})


code travelpackages/templates/travelpackages/black_friday.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <h4>Pacotes de Viagens</h4>

   <div class="row">
    {% for package in packages %}
    <div class="col-md-4 mb-4">
     <div class="card mb-4 shadow">
      {% if package.image %}
      <img
       src="{{ package.image.url }}"
       alt="{{ package.name }}"
       class="card-img-top"
      />
      <div class="card-body text-center">
       <h5 class="card-title">{{ package.name}}</h5>
       <p class="card-text">
        <span class="text-muted"><del><small>
         R$ {{ package.original_price }}
        </small></del></span>
        <span class="text-success">
         R$ {{ package.discounted_price }}
        </span>
       </p>
       <a href="#" class="btn btn-primary btn-sm">
        Mais Detalhes
       </a>
      </div>
      {% endif %}
     </div>
    </div>
    {% endfor %}
   </div>
  </div>
{% endblock content %}


code travelpackages/templates/travelpackages/base.html

{# load the tag library #}
{% load bootstrap5 %}
<!DOCTYPE html>
<html lang="pt-BR" class="h-100">
 <head>
  <title>Celke</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {# load Bootstrap CSS #}
  {% bootstrap_css %}
 </head>
 <body class="d-flex flex-column h-100">
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
   <div class="container">
    <a class="navbar-brand" href="#">
     Celke
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
     <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
       <a class="nav-link active" href="{% url 'home' %}">
        Home
       </a>
      </li>
      <li class="nav-item">
       <a class="nav-link active" href="{% url 'black_friday' %}">
        Black Friday
       </a>
      </li>
     </ul>
     <div class="col-md-3 text-end">
      <a
       target="_blank"
       href="{% url 'admin:index' %}"
       class="btn btn-outline-light me-2"
      >
       LogIn
      </a>
     </div>
    </div>
   </div>
  </nav>

  {% block content %}
  {% endblock content %}

  <footer class="footer mt-auto py-3 bg-light">
   <div class="container text-center">
    <span class="text-muted">
     Copyright &copy; Celke {% now "Y" %}
    </span>
   </div>
  </footer>

  {# load Bootstrap JS #}
  {% bootstrap_javascript %}
 </body>
</html>


code travelpackages/templates/travelpackages/home.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <h4>Pacotes de Viagens</h4>

   <div class="row">
    {% for package in packages %}
    <div class="col-md-4 mb-4">
     <div class="card mb-4 shadow">
      {% if package.image %}
      <img
       src="{{ package.image.url }}"
       alt="{{ package.name }}"
       class="card-img-top"
      />
      <div class="card-body text-center">
       <h5 class="card-title">{{ package.name}}</h5>
       <p class="card-text">
        <span class="text-muted"><del><small>
         R$ {{ package.original_price }}
        </small></del></span>
        <span class="text-success">
         R$ {{ package.discounted_price }}
        </span>
       </p>
       <a href="#" class="btn btn-primary btn-sm">
        Mais Detalhes
       </a>
      </div>
      {% endif %}
     </div>
    </div>
    {% endfor %}
   </div>
  </div>
{% endblock content %}
```

Incluir no Banco de Dados a coluna descrição (descrition)

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
 description = models.TextField(verbose_name="Descrição", blank=True, null=True)
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

Criar Migrações com Alteração no Banco de Dados e Executar Migrações

```bash
python manage.py makemigrations

Migrations for 'travelpackages':
  travelpackages/migrations/0002_alter_travelpackage_options_and_more.py
    - Change Meta options on travelpackage
    - Add field description to travelpackage

python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, travelpackages
Running migrations:
  Applying travelpackages.0002_alter_travelpackage_options_and_more... OK
```

Instalar no projeto Django um Editor WYSIWYG (What You See Is What You Get)

```bash
pip install django-tinymce
```

Incluir no projeto Django o Editor TinyMCE

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
 'bootstrap5',
 'tinymce',
]


code travelpackages/admin.py

from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import TravelPackage


# Register your models here.

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'original_price', 'discounted_price')

 formfield_overrides = {
  models.TextField: {'widget': TinyMCE()}
 }
```

### Stopped in 01:29:30

Criar página detalhe do pacote

```bash
code travelpackages/views.py

from django.shortcuts import render, get_object_or_404
from .models import TravelPackage


# Create your views here.

def home(request):
 packages = TravelPackage.objects.all().order_by('-id')
 return render(request, 'travelpackages/home.html', {'packages': packages})

def black_friday(request):
 packages = TravelPackage.objects.all().order_by('discounted_price')
 return render(request, 'travelpackages/black_friday.html', {'packages': packages})

def package_detail(request, id):
 package = get_object_or_404(TravelPackage, id=id)
 return render(request, 'travelpackages/package_detail.html', {'package': package})


code travelpackages/urls.py

from django.urls import path
from . import views


urlpatterns = [
 path('', views.home, name='home'),
 path('black-friday', views.black_friday, name='black_friday'),
 path('package/<int:id>/', views.package_detail, name='package_detail'),
]


code travelpackages/templates/base.html

{# load the tag library #}
{% load bootstrap5 %}
<!DOCTYPE html>
<html lang="pt-BR" class="h-100">
 <head>
  <title>Celke</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {# load Bootstrap CSS #}
  {% bootstrap_css %}

  <style>
   .list-travel-package {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 10px;
   }

   .title-list-travel-package {
    color: #324688;
    font-optical-sizing: 1.5rem;
    font-weight: bold;
   }

   .title-bar-list-travel-package {
    margin-right: 10px;
    width: 5px;
    height: 45px;
    background-color: #0661a7;
   }
  </style>
 </head>
 <body class="d-flex flex-column h-100">
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
   <div class="container">
    <a class="navbar-brand" href="#">
     Celke
    </a>
    <button
     class="navbar-toggler"
     type="button"
     data-bs-toggle="collapse"
     data-bs-target="#navbarSupportedContent"
     aria-controls="navbarSupportedContent"
     aria-expanded="false"
     aria-label="Toggle navigation"
    >
     <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
     <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
       <a class="nav-link active" href="{% url 'home' %}">
        Home
       </a>
      </li>
      <li class="nav-item">
       <a class="nav-link active" href="{% url 'black_friday' %}">
        Black Friday
       </a>
      </li>
     </ul>
     <div class="col-md-3 text-end">
      <a
       target="_blank"
       href="{% url 'admin:index' %}"
       class="btn btn-outline-light me-2"
      >
       LogIn
      </a>
     </div>
    </div>
   </div>
  </nav>

  {% block content %}
  {% endblock content %}

  <footer class="footer mt-auto py-3 bg-light">
   <div class="container text-center">
    <span class="text-muted">
     Copyright &copy; Celke {% now "Y" %}
    </span>
   </div>
  </footer>

  {# load Bootstrap JS #}
  {% bootstrap_javascript %}
 </body>
</html>


code travelpackages/templates/home.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <div class="mb-2 pt-1 pb-4 list-travel-package">
    <div class="title-bar-list-travel-package"></div>
    <h4 class="title-list-travel-package">Pacotes de Viagens</h4>
   </div>

   <div class="row">
    {% for package in packages %}
    <div class="col-md-4 mb-4">
     <div class="card mb-4 border-light shadow">
      {% if package.image %}
      <img
       src="{{ package.image.url }}"
       alt="{{ package.name }}"
       class="card-img-top"
      />
      <div class="card-body text-center">
       <h5 class="card-title">{{ package.name}}</h5>
       <p class="card-text">
        <span class="text-muted"><del><small>
         R$ {{ package.original_price }}
        </small></del></span>
        <span class="text-success">
         R$ {{ package.discounted_price }}
        </span>
       </p>
       <a
        href="{% url 'package_detail' id=package.id %}"
        class="btn btn-primary btn-sm"
       >
        Mais Detalhes
       </a>
      </div>
      {% endif %}
     </div>
    </div>
    {% endfor %}
   </div>
  </div>
{% endblock content %}


code travelpackages/templates/black_friday.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <div class="mb-2 pt-1 pb-4 list-travel-package">
    <div class="title-bar-list-travel-package"></div>
    <h4 class="title-list-travel-package">Black Friday Prorrogada</h4>
   </div>

   <div class="row">
    {% for package in packages %}
    <div class="col-md-4 mb-4">
     <div class="card mb-4 border-light shadow">
      {% if package.image %}
      <img
       src="{{ package.image.url }}"
       alt="{{ package.name }}"
       class="card-img-top"
      />
      <div class="card-body text-center">
       <h5 class="card-title">{{ package.name}}</h5>
       <p class="card-text">
        <span class="text-muted"><del><small>
         R$ {{ package.original_price }}
        </small></del></span>
        <span class="text-success">
         R$ {{ package.discounted_price }}
        </span>
       </p>
       <a
        href="{% url 'package_detail' id=package.id %}"
        class="btn btn-primary btn-sm"
       >
        Mais Detalhes
       </a>
      </div>
      {% endif %}
     </div>
    </div>
    {% endfor %}
   </div>
  </div>
{% endblock content %}


code travelpackages/templates/package-detail.html

{% extends "travelpackages/base.html" %}
{% block content %}
  <div class="container mt-5">
   <div class="mb-2 pt-1 pb-4 list-travel-package">
    <div class="title-bar-list-travel-package"></div>
    <h4 class="title-list-travel-package">Black Friday Prorrogada</h4>
   </div>

   <div class="row">
    {% for package in packages %}
    <div class="col-md-4 mb-4">
     <div class="card mb-4 border-light shadow">
      {% if package.image %}
      <img
       src="{{ package.image.url }}"
       alt="{{ package.name }}"
       class="card-img-top"
      />
      <div class="card-body text-center">
       <h5 class="card-title">{{ package.name}}</h5>
       <p class="card-text">
        <span class="text-muted"><del><small>
         R$ {{ package.original_price }}
        </small></del></span>
        <span class="text-success">
         R$ {{ package.discounted_price }}
        </span>
       </p>
       <a
        href="{% url 'package_detail' id=package.id %}"
        class="btn btn-primary btn-sm"
       >
        Mais Detalhes
       </a>
      </div>
      {% endif %}
     </div>
    </div>
    {% endfor %}
   </div>
  </div>
{% endblock content %}
```
