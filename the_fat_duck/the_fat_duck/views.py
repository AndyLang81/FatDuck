from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpResponse

# Create the submit_booking view
def submit_booking(request):
    if request.method == 'POST':
        # Get form data from POST req
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        guests = request.POST['guests']

        # Create and save booking in the db
        booking = Booking(
            name=name,
            email=email,
            phone=phone,
            date=date,
            guests=guests
        )
        booking.save()

        # Redirect to a success page (or back to booking form)
        return HttpResponse('Booking submitted successfully!')
    
    return render(request, 'book.html')  # If GET request, render form again
