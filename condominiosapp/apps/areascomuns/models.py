from django.db import models
from condominio.models import Condominio

class AreaComum(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='areascomuns')

    class Meta:
        verbose_name = 'Área Comum'
        verbose_name_plural = 'Áreas Comuns'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - {self.condominio.nome}"
