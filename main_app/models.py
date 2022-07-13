from django.db import models
from django.urls import reverse

# Create your models here.

class Recipe:  # Note that parens are optional if not inheriting from another class
  def __init__(self, meal, title, length, ingredients, prep):
    self.meal = meal
    self.title = title
    self.length = length
    self.ingredients = ingredients
    self.prep = prep

recipes = [
  Recipe('Lunch', 'Grilled Potato Salad', '45mins', '2lb Potatoes, 1/4 cup olive oil, salt & pepper to taste, 3 tbsp vinegar, 1 tbsp mustard, 1 tsp celery seeds, 1 tsp sugar, 2 tsp chopped herbs', 'mix it all together'),
]