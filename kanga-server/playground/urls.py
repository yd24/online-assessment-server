from django.urls import path
from . import views

#routes
urlpatterns = [
    path('hello/', views.hello_world),
]
