from django.db import models
from condominio.models import Condominio

# Create your models here.

class Bloco(models.Model):
    nome = models.CharField(max_length=50)
    numero = models.IntegerField()
    qtd_apartamentos = models.IntegerField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='blocos')

    class Meta:
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - Bloco {self.numero}"