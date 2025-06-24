from django.db import models
from apartamentos.models import Apartamento

class Morador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='moradores')

    def __str__(self):
        return f"{self.nome} - Apartamento {self.apartamento.numero}"