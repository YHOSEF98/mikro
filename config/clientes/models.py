from django.db import models
from .choices import *

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    tipodocu = models.CharField(max_length=3, choices=tipodocu, default='CC')
    documento = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    codigopostal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    corregimiento = models.CharField(max_length=50)
    barrio = models.CharField(max_length=50)
    correoelectronico= models.EmailField()
    telefoo = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nombre} - {self.documento}'