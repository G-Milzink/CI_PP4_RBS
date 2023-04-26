from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


def get_user_instance(request):

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class Bookings(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'bookings.html',
                      {'booking_form': booking_form})
