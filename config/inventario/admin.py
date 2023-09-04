from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)
    list_filter = ('nombre', 'precio',)

admin.site.register(EntradaInventario)
admin.site.register(SalidaInventario)
