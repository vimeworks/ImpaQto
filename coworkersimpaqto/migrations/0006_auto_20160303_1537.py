# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 20:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coworkersimpaqto', '0005_auto_20160222_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlConsumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('control_minutos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'ordering': ['anio'],
                'verbose_name_plural': 'Resumen del Consumo',
            },
        ),
        migrations.RenameField(
            model_name='contrato',
            old_name='tiempo_sobrante',
            new_name='minutos_mes',
        ),
        migrations.RemoveField(
            model_name='consumo',
            name='contrato',
        ),
        migrations.AddField(
            model_name='consumo',
            name='minutos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='membresia',
            name='modalidad',
            field=models.CharField(choices=[('M', 'Mensual')], max_length=1, verbose_name='Modalidad de la membresía'),
        ),
        migrations.AddField(
            model_name='controlconsumo',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coworkersimpaqto.Contrato', verbose_name='Contrato a elegir'),
        ),
        migrations.AddField(
            model_name='consumo',
            name='control_consumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coworkersimpaqto.ControlConsumo', verbose_name='Control Consumo'),
            preserve_default=False,
        ),
    ]