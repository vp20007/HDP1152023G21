# Generated by Django 3.2 on 2023-06-04 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InflacionDeCanasta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anio',
            name='id_Producto',
            field=models.ForeignKey(db_column='id_Producto', on_delete=django.db.models.deletion.PROTECT, to='InflacionDeCanasta.producto'),
        ),
    ]
