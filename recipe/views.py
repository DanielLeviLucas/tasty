from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Recipe, Ingredient, Cuisine
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from .forms import RecipeForm, IngredientForm
from django.shortcuts import redirect
from .filters import RecipeFilter


def testPage(request):
    greet = 'Welcom to the test page!'
    return render(request,
                  'recipes/recipe/testPage.html',
                  {'greet': greet})


def dashboard(request):
    return render(request,
                  'recipes/recipe/dashboard.html',)


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes-list.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET,
                                         queryset=self.get_queryset())
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe/recipe-detail.html'
    context_object_name = 'recipe'


def createRecipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST or None)
        ingredient_form = IngredientForm(request.POST or None)
        if recipe_form.is_valid() and ingredient_form.is_valid():
            recipe = recipe_form.save()
            ingredient = ingredient_form.save(commit=False)

            ingredient.recipe = recipe
            ingredient.save()

            return redirect('recipe:dashboard')

    else:
        recipe_form = RecipeForm()
        ingredient_form = IngredientForm()

    return render(request,
                  'recipes/recipe/create-recipe.html',
                  {'recipe_form': recipe_form,
                   'ingredient_form': ingredient_form})
