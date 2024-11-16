from django.db import models

# Create your models here.
class Material(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Merenda(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    consumo = models.IntegerField(default=0)  # Quantidade consumida
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
