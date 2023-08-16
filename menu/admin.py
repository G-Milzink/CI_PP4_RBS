# Third party imports:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal imports:
from .models import FoodItem, DrinkItem, BitesItem


@admin.register(DrinkItem)
class DrinksAdmin(SummernoteModelAdmin):
    """
    register drinkitem model with admin panel
    """
    list_display = ('item_name',
                    'item_category',
                    'item_price',
                    'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):
    """
    register fooditem model with admin panel
    """
    list_display = ('item_name',
                    'item_category',
                    'item_price',
                    'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')


@admin.register(BitesItem)
class BitesAdmin(SummernoteModelAdmin):
    """
    register fooditem model with admin panel
    """
    list_display = ('item_name',
                    'item_category',
                    'item_price',
                    'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')
