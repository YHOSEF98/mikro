from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("servidores/", MikrotikListView.as_view(), name="mikrotiks"),
    path("servidores/add", MikrotikCreateView.as_view(), name="mikrotiksadd"),
    path("servidores/detail/<int:pk>", MikrotikDetailView.as_view(), name="detailmikro"),
    path("servidores/reglascorte/<int:pk>", MikrotikreglasView.as_view(), name="reglas-corte"),
    path("servicios", ServiciosListView.as_view(), name="servicios"),
    path("servicio/add", ServicioCreateView.as_view(), name="servicioadd"),
    path('servicio/delete/<int:pk>/', ServicioDeleteView.as_view(), name='eliminar_servicio'),
    path('servicio/edit/<int:pk>/', ServicioUpdateView.as_view(), name='editar_servicio'),
]