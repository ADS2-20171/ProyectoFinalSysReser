# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('detalle_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.DetalleReserva')),
            ],
            options={
                'verbose_name_plural': 'Comprobantes',
                'verbose_name': 'Comprobante',
            },
        ),
    ]