from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name="Recipe name")
    slug = models.SlugField(blank=True, null=True)
    cover_img = models.ImageField(upload_to="recipe_img/")
    description = models.TextField(null=True, blank=True)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("core:detail", args=[self.slug])