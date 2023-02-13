from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Comment model
    """
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    posted_on = models.DateTimeField(default=timezone.now)
    post = models.OneToOneField('posts.Post', on_delete=models.CASCADE)
    is_flagged = models.BooleanField(default=False, editable=True)
