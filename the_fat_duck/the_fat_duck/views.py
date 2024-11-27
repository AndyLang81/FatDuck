# the_fat_duck/views.py

from django.shortcuts import render, redirect
from .forms import BookingForm

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking data to the database
            return redirect('booking_success')  # Redirect to a success page or confirmation page
    else:
        form = BookingForm()
    
    return render(request, 'book.html', {'form': form})