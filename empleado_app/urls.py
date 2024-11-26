from django.urls import path
from empleado_app import views

urlpatterns = [
    path('empleado',views.inicio_vistaEmpleado,name='empleado'),
    path('registrarEmpleado/',views.registrarEmpleado,name="registrarEmpleado"),
    path('seleccionarEmpleado/<idempleado>',views.seleccionarEmpleado,name='seleccionarEmpleado'),
    path('editarEmpleado/',views.editarEmpleado,name='editarEmpleado'),
    path('borrarEmpleado/<idempleado>',views.borrarEmpleado,name='borrarEmpleado'),
]
