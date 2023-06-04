from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views as v


router = DefaultRouter()
router.register("post", v.PostViewSet, basename="post")
router.register("post-categories", v.PostsCategoryViewSet, basename="post-cats")
router.register("post-comments", v.PostCommentViewSet, basename="post-comments")
router.register("inbox", v.InboxViewSet, basename="inbox")

app_name = "post-api"
urlpatterns = [
    path("", include(router.urls)),
]