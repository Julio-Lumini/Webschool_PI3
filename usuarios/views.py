from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.db import transaction
from secretaria.models import Cadastro_Professor


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        perfil = request.POST.get('perfil')
        if not perfil or perfil not in ["professor", "secretaria"]:
            messages.add_message(request, constants.ERROR, 'Perfil inválido ou obrigatório')
            return redirect('/usuarios/cadastro')
        
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas devem ser iguais")
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A Senha precisa conter pelo menos 6 caracteres')
            return redirect('/usuarios/cadastro')
        
        users = User.objects.filter(username=username)
        print(users.exists())
        
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já cadastrado com esse nome')
            return redirect('/usuarios/cadastro')
        
        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
        # Relacione o perfil ao usuário
            if perfil == "professor":
                if hasattr(Cadastro_Professor, 'user'):
                    Cadastro_Professor.objects.create(user=user)
                else:
                    messages.add_message(request, constants.ERROR, 'Erro ao associar perfil de professor')
                    return redirect('/usuarios/cadastro')
            # Membro da secretaria não precisa de model adicional
            return redirect('/usuarios/login')
    
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        
        user = auth.authenticate(request, username=username, password=senha)
        
        if user:
            auth.login(request, user)
            
            # Verifique o perfil
            if Cadastro_Professor.objects.filter(user=user).exists():
                return redirect('/professor/home')  # Página do professor
            else:
                return redirect('/secretaria/home_secretaria')  # Página da secretaria
            
                
        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('/usuarios/login')
    
    
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')








