from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FoodItem


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):
    list_display = ('item_name', 'item_category', 'item_price', 'item_available')  # noqa
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')

@admin.register(DrinksItem)
class FoodAdmin(SummernoteModelAdmin):
    list_display = ('item_name', 'item_category', 'item_price', 'item_available')  # noqa
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')
