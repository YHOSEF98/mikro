from django import forms
from .models import *

class ServicioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = servicio
        fields = ['cli', 'mikro', 'nombre', 'ip', 'max_limit']

        labels = {
            'cli': 'Cliente',  # Cambiar el nombre del campo
            'mikro': 'Mikrotik',
            'ip': 'Servicio Ip',
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