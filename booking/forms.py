from django import forms
from datetime import datetime
from datetime import date
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    booking_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    phone = PhoneNumberField()

    class Meta:
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'nr_of_guests',
            'booking_date',
            'booking_time')