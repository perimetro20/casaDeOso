# Generated by Django 2.0.4 on 2018-09-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_auto_20180918_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='modelo',
            field=models.CharField(blank=True, max_length=155, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='brand',
            field=models.CharField(blank=True, max_length=155, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='sku',
            name='part_number',
            field=models.CharField(blank=True, max_length=155, verbose_name='Número de Parte'),
        ),
    ]