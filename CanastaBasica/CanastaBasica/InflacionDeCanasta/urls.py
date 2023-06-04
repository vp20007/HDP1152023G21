from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('InflacionUsuario',views.inflacionUsuario, name='InflacionUsuario'),
    path('SeleccionarAnio',views.seleccionarAnio, name='SeleccionarAnio'),
    path('GestionarProductos',views.gestionProductos, name='GestionarProductos'),
    path('ListaDeProductosAdmin',views.listaProductos, name='ListaDeProductosAdmin'),
    path('ModificarProductos',views.modificarProductos, name='ModificarProductos'),
    path('ReporteInflacion',views.reporteInflacion, name='ReporteInflacion'),
    path('iniciarSesion', views.iniciarSesion, name='iniciarSesion'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('lProductos', views.lProductos, name='lProductos'),
    path('AgregarProducto', views.AgregarProducto, name='AgregarProducto'),
]
]
