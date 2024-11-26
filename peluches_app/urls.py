from django.urls import path
from peluches_app import views

urlpatterns = [
    path('peluche',views.inicio_vistaPeluche,name='peluche'),
    path('registrarPeluche/',views.registrarPeluche,name="registrarPeluche"),
    path('seleccionarPeluche/<idpeluche>',views.seleccionarPeluche,name='seleccionarPeluche'),
    path('editarPeluche/',views.editarPeluche,name='editarPeluche'),
    path('borrarPeluche/<idpeluche>',views.borrarPeluche,name='borrarPeluche'),
]
