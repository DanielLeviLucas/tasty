from django.shortcuts import render
from .models import Recipe, Ingredient, Cuisine


def testPage(request):
    greet = 'Welcom to the test page!'
    return render(request,
                  'recipes/recipe/testPage.html',
                  {'greet': greet})


def dashboard(request):
    return render(request,
                  'recipes/recipe/dashboard',)


def list_recipes(request):
    recipes = Recipe.objects.all()

    return render(request,
                  'recipes/recipes-list.html',
                  {'recipes': recipes})
