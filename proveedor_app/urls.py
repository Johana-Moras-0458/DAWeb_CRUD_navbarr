from django.urls import path
from proveedor_app import views

urlpatterns = [
    path('proveedor',views.inicio_vistaProveedor,name='proveedor'),
    path('registrarProveedor/',views.registrarProveedor,name="registrarProveedor"),
    path('seleccionarProveedor/<idproveedor>',views.seleccionarProveedor,name='seleccionarProveedor'),
    path('editarProveedor/',views.editarProveedor,name='editarProveedor'),
    path('borrarProveedor/<idproveedor>',views.borrarProveedor,name='borrarProveedor'),
]
