# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0002_trip_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cUsers', to='travelApp.User'),
            preserve_default=False,
        ),
    ]
