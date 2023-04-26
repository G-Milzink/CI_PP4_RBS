from django.db import models
from django.contrib.auth.models import User


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

booking_status = (
    ('Unconfirmed', 'Unconfirmed'),
    ('Confirmed', 'Confirmed'),
    ('Rejected', 'Rejected'),
    ('Expired', 'Expired'),
)


class Table(models.Model):

    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=20, default='new', unique=True)
    nr_of_seats = models.PositiveIntegerField(default=2)

    class meta:
        ordering = ['-nr_of_seats']

    def __str__(self):
        return self.table_name
