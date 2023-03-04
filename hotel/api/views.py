import time
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import generics
from rest_framework import mixins

from hotel.models import Hotel, Room, Room_Type, Booking
from hotel.api.serializers import HotelSerializer, RoomSerializer, RoomTypeSerializer, BookingSerializer
from hotel.api.permissions import IsOwnHotelOrReadOnly, IsOwnBookingOrReadOnly


class HotelListCreateAPIView(APIView):

    def get(self, request):
        location = request.GET.get('location','')
        if (location):
            hotels = Hotel.objects.filter(location=location)
            serializer = HotelSerializer(hotels, many=True)
            return Response(serializer.data)
        else:
            u_id = self.request.query_params.get("user_id",None)
            if u_id is not None:
                hotels = Hotel.objects.filter(owner=u_id)
                serializer = HotelSerializer(hotels, many=True)
                return Response(serializer.data)
            else:
                hotels = Hotel.objects.all()
                serializer = HotelSerializer(hotels, many=True)
                return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class HotelViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]

"""
class HotelDetailAPIView(APIView):

    def get_object(self, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        return hotel

    def get(self, request, pk):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def put(self,request,pk):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        hotel = self.get_object(pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        
        h_id = self.request.query_params.get("hotel_id",None)
        if h_id is not None:
            queryset = Room.objects.filter(hotel_id=h_id)
            serializer = RoomSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)

class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]

    def get_queryset(self):
        #time.sleep(3)
        u_id = self.request.query_params.get("user_id",None)
        res = self.request.query_params.get("reservations",None)
        if u_id is not None:
            queryset = Booking.objects.filter(user_id=u_id)
            return queryset
        if res is not None:
            hotel_ids = Hotel.objects.filter(owner=res).values_list('id', flat=True)
            bookings = Booking.objects.filter(hotel_id__in=hotel_ids).order_by('id')
            return bookings

        return super().get_queryset()

"""
class RoomListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoomListCreateAPIView(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomTypeListCreateAPIView(APIView):

    def get(self, request):
        room_type = Room_Type.objects.all()
        serializer = RoomTypeSerializer(room_type, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""