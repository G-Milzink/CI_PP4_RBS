# Third party imports:
from django.urls import path
# Internal imports:
from . import views

# URL for the homepage
urlpatterns = [
    path('', views.home),
]
