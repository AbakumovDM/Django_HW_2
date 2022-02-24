from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'recipe.html')
    # name = request.GET.get("name")
    return HttpResponse(f'hello, {name}')

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'omlet': {
            'яйца, шт': 2 * servings,
            'молоко, л': 0.1 * servings,
            'соль, ч.л.': 0.5 * servings,
        },
    }
    return render(request, 'recipe.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'pasta': {
            'макароны, г': 0.3 * servings,
            'сыр, г': 0.05 * servings,
        },
    }
    return render(request, 'recipe.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'buter': {
            'хлеб, ломтик': 1 * servings,
            'колбаса, ломтик': 1 * servings,
            'сыр, ломтик': 1 * servings,
            'помидор, ломтик': 1 * servings,
        }
    }
    return render(request, 'recipe.html', context)

def sum(request, a, b):
    result = a + b
    return HttpResponse(f'Sum = {result}')