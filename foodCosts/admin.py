from django.contrib import admin
from foodCosts.models import Ingredient, Tool, Recipe, Meal, MealPlan, Consumer, Kitchen

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name','retailer', 'market_Unit_Price', 'market_Package_Type' )
    search_fields = ['name','retailer']

admin.site.register(Ingredient, IngredientAdmin)

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

admin.site.register(Tool, ToolAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'ingredients', 'created_By')

admin.site.register(Recipe, RecipeAdmin)

class MealAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'recipes', 'created_By')

admin.site.register(Meal, MealAdmin)
