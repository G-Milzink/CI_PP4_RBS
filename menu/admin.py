from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FoodItem, DrinkItem, BitesItem


# register drinkitem model with admin panel
@admin.register(DrinkItem)
class DrinksAdmin(SummernoteModelAdmin):
    list_display = ('item_name',
                    'item_category',
                    'item_price',
                    'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')


# register fooditem model with admin panel
@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):
    list_display = ('item_name',
                    'item_category',
                    'item_price',
                    'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')


# register bitesitem model with admin panel
@admin.register(BitesItem)
class BitesAdmin(SummernoteModelAdmin):
    list_display = ('item_name',
                    'item_category',
                    'item_price',
                    'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')
