from django.shortcuts import render,redirect
from .models import Sucursal

def inicio_vistaSucursal(request):
    sucursalitos=Sucursal.objects.all()
    return render (request,'gestionarSucursal.html',{'misSucursales':sucursalitos})

def registrarSucursal(request):
    idsucursal=request.POST['txtsucursal']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txtelefono']
    idempleado=request.POST['txtempleado']
    horario=request.POST['txthorario']
    correo=request.POST['txtcorreo']
    guardarsucursal=Sucursal.objects.create(idsucursal=idsucursal,nombre=nombre,direccion=direccion,telefono=telefono,horario=horario,idempleado=idempleado,correo=correo)
    return redirect('sucursal')

def seleccionarSucursal(request,idsucursal):
    sucursal=Sucursal.objects.get(idsucursal=idsucursal)
    return render (request,"editarSucursal.html",{'missucursales': sucursal})

def editarSucursal(request):
    idsucursal=request.POST['txtsucursal']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txtelefono']
    idempleado=request.POST['txtempleado']
    horario=request.POST['txthorario']
    correo=request.POST['txtcorreo']
    SUCURSAL=Sucursal.objects.get(idsucursal=idsucursal)
    SUCURSAL.idsucursal=idsucursal
    SUCURSAL.nombre=nombre
    SUCURSAL.direccion=direccion
    SUCURSAL.telefono=telefono
    SUCURSAL.idempleado=idempleado
    SUCURSAL.horario=horario
    SUCURSAL.correo=correo
    SUCURSAL.save()
    return redirect('sucursal')

def borrarSucursal(request,idsucursal):
    sucursall=Sucursal.objects.get(idsucursal=idsucursal)
    sucursall.delete()
    return  redirect("sucursal")