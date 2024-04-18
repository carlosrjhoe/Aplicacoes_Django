from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_medico
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.


def cadastro_medico(request):
    if is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Você já é médico!!')
        return redirect('/medico/abrir_horario.html')
        
        
    if request.method == 'GET':
        context = Especialidades.objects.all()
        return render(request, '/medico/cadastro_medico.html', {'context': context})
    elif request.method == 'POST':
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            cedula_identidade_medica=cim,
            rg=rg,
            foto=foto,
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
            user=request.user
        )

        dados_medico.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso!')
        return redirect('/medico/abrir_horario.html')
    
def abrir_horario(request):
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem abrir horário.')
        return redirect('/usuarios/sair.html')
    
    if request.method == 'GET':
        context = DadosMedico.objects.get(user=request.user)
        return render(request, 'medico/abrir_horario.html', {'context': context})