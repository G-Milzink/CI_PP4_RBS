from . import views
from django.urls import path

urlpatterns = [
    path('food', views.food_menu, name='food'),
    path('drinks', views.drinks_menu, name='drinks'),
    path('bites', views.bites_menu, name='bites')
]
