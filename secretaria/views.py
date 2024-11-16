from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cadastro_Professor, Cadastro_Aluno, Turma
from django.contrib.messages import constants
from django.contrib import messages  # Importação adicionada
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group



# Create your views here.
def home_secretaria(request):
    if request.method == "GET":
        return render(request, "home_secretaria.html" )
    
def cadastro_professor(request):    
    if is_professor(request.user):
        messages.add_message(request, constants.WARNING, "Você já está cadastrado como Professor")
        return redirect('/professor/home')
    
    if request.method == "GET":
        turma = Turma.objects.all()
        return render(request, "cadastro_professor.html", {"turma": turma})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro= request.POST.get('bairro')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        foto = request.FILES.get('foto')
        turma = request.POST.get('turma')
        
        cadastro_professor = Cadastro_Professor(
            nome=nome,
            rua=rua,
            numero=numero,
            bairro=bairro,
            cep=cep,
            cidade=cidade,
            telefone=telefone,
            celular=celular,
            email=email,
            foto=foto,
            turma_id=turma,
            user=request.user,
            
            
        )
        cadastro_professor.save()
        
        messages.add_message(request, constants.SUCCESS, "Cadastro Realizado com Sucesso")
        return redirect('/secretaria/home_secretaria/')
        
def cadastro_aluno(request):
    if request.method == "GET":
        turma = Turma.objects.all()
        return render(request, "cadastro_aluno.html", {"turma": turma})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        nome_mae = request.POST.get('nome_mae')
        nome_pai = request.POST.get('nome_pai')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        cadunico = request.POST.get('cadunico')
        ra = request.POST.get('ra')
        foto = request.FILES.get('foto')
        turma = request.POST.get('turma')
        periodo = request.POST.get('periodo')
        
        cadastro_aluno = Cadastro_Aluno(
            nome=nome,
            nome_mae=nome_mae,
            nome_pai=nome_pai,
            rua=rua,
            numero=numero,
            bairro=bairro,
            cep=cep,
            cidade=cidade,
            telefone=telefone,
            celular=celular,
            email=email,
            cadunico=cadunico,
            ra=ra,
            foto=foto,
            turma_id=turma,
            periodo=periodo,
        )
        
        cadastro_aluno.save()
        
        messages.add_message(request, constants.SUCCESS, "Cadastro Realizado com Sucesso")
        return redirect('/secretaria/cadastro_aluno/')



def relatorios_secretaria(request):
    if request.method == "GET":
        return render(request, "relatorios_secretaria.html")
    

def relatorios_diarios(request):
    if request.method == "GET":
        return render(request, "relatorios_diarios.html")
    

def filtrar_relatorio_diario(request):
    
    return render(request, 'relatorios_diarios.html', {'turma': "teste","periodo": "testes",'alunos_presentes': 10})
    
    #df = pd.read_excel("C:/Users/Lucae/Documents/teste.xlsx")
    #print(df)

    # teste de implementação de leitura de dataframes excel / sql para alimentação do banco -------------------------------------------------------------------------

    # try:        
    #     turma = HistoricoChamada.filter(turma=turma)
    #     total_alunos_presentes = HistoricoChamada.filter(total_alunos_presentes=total_alunos_presentes).count()
    #     periodo = HistoricoChamada.filter(periodo = periodo)
        
    #     return render(request, 'relatorios_diarios.html', {'turma': turma,'periodo': periodo,'alunos_presentes': total_alunos_presentes})
    # except HistoricoChamada.DoesNotExist:
    #     messages.add_message(request, constants.ERROR, 'Não há histórico de chamadas')
    #     return redirect('/secretaria/relatorios_diarios/')
   
@ login_required
def listar_professores(request):
    # # Permitir acesso apenas para membros da secretaria
    if not request.user.groups.filter(name='Secretaria').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('/')

    professores = Cadastro_Professor.objects.all()
    return render(request, 'listar_professores.html', {'professores': professores}) 


login_required
def editar_professor(request, professor_id):
    # Permitir acesso apenas para membros da secretaria
    if not request.user.groups.filter(name='Secretaria').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('/')

    professor = get_object_or_404(Cadastro_Professor, id=professor_id)
    turmas = Turma.objects.all()

    if request.method == 'GET':
        # Renderizar o formulário com os dados do professor e as turmas
        return render(request, 'cadastro_professor.html', {
            'professor': professor,
            'turmas': turmas,
        })

    elif request.method == 'POST':
        # Atualizar os dados do professor
        professor.nome = request.POST.get('nome')
        professor.rua = request.POST.get('rua')
        professor.numero = request.POST.get('numero')
        professor.bairro = request.POST.get('bairro')
        professor.cep = request.POST.get('cep')
        professor.cidade = request.POST.get('cidade')
        professor.telefone = request.POST.get('telefone')
        professor.celular = request.POST.get('celular')
        professor.email = request.POST.get('email')
        professor.turma_id = request.POST.get('turma')  # Certifique-se de que 'turma' é o name correto no HTML.

        try:
            professor.save()
            messages.success(request, "Dados do professor atualizados com sucesso!")
            return redirect('listar_professores')  # Redirecionar após o salvamento.
        except Exception as e:
            messages.error(request, f"Erro ao salvar os dados: {e}")
        
        # Caso haja erro ao salvar, re-renderize o formulário com os dados preenchidos
        return render(request, 'cadastro_professor.html', {
            'professor': professor,
            'turmas': turmas,
        })


def is_professor(user):
    """
    Verifica se o usuário pertence ao grupo 'Professor'.
    """
    return user.groups.filter(name='Professor').exists()