from django.urls import path
from . import views


app_name = 'recipe'

urlpatterns = [
    path('test/', views.testPage, name='testPage'),
    path('list-recipes/', views.list_recipes, name='list-recipes'),
    path('dashboard/', views.dashboard, name='dashboard')
]
