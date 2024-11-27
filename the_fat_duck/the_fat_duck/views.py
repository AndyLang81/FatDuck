from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpResponse

def submit_booking(request):
    if request.method == 'POST':
        # Extract form data and create a new Booking
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        guests = request.POST['guests']

        booking = Booking(
            name=name,
            email=email,
            phone=phone,
            date=date,
            guests=guests
        )
        booking.save()

        return HttpResponse('Booking submitted successfully!')

    return render(request, 'book.html')