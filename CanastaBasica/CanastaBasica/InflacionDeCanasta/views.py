from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404


# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Hola</h1>")

def inflacionUsuario(request):
    return render(request,'html/InflacionUsuario.html')
def seleccionarAnio(request):
    return render(request,'html/SeleccionarAño.html')

def gestionProductos(request):
    return render(request,'html/GestionarProductos.html')

def listaProductos(request):
    return render(request,'html/ListaDeProductosAdmin.html')

def modificarProductos(request):
    return render(request,'html/modificarProducto.html')

def reporteInflacion(request):
    return render(request,'html/Inflacion.html')