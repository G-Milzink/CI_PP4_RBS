from django.shortcuts import render
from .models import FoodItem


def food_menu(request):

    food_items = FoodItem.objects.all()
    return render(request, 'food.html', {'food_items': food_items})


def drinks_menu(request):

    food_items = FoodItem.objects.all()
    return render(request, 'drinks.html', {'drinks_items': food_items})
