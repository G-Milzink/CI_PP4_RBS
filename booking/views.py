from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib import messages
import datetime
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

    def post(self, request):

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking received")

        return render(request, 'received.html', {'booking_form': booking_form})


class Received(generic.DetailView):

    def get(self, request):
        return render(request, 'received.html')


class AllMyBookings(generic.ListView):

    model = Booking

    def get(self, request, *args, **kwargs):

        all_bookings = Booking.objects.all()
        today = datetime.datetime.now().date()

        for date in all_bookings:
            if date.booking_date < today:
                date.booking_status = 'Expired'

        if request.user.is_authenticated:
            my_bookings = Booking.objects.filter(
                user=request.user).filter().order_by('booking_date')

            return render(
                request,
                'all_my_bookings.html',
                {
                    'all_bookings': all_bookings,
                    'my_bookings': my_bookings})
        else:
            return redirect('accounts/login.html')
