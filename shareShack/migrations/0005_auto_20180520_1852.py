# Generated by Django 2.0 on 2018-05-20 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shareShack', '0004_auto_20180430_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkout',
            name='due_Back',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
