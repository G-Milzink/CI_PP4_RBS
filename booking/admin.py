from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    """
    register booking model for admin panel
    """
    list_display = ('booking_date', 'booking_time', 'booking_status')
    search_fields = ('booking_date',)
    list_filter = ('booking_date', 'booking_time', 'booking_status')
