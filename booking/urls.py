from django.urls import path
from booking import views


# Urls for all the pages in the bookings app
urlpatterns = [
    path('bookings', views.Bookings.as_view(), name='bookings'),
    path('received', views.Received.as_view(), name='received'),
]
