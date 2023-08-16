# Third party imports:
from django.contrib import admin
from django.contrib import auth


# remove 'groups' section from admin panel
admin.site.unregister(auth.models.Group)
