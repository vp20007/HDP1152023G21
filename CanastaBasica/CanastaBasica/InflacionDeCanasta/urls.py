from django.urls import path
from . import views

urlpatterns = [
   # path('',views.inicio, name='inicio'),
    path('InflacionUsuario',views.inflacionUsuario, name='InflacionUsuario'),
    path('',views.seleccionarAnio, name='SeleccionarAnio'),
    path('GestionarProductos',views.gestionProductos, name='GestionarProductos'),
    path('ListaDeProductosAdmin',views.listaProductos, name='ListaDeProductosAdmin'),
    path('ModificarProductos',views.modificarProductos, name='ModificarProductos'),
    path('ReporteInflacion',views.reporteInflacion, name='ReporteInflacion'),
    path('iniciarSesion', views.iniciarSesion, name='iniciarSesion'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('lProductos/2018', views.lProductos, name='lProductos18'),
    path('lProductos/2019', views.lProductos, name='lProductos19'),
    path('lProductos/2020', views.lProductos, name='lProductos20'),
    path('lProductos/2021', views.lProductos, name='lProductos21'),
    path('lProductos/2022', views.lProductos, name='lProductos'),
    path('AgregarProducto', views.AgregarProducto, name='AgregarProducto'),
]

