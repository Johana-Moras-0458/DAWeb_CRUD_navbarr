from django.shortcuts import render,redirect
from .models import Peluche

def inicio_vistaPeluche(request):
    peluchitos=Peluche.objects.all()
    return render (request,'gestionarPeluche.html',{'misPeluches':peluchitos})

def registrarPeluche(request):
    idpeluche=request.POST['txtpeluche']
    idproveedor=request.POST['txtproveedor']
    nombre=request.POST['txtnombre']
    color=request.POST['txtcolor']
    tamaño=request.POST['txtamaño']
    precio=request.POST['txtprecio']
    tipotela=request.POST['txtela']
    idsucursal=request.POST['txtsucursal']
    guardarpeluche=Peluche.objects.create(idproveedor=idproveedor,idpeluche=idpeluche,nombre=nombre,color=color,tamaño=tamaño,tipotela=tipotela,precio=precio,idsucursal=idsucursal)
    return redirect('peluche')

def seleccionarPeluche(request,idpeluche):
    peluche=Peluche.objects.get(idpeluche=idpeluche)
    return render (request,"editarPeluche.html",{'mispeluches':peluche})

def editarPeluche(request):
    idpeluche=request.POST['txtpeluche']
    idproveedor=request.POST['txtproveedor']
    nombre=request.POST['txtnombre']
    color=request.POST['txtcolor']
    tamaño=request.POST['txtamaño']
    precio=request.POST['txtprecio']
    tipotela=request.POST['txtela']
    idsucursal=request.POST['txtsucursal']
    PELUCHE=Peluche.objects.get(idpeluche=idpeluche)
    PELUCHE.idproveedor=idproveedor
    PELUCHE.idpeluche=idpeluche
    PELUCHE.nombre=nombre
    PELUCHE.color=color
    PELUCHE.tamaño=tamaño
    PELUCHE.precio=precio
    PELUCHE.tipotela=tipotela
    PELUCHE.idsucursal=idsucursal
    PELUCHE.save()
    return redirect('peluche')

def borrarPeluche(request,idpeluche):
    peluchee=Peluche.objects.get(idpeluche=idpeluche)
    peluchee.delete()
    return  redirect("peluche")