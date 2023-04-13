from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "Foto do telescopio NASA"},
        2: {"nome": "Galaxias",
            "legenda": "Foto do telescopio NASA/ hubble"}
    }

    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')

