from django.db import models
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    meal = models.CharField(max_length=20)
    length = models.IntegerField()
    ingredients = models.CharField(max_length=250)
    directions = models.TextField(max_length=250)

