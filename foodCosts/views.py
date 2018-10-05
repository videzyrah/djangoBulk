from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db.models import Sum

from foodCosts.models import Ingredient, Tool, Recipe, Meal, MealPlan

# Create your views here.
class ToolListView(ListView):
    template_name = "tools.html"

    model = Tool
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class IngredientListView(ListView):
    template_name = "ingredients.html"

    model = Ingredient
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #to include an average price calculation:
        #context['avg'] = Ingredient.objects.all().aggregate(Avg('market_Unit_Price'))

        return context

def ingredient_DetailView(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)

    return render(request, 'ingredientDetail.html', {'ingredient': ingredient })
    #return HttpResponse("recipes_DetailView")

class RecipeListView(ListView):
    template_name = "recipes.html"

    model = Recipe
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def recipe_DetailView(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    #gross cost of ingredients
        #Create queryset with extra attribute aliased as 'Cost_of_Ingredients'
        #which is the sum of ingredient costs bought by bag/box/etc.
    totc = recipe.ingredients.all().aggregate(Cost_of_Ingredients=Sum('market_Unit_Price'))
    tc = totc['Cost_of_Ingredients']

    #batch cost of ingredients
    qs = recipe.ingredients.all()
    count = recipe.ingredients.count()
    quantityList = recipe.quantitiesListConverter()
    print (quantityList)
    #quantityList = [2,2,2]
    recipe_price = 0.00
    x = 0

    for ingredient in qs:
        #ingredient unit price
        iup = ingredient.market_Unit_Price * ingredient.conversion_Factor
        #individual ingredient price total
        iipt = float(iup) * quantityList[x]

        #recipe price summing
        #recipe_price = float(recipe_price) + float(iup)
        recipe_price = float(recipe_price) + float(iipt)

        #quantities list iterating
        x= x+1
        pass


    ''' stuff that didn't work
    first = qs[1]
    name = first.iup
    #totalling up recipe cost per batch
    cor = recipe.ingredients.all().aggregate(Cost_of_Recipe=Sum(ingredient.rup))
    ic = cor['Cost_of_Recipe']
    '''

    return render(request, 'recipeDetail.html', {'recipe': recipe, 'tc': tc, 'count':count, 'recipe_price': recipe_price})
    #return HttpResponse("recipes_DetailView")

class MealListView(ListView):
    template_name = "meals.html"

    model = Meal
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MealPlanCreateView(CreateView):

    model = MealPlan
    fields = ["meals", "date", "notes"]
