# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-09 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodCosts', '0002_auto_20180706_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='conversion_Factor',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='market_Unit_Price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='market_Unit_To_Recipe_Unit_Conversion_Type',
            field=models.CharField(max_length=200),
        ),
    ]
