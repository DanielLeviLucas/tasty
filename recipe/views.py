from django.shortcuts import render
from .models import Recipe, Ingredient, Cuisine
# Create your views here.


def testPage(request):
    greet = 'Welcom to the test page!'
    return render(request,
                  'recipes/recipe/testPage.html',
                  {'greet': greet})


def list_recipes(request):
    recipes = Recipe.objects.all()

    return render(request,
                  'recipes/recipes-list.html',
                  {'recipes': recipes})
