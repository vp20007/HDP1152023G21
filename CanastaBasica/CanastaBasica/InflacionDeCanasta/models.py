from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


# Modelo Administrador
class Administrador(models.Model):
    id_Admnistrador = models.AutoField(primary_key=True)
    nombre_admin = models.CharField(max_length=50)
    correp_admin = models.CharField(max_length=50)
    contra_admin = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'administrador'
        
    def __str__(self):
        return self.nombre_admin


# Modelo Mes
class Mes(models.Model):
    id_Mes = models.AutoField(primary_key=True)
    nombre_mes = models.CharField(max_length=50)
    indice_precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_Producto=models.ForeignKey('Producto', on_delete=models.PROTECT, null=True, blank=True, db_column='id_Producto')
    id_Anio=models.ForeignKey('Anio', on_delete=models.PROTECT, null=True, blank=True, db_column='id_Anio')
    id_Canasta=models.ForeignKey('CanastaBasica', on_delete=models.PROTECT, null=True, blank=True, db_column='id_Canasta')

    class Meta:
        db_table = 'mes'
    
    
    


# Modelo Producto
class Producto(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    gramos_persona = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    id_Canasta=models.ForeignKey('CanastaBasica', on_delete=models.PROTECT, null=True, blank=True, db_column='id_Canasta')
    id_Anio=models.ForeignKey('Anio', on_delete=models.PROTECT, null=True, blank=True, db_column='id_Anio')
    
    
    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre_producto
    
# Modelo Anio
class Anio(models.Model):
    id_Anio = models.AutoField(primary_key=True)
    numero_Anio = models.IntegerField(max_length=10)
  #  id_Producto = models.ForeignKey(Producto, on_delete=models.PROTECT,
   #                                     db_column='id_Producto')
    
    class Meta:
        db_table = 'anio'

    def __str__(self):
        return self.id_Anio
    
    
# Modelo Gasto
class Gasto(models.Model):
    id_Gasto = models.AutoField(primary_key=True)
    id_Canasta = models.ForeignKey('CanastaBasica', on_delete=models.PROTECT, null=True, blank=True,
                                        db_column='id_CanaSta')
    gasto_mensual = models.DecimalField(max_digits=10, decimal_places=2)
  # diferencia = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    class Meta:
        db_table = 'gasto'

    def __str__(self):
        return self.id_Gasto

# Modelo Inflacion   
class Inflacion(models.Model):
    id_inflacion = models.AutoField(primary_key=True)
    inflacion = models.DecimalField(max_digits=10, decimal_places=2)
    id_Canasta = models.ForeignKey('CanastaBasica', on_delete=models.PROTECT, null=True, blank=True,
                                     db_column='id_Canasta')
    id_Gasto= models.ForeignKey(Gasto, on_delete=models.PROTECT, null=True, blank=True,
                                        db_column='id_Febrero')  
    class Meta:
        db_table = 'inflacion'

    def __str__(self):
        return self.id_inflacion

# Modelo CanastaBasica
class CanastaBasica(models.Model):
    id_CanastaBasica = models.AutoField(primary_key=True)
    tipo_de_zona = models.CharField(max_length=50)
    integrantes_por_familia = models.DecimalField(max_digits=10, decimal_places=2)
    id_Anio = models.ForeignKey(Anio, on_delete=models.PROTECT,
                                        db_column='id_Anio')
    
    class Meta:
        db_table = 'canastabasica'

    def __str__(self):
        return self.id_CanastaBasica



