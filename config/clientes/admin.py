from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Cliente)
# class MikrotikAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'cedula')
#     search_fields = ('nombre', 'cedula')
#     list_filter = ('nombre', 'cedula')

admin.site.register(Cliente)