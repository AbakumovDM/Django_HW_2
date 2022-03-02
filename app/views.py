from django.shortcuts import render
from app.templates.data import DATA

def recipe(request, name):
    servings = int(request.GET.get('servings', 1))
    recipe_serv = {}
    for key, value in DATA[name].items():
        recipe_serv[key] = value * servings
    context = {
       'recipe': recipe_serv
    }
    return render(request, 'recipe.html', context)
