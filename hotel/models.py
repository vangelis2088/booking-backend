from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_description = models.CharField(max_length=200)
    location = models.CharField(max_length=120)
    total_rooms = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner")

    def __str__(self) -> str:
        return f"{ self.hotel_name}"

class Room_Type(models.Model):
    room_name = models.CharField(max_length=50)
    room_description = models.CharField(max_length=200)
    room_price = models.FloatField()

    def __str__(self) -> str:
        return f"{ self.room_name }"

class Room(models.Model):
    room_number = models.IntegerField()
    occupancy = models.BooleanField(default=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.ForeignKey(Room_Type, on_delete=models.CASCADE, default=0, related_name="types")

    def __str__(self) -> str:
        return f"{ self.room_number }"

class Booking(models.Model):

    ACT = "ACTIVE"
    CAN = "CANCEL"

    BOOKING_CHOICES = (
        (ACT, "Active"),
        (CAN, "Cancel"),
    )

    rooms_count = models.IntegerField(default=1)
    date_in = models.DateField()
    date_out = models.DateField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room")
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    status = models.CharField(max_length=6,choices=BOOKING_CHOICES,default=ACT)

    def __str__(self) -> str:
        return f"{ self.rooms_count } { self.date_in }"