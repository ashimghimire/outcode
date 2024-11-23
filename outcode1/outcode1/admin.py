# admin.py
from django.contrib import admin
from .models import Booking, Reviews, Room, Hotel

# Register the Booking model
admin.site.register(Booking)
admin.site.register(Reviews)
admin.site.register(Room)
admin.site.register(Hotel)
