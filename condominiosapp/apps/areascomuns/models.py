from django.db import models
from condominio.models import Condominio

class AreaComum(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='areascomuns')

    def __str__(self):
        return f"{self.nome} - {self.condominio.nome}"