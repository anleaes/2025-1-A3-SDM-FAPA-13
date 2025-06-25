from django.db import models
from moradores.models import Morador

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return f"{self.nome} - {self.data} - {self.morador.nome}"
