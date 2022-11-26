from django.shortcuts import render
from django.views import View

# Create your views here.

ingredients = {
    'meats': ['turkey', 'veggie burger', 'ham'],
    'cheeses': ['provolone', 'pepper jack', 'fondue'],
    'toppings': ['onions', 'cream cheese', 'relish']
}

class SandwichAppView(View):
    def get(self, request):
        return render (
            request = request,
            template_name= 'sandwich_app.html',
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsView(View):
    def get(self, request, ingredient_type):
        return render (
            request = request,
            template_name = 'ingredients_list.html',
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type
            }
        )