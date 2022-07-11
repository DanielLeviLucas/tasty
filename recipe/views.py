from django.views.generic.base import TemplateResponseMixin, View
from .forms import RecipeModelForm, IngredientFormset, CollectionModelForm
from django.forms.models import modelformset_factory
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Recipe, Ingredient, Collection
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.shortcuts import redirect
from .filters import RecipeFilter
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def testPage(request):
    greet = 'Welcom to the test page!'
    return render(request,
                  'recipes/recipe/testPage.html',
                  {'greet': greet})


def dashboard(request):
    template_name = 'navbar/dashboard.html'
    return render(request, template_name)


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes-list.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET,
                                         queryset=self.get_queryset())
        return context

class AuthorRecipe(LoginRequiredMixin, RecipesListView):
    template_name = 'recipes/author/author-recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user.pk)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe/recipe-detail.html'
    context_object_name = 'recipe'


def create_recipe(request):
    template_name = 'recipes/recipe/create-recipe.html'

    recipe_form = RecipeModelForm(request.POST or None, request.FILES)
    formset = IngredientFormset(request.POST or None)

    if recipe_form.is_valid() and formset.is_valid():
        recipe_instance = recipe_form.save(commit=False)
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



def edit_recipe(request, id=None):
    template_name = 'recipes/recipe/edit/edit-recipe.html'

    recipe_obj = get_object_or_404(Recipe, id=id, author=request.user)
    recipe_form = RecipeModelForm(request.POST or None, request.FILES, instance=recipe_obj)
    recipe_ingredient_formset = modelformset_factory(Ingredient,
                                         fields=('name', 'quantity',
                                                 'measurement', 'optional'),
                                         extra=0)
    qs = recipe_obj.recipe_ingredients.all()

    formset = recipe_ingredient_formset(request.POST or None, queryset=qs)
    context = {
        "recipe_form": recipe_form,
        "formset": formset,
        "recipe_obj": recipe_obj

    }

    if recipe_form.is_valid() and formset.is_valid():
        recipe_instance = recipe_form.save(commit=False)
        recipe_instance.save()
        for form in formset:
            ingredient_instance = form.save(commit=False)
            ingredient_instance.recipe = recipe_instance
            ingredient_instance.save()
    return render(request, template_name, context)

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe/recipe_confirm_delete.html'

    success_url = reverse_lazy('recipe:list-recipes')

def create_collection(request):
    template_name = 'navbar/collection/create/create-collection.html'

    collection_form = CollectionModelForm(request.POST or None)

    if collection_form.is_valid():
        collection_instance = collection_form.save(commit=False)
        collection_instance.author = get_object_or_404(
            User, pk=request.user.pk)
        collection_instance.save()
        return redirect('recipe:list-recipes')

    collection_form = CollectionModelForm()

    context = {}
    context['collection_form'] = collection_form
    return render(request, template_name, context)


class AuthorCollectionListView(ListView):
    model = Collection
    template_name = 'recipes/author/author-recipe-collection.html'
    context_object_name = 'collection'

    def get_queryset(self):
        return Collection.objects.filter(author=self.request.user.pk)

class CollectionListView(ListView):
    model = Collection
    template_name = 'recipes/recipe-collection.html'
    context_object_name = 'collection'

