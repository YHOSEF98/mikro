from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.cedula}'