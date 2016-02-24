# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworkersimpaqto', '0003_auto_20160211_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_registro', models.CharField(choices=[('E', 'Entrada'), ('S', 'Salida')], default='E', max_length=1, verbose_name='Registro de ')),
                ('fecha_entrada', models.DateTimeField()),
                ('fecha_salida', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Asistencia',
                'ordering': ['fecha_entrada'],
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='tiempo_sobrante',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='consumo',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coworkersimpaqto.Contrato', verbose_name='Contrato a elegir'),
        ),
    ]