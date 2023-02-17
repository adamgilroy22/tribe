from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(User,
                                related_name='profile',
                                on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)
    profile_pic = CloudinaryField('profile_pic',
                                  default='placeholder',
                                  blank=True)
    bg_pic = CloudinaryField('bg_pic',
                             default='placeholder',
                             blank=True)
    is_suspended = models.BooleanField(default=False, editable=True)
    followers = models.ManyToManyField(User, blank=True,
                                       related_name='followers')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates user profile on signup
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Saves user profile
    """
    instance.profile.save()
