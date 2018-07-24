"# connectedin" 


Aula 1
 -> Preparando ambientes
    - django-admin.py startproject connectedin => Criando projeto
    - cd connectedin
      python manage.py migrate - Criando BD SQLite
    - python manage.py runserver

 -> Separando as responsabilidades
    - python manage.py startapp perfis => Criando uma aplicação dentro do projeto criado

 -> Registrando a aplicação criado no projeto
    - file: connectedin/connectedin/settings.py
        INSTALLED_APPS = (
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'perfis'
        )

Aula 2
    -> Pagina principal
