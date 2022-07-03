from django import forms

from django.forms import modelform_factory, modelformset_factory

from .models import Recipe, Ingredient


class RecipeModelForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['created', 'modified', 'author']


IngredientFormset = modelformset_factory(Ingredient,
                                         fields=('name', 'quantity',
                                                 'measurement', 'optional'),
                                         extra=0,
                                         can_delete=True)
