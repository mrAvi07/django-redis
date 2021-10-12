from django.urls import path
from .views import home, recipe_detail

app_name="core"

urlpatterns = [
    path('', home, name="home"),
    path('detail/<slug>', recipe_detail, name="detail")
]