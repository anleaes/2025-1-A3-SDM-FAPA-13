from django.db import models
from condominio.models import Condominio

class Manutencao(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    status = models.CharField(max_length=50)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='manutencoes')

    def __str__(self):
        return f"Manutenção {self.descricao} - {self.data} - {self.condominio.nome}"