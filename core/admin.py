from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created']
    list_display_links = ['slug']
    list_filter = ['created', 'updated']
    ordering = ['created']
    search_fields = ['name']