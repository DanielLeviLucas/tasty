import django_filters
from .models import Recipe, Cuisine
# It should be able to sort recipes by date created/modified, calories
# It should be filter by user, cuisine, difficulty level, veg,


class RecipeFilter(django_filters.FilterSet):

    class Meta:
        model = Recipe
        fields = ('title', 'author', 'cuisine', 'difficulty',
                  'type')
