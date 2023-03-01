from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
#from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins

from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer

from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

#class ProfileViewSet(ReadOnlyModelViewSet):
class ProfileViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


""" class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated] """

""" class ProfilesListCreateAPIView(APIView):

    def get(self, request):
        hotels = Profile.objects.all()
        serializer = ProfileSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
"""