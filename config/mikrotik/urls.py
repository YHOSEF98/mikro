from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("servidores/", MikrotikListView.as_view(), name="mikrotiks"),
    path("servicios", ServiciosListView.as_view(), name="servicios"),
    path("servicio/add", ServicioCreateView.as_view(), name="servicioadd"),
    path('servicio/delete/<int:pk>/', ServicioDeleteView.as_view(), name='eliminar_servicio'),
    path('servicio/edit/<int:pk>/', ServicioUpdateView.as_view(), name='editar_servicio'),
]