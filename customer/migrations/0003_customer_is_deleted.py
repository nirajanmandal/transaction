# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-25 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190123_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
