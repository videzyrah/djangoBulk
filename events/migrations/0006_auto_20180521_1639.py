# Generated by Django 2.0 on 2018-05-21 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180521_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='host',
            new_name='name',
        ),
    ]
