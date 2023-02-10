from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False, editable=True)
    is_flagged = models.BooleanField(default=False, editable=True)

    class Meta:
        ordering = ['-posted_on']
