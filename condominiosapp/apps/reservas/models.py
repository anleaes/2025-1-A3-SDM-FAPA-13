from django.db import models
from moradores.models import Morador
from areascomuns.models import AreaComum

class ReservaAreaComum(models.Model):
    data_reserva = models.DateField()
    status = models.CharField(max_length=20)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='reservas')
    area_comum = models.ForeignKey(AreaComum, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.area_comum.nome} - {self.data_reserva} ({self.morador.nome})"
