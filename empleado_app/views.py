from django.shortcuts import render,redirect
from .models import Empleado

def inicio_vistaEmpleado(request):
    empleaditos=Empleado.objects.all()
    return render (request,'gestionarEmpleado.html',{'misEmpleados':empleaditos})

def registrarEmpleado(request):
    idempleado=request.POST['txtempleado']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    telefono=request.POST['txtelefono']
    salario=request.POST['txtsalario']
    horario=request.POST['txthorario']
    direccion=request.POST['txtdireccion']
    guardarempleado=Empleado.objects.create(idempleado=idempleado,nombre=nombre,apellido=apellido,telefono=telefono,salario=salario,horario=horario,direccion=direccion)
    return redirect('empleado')

def seleccionarEmpleado(request,idempleado):
    empleado=Empleado.objects.get(idempleado=idempleado)
    return render (request,"editarEmpleado.html",{'misempleados': empleado})

def editarEmpleado(request):
    idempleado=request.POST['txtempleado']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    telefono=request.POST['txtelefono']
    salario=request.POST['txtsalario']
    horario=request.POST['txthorario']
    direccion=request.POST['txtdireccion']
    EMPLEADO=Empleado.objects.get(idempleado=idempleado)
    EMPLEADO.idempleado=idempleado
    EMPLEADO.nombre=nombre
    EMPLEADO.apellido=apellido
    EMPLEADO.telefono=telefono
    EMPLEADO.salario=salario
    EMPLEADO.horario=horario
    EMPLEADO.direccion=direccion
    EMPLEADO.save()
    return redirect('empleado')

def borrarEmpleado(request,idempleado):
    empleadoo=Empleado.objects.get(idempleado=idempleado)
    empleadoo.delete()
    return  redirect("empleado")