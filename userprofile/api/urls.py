from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views as v


router = DefaultRouter()
router.register("profile", v.ProfileViewSet, basename="profile")

app_name = "userprofile-api"
urlpatterns = [
    path("", include(router.urls)),
    path("user/<int:pk>/", v.RetrieveUpdateUserView.as_view(), name='user'),
    path("register/", v.RegisterView.as_view(), name='auth_register'),
]