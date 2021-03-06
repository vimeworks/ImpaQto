# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado del contrato')),
            ],
            options={
                'verbose_name_plural': "Planes - Coworker's",
            },
        ),
        migrations.CreateModel(
            name='Coworker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre del Coworker')),
                ('apellido', models.CharField(max_length=250, verbose_name='Apellido del Coworker')),
                ('mail', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Correo Electrónico del Coworker')),
            ],
            options={
                'verbose_name_plural': "Coworker's",
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre de la membresía')),
                ('uso_espacio', models.IntegerField(verbose_name='Uso de Espacio')),
                ('modalidad', models.CharField(choices=[('D', 'Diario'), ('M', 'Mensual'), ('S', 'Semestral'), ('A', 'Anual')], max_length=1, verbose_name='Modalidad de la membresía')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1, verbose_name='Estado de la membresía')),
            ],
        ),
        migrations.AddField(
            model_name='contrato',
            name='coworker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coworkersimpaqto.Coworker', verbose_name='Nombre del Coworkers'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='membresia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coworkersimpaqto.Membresia', verbose_name='Nombre de la membresía'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='contrato',
            order_with_respect_to='coworker',
        ),
    ]
