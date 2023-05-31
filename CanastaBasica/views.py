from django.shortcuts import render, redirect
from models import*
#Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request,'canasta_basica/lista_productos.html',{'productos':productos})

def eliminar_productos(request,id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect('lista_productos')

def registrar_producto(request):
    nombre_producto = None
    descripcion_producto = None
    precio = None
    if(request.method == 'POST'):
        nombre_producto = request.POST['nombre_producto']
        descripcion_producto = request.POST['descripcion_producto']
        precio = request.POST['precio_producto']
        producto = Producto.objects.create(nombre_producto = nombre_producto, descripcion_producto = descripcion_producto, precio_producto = precio)
        producto.save()
        return redirect('lista_productos')
    else:
        return render(request,'CanastaBasic/registrar_producto.html')
