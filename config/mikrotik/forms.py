from django import forms
from .models import *

class ServicioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = servicio
        fields = ['cli', 'mikro', 'nombre', 'ip', 'plan']

        labels = {
            'cli': 'Cliente',  # Cambiar el nombre del campo
            'mikro': 'Mikrotik',
            'ip': 'Servicio Ip',
            'plan': 'Plan de velocidad',
        }
        
class MikrotikForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mikrotik
        fields = ['nombre', 'ip', 'puertoweb', 'puertoapi', 'puertowinbox', 'interfazWan', 'interfazlan', 'usuario', 'contraseña']

        labels = {
            'nombre': 'Nombre del Mikrotik',  # Cambiar el nombre del campo
            'ip': 'Direccion IP',
            'puertoweb': 'Puerto Web',
            'puertoapi': 'Puerto Api',
            'puertowinbox': 'Puerto Winbox',
            'interfazWan': 'Interfaz Wan',
            'interfazlan': 'Interfaz Lan',
            'usuario': 'Usuario',
            'contraseña': 'Contraseña',
        }   

class planVelocidadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = planVelocidad
        fields = ['nombre', 'precio', 'velocidad', 'tipo', 'burst_limit', 'limit_at', 'burst_threshold', 'burst_time', 'priority']

        labels = {
            'nombre': 'Nombre del Plan',  # Cambiar el nombre del campo
            'precio': 'Precio del plan',
            'velocidad': 'Velocidad',
            'tipo': 'Tipo de plan',
            'burst_limit': 'Burst limit',
            'limit_at': 'Limit at',
            'burst_threshold': 'Burst threshold',
            'burst_time': 'Burst time',
            'priority': 'Priority',
        }


    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    velocidad = models.CharField(max_length=9)
    tipo = models.CharField(max_length=1, choices=tipoPlan, default='R')
    burst_limit = models.CharField(max_length=7, default='0/0')
    limit_at = models.CharField(max_length=7, default='0/0')
    burst_threshold = models.CharField(max_length=13, default='0/0')
    burst_time = models.CharField(max_length=5, default='0/0')
    priority = models.CharField(max_length=3, default='8/8')