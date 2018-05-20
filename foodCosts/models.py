from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    market_Unit_Price = models.DecimalField(max_digits=5, decimal_places=3)
    market_Package_Type = models.CharField(max_length=200)
    market_Unit_To_Recipe_Unit_Conversion_Type = models.CharField(max_length=200, unique=True)

    conversion_Factor =models.DecimalField(max_digits=5, decimal_places=3)
    retailer = models.CharField(max_length=200, unique=True)
    updated = models.DateField()

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=200, unique=True)
    tutorial_Link = models.URLField(null = True, blank = True)
    product_Link = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.ManyToManyField(Ingredient)
    quantities =  models.CharField(max_length=200, default = "admin")
    tools = models.ManyToManyField(Tool)
    instructions = models.TextField(max_length=1000)
    created_By = models.CharField(max_length=200, default = "admin")

    vegan = models.BooleanField(default=False)
    vegetarianish = models.BooleanField(default= False)
    lactose_Free = models.BooleanField(default=False)
    paleo = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    meals = models.ManyToManyField(Meal)
    date = models.DateField()
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.date


class GroceryPlan(models.Model):
    date = models.DateField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.date

class Consumer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    meal_Plans =  models.ManyToManyField(MealPlan)
    grocery_Plans = models.ForeignKey(GroceryPlan, on_delete = models.CASCADE)
    vegan = models.BooleanField(default=False)
    vegetarianish = models.BooleanField(default= False)
    lactose_Free = models.BooleanField(default=False)
    paleo = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Kitchen(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    tools = tools = models.ManyToManyField(Tool)
    consumer = models.OneToOneField(
        Consumer,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return "%s Kitchen of "  % self.consumer
