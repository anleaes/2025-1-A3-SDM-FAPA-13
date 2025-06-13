from django.db import models

# Create your models here.

class Condominio(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.TextField('Endereço')
    cnpj = models.CharField('CNPJ', max_length=18)
    quantidade_blocos = models.IntegerField('Quantidade de blocos')

    class Meta:
        verbose_name = 'Condominio'
        verbose_name_plural = 'Condominios'
        ordering = ['id']

    def __str__(self):
        return self.nome