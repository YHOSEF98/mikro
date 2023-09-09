from django.db import models
from .choices import *

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    tipodocu = models.CharField(max_length=3, choices=tipodocu, default='CC')
    documento = models.CharField(max_length=50, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    departamento = models.CharField(max_length=50, blank=True)
    municipio = models.CharField(max_length=50, blank=True)
    codigopostal = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    corregimiento = models.CharField(max_length=50, blank=True)
    barrio = models.CharField(max_length=50, blank=True)
    correoelectronico= models.EmailField(blank=True)
    telefoo = models.CharField(max_length=50, blank=True)
    celular = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'