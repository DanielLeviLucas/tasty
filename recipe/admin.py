from django.contrib import admin
from .models import Cuisine, Ingredient, Collection, Recipe

# Register your models here.


class IngredientInline(admin.StackedInline):
    model = Ingredient


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Recipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'type',
                    'image', 'difficulty', 'instructions',
                    'servings', 'preparation_time', 'total_time',
                    'calories']
    search_fields = ('title', 'author', 'type')
    inlines = [IngredientInline]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', ]
