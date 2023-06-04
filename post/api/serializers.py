from post.models import Post, PostComment, PostsCategory, Inbox
from rest_framework import serializers


class PostCommentSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %I:%M %p", required=False)
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return {
           "name": f"{obj.by_user.first_name or obj.by_user.username} {obj.by_user.last_name}",
           "avatar": obj.by_user.profile.get_avatar,
        }
            
    class Meta:
        model = PostComment
        fields = "__all__"
    

class PostSerializer(serializers.ModelSerializer):
    imageurl = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %I:%M %p", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %I:%M %p", required=False)
    comments_count = serializers.SerializerMethodField()
    comments = PostCommentSerializer(many=True, read_only=True)

    def get_imageurl(self, obj):
        return obj.get_image

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = "__all__"


class PostsCategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.posts.all().count()

    class Meta:
        model = PostsCategory
        fields = "__all__"


class InboxSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %I:%M %p", required=False)

    class Meta:
        model = Inbox
        fields = "__all__"
    