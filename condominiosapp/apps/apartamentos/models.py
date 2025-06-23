from django.db import models
from blocos.models import Bloco

class Apartamento(models.Model):
    numero = models.CharField(max_length=10)
    andar = models.IntegerField()
    metragem = models.DecimalField(max_digits=5, decimal_places=2)
    vagas_garagem = models.IntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, related_name='apartamentos')

    

    def __str__(self):
        return f"Apartamento {self.numero} - Bloco {self.bloco.nome}"
