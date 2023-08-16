# Third party imports:
from django.contrib import admin
# Internal imports:
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    register contact section for admin panel
    """
    list_filter = ('user', 'name', 'email', 'created_on')
    list_display = ('user', 'name', 'message', 'created_on')
    search_fields = ['name', 'created_on']
    list_filter = ('created_on',)
