# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-07 00:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20171206_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potluck',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
