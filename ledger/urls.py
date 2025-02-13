from django.urls import path
from .views import index, recipes_list, first_recipe, second_recipe

urlpatterns = [
	path('', index, name='index'),
    path('recipes/list', recipes_list, name="recipes-list"),
    path('recipe/1', first_recipe, name='recipe1'),
    path('recipe/2', second_recipe, name='recipe2'),
]

app_name = 'ledger'