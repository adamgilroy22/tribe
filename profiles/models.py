from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)
    profile_pic = CloudinaryField('profile_pic', default='placeholder')
    bg_pic = CloudinaryField('bg_pic', default='placeholder')
    is_suspended = models.BooleanField(default=False, editable=True)
