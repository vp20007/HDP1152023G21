from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Hola</h1>")

def inflacionUsuario(request):
    return render(request,'html/InflacionUsuario.html')

def seleccionarAnio(request):
    return render(request,'html/SeleccionarAño.html')

def gestionProductos(request):
    return render(request,'html/GestionarProductos.html')

def listaProductos(request,anio):
    anio=Anio.objects.get(numero_Anio=anio)
    canastaR=CanastaBasica.objects.get(id_Anio=anio.id_Anio,tipo_de_zona='Rural')
    canastaU=CanastaBasica.objects.get(id_Anio=anio.id_Anio,tipo_de_zona='Urbana')
    listProdU=Producto.objects.filter(id_Anio=anio.id_Anio,id_Canasta=canastaU.id_CanastaBasica)
    listProdR=Producto.objects.filter(id_Anio=anio.id_Anio,id_Canasta=canastaR.id_CanastaBasica)
    listaMesesU=Mes.objects.filter(id_Anio=anio.id_Anio, id_Canasta=canastaU.id_CanastaBasica)
    listaMesesR=Mes.objects.filter(id_Anio=anio.id_Anio, id_Canasta=canastaR.id_CanastaBasica)
    formR = canastaEditForm(request.POST or None, instance=canastaR)
    formU = canastaEditForm(request.POST or None, instance=canastaU)
    if formR.is_valid() and request.POST:
        formR.save()
        messages.success(request, "Se han almacenado las modificaciones exitosamente!")
    if formU.is_valid() and request.POST:
        formU.save()

        messages.success(request, "Se han almacenado las modificaciones exitosamente!")

    return render(request,'html/ListaDeProductosAdmin.html',context={'listProdU': listProdU, 'listProdR': listProdR, 'listaMesesU': listaMesesU, 'listaMesesR': listaMesesR, 'canastaU':canastaU,'canastaR':canastaR,'formR': formR, 'formU': formU   })

def modificarProductos(request,id):
    producto=Producto.objects.get(id_Producto=id)
    listaMeses=Mes.objects.filter(id_Producto=id,id_Anio=producto.id_Anio, id_Canasta=producto.id_Canasta)
    formulario = productosEditForm(request.POST or None, instance=producto)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        
        messages.success(request, "Se han almacenado las modificaciones exitosamente!")
    
    return render(request,'html/modificarProducto.html', context={'producto': producto,'listaMeses': listaMeses,'formulario': formulario })

def eliminarProducto(request, id):
        producto = Producto.objects.get(id_Producto=id)
        meses=Mes.objects.filter(id_Producto=producto.id_Producto)
        meses.delete()
        temp = producto.nombre_producto
        producto.delete()
        messages.success (request, "Se ha eliminado el producto: " + temp)
        return redirect('GestionarProductos')

def reporteInflacion(request):
    return render(request,'html/Inflacion.html')

def iniciarSesion (request):
    return render(request,'html/iniciar_sesion.html')

def registrarse (request):
    return render(request, 'html/registrarse.html')

def lProductos (request):
    return render(request, 'html/lProductos.html')

def AgregarProducto (request):
    producto = Producto
    mes = Mes
    return render(request,'html/AgregarProducto.html', {'producto': producto, 'mes': mes})


