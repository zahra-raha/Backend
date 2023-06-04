from django_filters.rest_framework import DjangoFilterBackend
from post.models import Post, PostComment, PostsCategory, Inbox
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import PostsCategorySerializer, PostSerializer, PostCommentSerializer, InboxSerializer


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "description", "address"]
    filterset_fields = {
        "created_at": ["gte", "lte", "exact"],
        "updated_at": ["gte", "lte", "exact"],
        "price": ["gte", "lte", "exact"],
        "color": ["exact"],
        "category": ["exact"],
        "owner__id": ["exact"],
    }


class PostsCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostsCategory.objects.all()
    serializer_class = PostsCategorySerializer


class InboxViewSet(viewsets.ModelViewSet):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "post": ["exact"],
        "post__owner__id": ["exact"],
        "by_user__id": ["exact"],
    }
