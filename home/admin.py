from django.contrib import admin
from django.contrib import auth


admin.site.unregister(auth.models.Group)
