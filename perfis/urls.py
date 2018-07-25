from django.conf.urls import url
from perfis.views import index, exibir, convidar,aceitar




urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar , name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$',  aceitar, name='aceitar')
]