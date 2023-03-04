from django.urls import include,path
from hotel.api.views import (HotelListCreateAPIView, HotelDetailAPIView, 
                RoomListCreateAPIView, RoomDetailAPIView, BookingViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"bookings",BookingViewSet)

urlpatterns = [
    path("hotels/",HotelListCreateAPIView.as_view(), name="hotels-list"),
    path("hotels/<int:pk>/",HotelDetailAPIView.as_view(), name="hotel-detail"),
    path("rooms/",RoomListCreateAPIView.as_view(), name="rooms-list"),
    path("rooms/<int:pk>/",RoomDetailAPIView.as_view(), name="room-detail"),
    path("", include(router.urls))

]