from . import views
from django.urls import path

urlpatterns = [
    path('food', views.food_menu, name='food'),
]
