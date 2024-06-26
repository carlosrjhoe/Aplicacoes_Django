from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos!')
        return redirect('/usuarios/login/')

def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login/')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha e o confirmar senha deve ser iguais!')
            return redirect('/usuarios/cadastro/')

        if len(senha) < 3:
            messages.add_message(request, constants.ERROR, 'A senha deve ter mais de 6 digitos!')
            return redirect('/usuarios/cadastro/')

        users = User.objects.filter(username=username)
        
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuário ja cadastrado!')
            return redirect('/usuarios/cadastro/')

        user = User.objects.create_user(
            username = username,
            email = email,
            password = senha
        )
        return redirect('/usuarios/login/')