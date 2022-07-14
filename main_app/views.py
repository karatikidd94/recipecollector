from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import MessagingForm

# class Recipe:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, title, meal, length, ingredients, directions):
#         self.title = title
#         self.meal = meal
#         self.length = length
#         self.ingredients = ingredients
#         self.directions = directions


# recipes = [
#   Recipe('Grilled Potato Salad', 'Lunch', '45 mins', '2lb Potatoes, 1/4 cup olive oil, salt & pepper to taste, 3 tbsp vinegar, 1 tbsp mustard, 1 tsp celery seeds, 1 tsp sugar, 2 tsp chopped herbs', 'mix it all together'),
#   Recipe('Spinach & Egg Tacos', 'Breakfest', '10 mins', '1/4 avocado, 1 tsp lime juice, Pinch of Salt, 2 chopped hard-boiled eggs, 2 corn tortillas, 1 cup chopped spinach, 2 tbsp shredded cheddar, 2 tbsp salsa', 'Smash avocado in a small bowl with lime juice and salt. Mix in eggs. Divide the mixture between tortillas and top each with 1/2 cup spinach and 1 tablespoon each cheese and salsa.')
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    messaging_form = MessagingForm()
    return render(request, 'recipes/detail.html', {
        'recipe': recipe, 'messaging_form': messaging_form
    })

def add_messaging(request, recipe_id):
    form = MessagingForm(request.POST)
    if form.is_valid():
        new_messaging = form.save(commit=False)
        new_messaging.recipe_id = recipe_id
        new_messaging.save()
    return redirect('detail', recipe_id=recipe_id)

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'
    # fields = ['title', 'meal', 'length', 'ingredients', 'directions']

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['title', 'meal', 'length', 'ingredients', 'directions']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'