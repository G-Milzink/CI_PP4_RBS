# Third party imports:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal imports:
from .models import Blogpost, Comment


@admin.register(Blogpost)
class PostAdmin(SummernoteModelAdmin):
    """
    register blogpost section for admin panel
    """
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    register comment section for admin panel
    """
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
