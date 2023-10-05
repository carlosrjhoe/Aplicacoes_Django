from django.shortcuts import render
from .models import Cavaleiro

# Create your views here.

def index(request):
    # Primeiro, buscamos os cavaleiros
    cavaleiros = Cavaleiro.objects.all()
    
    # Incluímos no contexto
    context = {
        'cavaleiros': cavaleiros
    }

    # Retornamos o template para listar os cavaleiros
    return render(request, 'galeria/index.html', context)

def imagem(request):
    return render(request, 'galeria/imagem.html')