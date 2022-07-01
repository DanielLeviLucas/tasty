from .forms import RecipeModelForm, IngredientFormset
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Recipe, Ingredient, Cuisine
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from django.shortcuts import redirect
from .filters import RecipeFilter
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


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
    template_name = 'recipes/recipe/create-recipe.html'

    recipe_form = RecipeModelForm(request.POST or None, request.FILES)
    formset = IngredientFormset(request.POST or None)

    if recipe_form.is_valid() and formset.is_valid():
        recipe_instance = recipe_form.save(commit=False)
        print(recipe_instance.title,
              end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n33333333333333333333333333333333333333333333333333333333333333")
        recipe_instance.author = get_object_or_404(User, pk=request.user.pk)
        recipe_instance.save()
        for form in formset:
            ingredient_instance = form.save(commit=False)
            ingredient_instance.recipe = recipe_instance
            ingredient_instance.save()
        return redirect('recipe:list-recipes')

    recipe_form = RecipeModelForm(request.GET)
    formset = IngredientFormset(queryset=Recipe.objects.none())

    context = {}
    context['recipe_form'] = recipe_form
    context['formset'] = formset

    return render(request, template_name, context)
