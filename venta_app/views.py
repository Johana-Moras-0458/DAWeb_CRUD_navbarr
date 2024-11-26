from django.shortcuts import render,redirect
from .models import Ventas

def inicio_vistaVenta(request):
    ventitas=Ventas.objects.all()
    return render (request,'gestionarVenta.html',{'misVentas':ventitas})

def registrarVenta(request):
    idventa=request.POST['txtventa']
    idempleado=request.POST['txtempleado']
    idproducto=request.POST['txtproducto']
    idcliente=request.POST['txtcliente']
    idsucursal=request.POST['txtsucursal']
    total=request.POST['txt_total']
    fechacompra=request.POST['txtfecha']
    guardarventa=Ventas.objects.create(idventa=idventa,idempleado=idempleado,idproducto=idproducto,idcliente=idcliente,idsucursal=idsucursal,total=total,fechacompra=fechacompra)
    return redirect('venta')

def seleccionarVenta(request,idventa):
    venta=Ventas.objects.get(idventa=idventa)
    return render (request,"editarVenta.html",{'misventas': venta})

def editarVenta(request):
    idventa=request.POST['txtventa']
    idempleado=request.POST['txtempleado']
    idproducto=request.POST['txtproducto']
    idcliente=request.POST['txtcliente']
    idsucursal=request.POST['txtsucursal']
    total=request.POST['txt_total']
    fechacompra=request.POST['txtfecha']
    VENTA=Ventas.objects.get(idventa=idventa)
    VENTA.idempleado=idempleado
    VENTA.idproducto=idproducto
    VENTA.idcliente=idcliente
    VENTA.idsucursal=idsucursal
    VENTA.total=total
    VENTA.fechacompra=fechacompra
    VENTA.save()
    return redirect('venta')

def borrarVenta(request,idventa):
    ventaa=Ventas.objects.get(idventa=idventa)
    ventaa.delete()
    return  redirect("venta")