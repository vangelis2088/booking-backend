from django.urls import include,path
#from hotel.api.views import hotel_list_create_api_view, hotel_detail_api_view
from hotel.api.views import (HotelListCreateAPIView, HotelDetailAPIView, 
                RoomListCreateAPIView, RoomDetailAPIView, BookingViewSet)
#from hotel.api.views import RoomListCreateAPIView, RoomDetailAPIView
#from hotel.api.views import HotelViewSet
from rest_framework.routers import DefaultRouter

#hotels_list = HotelViewSet.as_view({"get":"list"})
#hotel_detail = HotelViewSet.as_view({"get":"retrieve"})

router = DefaultRouter()
router.register(r"bookings",BookingViewSet)

#booking_list = BookingViewSet.as_view({"get":"list"})
#booking_detail = BookingViewSet.as_view({"get":"retrieve"})

urlpatterns = [
    path("hotels/",HotelListCreateAPIView.as_view(), name="hotels-list"),
    path("hotels/<int:pk>/",HotelDetailAPIView.as_view(), name="hotel-detail"),
    #path("hotels/",hotels_list, name="hotels-list"),
    #path("hotels/<int:pk>/",hotel_detail, name="hotel-detail"),

    path("rooms/",RoomListCreateAPIView.as_view(), name="rooms-list"),
    path("rooms/<int:pk>/",RoomDetailAPIView.as_view(), name="room-detail"),

    path("", include(router.urls))

    #path("bookings/",booking_list, name="booking-list"),
    #path("bookings/<int:pk>/",booking_detail, name="booking-detail"),
    #path("rooms_type/",RoomTypeListCreateAPIView.as_view(), name="rooms-type-list"),
    #path("hotels/",hotel_list_create_api_view, name="hotels-list"),
    #path("hotels/<int:pk>",hotel_detail_api_view, name="hotel-detail"),
]