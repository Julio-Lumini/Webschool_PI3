from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Cadastro_Professor, is_professor, Cadastro_Aluno, Turma
from django.contrib import messages
from django.contrib.messages import constants
import pandas as pd





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
    
   