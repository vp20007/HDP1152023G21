# Generated by Django 3.2 on 2023-06-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InflacionDeCanasta', '0003_mes_id_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='gramos_persona',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]