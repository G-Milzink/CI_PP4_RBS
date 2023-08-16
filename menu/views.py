# Third party imports:
from django.shortcuts import render
# Internal imports:
from .models import FoodItem, DrinkItem, BitesItem


def food_menu(request):
    """
    display food menu
    """
    food_items = FoodItem.objects.all()
    return render(request, 'food.html', {'food_items': food_items})


def drinks_menu(request):
    """
    display drinks menu
    """
    drink_items = DrinkItem.objects.all()
    return render(request, 'drinks.html', {'drink_items': drink_items})


def bites_menu(request):
    """
    display bites menu
    """
    bites_items = BitesItem.objects.all()
    return render(request, 'bites.html', {'bites_items': bites_items})
