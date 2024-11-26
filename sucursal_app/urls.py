from django.urls import path
from sucursal_app import views

urlpatterns = [
    path('sucursal',views.inicio_vistaSucursal,name='sucursal'),
    path('registrarSucursal/',views.registrarSucursal,name="registrarSucursal"),
    path('seleccionarSucursal/<idsucursal>',views.seleccionarSucursal,name='seleccionarSucursal'),
    path('editarSucursal/',views.editarSucursal,name='editarSucursal'),
    path('borrarSucursal/<idsucursal>',views.borrarSucursal,name='borrarSucursal'),
]
