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

""" class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hotel_name = serializers.CharField()
    hotel_description = serializers.CharField()
    location = serializers.CharField()
    total_rooms = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hotel_name = validated_data.get('hotel_name', instance.hotel_name)
        instance.hotel_description = validated_data.get('hotel_description', instance.hotel_description)
        instance.location = validated_data.get('location', instance.location)
        instance.total_rooms = validated_data.get('total_rooms', instance.total_rooms)
        instance.save()
        return instance

     """