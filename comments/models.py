from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Comment model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    posted_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, blank=True, related_name='comment_likes')
