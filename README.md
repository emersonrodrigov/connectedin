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
    -> configurando rotas

Aule 3
    -> Criar pagina de perfil
    -> Configurando a rota
    -> Utilizando extencao de expressao regular no python
        - url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir')

Aula 4
    -> Primeiros passos com persistência
    -> Criando a classe Perfil usando django.db
    -> comando => python manage.py makemigrations (cria modelo da base de dados)
    -> comando => python manage.py migrate(cria o modelo apos o comando makemigrations)
    -> Criando perfil usando django shell (python manage.py shell)
        >>> perfil = Perfil(nome='Oswaldo', email='oswaldo@oswaldo.com', telefone='n/a', nome_empresa='Alura')
        >>> perfil.save()

Aula 10
    -> Criar aplicacao para administrar usuarios