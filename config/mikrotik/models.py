from django.db import models
from clientes.models import Cliente
from django.forms.models import model_to_dict
from .choices import *

# Create your models here.
class Mikrotik(models.Model):
    nombre = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    puertoweb = models.IntegerField()
    puertoapi = models.IntegerField()
    puertowinbox = models.IntegerField()
    interfazWan = models.CharField(max_length=50, null=True, blank=True)
    interfazlan = models.CharField(max_length=50, null=True, blank=True)
    usuario = models.CharField(max_length=60)
    contraseña = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Mikrotik'
        verbose_name_plural = 'Servidores mikrotik'


class Segmentos(models.Model):
    mikro = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    segmento = models.CharField(max_length=18)

    class Meta:
        verbose_name = 'Segmento'
        verbose_name_plural = 'Segmentos de red'


class servicio(models.Model):
    cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mikro = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=15)
    max_limit = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def tojson(self):
        return self.model_to_dict(self)
    
class grupoCorte(models.Model):
    nombre = models.CharField(max_length=50)
    afacturar = models.IntegerField(choices=dia_choices, default=0)
    apagar = models.IntegerField(choices=dia_choices, default=0)
    acortar = models.IntegerField(choices=dia_choices, default=0)
    hora = models.TimeField(default='12:00am')

    class Meta:
        verbose_name = 'Grupo de corte'
        verbose_name_plural = 'Grupos de corte'
    
class planVelocidad(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    velociadad = models.CharField(max_length=9)
    tipo = models.CharField(max_length=1, choices=tipoPlan, default='R')

    class Meta:
        verbose_name = 'Plan de Velocidad'
        verbose_name_plural = 'Planes de Velocidad'