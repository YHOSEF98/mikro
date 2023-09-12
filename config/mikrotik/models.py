from typing import Any
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

    def __str__(self):
        return f'{self.nombre} - {self.ip}'

    class Meta:
        verbose_name = 'Mikrotik'
        verbose_name_plural = 'Servidores mikrotik'


class Segmentos(models.Model):
    mikro = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    segmento = models.CharField(max_length=18)

    class Meta:
        verbose_name = 'Segmento'
        verbose_name_plural = 'Segmentos de red'

    
class grupoCorte(models.Model):
    nombre = models.CharField(max_length=50)
    afacturar = models.CharField(max_length=2, choices=dia_choices)
    apagar = models.CharField(max_length=2, choices=dia_choices)
    acortar = models.CharField(max_length=2, choices=dia_choices)
    hora = models.TimeField(default='23:59:59')

    class Meta:
        verbose_name = 'Grupo de corte'
        verbose_name_plural = 'Grupos de corte'

    def __str__(self):
            return f'{self.nombre} - {self.acortar}'
    
class planVelocidad(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    velocidad = models.CharField(max_length=9)
    tipo = models.CharField(max_length=1, choices=tipoPlan, default='R')
    burst_limit = models.CharField(max_length=7, default='0/0')
    limit_at = models.CharField(max_length=7, default='0/0')
    burst_threshold = models.CharField(max_length=13, default='0/0')
    burst_time = models.CharField(max_length=5, default='0/0')
    priority = models.CharField(max_length=3, default='8/8')

    class Meta:
        verbose_name = 'Plan de Velocidad'
        verbose_name_plural = 'Planes de Velocidad'

    def __str__(self):
            return f'{self.nombre} - {self.velocidad}'
    



class servicio(models.Model):
    cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mikro = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=15)
    plan = models.ForeignKey(planVelocidad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def tojson(self):
        return self.model_to_dict(self)
    
    def __str__(self):
        return f'{self.cli} - {self.mikro}'