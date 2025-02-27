from django.contrib import admin
from .models import Recipe, RecipeIngredient


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine,]
    search_fields = ("name",)
    list_display = ("name",)
    list_filter = ("name",)

admin.site.register(Recipe, RecipeAdmin)
