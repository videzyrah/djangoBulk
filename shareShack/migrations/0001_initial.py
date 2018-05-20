# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-01 05:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cardnumber', models.IntegerField()),
                ('dateJoined', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='checkOuts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateIssued', models.DateField()),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareShack.Borrower')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writtenId', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('donor', models.CharField(max_length=30)),
                ('dateAdded', models.DateField()),
                ('condition', models.TextField(blank=True, max_length=200, null=True)),
                ('inStock', models.BooleanField(default=True)),
                ('dueBack', models.DateField()),
                ('checkedOutTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareShack.Borrower')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareShack.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('contactPerson', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='returns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateReturned', models.DateField()),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareShack.Borrower')),
                ('items', models.ManyToManyField(to='shareShack.Item')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkouts',
            name='items',
            field=models.ManyToManyField(to='shareShack.Item'),
        ),
        migrations.AddField(
            model_name='checkouts',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='borrower',
            name='memberOf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareShack.Organization'),
        ),
    ]