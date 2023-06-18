from django.urls import path
from . import views

urlpatterns = [
   # path('',views.inicio, name='inicio'),
    path('InflacionUsuario',views.inflacionUsuario, name='InflacionUsuario'),
    path('',views.seleccionarAnio, name='SeleccionarAnio'),
    path('GestionarProductos',views.gestionProductos, name='GestionarProductos'),
    path('ListaDeProductosAdmin',views.listaProductos, name='ListaDeProductosAdmin'),
    path('ModificarProductos/<int:id>',views.modificarProductos, name='ModificarProductos'),
    path('ReporteInflacion',views.reporteInflacion, name='ReporteInflacion'),
    path('iniciarSesion', views.iniciarSesion, name='iniciarSesion'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('lProductos18', views.lProductos, name='lProductos18'), ##le movi desde aqui hasta el comentario de abajo
    path('lProductos19', views.lProductos, name='lProductos19'),
    path('lProductos20', views.lProductos, name='lProductos20'),
    path('lProductos21', views.lProductos, name='lProductos21'),
    path('lProductos22', views.lProductos, name='lProductos22'), ##error al realizar el cambio en esta linea (actualizacion, error corregido)
    path('AgregarProducto', views.AgregarProducto, name='AgregarProducto'),
]

