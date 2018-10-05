from django.conf.urls import url
from foodCosts import views as fC_views
from foodCosts.views import IngredientListView, ToolListView, RecipeListView, MealListView
from django.contrib.auth.views import login

urlpatterns = [

    #url(r'^ingredientsList/$', fC_views.ingredients_ListView, name = 'ingredientsList'),
    url(r'^ingredientsList/$', IngredientListView.as_view(), name= 'ingredientsList'),

    url(r'^ingredientDetail/(?P<ingredient_id>\d+)$', fC_views.ingredient_DetailView, name = 'ingredientDetail'),

    #url(r'^toolsList/$', fC_views.tools_ListView, name = 'toolsList'),
    url(r'^toolsList/$', ToolListView.as_view(), name = 'toolsList'),

    #url(r'^recipesList/$', fC_views.recipes_ListView, name = 'recipesList'),
    url(r'^recipesList/$', RecipeListView.as_view(), name = 'recipesList'),

    url(r'^recipeDetail/(?P<recipe_id>\d+)$', fC_views.recipe_DetailView, name = 'recipeDetail'),

    url(r'^mealsList/$', MealListView.as_view(), name = 'mealList'),
]
