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
       