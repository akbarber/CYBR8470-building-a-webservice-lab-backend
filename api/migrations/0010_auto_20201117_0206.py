# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-17 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201116_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Breed'),
        ),
    ]
