from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_recipe(q=None):
    if q:
        recipes = Recipe.objects.filter(name__icontains=q)
    else:
        recipes = Recipe.objects.all()[:6]

    return recipes


def home(request):

    filter_recipe = request.GET.get('name')
    if cache.get(filter_recipe):
        recipe = cache.get(filter_recipe)

    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter_recipe, recipe)
        else:
            recipe = get_recipe()

    context = {
        'recipes': recipe,
    }
    return render(request, "core/index.html", context)




def recipe_detail(request, slug):
    if cache.get(slug):
        recipe = cache.get(slug)
    else:
        recipe = get_object_or_404(Recipe, slug=slug)
        cache.set(slug, recipe)

    context = {
        'recipe' : recipe
    }

    return render(request, "core/recipe_detail.html", context)

