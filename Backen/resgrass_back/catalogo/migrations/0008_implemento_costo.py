# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_auto_20170625_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='implemento',
            name='costo',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]