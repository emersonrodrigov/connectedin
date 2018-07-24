from os import rename

from django.http import HttpResponse
from django.shortcuts import render
from perfis.models import Perfil
# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    print(f"ID do perfil {perfil_id}")
    perfil = Perfil()

    if(perfil_id == '1'):
        perfil = Perfil('Flavio Almeida', 'flavio@flavio.com.br', '777777', 'Caelum')
    if(perfil_id == '2'):
        perfil = Perfil('Romulo Henrique', 'romulo@romulo.com.br', '888888', 'Caelum')

    return render(request, 'perfil.html', { "perfil" : perfil })