import django_filters
from .models import Recipe, Cuisine
# It should be able to sort recipes by date created/modified, calories
# It should be filter by user, cuisine, difficulty level, veg,


class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(
        field_name='author', lookup_expr='icontains')
    cuisine__in = django_filters.filters.ModelMultipleChoiceFilter(
        field_name='cuisine__id',
        to_field_name='id',
        lookup_expr='in',
        queryset=Cuisine.objects.all(),
    )
    type = django_filters.MultipleChoiceFilter(
        field_name='type', choices=Recipe.type
    )

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Recipe
        fields = ('title', 'author', 'cuisine', 'difficulty',
                  'type')


def filter_by_order(self, queryset, name, value):
    expression = 'created' if value == 'ascending' else 'modified'
    return queryset.order_by(expression)
