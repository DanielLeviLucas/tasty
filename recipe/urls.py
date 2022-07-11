from django.urls import path
from . import views


app_name = 'recipe'

urlpatterns = [
    path('test/', views.testPage, name='testPage'),
    path('list-recipes/', views.RecipesListView.as_view(), name='list-recipes'),
    path('author-recipes/', views.AuthorRecipe.as_view(), name='author-recipes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/create/', views.create_recipe, name='create-recipe'),
    path("recipe/<int:id>/edit/", views.edit_recipe, name='edit-recipe'),
    path('recipe/<int:pk>/delete/',
         views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('collection/create/',
         views.create_collection, name='create-collection'),
    path('collection/list', views.AuthorCollectionListView.as_view(),
         name='list-collection')
]
