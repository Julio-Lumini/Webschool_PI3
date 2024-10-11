from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Presenca
from secretaria.models import Cadastro_Aluno, Cadastro_Professor
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from datetime import date

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

login_required
def chamada(request ):
    try:
        professor = Cadastro_Professor.objects.get(user=request.user)
        alunos = Cadastro_Aluno.objects.filter(turma=professor.turma)
        data_hoje = date.today().strftime("%d/%m/%Y")

        return render(request, 'chamada.html', {'professor': professor, 'alunos': alunos, 'data_hoje': data_hoje,})
    except Cadastro_Professor.DoesNotExist:
        messages.add_message(request, constants.ERROR, 'Você não é um Professor Cadastrado')
        return redirect('/usuarios/login')
    


@login_required
def atualizar_presenca(request):
    if request.method == 'POST':
        professor = Cadastro_Professor.objects.get(user=request.user)
        alunos = Cadastro_Aluno.objects.filter(turma=professor.turma)
        for aluno in alunos:
            presenca_key = f'presenca_{aluno.id}'
            if presenca_key in request.POST:
                aluno.status_presenca = 1  # Marcado como presente
            else:
                aluno.status_presenca = 0  # Marcado como ausente
            aluno.save()
        return redirect('chamada')



@login_required
def gerar_relatorio(request):
    try:
        professor = Cadastro_Professor.objects.get(user=request.user)
        alunos = Cadastro_Aluno.objects.filter(turma=professor.turma)
        
        total_presente = alunos.filter(status_presenca=1).count()
        total_ausente = alunos.filter(status_presenca=0).count()
        data_hoje = date.today().strftime("%d/%m/%Y")
        
        return render(request, 'relatorio.html', {'professor': professor,'alunos': alunos,'total_presente': total_presente,'total_ausente': total_ausente,'data_hoje': data_hoje,})
    except Cadastro_Professor.DoesNotExist:
        messages.add_message(request, constants.ERROR, 'Você não é um Professor Cadastrado')
        return redirect('/usuarios/login')