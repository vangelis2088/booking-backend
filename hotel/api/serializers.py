from rest_framework import serializers
from hotel.models import Hotel, Room, Room_Type, Booking

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        #exclude = ("id",)   #all the fields except id
        fields = "__all__" #all the fields of Hotel model

    # validation
    def validate(self, data):
        if data["hotel_name"] == data["hotel_description"]:
            raise serializers.ValidationError("Name and Description must be different from one another")
        return data

    # field validation
    def validate_location(self, value):   
        if len(value) < 5:
            raise serializers.ValidationError("Location name must be at least 5 characters long!")
        return value

class RoomSerializer(serializers.ModelSerializer):

    #hotel_id = serializers.StringRelatedField()
    room_type = serializers.StringRelatedField()

    class Meta:
        model = Room
        exclude = ("id",)

class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room_Type
        exclude = ("id",)

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"
