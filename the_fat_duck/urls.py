from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', views.book_table, name='book_table'),  # Link the booking form to the /book/ URL
]
