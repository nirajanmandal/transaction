# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0004_auto_20190118_1143'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=120)),
                ('total', models.CharField(max_length=120)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='customer.Customer')),
                ('itemname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemname', to='item.Item')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'transactions',
            },
        ),
    ]
