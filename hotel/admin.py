from django.contrib import admin
from hotel.models import Hotel, Room, Room_Type, Booking

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Room_Type)
admin.site.register(Booking)