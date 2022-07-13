from django.shortcuts import render
from .models import Recipe
from django.http import HttpResponse

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

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    # recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })