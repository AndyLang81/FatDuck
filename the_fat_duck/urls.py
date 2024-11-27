from django.contrib import admin
from django.urls import path
from . import views  # Import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit-booking/', views.submit_booking, name='submit_booking'),
]
