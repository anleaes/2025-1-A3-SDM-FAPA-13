from django.db import models
from condominio.models import Condominio

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    turno = models.CharField(max_length=20)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='funcionarios')

    def __str__(self):
        return f"{self.nome} - {self.funcao} - {self.condominio.nome}"