from django.shortcuts import render
from .models import FoodItem


def food_menu(request):

    food_items = FoodItem.objects.all()
    return render(request, 'menu/food_menu.html', {'food_items'})
