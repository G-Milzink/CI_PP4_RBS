from django.urls import path
from booking import views


# Urls for all the pages in the bookings app
urlpatterns = [
    path('bookings', views.Bookings.as_view(), name='bookings'),
    path('received', views.Received.as_view(), name='received'),
    path('allmybookings', views.AllMyBookings.as_view(), name='allmybookings'),
    path('edit_booking/<int:pk>', views.EditBooking.as_view(), name='edit_booking'),
    path('cancel_booking/<int:pk>', views.cancel_booking, name='cancel_booking')
]
