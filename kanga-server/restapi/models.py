from django.db import models
from .utils import random_img_int, random_view_int

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image_url = models.IntegerField(default = random_img_int)
    view_count = models.IntegerField(default  = random_view_int)

    def __str__(self):
        return self.title