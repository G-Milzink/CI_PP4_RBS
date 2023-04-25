from django.contrib import admin
from django_summernote import SummnoteModelAdmin
from .models import FoodItem


@admin.register(FoodItem)
class FoodAdmin(SummnoteModelAdmin):
    list_display = ('item_name', 'item_category', 'item_price', 'item_available')
    search_fields = ('item_name', 'item_description')
    list_filter = ('item_category', 'item_available')
    summernote_fields = ('item_description')
