# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_auto_20170625_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='precio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='implemento',
            name='costo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
