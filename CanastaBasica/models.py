from django.forms import models
from django.db import models
from django.contrib.auth.models import User

class Adminiatrador(models.Model):
    id_Administrador = models.AutoField(primary_key=True)
    id_CanastaBasica = models.ForeignKey()
    nombre_admin = models.CharField(max_length=100, null=False, blank=False)
    correo_admin = models.CharField(max_length=100, null=False, blank=False)
    contrasena_admin = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre_admin


class CanastaBasica(models.Model):
    id_CanastaBasica = models.AutoField(primary_key=True)
    tipo_de_zona = models.CharField(max_length=50, null=False, blank=False)
    integrantes_por_familia = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    id_Anio1 = models.ForeignKey()
    id_Anio2 = models.ForeignKey()

    def __str__(self):
        return self.id_CanastaBasica


class Producto(models.Model):
    objects = None
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Anio(models.Model):
    id_Anio = models.AutoField(primary_key=True)
    numero_de_anio = models.IntegerField(null=False, blank=False)


    def __str__(self):
        return self.id_Anio


class Mes(models.Model):
    id_Mes = models.AutoField(primary_key=True)
    nombre_mes = models.CharField(max_length=50, null=False, blank=False)
    indice_precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


    def __str__(self):
        return self.id_Mes


class Gasto(models.Model):
    id_Gasto = models.AutoField(primary_key=True)
    gasto_mensual = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    diferencia = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.gasto_mensual


class Inflacion(models.Model):
    id_Inflacion = models.AutoField(primary_key=True)
    inflacion = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.inflacion



