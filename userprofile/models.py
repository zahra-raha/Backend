from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

USER = get_user_model()

# upload paths
def upload_user_avatar_path(_, name):
    return f"avatars/{name}"

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(USER, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_user_avatar_path, blank=True, null=True)
    phonenumber = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['-pk']

    def __str__(self):
        return super(Profile, self).__str__()

    # Create token and profile when a user is created
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
            Profile.objects.create(user=instance)

    @property
    def get_avatar(self):
        if self.avatar:
            return settings.HOST_URL+self.avatar.url
        return "https://shorturl.at/mGOT6"
    