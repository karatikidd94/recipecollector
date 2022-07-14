from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    meal = models.CharField(max_length=20, choices=MEALS, default=MEALS[0][0])
    length = models.IntegerField()
    ingredients = models.CharField(max_length=250)
    directions = models.TextField(max_length=250)
    # Add the M:M relationship

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Messaging(models.Model):
    # date = models.DateTimeField(auto_now_add=True)
    date = models.DateField('Messaging Date')
    message = models.TextField(max_length=300)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message} on {self.date}"
    
    class Meta:
        ordering = ['-date']
