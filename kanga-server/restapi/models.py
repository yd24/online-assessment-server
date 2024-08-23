from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image_url = models.URLField()
    view_count = models.IntegerField()

    def __str__(self):
        return self.title