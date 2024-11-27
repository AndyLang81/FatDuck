from django.contrib import admin
from django.urls import path
from .views import submit_booking  # Import submit_booking from views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit-booking/', submit_booking, name='submit_booking'),
]