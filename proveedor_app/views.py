from django.shortcuts import render,redirect
from .models import Proveedor

def inicio_vistaProveedor(request):
    proveedorsitos=Proveedor.objects.all()
    return render (request,'gestionarProveedor.html',{'misProveedores':proveedorsitos})

def registrarProveedor(request):
    idproveedor=request.POST['txtproveedor']
    idpeluche=request.POST['txtpeluche']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txtelefono']
    precio=request.POST['txtprecio']
    horarios=request.POST['txthorario']
    guardarventa=Proveedor.objects.create(idproveedor=idproveedor,idpeluche=idpeluche,nombre=nombre,direccion=direccion,telefono=telefono,precio=precio,horarios=horarios)
    return redirect('proveedor')

def seleccionarProveedor(request,idproveedor):
    proveedor=Proveedor.objects.get(idproveedor=idproveedor)
    return render (request,"editarProveedor.html",{'misproveedores': proveedor})

def editarProveedor(request):
    idproveedor=request.POST['txtproveedor']
    idpeluche=request.POST['txtpeluche']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txtelefono']
    precio=request.POST['txtprecio']
    horarios=request.POST['txthorario']
    PROVEEDOR=Proveedor.objects.get(idproveedor=idproveedor)
    PROVEEDOR.idproveedor=idproveedor
    PROVEEDOR.idpeluche=idpeluche
    PROVEEDOR.nombre=nombre
    PROVEEDOR.direccion=direccion
    PROVEEDOR.telefono=telefono
    PROVEEDOR.precio=precio
    PROVEEDOR.horarios=horarios
    PROVEEDOR.save()
    return redirect('proveedor')

def borrarProveedor(request,idproveedor):
    proveedorr=Proveedor.objects.get(idproveedor=idproveedor)
    proveedorr.delete()
    return  redirect("proveedor")