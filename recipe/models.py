from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from model_utils.models import TimeStampedModel
# Create your models here.


class Cuisine (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(TimeStampedModel):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_recipes')
    TYPE_CHOICES = (
        ('veg', 'VEG'),
        ('non-veg', 'NON-VEG'),
        ('vegan', "VEGAN"),
    )
    type = models.CharField(max_length=10,
                            choices=TYPE_CHOICES,
                            default='veg')
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    cuisine = models.ManyToManyField(Cuisine, related_name='style_of_cooking')
    difficulty = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)])
    instructions = models.TextField()
    servings = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)])
    preparation_time = models.CharField(max_length=25)
    total_time = models.CharField(max_length=25)
    calories = models.IntegerField(validators=[MaxValueValidator(750)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.title}| {self.type}| {self.cuisine}'


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    measurement = models.CharField(blank=True, max_length=25)
    optional = models.BooleanField(default=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='recipe_ingredients')

    def __str__(self):
        return f'{self.name} : {self.quantity}{self.measurement} | {self.optional}'


class Collection(models.Model):
    title = models.CharField(max_length=250)
    recipes = models.ManyToManyField(
        Recipe, related_name='recipe_collections')

    def __str__(self):
        return self.title
