# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20181004_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
