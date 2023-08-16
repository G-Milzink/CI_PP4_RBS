# Third party imports:
from django.urls import path
# Internal imports:
from . import views

# URL's for food, drinks and bites menu pages.
urlpatterns = [
    path('food', views.food_menu, name='food'),
    path('drinks', views.drinks_menu, name='drinks'),
    path('bites', views.bites_menu, name='bites')
]
