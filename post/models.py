from colorfield.fields import ColorField
from django.db import models
from userprofile.models import USER, Profile
from django.conf import settings


# upload paths
def upload_category_icon_path(instance, name):
    return f"categories/{name}"


def upload_post_images_path(instance, name):
    return f"posts/{instance.category}/{name}"


# Create your models here.
class PostsCategory(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to=upload_category_icon_path)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    CONDITIONS = [
        ("or", "Never Worn, with Original Tags"),
        ("ne", "Never Worn"),
        ("vg", "Very Good Condition"),
        ("gd", "Good Condition"),
        ("fr", "Fair Condition"),
    ]
    owner = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="posts"
    )
    category = models.ForeignKey(
        PostsCategory, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=128)
    description = models.TextField()

    dimensions = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    image = models.ImageField(
        upload_to=upload_post_images_path, blank=True, null=True
    )
    color = ColorField(image_field="image", blank=True, null=True)

    condition = models.CharField(
        max_length=8, choices=CONDITIONS, default="normal"
    )
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    liked_by = models.ManyToManyField(
        USER, blank=True, related_name="liked_posts"
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-pk"]

    def __str__(self):
        return super(Post, self).__str__()

    @property
    def get_image(self):
        if self.image:
            return settings.HOST_URL+self.image.url
        return "https://shorturl.at/CGNS2"


class PostComment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField()
    by_user = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="comments"
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.comment


class Inbox(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="inbox")
    by_user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=32)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Inbox"
        verbose_name_plural = "Inboxs"
        ordering = ['-pk']

    def __str__(self):
        return super(Inbox, self).__str__()

    