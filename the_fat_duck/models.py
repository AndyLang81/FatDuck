# the_fat_duck/models.py

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)   # The name of the person making the booking
    email = models.EmailField()                # The email of the person
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    date = models.DateField()                  # Date of booking
    time = models.TimeField()                  # Time of booking
    guests = models.IntegerField()             # Number of guests

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"
