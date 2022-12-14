from django.urls import path
from sandwich_app.views import SandwichAppView, IngredientsView, SandwichGeneratorView, SandwichMenuView

urlpatterns = [
    path('', SandwichAppView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
    path('menu/', SandwichMenuView.as_view(), name='sandwich_menu')
]