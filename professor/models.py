from django.db import models
from django.contrib.auth.models import User
from secretaria.models import Cadastro_Aluno

# Create your models here.
class Presenca(models.Model):
    aluno = models.ForeignKey(Cadastro_Aluno, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)