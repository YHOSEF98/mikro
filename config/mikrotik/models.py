from django.db import models
from clientes.models import Cliente
from django.forms.models import model_to_dict

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
        return f'{self.nombre}'


class Segmentos(models.Model):
    mikro = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    segmento = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.segmento} - {self.mikro}'


class servicio(models.Model):
    cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mikro = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True)
    ip = models.CharField(max_length=15)
    max_limit = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.ip} - {self.cli}'
    
    def tojson(self):
        return self.model_to_dict(self)