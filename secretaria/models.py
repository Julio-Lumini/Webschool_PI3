from django.db import models
from django.contrib.auth.models import User



class Turma(models.Model):
    turma = models.CharField(max_length=20)
    
    def __str__(self):
        return self.turma


def is_professor(user):
    return Cadastro_Professor.objects.filter(user=user).exists()

# Create your models here.

class Cadastro_Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associa o professor a um usuário
    nome = models.CharField(max_length=200)
    rua = models.CharField( max_length=50)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField( max_length=50)
    cep = models.CharField(max_length=15 )
    cidade = models.CharField(max_length=50)
    telefone = models.CharField( max_length=50)
    celular = models.CharField(max_length=50 )
    email = models.EmailField( max_length=254)
    foto = models.ImageField( upload_to= "perfil_professor")
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)
    #user= models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.user.username
    
    
class Cadastro_Aluno(models.Model):
    nome = models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)
    nome_pai = models.CharField(max_length=200)
    rua = models.CharField( max_length=50)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=15 )
    cidade = models.CharField (max_length=50)
    telefone = models.CharField(max_length=50)
    celular = models.CharField(max_length=50 )
    email = models.EmailField(max_length=254)
    cadunico = models.CharField(max_length=50)
    ra = models.CharField(max_length=50 )
    foto = models.ImageField(upload_to= "perfil_aluno")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')
    periodo = models.CharField(max_length=20)
    status_presenca = models.IntegerField(default=0)

    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ('nome',)

class HistoricoChamada(models.Model):
    turma = models.CharField(max_length=50)
    data = models.DateField( )
    periodo = models.CharField(max_length=50)
    total_alunos_presentes = models.IntegerField( )
    
    def __str__(self):
        return self.hist_chamada