from django.shortcuts import render,redirect
from .models import Cliente

def inicio_vistaCliente(request):
    clientitos=Cliente.objects.all()
    return render (request,'gestionarCliente.html',{'misClientes':clientitos})

def registrarCliente(request):
    idcliente=request.POST['txtcliente']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    direccion=request.POST['txtdireccion']
    correo=request.POST['txtcorreo']
    telefono=request.POST['txtelefono']
    fecharegistro=request.POST['txtfecha']
    guardarcliente=Cliente.objects.create(idcliente=idcliente,nombre=nombre,apellido=apellido,direccion=direccion,correo=correo,telefono=telefono,fecharegistro=fecharegistro)
    return redirect('cliente')

def seleccionarCliente(request,idcliente):
    cliente=Cliente.objects.get(idcliente=idcliente)
    return render (request,"editarCliente.html",{'misclientes': cliente})

def editarCliente(request):
    idcliente=request.POST['txtcliente']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    direccion=request.POST['txtdireccion']
    correo=request.POST['txtcorreo']
    telefono=request.POST['txtelefono']
    fecharegistro=request.POST['txtfecha']
    CLIENTE=Cliente.objects.get(idcliente=idcliente)
    CLIENTE.idcliente=idcliente
    CLIENTE.nombre=nombre
    CLIENTE.apellido=apellido
    CLIENTE.direccion=direccion
    CLIENTE.correo=correo
    CLIENTE.telefono=telefono
    CLIENTE.fecharegistro=fecharegistro
    CLIENTE.save()
    return redirect('cliente')

def borrarCliente(request,idcliente):
    clientee=Cliente.objects.get(idcliente=idcliente)
    clientee.delete()
    return  redirect("cliente")