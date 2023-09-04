from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Mikrotik)
class MikrotikAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ip', 'puertoapi')
    search_fields = ('nombre',)
    list_filter = ('nombre', 'ip',)

@admin.register(servicio)
class servicioAdmin(admin.ModelAdmin):
    list_display = ('cli', 'ip', 'mikro')
    search_fields = ('cli', 'ip', 'mikro')
    list_filter = ('cli', 'ip', 'mikro',)