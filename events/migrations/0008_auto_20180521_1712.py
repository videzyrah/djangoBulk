# Generated by Django 2.0 on 2018-05-21 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180521_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potluck',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Host'),
        ),
    ]
