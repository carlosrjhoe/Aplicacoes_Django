from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'usuarios/cadastro.html')