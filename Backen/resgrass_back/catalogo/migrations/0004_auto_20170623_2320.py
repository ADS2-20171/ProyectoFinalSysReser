# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-23 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_local_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCancha',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'TipoCanchas',
                'verbose_name': 'TipoCancha',
            },
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
    ]
