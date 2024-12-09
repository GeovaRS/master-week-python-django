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

Remover o diretório do cache do GIT.

```bash
git rm --cached -r admin/__pycache__/
```
