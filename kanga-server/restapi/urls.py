from django.urls import path
from . import views

#routes
urlpatterns = [
    path("recipe/", views.RecipeList.as_view(), name="recipe-read-create")
]
