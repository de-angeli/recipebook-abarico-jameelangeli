from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name="recipe-list"),
    path('<int:pk>/', RecipeDetailView.as_view(), name="recipe-detail"),
    path('add/', RecipeCreateView.as_view(), name='recipe-add'),
    path('<int:pk>/add_image/', RecipeImageCreateView.as_view(), name='recipe-add-image'),
]

app_name = 'ledger'
