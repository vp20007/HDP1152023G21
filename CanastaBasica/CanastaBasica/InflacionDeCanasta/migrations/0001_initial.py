# Generated by Django 3.2 on 2023-06-04 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_Admnistrador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_admin', models.CharField(max_length=50)),
                ('correp_admin', models.CharField(max_length=50)),
                ('contra_admin', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'administrador',
            },
        ),
        migrations.CreateModel(
            name='Anio',
            fields=[
                ('id_Anio', models.AutoField(primary_key=True, serialize=False)),
                ('numero_Anio', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'ano',
            },
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id_Gasto', models.AutoField(primary_key=True, serialize=False)),
                ('gasto_mensual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('diferencia', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'gasto',
            },
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id_Mes', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_mes', models.CharField(max_length=50)),
                ('indice_precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_Anio', models.ForeignKey(db_column='id_Anio', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.anio')),
            ],
            options={
                'db_table': 'mes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_Producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('gramos_persona', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_Mes', models.ForeignKey(db_column='id_Mes', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.mes')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='Inflacion',
            fields=[
                ('id_inflacion', models.AutoField(primary_key=True, serialize=False)),
                ('inflacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_Gasto', models.ForeignKey(db_column='id_Gasto', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.gasto')),
            ],
            options={
                'db_table': 'inflacion',
            },
        ),
        migrations.AddField(
            model_name='gasto',
            name='id_Mes',
            field=models.ForeignKey(db_column='id_Mes', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.mes'),
        ),
        migrations.CreateModel(
            name='CanastaBasica',
            fields=[
                ('id_CanastaBasica', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_de_zona', models.CharField(max_length=50)),
                ('integrantes_por_familia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_Anio', models.ForeignKey(db_column='id_Anio', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.anio')),
            ],
            options={
                'db_table': 'canastabasica',
            },
        ),
        migrations.AddField(
            model_name='anio',
            name='id_Producto',
            field=models.ForeignKey(db_column='id_CanastaBasica', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.producto'),
        ),
    ]
