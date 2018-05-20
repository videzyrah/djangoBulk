# Generated by Django 2.0 on 2018-04-30 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarianish', models.BooleanField(default=False)),
                ('lactose_Free', models.BooleanField(default=False)),
                ('paleo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('market_Unit_Price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('market_Package_Type', models.CharField(max_length=200)),
                ('market_Unit_To_Recipe_Unit_Conversion_Type', models.CharField(max_length=200, unique=True)),
                ('conversion_Factor', models.DecimalField(decimal_places=3, max_digits=5)),
                ('retailer', models.CharField(max_length=200, unique=True)),
                ('updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField(max_length=500)),
                ('meals', models.ManyToManyField(to='foodCosts.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('quantities', models.CharField(default='admin', max_length=200)),
                ('instructions', models.TextField(max_length=1000)),
                ('created_By', models.CharField(default='admin', max_length=200)),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarianish', models.BooleanField(default=False)),
                ('lactose_Free', models.BooleanField(default=False)),
                ('paleo', models.BooleanField(default=False)),
                ('ingredients', models.ManyToManyField(to='foodCosts.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('tutorial_Link', models.URLField(blank=True, null=True)),
                ('product_Link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('consumer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='foodCosts.Consumer')),
                ('ingredients', models.ManyToManyField(to='foodCosts.Ingredient')),
                ('tools', models.ManyToManyField(to='foodCosts.Tool')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tools',
            field=models.ManyToManyField(to='foodCosts.Tool'),
        ),
        migrations.AddField(
            model_name='meal',
            name='recipes',
            field=models.ManyToManyField(to='foodCosts.Recipe'),
        ),
        migrations.AddField(
            model_name='groceryplan',
            name='ingredients',
            field=models.ManyToManyField(to='foodCosts.Ingredient'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='grocery_Plans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodCosts.GroceryPlan'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='meal_Plans',
            field=models.ManyToManyField(to='foodCosts.MealPlan'),
        ),
    ]