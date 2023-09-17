from django.shortcuts import render
from .models import Fotografia

# Create your views here.
def index(request):
    imagens = Fotografia.objetos.all()
    contexto = {'imagens': imagens}
    return render(request, 'galeria/index.html', contexto)

def imagem(request):
    imagens = Fotografia.objetos.all()
    contexto = {'imagens': imagens}
    return render(request, 'galeria/imagem.html', contexto)