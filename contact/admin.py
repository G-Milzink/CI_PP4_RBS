from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('user', 'name', 'email', 'created_on')
    list_display = ('message_id', 'user', 'name', 'message', 'created_on')
    search_fields = ['name', 'created_on']
    list_filter = ('created_on',)
