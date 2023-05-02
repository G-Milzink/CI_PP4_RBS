from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# kitchen open from 16:00 til 00:00
# latest possible time-slot for booking is 23:00
time_slots = (
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
    ('22:30', '22:30'),
    ('23:00', '23:00'),
)

status_options = (
    ('Unconfirmed', 'Unconfirmed'),
    ('Confirmed', 'Confirmed'),
    ('Rejected', 'Rejected'),
    ('Expired', 'Expired'),
)


# model for bookings
class Booking(models.Model):

    booking_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField()
    booking_time = models.CharField(
        max_length=10,
        choices=time_slots,
        default='16:00'
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        null=True
        )
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=250, default='')
    phone = PhoneNumberField(null=True)
    booking_status = models.CharField(
        max_length=12,
        choices=status_options,
        default='Unconfirmed'
        )
    nr_of_seats = (
        (1, '1 Guest'),
        (2, '2 Guests'),
        (3, '3 Guests'),
        (4, '4 Guests'),
        (5, '5 Guests'),
        (6, '6 Guests'),
        (7, '7 Guests'),
        (8, '8 Guests'),
    )
    nr_of_guests = models.IntegerField(choices=nr_of_seats, default=2)

    class Meta:
        ordering = ['-booking_time']

    def __str__(self):
        return self.booking_status
