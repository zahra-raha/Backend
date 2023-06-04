from django.contrib.auth.models import User
from rest_framework import viewsets
from userprofile.models import Profile
from rest_framework import generics
from rest_framework.permissions import AllowAny
from post.models import Post

from .serializers import RegisterSerializer, ProfileSerializer, UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_object(self):
        if self.kwargs.get("pk") == "0":
            return self.request.user.profile
        return super().get_object()

    def get_queryset(self):
        return Profile.objects.filter()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
