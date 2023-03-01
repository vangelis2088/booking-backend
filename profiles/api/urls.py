from django.urls import include, path
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView
from rest_framework.routers import DefaultRouter
#from profiles.api.views import ProfileList
#from profiles.api.views import ProfilesListCreateAPIView

#profile_list = ProfileViewSet.as_view({"get":"list"})
#profile_detail = ProfileViewSet.as_view({"get":"retrieve"})

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
    #path("profiles/",profile_list, name="profiles-list"),
    #path("profiles/<int:pk>/",profile_detail, name="profile-detail")
]