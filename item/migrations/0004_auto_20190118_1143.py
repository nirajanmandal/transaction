# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 11:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20190118_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='deleted_at',
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2019, 1, 18, 11, 43, 29, 926201, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]
