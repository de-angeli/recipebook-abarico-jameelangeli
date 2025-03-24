from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine, RecipeImageInLine,]
    search_fields = ("name",)
    list_display = ("name",)
    list_filter = ("name",)

admin.site.register(Recipe, RecipeAdmin)
