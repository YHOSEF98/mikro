from typing import Any
from .utils import create_queue, eliminar_queue, editar_queue
from django import http
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

# Create your views here.
def listar_productos(request):
    mikrotik = Mikrotik.objects.all()
    return render(request, 'inventario/base2.html', {'productos': mikrotik})


class MikrotikListView(ListView):
    model = Mikrotik
    template_name = 'mikrotik/servidores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Servidores Mikrotik"
        context["upfooter"] = "Servidores"

        return context

class ServiciosListView(ListView):
    model = servicio
    template_name = 'mikrotik/servicios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Servicios contratados"
        context["upfooter"] = "Servicios"

        return context
    
class ServicioCreateView(CreateView):
    model = servicio
    form_class = ServicioForm
    template_name = 'mikrotik/createform.html'
    success_url = reverse_lazy('servicios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Crear servicio"
        context["upfooter"] = "Servicios"
        context["action"] = "add"
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            mikro_instance = form.cleaned_data['mikro']
            host = mikro_instance.ip
            username = mikro_instance.usuario
            password = mikro_instance.contraseña
            port = mikro_instance.puertoapi
            queue_name = form.cleaned_data['nombre']
            target_ip = form.cleaned_data['ip']
            max_limit = form.cleaned_data['max_limit']

            create_queue(host, username, password, port, queue_name, target_ip, max_limit)

            return super().form_valid(form)
        
class ServicioDeleteView(DeleteView):
    model = servicio
    template_name = 'mikrotik/delete.html'
    success_url = reverse_lazy('servicios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Servicio"
        context["upfooter"] = "Servicios"
        return context
    
    def form_valid(self, form):
            servicio = self.get_object()
            mikro_instance = servicio.mikro
            host = mikro_instance.ip
            username = mikro_instance.usuario
            password = mikro_instance.contraseña
            port = mikro_instance.puertoapi
            queue_name = servicio.nombre

            eliminacion = eliminar_queue(host, username, password, port, queue_name)
            if eliminacion:
                #servicio = self.get_object()  # Obtén la instancia actual del servicio
                servicio.delete()

                return super().form_valid(form)
            else:
                return HttpResponse("no se pudo eliminar la cola")
    

class ServicioUpdateView(UpdateView):
    model = servicio
    form_class = ServicioForm
    template_name = 'mikrotik/createform.html'
    success_url = reverse_lazy('servicios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar servicio"
        context["upfooter"] = "Servicios"
        return context
    
    def form_valid(self, form):
            servicio = self.get_object()
            mikro_instance = servicio.mikro
            host = mikro_instance.ip
            username = mikro_instance.usuario
            password = mikro_instance.contraseña
            port = mikro_instance.puertoapi
            queue_name = servicio.nombre
            target_ip = form.cleaned_data['ip']
            max_limit = form.cleaned_data['max_limit']
            new_name = form.cleaned_data['nombre']

            
            actualizacion = editar_queue(host, username, password, port, queue_name, new_name, target_ip, max_limit)
            if actualizacion:
                return super().form_valid(form)
            else:
                return HttpResponse("No se pudo actualizar la cola")
    
    