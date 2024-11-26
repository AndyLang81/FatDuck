from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_booking = models.DateTimeField()
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.full_name} on {self.date_of_booking}"