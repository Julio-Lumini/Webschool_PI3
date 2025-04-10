from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Turma(models.Model):
    turma = models.CharField(max_length=20)
    
    def __str__(self):
        return self.turma

    class Meta:
        verbose_name = _("Turma")
        verbose_name_plural = _("Turmas")


class Cadastro_Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associa o professor a um usuário
    nome = models.CharField(max_length=200)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50, default='', blank=True)
    celular = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    foto = models.ImageField(upload_to="perfil_professor", default='perfil_professor/default_professor.jpg', blank=True, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True, related_name='professores')

    class Meta:
        ordering = ('nome',)
        verbose_name = _("Cadastro de Professor")
        verbose_name_plural = _("Cadastros de Professores")

    def __str__(self):
        return self.user.username


def is_professor(user):
    return Cadastro_Professor.objects.filter(user=user).exists()


class Cadastro_Aluno(models.Model):
    nome = models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)
    nome_pai = models.CharField(max_length=200)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cadunico = models.CharField(max_length=50, default='', blank=True)
    ra = models.CharField(max_length=50, default='', blank=True)
    foto = models.ImageField(upload_to="perfil_aluno", default='perfil_aluno/default_aluno.jpg', blank=True, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name='alunos_cadastro')
    periodo = models.CharField(max_length=20, default='', blank=True)
    status_presenca = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = _("Cadastro de Aluno")
        verbose_name_plural = _("Cadastros de Alunos")


class HistoricoChamada(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    periodo = models.CharField(max_length=50, default='', blank=True)
    total_alunos_presentes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.turma} - {self.data} - {self.periodo}"

    class Meta:
        verbose_name = _("Histórico de Chamada")
        verbose_name_plural = _("Históricos de Chamada")