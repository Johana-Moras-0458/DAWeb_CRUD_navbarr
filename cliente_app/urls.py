from django.urls import path
from cliente_app import views

urlpatterns = [
    path('cliente',views.inicio_vistaCliente,name='cliente'),
    path('registrarCliente/',views.registrarCliente,name="registrarCliente"),
    path('seleccionarCliente/<idcliente>',views.seleccionarCliente,name='seleccionarCliente'),
    path('editarCliente/',views.editarCliente,name='editarCliente'),
    path('borrarCliente/<idcliente>',views.borrarCliente,name='borrarCliente'),
]
