from django.shortcuts import render
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/base2.html', {'productos': productos})
