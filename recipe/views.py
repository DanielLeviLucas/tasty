from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Recipe, Ingredient, Cuisine
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView


def testPage(request):
    greet = 'Welcom to the test page!'
    return render(request,
                  'recipes/recipe/testPage.html',
                  {'greet': greet})


def dashboard(request):
    return render(request,
                  'recipes/recipe/dashboard',)


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes-list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe/recipe-detail.html'
    context_object_name = 'recipe'
