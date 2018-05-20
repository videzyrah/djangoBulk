# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-06 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200, unique=True)),
                ('host', models.CharField(max_length=200)),
                ('facebookPage', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.TextField(max_length=2000)),
            ],
        ),
    ]
