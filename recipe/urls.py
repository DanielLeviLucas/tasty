from django.urls import path
from . import views


app_name = 'recipe'

urlpatterns = [
    path('test/', views.testPage, name='testPage'),
    path('list-recipes/', views.RecipesListView.as_view(), name='list-recipes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/create/',views.createRecipe, name='create-recipe')
]
