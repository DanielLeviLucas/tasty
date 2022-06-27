from django.contrib import admin
from .models import Cuisine, Ingredient, Collection, Recipe

# Register your models here.


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'measurement', 'optional']


@admin.register(Recipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'type',
                    'image', 'cuisine', 'difficulty',
                    'instructions', 'servings', 'preparation_time',
                    'total_time', 'calories']
    search_fields = ('title', 'author', 'type')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', ]
