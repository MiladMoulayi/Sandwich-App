from django.urls import path
from sandwich_app.views import SandwichAppView, IngredientsView

urlpatterns = [
    path('', SandwichAppView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list')
]