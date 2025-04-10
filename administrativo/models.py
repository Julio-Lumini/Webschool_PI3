from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Material(models.Model):
    data_entrada = models.DateField(auto_now_add=True)
    nome_do_produto = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.IntegerField(default=0)


    def __str__(self):
        return self.nome_do_produto


class Merenda(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    consumo = models.IntegerField(default=0)  # Quantidade consumida
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
